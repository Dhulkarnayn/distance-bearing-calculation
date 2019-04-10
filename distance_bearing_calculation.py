from distance_bearing import distance_bearing
dist_brng = []
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
