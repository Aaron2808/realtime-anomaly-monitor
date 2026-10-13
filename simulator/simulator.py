import random
import time
import json
from datetime import datetime, timezone
from pathlib import Path

import requests


def next_reading(current, operating_min, operating_max, noise=0.1):
    change = random.uniform(-(noise), noise)
    current = current + change

    midpoint = (operating_max + operating_min)/2
    correction = (midpoint - current) * 0.1
    current = current + correction

    return current


CONFIG_PATH = Path(__file__).parent / "config.json"

with open(CONFIG_PATH) as f:
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

            requests.post("http://localhost:8080/readings", json=reading)

    
  
    time.sleep(1)