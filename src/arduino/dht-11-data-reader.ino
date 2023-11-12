#include <DHT.h>
#include "string.h"

#define DHTPIN 2      // Pin where the DHT11 is connected
#define DHTTYPE DHT11 // DHT sensor type

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println(F("{\"error\": \"Failed to read from DHT sensor!\""));
    return;
  }

  Serial.print(F("{\"temperature\": "));
  Serial.print(temperature);
  Serial.print(F(", \"humidity\": "));
  Serial.print(humidity);
  Serial.println(F("}"));
}