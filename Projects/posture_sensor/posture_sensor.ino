const int buttonOneBlue = 12;
const int buttonTwoGreen = 9;
const int buttonThreeRed = 6;
const int bipSound = 13;
const int pressureSensor = 10;

const int pressurePin1 = A0;

int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int pressureState = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600); 
  pinMode (bipSound, OUTPUT);
  pinMode (buttonOneBlue, INPUT);
  pinMode (buttonTwoGreen, INPUT);
  pinMode (buttonThreeRed, INPUT);
  pinMode (pressureSensor, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState1 = digitalRead (buttonOneBlue);
  buttonState2 = digitalRead (buttonTwoGreen);
  buttonState3 = digitalRead (buttonThreeRed);
  pressureState = digitalRead (pressureSensor);

  if (pressureSensor == HIGH) {
     if (buttonState1 == 1 && buttonState2==1 &&  buttonState3 == 1){
      Serial.println ("AllButtonPressed");
      digitalWrite (bipSound, LOW);
    }
    else if  (buttonState1 == 0 && buttonState2==1 &&  buttonState3==1){
      Serial.println ("ButtonOneNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(500);
      digitalWrite (bipSound, LOW);
      delay(5000);
      }
      else if  (buttonState1 == 1 && buttonState2==0 &&  buttonState3==1){
      Serial.println ("ButtonTwoNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(500);
      digitalWrite (bipSound, LOW);
      delay(5000);
      }
      else if  (buttonState1 == 1 && buttonState2==1 &&  buttonState3==0){
      Serial.println ("ButtonThreeNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(500);
      digitalWrite (bipSound, LOW);
      delay(5000);
      }
      else if  (buttonState1 == 0 && buttonState2 == 0 &&  buttonState3 == 1){
      Serial.println ("ButtonOneAndTwoNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(1000);
      digitalWrite (bipSound, LOW);
      delay(1000);
      }
      else if  (buttonState1 == 0 && buttonState2 == 1 &&  buttonState3 == 0){
      Serial.println ("ButtonOneAndThreeNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(1000);
      digitalWrite (bipSound, LOW);
      delay(1000);
      }
      else if  (buttonState1 == 1 && buttonState2 == 0 &&  buttonState3 == 0){
      Serial.println ("ButtonTwoAndThreeNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(1000);
      digitalWrite (bipSound, LOW);
      delay(1000);
      }
    else if  (buttonState1 == 0 && buttonState2 == 0 &&  buttonState3 == 0){
      Serial.println ("AllButtonNotPressed");
      digitalWrite (bipSound, HIGH);
      delay(500);
      digitalWrite (bipSound, LOW);
      delay(100);
    }

  }
      
}
