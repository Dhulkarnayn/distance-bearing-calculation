import math
R = 6371e3 #Radius of earth in metres
def distance_bearing(homeLattitude, homeLongitude, destinationLattitude, destinationLongitude):
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
def destination_location(homeLattitude, homeLongitude, distance, bearing):
	rlat1 = homeLattitude * (math.pi/180) 
	rlon1 = homeLongitude * (math.pi/180)
	d = distance
	bearing = bearing * (math.pi/180) #Converting bearing to radians
	rlat2 = math.asin((math.sin(rlat1) * math.cos(d/R)) + (math.cos(rlat1) * math.sin(d/R) * math.cos(bearing)))
	rlon2 = rlon1 + math.atan2((math.sin(bearing) * math.sin(d/R) * math.cos(rlat1)) , (math.cos(d/R) - (math.sin(rlat1) * math.sin(rlat2))))
	rlat2 = rlat2 * (180/math.pi) #Converting to degrees
	rlon2 = rlon2 * (180/math.pi) #converting to degrees
	location = [rlat2, rlon2]
	return location