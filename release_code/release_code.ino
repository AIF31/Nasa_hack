//RoboInges
//07/10/23
// We include the library to control the servo
#include <Servo.h>
//String required to release the payload
char bomb_release = 'r';
//UART read variable
char keyword;
// We declare the variable to control the servo
Servo servoMotor;

void setup() {
  Serial.begin(9600);
  // We start the servo so that it starts working with pin 8
  servoMotor.attach(8);
  // We initialize the servomotor at angle 0
  servoMotor.write(0);
}

void loop(){
if(Serial.available()>0){
  //Reads from serial
  keyword = Serial.read();
  if(keyword == bomb_release){
    //Release package
    servoMotor.write(90);
    keyword='t';
    Serial.println("Bombs released");
    delay(10000);
    //Servo returned no stand position
    servoMotor.write(0);
  }
}
delay(50);
}
