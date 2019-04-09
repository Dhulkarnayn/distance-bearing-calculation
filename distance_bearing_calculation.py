import math
dist_brng = []
def distance_bearing(homeLattitude, homeLongitude, destinationLattitude, destinationLongitude):
	R = 6371e3 #Radius of earth in metres
	rlat1 = homeLattitude * (math.pi/180) 
	rlat2 = destinationLattitude * (math.pi/180) 
	rlon1 = homeLongitude * (math.pi/180) 
	rlon2 = destinationLongitude * (math.pi/180) 
	dlat = (destinationLattitude - homeLattitude) * (math.pi/180)
	dlon = (destinationLongitude - homeLongitude) * (math.pi/180)
	#haversine formula to find distance
	a = (math.sin(dlat/2) * math.sin(dlat/2)) + (math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon/2) * math.sin(dlon/2)))
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	distance = R * c #distance in metres
	#formula for bearing
	y = math.sin(rlon2 - rlon1) * math.cos(rlat2)
	x = math.cos(rlat1) * math.sin(rlat2) - math.sin(rlat1) * math.cos(rlat2) * math.cos(rlon2 - rlon1)
	bearing = math.atan2(y, x) #bearing in radians
	bearingDegrees = bearing * (180/math.pi)
	out = [distance, bearingDegrees]
	return out
#Getting inputs from the user
print ("=====Decimals_Please=====")
print ("=====Enter_the_Latitude_of_Current_location=====")
lat1 = float(input())
print ("=====Enter_the_Longitude_of_Current_location=====")
lon1 = float(input())
print ("=====Enter_the_Latitude_of_Destination=====")
lat2 = float(input())
print ("=====Enter_the_Longitude_of_Destination=====")
lon2 = float(input())
dist_brng = distance_bearing(lat1, lon1, lat2, lon2)
#To display the distance and bearing
print ('Distance between the home and destination is ', dist_brng[0], ' m')
print ('Bearing angle between home and destination is ', dist_brng[1], 'degree')