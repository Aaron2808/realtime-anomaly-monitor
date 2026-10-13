import random
import time
import json
from datetime import datetime, timezone

#set_temperature = 30
#temp = 28

while False:

    change = random.uniform(-0.5, 0.5)
    temp = temp + change

    correction = (set_temperature - temp) * 0.1

    temp = temp + correction

    print(round(temp,2))


    time.sleep(2)


def next_reading(current, operating_min, operating_max, noise=0.1):
    change = random.uniform(-(noise), noise)
    current = current + change

    midpoint = (operating_max + operating_min)/2
    correction = (midpoint - current) * 0.1
    current = current + correction

    return current


while False:
    temp = next_reading(temp, 20, 40)

    print(round(temp,2))
    time.sleep(1)


with open('simulator/config.json') as f:
    equipment_values = json.load(f)

  
for name, metrics in equipment_values.items():
    for metric, value in metrics.items():
        value['current'] = (value['max'] + value['min'])/2


while True:
    currentTime = datetime.now(timezone.utc).isoformat()

    for name, metrics in equipment_values.items():
        for metric, value in metrics.items():
            value["current"] = next_reading(value["current"], value["min"], value["max"], value["noise"])

            reading = {
                   "timestamp" : currentTime,
                   "machine_id" : name,
                   "metric" : metric,
                   "value" : round(value['current'],2)
               }
           
            print(json.dumps(reading))

    
  
    time.sleep(1)