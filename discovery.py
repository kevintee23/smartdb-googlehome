#This script will discover Google Home devices that is connected on your network


import requests
import json

response = requests.get("http://10.14.122.163:3000/device")
y = json.loads(response.content)

f = open("discovery.txt", "w")

count = 1

for item in y:
    f.write ('Speaker Name: '+ item['name']+"\n")
    f.write ('Speaker ID: '+ item['id']+"\n")
    f.write ('Port : '+str(item['address']['port'])+"\n")
    f.write ('Host : ' + item['address']['host']+"\n")
    f.write ("\n")

f.close()

print ('Copy the Speaker ID that you would like to use...')
print ('Run python google_setup.py to finish configuring...')
print ('If you do not see your device, please run this script again.')
print ('If you add more Google device later and would like to use it, run this script again')
