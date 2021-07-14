import socket
import datetime
import csv
import pandas as pd
from banco_dados import BancoDados 

#One warning before using this code to receive the data from esp, turn off the W10's(Windows 10) firewall, the public network.   
#Part 1

bd = BancoDados
#bd.create_table_acc()
#bd.create_table_gyr()

UDP_IP =  ""  #"IP of the computer that will receive the data"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

file_name = "shoulder_press"
activity = "shoulder_press"
n = 1200 # the number of data required by the user

with open(file_name +'.csv', 'w', 1) as f: #create a csv file
    writer = csv.writer(f)
        
    for i in range(0,n):
        date_time = datetime.datetime.now() # year-month-day hour:min:sec.millisec
        now = str(date_time).split('.')[0] # everything the same as above without the milliseconds 
        
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

        data = str(data, 'UTF-8') #It converts bytes to string 
        data = ((data.replace('[', '').replace(']', '')).split(',')) #It replaces '[' and ']' to an empty space('')
    
        acc_x, acc_y, acc_z = round(float(data[0]),3), round(float(data[1]),3), round(float(data[2]),3)
        gyr_x, gyr_y, gyr_z = round(float(data[3]),3), round(float(data[4]),3), round(float(data[5]),3)
        
        #bd.insert_val_acc(acc_x, acc_y, acc_z, now)
        #bd.insert_val_gyr(gyr_x, gyr_y, gyr_z, now)
        writer.writerow([activity, acc_x, acc_y, acc_z, now])
        print(data)
df = pd.read_csv(file_name + '.csv')
df.to_csv(file_name + '.csv', header=['Activity', 'X', 'Y', 'Z', 'Time'], index=False)
        
'''
# Part 2

# After collecting the data, you need to comment out the above part 1, 
# and uncomment this part 2 and then executing this part will merge the files into one.
# I chose '.head(3530)' because it's the lowest value of samples that I have, therefore I'm balancing the data. 

data1 = pd.read_csv('abd.csv')
data2 = pd.read_csv('flex.csv')
data3 = pd.read_csv('shoulder_press.csv')

abd = data1.head(99)
flex = data2.head(99)
shoulder = data3.head(99)

abd.to_csv('abd_pred.csv', header=['Activity', 'X', 'Y', 'Z', 'Time'], index=False)
flex.to_csv('flex_pred.csv', header=['Activity', 'X', 'Y', 'Z', 'Time'], index=False)
shoulder.to_csv('shoulder_pred.csv', header=['Activity', 'X', 'Y', 'Z', 'Time'], index=False)

data1 = data1.loc[100:1100]
data2 = data2.loc[100:1100]
data3 = data3.loc[100:1100]

concate_data = pd.concat([data1,data2,data3])
concate_data.to_csv("all.csv", index=False) 
'''
