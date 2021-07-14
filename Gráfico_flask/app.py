import json
import random
import time
import numpy as np
from datetime import datetime
from banco_dados import BancoDados

from flask import Flask, Response, render_template, request, jsonify, url_for

application = Flask(__name__)

matrixAngulos=[]
now =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data', methods=["GET"])
def chart_data():
    ax = str(request.args.get('a0'))
    ay = str(request.args.get('a1'))
    az = str(request.args.get('a2'))
    angles = [ax ,ay, az]
    print("ax = " + ax + " ay = " + ay + " az = " + az)
    print(angles)

    def generate_data():
        while True:
            json_data = json.dumps(
                {'time': now, 'value0': ax,'value1': ay, 'value2': az })
            yield f"data:{json_data}\n\n"
            time.sleep(1)
        #return render_template('index.html', angles = angles)
    return Response(generate_data(), mimetype='text/event-stream')
   
@application.route('/esp-data',methods=['GET'])
def recv_data():
    ax = str(request.args.get('a0'))
    ay = str(request.args.get('a1'))
    az = str(request.args.get('a2'))
    BancoDados.insert_val_mpu(ax, ay, az, now)
    angles = [ax ,ay, az]
    print("Angulos recebidos pelo esp: ", angles)
    matrixAngulos.append(angles)

    #aqui seria o processamento dos dados pela rede neural adquirindo os dados pela matrixAngulo
    #ou no próprio esp na parte depois da coleta

    return "200"

@application.route('/print-matrix',methods=['GET'])
def matrix_print():
    print(matrixAngulos)
    return matrixAngulos

@application.route('/canvas-data',methods=['GET'])
def get_data():
    def processed_data():
        while True:
            while matrixAngulos == []:
                time.sleep(1)
            ax = matrixAngulos[0][0]
            ay = matrixAngulos[0][1]
            az = matrixAngulos[0][2]
            print("Angulos enviados para o html: ",matrixAngulos[0])
            del matrixAngulos[0]
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value0': ax,'value1': ay, 'value2': az })
            yield f"data:{json_data}\n\n"

    return Response(processed_data(),mimetype='text/event-stream')

if __name__ == '__main__':
    application.run(host = '0.0.0.0', debug=True, threaded=True)

## LINK PRA ACESSAR O CÓDIGO
## http://192.168.0.10:5000/
#http://localhost:5000/