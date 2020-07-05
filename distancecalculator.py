import pandas as pd
import numpy as np

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
#For this demo, we have used  Harold M. Brathwaite Secondary School as the current location
currentlatitude, currentlongitude = 43.739408, -79.770568

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