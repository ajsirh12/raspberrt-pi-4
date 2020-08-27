#include <wiringPi.h>

#define LED 0

int main(){
	wiringPiSetup();
	pinMode(LED, OUTPUT);
	
	while(1){
		digitalWrite(LED,HIGH);
		delay(500);
		digitalWrite(LED,LOW);
		delay(500);
	}
	
	return 0;
}
