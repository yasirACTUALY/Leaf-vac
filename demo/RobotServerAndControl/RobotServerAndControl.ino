#include <WiFi.h>
#include <NetworkClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>

const char *ssid = "EyeRobot2";
const char *password = "IEDSucks";

WebServer server(80);
const int LeftBack  = 5;  // Pin 15 of L293 backwards
const int LeftForward  = 6;  // Pin 10 of L293 forwards
//Motor B
const int RightBack  = 2; // Pin  7 of L293 
const int RightForward  = 3;  // Pin  2 of L293

////////// Enable/PWM Pin //////////
const int mRspeed = 4; //enabler
const int mLspeed = 7; //enabler



// Leash Variables
int JoyX = 0, JoyY = 0, rollAngle = 0, pitchAngle = 0, AccelX = 0, AccelY = 0, AccelZ = 0, ButtonZ = 0, ButtonC = 0;

void handleRoot() {
  Serial.println("pong");
  server.send(200, "text/plain", "hello from esp32!");
}

void getLeashData()
{
  Serial.println("send leash data");

  // Webstuff
  String message = "";

  message += JoyX;
  message += ",";
  message += JoyY;
  message += ",";
  message += rollAngle;
  message += ",";
  message += pitchAngle;
  message += ",";
  message += AccelX;
  message += ",";
  message += AccelY;
  message += ",";
  message += ButtonZ;
  message += ",";
  message += ButtonC;

  server.send(200, "text/plain", message);
}

void driveForward()
{
  Serial.println("Recieved forward command");
  digitalWrite(LeftBack,HIGH);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,HIGH);
  digitalWrite(RightForward,LOW);
  delay(2000);
  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,LOW);


  // Do whatever you need to do, as long as last line gets called. 
  // This only gets called once per command, you probably want to
  // update globals and have driving logic in Update()

  server.send(200, "text/plain", "Driving forward");
}

void driveLeft()
{
  Serial.println("Recieved left command");
  digitalWrite(LeftBack,HIGH);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,HIGH);
  delay(3000);

  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,LOW);
  // Same as above

  server.send(200, "text/plain", "Driving left");
}

void driveRight()
{
  Serial.println("Recieved right command");

  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,HIGH);
  digitalWrite(RightBack,HIGH);
  digitalWrite(RightForward,LOW);
  delay(3000);

  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,LOW);

  // Same as above

  server.send(200, "text/plain", "Driving right");
}

void driveBackwards()
{
  Serial.println("Recieved backwards command");

  // Same as above

  Serial.println("Recieved left command");
  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,HIGH);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,HIGH);
  delay(1000);

  digitalWrite(LeftBack,LOW);
  digitalWrite(LeftForward,LOW);
  digitalWrite(RightBack,LOW);
  digitalWrite(RightForward,LOW);

  server.send(200, "text/plain", "Driving backwards");
}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);

}

void setup(void) {
  Serial.begin(115200);


    Serial.begin(9600);
    pinMode(LeftBack, OUTPUT);
    pinMode(LeftForward, OUTPUT);
    pinMode(RightBack, OUTPUT);
    pinMode(RightForward, OUTPUT);
  if (!WiFi.softAP(ssid, password)) {
    Serial.println("Soft AP creation failed.");
    while (1);
  }  
  Serial.println("begun wifi");
  Serial.println(WiFi.softAPIP());

  server.on("/", handleRoot);

  server.on("/leash", getLeashData);
  server.on("/forward", driveForward);
  server.on("/left", driveLeft);
  server.on("/right", driveRight);
  server.on("/backwards", driveBackwards);

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
  delay(2);  //allow the cpu to switch to other tasks
}