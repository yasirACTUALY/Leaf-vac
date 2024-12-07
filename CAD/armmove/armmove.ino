#include <Servo.h>

// Create Servo objects
Servo Servo1, Servo2, Servo3, Servo4;

// Pin assignments
int servoPin1 = 9, servoPin2 = 10, servoPin3 = 11, servoPin4 = 6;

// Current angles for each servo
int currentAngle1 = 0, currentAngle2 = 0, currentAngle3 = 0, currentAngle4 = 0;

void setup() {
  Serial.begin(9600);

  // Attach servos to their respective pins
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
  Servo3.attach(servoPin3);
  Servo4.attach(servoPin4);

  // Initialize all servos at 0 degrees
  Servo1.write(currentAngle1);
  Servo2.write(currentAngle2);
  Servo3.write(currentAngle3);
  Servo4.write(currentAngle4);

  delay(1000); // Allow servos to initialize
  Serial.println("Servo control initialized.");
}

// General function to move a servo to a specified angle at a reduced speed
void moveServoToAngle(Servo &servo, int &currentAngle, int targetAngle, int speed) {
  targetAngle = constrain(targetAngle*0.75, 0, 180);
  Serial.println("Moving servo to: " + String(targetAngle) + " degrees");

  if (currentAngle < targetAngle) {
    for (int angle = currentAngle; angle <= targetAngle; angle++) {
      servo.write(angle);
      delay(speed);
    }
  } else {
    for (int angle = currentAngle; angle >= targetAngle; angle--) {
      servo.write(angle);
      delay(speed);
    }
  }

  currentAngle = targetAngle;
}

void loop() {
  // Example movements for all servos
  moveServoToAngle(Servo3, currentAngle3, 90, 15); // Move Servo3 to 135
  delay(1000);
  
  moveServoToAngle(Servo4, currentAngle4, 90, 15); // Move Servo4 to 180
  delay(1000);

  moveServoToAngle(Servo1, currentAngle1, 0, 15);  // Move Servo1 to 90
  moveServoToAngle(Servo2, currentAngle2, 0, 15);  // Move Servo2 to 45

  moveServoToAngle(Servo3, currentAngle3, 45, 15); // Move Servo3 to 135
  delay(1000);
  
  moveServoToAngle(Servo4, currentAngle4, 45, 15); // Move Servo4 to 180

  delay(1000); // Wait for 1 second

  moveServoToAngle(Servo1, currentAngle1, 180, 15);   // Move Servo1 to 0
  moveServoToAngle(Servo2, currentAngle2, 180, 15);  // Move Servo2 to 90

  moveServoToAngle(Servo3, currentAngle3, 135, 15);  // Move Servo3 to 45
  delay(1000);

  moveServoToAngle(Servo4, currentAngle4, 135, 15);  // Move Servo4 to 90

  delay(1000); // Wait for 1 second
}
