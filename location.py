from distance_bearing import destination_location
dest_loc =[]
print ("=====Decimals_Please=====")
print ("=====Enter_the_Latitude_of_Current_location=====")
lat1 = float(input())
print ("=====Enter_the_Longitude_of_Current_location=====")
lon1 = float(input())
print ("=====Enter_Distance_between_home_and_destination")
distance = float(input())
print ("=====Enter_bearing_angle_between_home_and_destination")
bearing = float(input())
dest_loc = destination_location(lat1, lon1, distance, bearing)
print ("Geographic_coordinates_of_destination_is ", dest_loc)
