#define trigPin 12
#define echoPin 13
int buzzer = 8; 
int ledPin= 6;  
int duration, distance;  

void setup() {
        Serial.begin (9600); 
        
        pinMode(trigPin, OUTPUT); 
        pinMode(echoPin, INPUT);
        pinMode(Buzzer, OUTPUT);
        pinMode(ledPin, OUTPUT);
}

void loop() {

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
