//RoboInges
//07/10/23
#include <Arduino.h>
#if defined(ESP32)
  #include <WiFi.h>
  #include <SD.h>
#elif defined(ESP8266)
#endif
#include <Firebase_ESP_Client.h>

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Insert your network credentials
#define WIFI_SSID "Mi 9T Pro"
#define WIFI_PASSWORD "Aviones31"

// Insert Firebase project API Key
#define API_KEY "AIzaSyAJURRTV8547L1tU-dvIJI0dEmKEiEexi4"

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://nasa-hackaton-3568e-default-rtdb.firebaseio.com/" 

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
float floatValue;
bool signupOK = false;
//Function variables
int counter=0;
bool state;
//Ultrasonic Sensor setup
const int Trigger = 32;   //Pin digital 2 para el Trigger del sensor (Input pin)
const int Echo = 33;   //Pin digital 3 para el Echo del sensor (Output pin)
int t; //timepo que demora en llegar el eco
int distance; //distancia en centimetros
//set Counter function
void setCont(int counter){
  Firebase.RTDB.setInt(&fbdo, "Counter", counter);
}
//get state function
int getStates(){
  Firebase.RTDB.getInt(&fbdo, "State");
  state = fbdo.intData();
  return state;
}
//get distance
int getDistance(){
  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);  //Pulse every de 10us
  digitalWrite(Trigger, LOW);
  t = pulseIn(Echo, HIGH); 
  distance = t/59;
  return distance;
}
void setup(){
  Serial.begin(9600);
  //LED configuration
  pinMode(25,OUTPUT);
  pinMode(26,OUTPUT);
  //Ultrasonic configuration
  pinMode(Trigger, OUTPUT); 
  pinMode(Echo, INPUT);  
  digitalWrite(Trigger, LOW);
  //Initialize Wifi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    delay(100);
  }
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
  setCont(0);
}

void loop(){
  int dist = getDistance();
  if (Firebase.ready() && signupOK && dist <= 100){
    state = getStates();
    if((millis() - sendDataPrevMillis > 10000 || sendDataPrevMillis == 0)){
      sendDataPrevMillis = millis();
      counter++;
      setCont(counter);
    }
    if(state == 0){
      digitalWrite(26, HIGH);
      digitalWrite(25, LOW);
    }else if(state == 1){
      digitalWrite(26, LOW);
      digitalWrite(25, HIGH);
    }
  }else{
    digitalWrite(26, LOW);
    digitalWrite(25, LOW);
  }
  delay(50);
}
