import requests
import random
import time

api_key = '35WH7TZRZZWJ87NR'

def upload_to_thingspeak(api_key, temperature):
    payload = {'api_key': api_key, 'field1': temperature}
    response = requests.post('https://api.thingspeak.com/update', params=payload)
    if response.status_code == 200:
        print("Data uploaded successfully!")
    else:
        print("Failed to upload data:", response.text)

while True:
    #value between 0 and 100
    temperature = round(random.uniform(0, 100), 2)
    print("Generated temperature:", temperature)

    upload_to_thingspeak(api_key, temperature)
    
    time.sleep(15)
