import requests

api_key = '35WH7TZRZZWJ87NR'
temperature = 30  # Example temperature value

# Format the data as per ThingSpeak requirements
payload = {'api_key': api_key, 'field1': temperature}

# Make the HTTP POST request to upload the data
response = requests.post('https://api.thingspeak.com/update', params=payload)

# Check the response
if response.status_code == 200:
    print("Data uploaded successfully!")
else:
    print("Failed to upload data:", response.text)
