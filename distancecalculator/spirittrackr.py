import pandas as pd
import numpy as np

#Haversine Formula to calculate the distance between two points on a sphere, (code sample from Google)
def haversine_distance(latitude1, longitude1, latitude2, longitude2):
   r = 6371
   phi1 = np.radians(latitude1)
   phi2 = np.radians(latitude2)
   delta_phi = np.radians(latitude2 - latitude1)
   delta_lambda = np.radians(longitude2 - longitude1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
   return np.round(res, 2)

#In a real app, this current latitude and longitude would be fetched in real time via Google Maps API
#However, Google Maps API is paid, so we cannot use their services at this time
#For this demo, the user manually enters their latitude and longitude
currentlatitude = float(input("What is your current latitude?"))
currentlongitude = float(input("What is your current longitude?"))

landmarks = pd.DataFrame(data={
   'Landmark': ['Kwakiutl Statue', 'Neyagawa Park', 'Bronte Harbour'],
   'Lat' : [43.723047, 43.457796, 43.394591],
   'Lon' : [-79.721298, -79.729519, -79.708563]
})

distances_km = []
for row in landmarks.itertuples(index=False):
   distances_km.append(
       haversine_distance(currentlatitude, currentlongitude, row.Lat, row.Lon)
   )

landmarks['Distance (km)'] = distances_km

print (landmarks)

#Output to determine whether or not to send notification
if distances_km[0] < 5:
   print("You are nearby the Kwakiutl Statue!")
else:
   print("You are not nearby the Kwakiutl Statue!")

if distances_km[1] < 5:
   print("You are nearby Neyagawa Park!")
else:
   print("You are not nearby Neyagawa Park!")

if distances_km[2] < 5:
   print("You are nearby Bronte Harbour!")
else:
   print("You are not nearby Bronte Harbour!")
