#include <wiringPi.h>

#define LED 0
#define LIGHT_TIME 50

int main(){
	wiringPiSetup();
	pinMode(LED, OUTPUT);
	int bright = 0;
	int chg = 1;
	
	while(1){
		digitalWrite(LED,HIGH);
		delay(LIGHT_TIME + bright);
		digitalWrite(LED,LOW);
		delay(LIGHT_TIME - bright);
		
		bright += chg;
		
		if(bright == 50 || bright == -50){
			chg *= -1;
		}
	}
	
	return 0;
}
