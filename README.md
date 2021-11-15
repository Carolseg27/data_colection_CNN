# data_colection_CNN

* Objetivo desse projeto: classificar movimentos do braço usando redes neurais artificiais.

* Função de cada código e pasta:

    1 - O código com o nome de Gráfico_flask foi escrito em Python para armazenar em um banco de dados, SQLite3, os dados do acelerômetro e do giroscópio do sensor MPU6050 e formar um gráfico dinâmico numa página web. A coleta das informações do sensor se deu a partir do ESP8266, usando a IDE do arduino . O gráfico foi feito em JavasScript, com o eixo vertical representando as acelerações obtidas em cada coordenada (X, Y e Z), em um formato bruto, e o eixo horizontal, a data e a hora do recebimento, a foto do mesmo está com o nome de TCP_Graph, na pasta photo_results. Emprega o protocolo TCP (Protocolo de Controle de Transmissão) para enviar a informação, verificando e reenviando pacotes perdidos e remontando-os em ordem, logo para cada dado enviado existe uma abertura e um fechamento de uma conexão para obter o controle da sequência de recebimento dos mesmos. A consequência é uma baixa frequência de transmissão e grande perda de pacotes.

    2 - Na pasta esp_socket_CNN, usou-se um código de socket em Python para enviar os dados do sensor ao banco de dados, dessa vez em CSV. Utiliza o protocolo UDP (do inglês: User Datagram Protocol) que envia os dados sem que haja um controle de transmissão, logo possui baixa latência em relação ao código do flask. Nessa pasta, tem os códigos das CNNs(Convolutional Neural Network) para classificar as posições e os movimentos do braço, juntamente com os dados coletados para cada classificação.

   3 - Na pasta photo_results, estão contidos os resultados das CNNs com a demonstração dos movimentos do braço feitos.

* Como utilizar os códigos da pasta esp_socket_CNN?

        Nesta pasta, há uma outra chamada acc_gyr, ao fazer o upload do arquivo acc_gyr.ino no ESP8266, coletam-se os dados do sensor MPU6050 (escolhendo que tipo de dado serão armazenados, sendo movimento ou posição), e ao executar conjuntamente o arquivo sockreceive.py, esses dados são armazenados em um banco de dados. Esses dados podem ser vistos no terminal enquanto o código de socket é executado, caso isso não aconteça e o usuário estiver usando Windows, considere a desativação do Firewall.
        Após a coleta, no Jupyter Notebook, selecionam-se os bancos de dados que farão parte da classificação, ou seja, um banco com todas as classes de atividades juntas, e outros com somente uma classe cada para testarem a CNN que será criada a partir desse banco de dados maior com todas as classes juntas, depois executa-se o arquivo CNN_colab.ipynb ou cnn_position.py dependendo da categoria do dado que foi escolhida. Esses códigos das CNNs foram divididos em 2 partes, a primeira para criar a CNN e a segunda para testar o desempenho dela em novas amostras.


