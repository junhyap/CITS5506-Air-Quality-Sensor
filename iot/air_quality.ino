#include <GP2YDustSensor.h>    // Dust Sensor library
const uint8_t SHARP_LED_PIN = 7;    // Sharp Dust/particle sensor Led Pin
const uint8_t SHARP_VO_PIN = A0;    // Sharp Dust/particle analog out pin used for reading 
GP2YDustSensor dustSensor(GP2YDustSensorType::GP2Y1014AU0F, SHARP_LED_PIN, SHARP_VO_PIN);

#include <Wire.h>
#include "SparkFunBME280.h"    // BME280 library
BME280 mySensor;

#include "ccs811.h"    // CCS811 library
CCS811 ccs811(13); 

float TempF;
float TempC;

void setup() {
  // Initialize a serial connection for reporting values to the host
  Serial.begin(9600);
  
  // Initiate the Wire library
  Wire.begin();
  dustSensor.begin();
  
  // Begin communication over I2C
  mySensor.beginI2C();
  ccs811.begin();
  ccs811.start(CCS811_MODE_1SEC);

}

void loop() {

  uint16_t eco2, etvoc, errstat, raw;
  ccs811.read(&eco2,&etvoc,&errstat,&raw);

  TempF = mySensor.readTempF();
  TempC = (TempF-32)*.5556;
  Serial.print(int(TempC));
  Serial.print(";");

  Serial.print(mySensor.readFloatHumidity(), 0);
  Serial.print(";");

  Serial.print(dustSensor.getDustDensity());
  Serial.print(";");

  Serial.print(int(eco2));
  Serial.print(";");
  
  Serial.print(int(etvoc));    
  Serial.println();

  delay(2000);
  
}

