import random
import time


set_temperature = 30
temp = 28

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


equipment_values = {

    "air_compressor" : {
        "vibration" : {
            "current" : 5,
            "min" : 0,
            "max" : 10, 
            "noise" : 0.2,
        },

        "temp":{
            "current" : 30,
            "min" : 20,
            "max" : 40, 
            "noise" : 1,
        },

        "pressure": {
            "current" : 60,
            "min" : 0,
            "max" : 120,
            "noise" : 5,
        },
    },

    "welder" : {
         "vibration" : {
                "current" : 5,
                "min" : 0,
                "max" : 10,
                "noise" : 0.2, 
            },
        
            "temp":{
                "current" : 30,
                "min" : 20,
                "max" : 40, 
                "noise" : 1,
            },
                
            "pressure": {
                "current" : 60,
                "min" : 0,
                "max" : 120,
                "noise" : 5,
            },
    }
}


for name, metrics in equipment_values.items():
    for metric, value in metrics.items():
        print(f"Name: {metric} Value: {value}")


while True:
    for name, metrics in equipment_values.items():
        for metric, value in metrics.items():
            value["current"] = next_reading(value["current"], value["min"], value["max"], value["noise"])

            print(f"Name: {name} Metric: {metric} Value: {round(value['current'],2)}")

    time.sleep(1)