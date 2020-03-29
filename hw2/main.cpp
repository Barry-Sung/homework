#include "mbed.h"

Serial pc( USBTX, USBRX );
AnalogOut Aout(DAC0_OUT);
AnalogIn Ain(A0);
DigitalIn  Switch(SW3);
DigitalOut redLED(LED1);
DigitalOut greenLED(LED2);
BusOut display(D6, D7, D9, D10, D11, D5, D4, D8);
char table[3] = {0x3F, 0x06, 0xBF};
int sample = 128;

int i;

float ADCdata[128];

int main(){

  for (i = 0; i < sample; i++){

    Aout = Ain;

    ADCdata[i] = Ain;

    wait(1./sample);

  }

  for (i = 0; i < sample; i++){

    pc.printf("%1.3f\r\n", ADCdata[i]);

    wait(0.1);

  }

  while(1){

    if( Switch == 1 ){

      greenLED = 0;

      redLED = 1;

      display = table[1];
      
      wait(1);

      display = table[0];
      
      wait(1);

      display = table[2];
      
      wait(1);  



    }

    else{

      redLED = 0;

      greenLED = 1;

    }

  }
  
  float j;

  while(1){

    for( j=0; j<2; j+=0.05 ){

      Aout = 0.5 + 0.5*sin(j*3.14159);

      wait(0.001);

    }

  }

}