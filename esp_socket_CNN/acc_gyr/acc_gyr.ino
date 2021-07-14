#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;
WiFiUDP UDP;

String acc; // accelerometer data
String gyr; //gyroscope data
String acc_gyr; //both are sent together 
int value = 0; 
const char* ssid = "CHARLOTTE"; //replace with your own wifi ssid 
const char* password = "doce1210"; //replace with your own //wifi ssid password 

const char* host = "192.168.0.9";//IPV4->w10-> terminal and then ipconfig to see the IPV4

const int port = 5000; //porta

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); 

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  delay(100);
  
  //wifi initiating connection
  delay(10); // We start by connecting to a WiFi network Serial.println();
  Serial.println(); 
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  /* Explicitly set the ESP8266 to be a WiFi-client, otherwise, it by default, 
  would try to act as both a client and an access-point and could cause network-issues 
  with your other WiFi-devices on your WiFi-network. */
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
  delay(500);
  Serial.print(".");}
  
  Serial.println("");
  Serial.println("WiFi connected"); 
  Serial.println("IP address: "); 
  Serial.println(WiFi.localIP());
}

void loop() {

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  //[0.02, 0.18, 10.02, -0.03, -0.08, -0.05]
  
  a.acceleration.x = a.acceleration.x - 0.02;
  a.acceleration.y = a.acceleration.y - 0.20;
  a.acceleration.z = a.acceleration.z - 0.24;
  g.gyro.x = g.gyro.x + 0.03;
  g.gyro.y = g.gyro.y + 0.08;
  g.gyro.z = g.gyro.z + 0.05;

  acc = "[" + String(a.acceleration.x) + ", " + String(a.acceleration.y) + ", " + String(a.acceleration.z) + ", "; // acc = [m/s^2]
  gyr = String(g.gyro.x) + ", " + String(g.gyro.y) + ", " + String(g.gyro.z) + "]"; // gyr = [rad/s]
  acc_gyr = acc + gyr;
  Serial.println(acc_gyr);
  //String temperature = String(temp.temperature); // temperature = [°C]
  //Serial.println(acc_gyr);
  //Serial.println(temperature);

  /* Sending data */
  
  delay(200); 
  ++value; 
  Serial.print("connecting to ");
  Serial.println(host); // Use WiFiClient class to create TCP connections
  WiFiClient client;

  /* We now create a URI for the request this url 
  contains the informtation we want to send to the server
  if esp8266 only requests the website, the url is empty */

  String url = acc_gyr;

    //aqui eu crio a conexão UDP para enviar os valores da string url
    UDP.beginPacket(host, port); //informo que vou enviar pro ip "host" na porta "port"
    char copy[50]; //crio esse char pois o udp write so aceita char e nao string
    url.toCharArray(copy, 50); //transformo a string em vetor de char
    int i = 0;
    while (copy[i] != 0)
    UDP.write((uint8_t)copy[i++]);//escrevo no socket udp o char com os valores da string
    UDP.endPacket();
   // UDP.write(copy); //escrevo no socket udp o char com os valores da string
    //UDP.endPacket(); //finalizo

}
