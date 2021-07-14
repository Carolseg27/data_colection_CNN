# data_colection_CNN
O objetivo desse projeto foi de classificar movimentos do braço usando redes neurais artificiais.

O código com o nome de Gráfico_flask foi escrito em Python para armazenar em um banco de dados, SQLite3, os dados do acelerômetro e do giroscópio do sensor MPU6050 e formar um gráfico dinâmico numa página web. A coleta das informações do sensor se deu a partir do ESP8266, usando a IDE do arduino . O gráfico foi feito em JavasScript, com o eixo vertical representando as acelerações obtidas em cada coordenada (X, Y e Z), em um formato bruto, e o eixo horizontal, a data e a hora do recebimento, a foto do mesmo está com o nome de TCP_Graph, na pasta photo_results. Emprega o protocolo TCP (Protocolo de Controle de Transmissão) para enviar a informação, verificando e reenviando pacotes perdidos e remontando-os em ordem, logo para cada dado enviado existe uma abertura e um fechamento de uma conexão para obter o controle da sequência de recebimento dos mesmos. A consequência é uma baixa frequência de transmissão e grande perda de pacotes.

Na pasta esp_socket_CNN, usou-se um código de socket em Python para enviar os dados do sensor ao banco de dados, dessa vez em CSV. Utiliza o protocolo UDP (do inglês: User Datagram Protocol) que envia os dados sem que haja um controle de transmissão, logo possui baixa latência em relação ao código do flask. Nessa pasta, tem os códigos das CNNs(Convolutional Neural Network) para classificar as posições e os movimentos do braço, juntamente com os dados coletados para cada classificação.

Na pasta photo_results, são contidos os resultados das CNNs com a demonstração dos movimentos do braço feitos.

