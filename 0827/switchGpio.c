#include <wiringPi.h>
#include <stdio.h>

#define LED 1
#define SW 5

int switchControl(){
	
	pinMode(SW, INPUT);
	pinMode(LED, OUTPUT);
	
	while(1){
		if(digitalRead(SW) == LOW){
			printf("push %d\n", digitalRead(SW));
			digitalWrite(LED,HIGH);
			delay(1000);
			digitalWrite(LED,LOW);
		}
		delay(10);
	}
	return 0;
}

int main(){
	wiringPiSetup();
	switchControl();
	return 0;
}
