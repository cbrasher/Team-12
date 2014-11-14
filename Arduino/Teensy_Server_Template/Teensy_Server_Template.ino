#include <Streaming.h>

//Constants go in this block
//==========================
String Sbracket;
String Cbracket;
String quote;
String colon;
String comma;
String id1, id2, id3, s1, s2, s3;
String SendString;
String RecString;
String ConstructedString;
const int comm_t = 100;   //rate of data transmission
unsigned long lastComm = 0;
String Data1, Data2, Data3; 
String Part1, Part2, Part3, Part4, Part5, Part6;
//==========================

void setup() {
  Serial.begin(57600);
  Sbracket = String("'{"); 
  Cbracket = String("}'");
  quote = String('"');
  colon = String(":");
  comma = String(",");
  id1 = "id1"; id2 = "id2"; id3 = "id3";
  s1 = "Sensor1"; s2 = "Sensor2"; s3 = "Sensor3";
  
  randomSeed(analogRead(0));
}

//Functions that the Program has to call go here
//==============================================
String Reading1(){
  int randreading1 = random(0 ,1000);
  String randNumber1 = String(randreading1);
  return randNumber1;
}
String Reading2(){
  int randreading2 = random(0 ,1000);
  String randNumber2 = String(randreading2);
  return randNumber2;
}
String Reading3(){
  int randreading3 = random(0 ,1000);
  String randNumber3 = String(randreading3);
  return randNumber3;
}
void HeartBeat(){
  //double randNum = random(0.0, 2000.0);
  //Serial << randNum << endl;
  Serial.flush();
  delay(100);
}
String ConstructString(){
  Data1 = String(Reading1());
  Data2 = String(Reading2());
  Data3 = String(Reading3());
  Part1 = String(quote+id1+quote+colon+quote+s1+quote+comma);
  Part2 = String(quote+s1+quote+colon+Data1+comma);
  Part3 = String(quote+id2+quote+colon+quote+s2+quote+comma);
  Part4 = String(quote+s2+quote+colon+Data2+comma);
  Part5 = String(quote+id3+quote+colon+quote+s3+quote+comma);
  Part6 = String(quote+s3+quote+colon+Data3);
  ConstructedString = String(Part1+Part2+Part3+Part4+Part5+Part6);
  return ConstructedString;
}
void SendSerial(){
 unsigned long currentMillis = millis();
 
  if(currentMillis - lastComm > comm_t) 
    lastComm = currentMillis;   

  Serial.print(SendString); Serial.println(' ');
}
void RecieveSerial(){
  while(Serial.available()){
    delay(3);
    if (Serial.available() > 0){
      char c = Serial.read();
      readString += c;
    }
  }
  if (readString.length() >0) {
      //Serial.println(readString); //see what was received      
      RecString = readString.substring(0, 1);
      
      readString="";
   )
}
//==============================================

void loop() {
   //RecieveSerial();
  SendString = ConstructString();
  SendSerial();
  HeartBeat();
}
