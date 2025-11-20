import typing
from BaseClasses import Location, Region, CollectionState

if typing.TYPE_CHECKING:
    from . import KRtDLWorld

BaseLocationID = 24102011 + 40

class KRtDLLocation(Location):
    game: str = "Kirby's Return to Dream Land"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: composite_location[location_name] for location_name in location_names}

StageNames = [
    "Cookie Country Stage 1 ",
    "Cookie Country Stage 2 ",
    "Cookie Country Stage 3 ",
    "Cookie Country Stage 4 ",
    "Cookie Country Stage 5 ",
    "Raisin Ruins Stage 1 ",
    "Raisin Ruins Stage 2 ",
    "Raisin Ruins Stage 3 ",
    "Raisin Ruins Stage 4 ",
    "Raisin Ruins Stage 5 ",
    "Onion Ocean Stage 1 ",
    "Onion Ocean Stage 2 ",
    "Onion Ocean Stage 3 ",
    "Onion Ocean Stage 4 ",
    "Onion Ocean Stage 5 ",
    "White Wafers Stage 1 ",
    "White Wafers Stage 2 ",
    "White Wafers Stage 3 ",
    "White Wafers Stage 4 ",
    "White Wafers Stage 5 ",
    "White Wafers Stage 6 ",
    "Nutty Noon Stage 1 ",
    "Nutty Noon Stage 2 ",
    "Nutty Noon Stage 3 ",
    "Nutty Noon Stage 4 ",
    "Nutty Noon Stage 5 ",
    "Nutty Noon Stage 6 ",
    "Egg Engines Stage 1 ",
    "Egg Engines Stage 2 ",
    "Egg Engines Stage 3 ",
    "Egg Engines Stage 4 ",
    "Egg Engines Stage 5 ",
    "Egg Engines Stage 6 ",
    "Dangerous Dinner Stage 1 ",
    "Dangerous Dinner Stage 2 ",
    "Dangerous Dinner Stage 3 ",
    "Dangerous Dinner Stage 4 ",
    "Another Dimension ",
]

locationincrement = 0
stage_completion_table = {}
for i in StageNames:
    if i != "Another Dimension ":
        stage_completion_table[i + "- Complete"] = BaseLocationID + locationincrement
        locationincrement += 1
#should end at ID 68
    
energy_sphere_table = {}
#Cookie Country 1
energy_sphere_table[StageNames[0] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[0] + "Room 5 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 2
energy_sphere_table[StageNames[1] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[1] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[1] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 3
energy_sphere_table[StageNames[2] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[2] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[2] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 4
energy_sphere_table[StageNames[3] + "Room 1 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[3] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[3] + "Room 7 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 1
energy_sphere_table[StageNames[5] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[5] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[5] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 2
energy_sphere_table[StageNames[6] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[6] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[6] + "Room 10 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 3
energy_sphere_table[StageNames[7] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[7] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[7] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[7] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 4
energy_sphere_table[StageNames[8] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[8] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[8] + "Room 7 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[8] + "Room 10 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 1
energy_sphere_table[StageNames[10] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[10] + "Room 9 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 2
energy_sphere_table[StageNames[11] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[11] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[11] + "Room 6 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 3
energy_sphere_table[StageNames[12] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[12] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[12] + "Room 10 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 4
energy_sphere_table[StageNames[13] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[13] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[13] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[13] + "Room 7 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[13] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 1
for i in range(1,3+1): #White Wafers 1
    energy_sphere_table[StageNames[15] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 2
for i in range(1,4+1): #White Wafers 2
    energy_sphere_table[StageNames[16] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 3
for i in range(1,4+1): #White Wafers 3
    energy_sphere_table[StageNames[17] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 4
for i in range(1,4+1): #White Wafers 4
    energy_sphere_table[StageNames[18] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 5
for i in range(1,4+1): #White Wafers 5
    energy_sphere_table[StageNames[19] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 1
for i in range(1,4+1): #Nutty Noon 1
    energy_sphere_table[StageNames[21] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 2
for i in range(1,4+1): #Nutty Noon 2
    energy_sphere_table[StageNames[22] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 3
for i in range(1,4+1): #Nutty Noon 3
    energy_sphere_table[StageNames[23] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 4
for i in range(1,4+1): #Nutty Noon 4
    energy_sphere_table[StageNames[24] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 5
for i in range(1,4+1): #Nutty Noon 5
    energy_sphere_table[StageNames[25] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Egg Engines 1
for i in range(1,3+1): #Egg Engines 1
    energy_sphere_table[StageNames[27] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 2
for i in range(1,4+1): #Egg Engines 2
    energy_sphere_table[StageNames[28] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 3
for i in range(1,4+1): #Egg Engines 3
    energy_sphere_table[StageNames[29] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
#Egg Engines 4
for i in range(1,5+1): #Egg Engines 4
    energy_sphere_table[StageNames[30] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 5
for i in range(1,5+1): #Egg Engines 5
    energy_sphere_table[StageNames[31] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 1
for i in range(1,5+1): #Dangerous Dinner 1
    energy_sphere_table[StageNames[33] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 2
for i in range(1,5+1): #Dangerous Dinner 2
    energy_sphere_table[StageNames[34] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 3
for i in range(1,5+1): #Dangerous Dinner 3
    energy_sphere_table[StageNames[35] + "Room 1 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
#should end at ID 309
    
SimplificationArray = [9,14,20,26]
part_sphere_table = {}
part_sphere_table[StageNames[4] + "Room 1 - Part Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in SimplificationArray:
    part_sphere_table[StageNames[i] + "Room 2 - Part Sphere"] = BaseLocationID + locationincrement
    locationincrement += 1

gold_star_table = {}
#Cookie Country 1
for i in range(1,13+1):
    gold_star_table[StageNames[0] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    gold_star_table[StageNames[0] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,25+1):
    gold_star_table[StageNames[0] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,12+1):
    gold_star_table[StageNames[0] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 2
for i in range(1,3+1):
    gold_star_table[StageNames[1] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    gold_star_table[StageNames[1] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[1] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    gold_star_table[StageNames[1] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
gold_star_table[StageNames[1] + "Room 6 - Gold Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 3
for i in range(1,3+1):
    gold_star_table[StageNames[2] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    gold_star_table[StageNames[2] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,17+1):
    gold_star_table[StageNames[2] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,12+1):
    gold_star_table[StageNames[2] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[2] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 4
for i in range(1,9+1):
    gold_star_table[StageNames[3] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    gold_star_table[StageNames[3] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[3] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,55+1):
    gold_star_table[StageNames[3] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,5+1):
    gold_star_table[StageNames[3] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Raisin Ruins 1
for i in range(1,12+1):
    gold_star_table[StageNames[5] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[5] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,10+1):
    gold_star_table[StageNames[5] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,5+1):
    gold_star_table[StageNames[5] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    gold_star_table[StageNames[5] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[5] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Raisin Ruins 2
for i in range(1,20+1):
    gold_star_table[StageNames[6] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,19+1):
    gold_star_table[StageNames[6] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,16+1):
    gold_star_table[StageNames[6] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    gold_star_table[StageNames[6] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,41+1):
    gold_star_table[StageNames[6] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,35+1):
    gold_star_table[StageNames[6] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Raisin Ruins 3
for i in range(1,9+1):
    gold_star_table[StageNames[7] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[7] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,15+1):
    gold_star_table[StageNames[7] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,18+1):
    gold_star_table[StageNames[7] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,18+1):
    gold_star_table[StageNames[7] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[7] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1    
#Raisin Ruins 4
for i in range(1,17+1):
    gold_star_table[StageNames[8] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,6+1):
    gold_star_table[StageNames[8] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[8] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,4+1):
    gold_star_table[StageNames[8] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,12+1):
    gold_star_table[StageNames[8] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,28+1):
    gold_star_table[StageNames[8] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,21+1):
    gold_star_table[StageNames[8] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Onion Ocean 1
for i in range(1,18+1):
    gold_star_table[StageNames[10] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,27+1):
    gold_star_table[StageNames[10] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[10] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,15+1):
    gold_star_table[StageNames[10] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,21+1):
    gold_star_table[StageNames[10] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,12+1):
    gold_star_table[StageNames[10] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,19+1):
    gold_star_table[StageNames[10] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1   
#Onion Ocean 2
for i in range(1,12+1):
    gold_star_table[StageNames[11] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,7+1):
    gold_star_table[StageNames[11] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,15+1):
    gold_star_table[StageNames[11] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,28+1):
    gold_star_table[StageNames[11] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,45+1):
    gold_star_table[StageNames[11] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1   
#Onion Ocean 3
for i in range(1,4+1):
    gold_star_table[StageNames[12] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,19+1):
    gold_star_table[StageNames[12] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,14+1):
    gold_star_table[StageNames[12] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,16+1):
    gold_star_table[StageNames[12] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,69+1):
    gold_star_table[StageNames[12] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,55+1):
    gold_star_table[StageNames[12] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,23+1):
    gold_star_table[StageNames[12] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
#Onion Ocean 4
for i in range(1,12+1):
    gold_star_table[StageNames[13] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,11+1):
    gold_star_table[StageNames[13] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,10+1):
    gold_star_table[StageNames[13] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,21+1):
    gold_star_table[StageNames[13] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,15+1):
    gold_star_table[StageNames[13] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,27+1):
    gold_star_table[StageNames[13] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1    
    
red_star_table = {}
#Cookie Country 1
red_star_table[StageNames[0] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[0] + "Room 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 2
red_star_table[StageNames[1] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[1] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 3
red_star_table[StageNames[2] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[2] + "Room 4 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[2] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 4
for i in range(1,5+1):
    red_star_table[StageNames[3] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[3] + "Room 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[3] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 1
red_star_table[StageNames[5] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[5] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 2
red_star_table[StageNames[6] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,6+1):
    red_star_table[StageNames[6] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 3
for i in range(1,3+1):
    red_star_table[StageNames[7] + "Room 1 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[7] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[7] + "Room 4 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[7] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[7] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 4
red_star_table[StageNames[8] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[8] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[8] + "Room 9 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 1
red_star_table[StageNames[10] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[10] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[10] + "Room 4 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[10] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[10] + "Room 8 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Onion Ocean 2
red_star_table[StageNames[11] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[11] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Onion Ocean 3
for i in range(1,2+1):
    red_star_table[StageNames[12] + "Room 1 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[12] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[12] + "Room 4 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[12] + "Room 5 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[12] + "Room 7 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[12] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    red_star_table[StageNames[12] + "Room 9 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 4
red_star_table[StageNames[13] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[13] + "Room 4 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[13] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[13] + "Room 7 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[13] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
blue_star_table = {}
blue_star_table[StageNames[1] + "Room 2 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[5] + "Room 8 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[6] + "Room 8 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[10] + "Room 2 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[10] + "Room 7 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[12] + "Room 7 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
    
flower_table = {}
#Cookie Country 1
for i in range(1,6+1):
    flower_table[StageNames[0] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    flower_table[StageNames[0] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 2
for i in range(1,4+1):
    flower_table[StageNames[1] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 3
for i in range(1,2+1):
    flower_table[StageNames[2] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[2] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 4
for i in range(1,8+1):
    flower_table[StageNames[3] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15+1):
    flower_table[StageNames[3] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[3] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    flower_table[StageNames[3] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 1
for i in range(1,2+1):
    flower_table[StageNames[5] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[5] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
flower_table[StageNames[5] + "Room 5 - Flower"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[5] + "Room 7 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[5] + "Room 8 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 2
for i in range(1,7+1):
    flower_table[StageNames[6] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[6] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[6] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 3
for i in range(1,2+1):
    flower_table[StageNames[7] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[7] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 1
for i in range(1,8+1):
    flower_table[StageNames[10] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[10] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    flower_table[StageNames[10] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    flower_table[StageNames[10] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    flower_table[StageNames[10] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[10] + "Room 7 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 2
for i in range(1,2+1):
    flower_table[StageNames[11] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[11] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    flower_table[StageNames[11] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1):
    flower_table[StageNames[11] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    flower_table[StageNames[11] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 3
for i in range(1,8+1):
    flower_table[StageNames[12] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[12] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
flower_table[StageNames[12] + "Room 4 - Flower"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,9+1):
    flower_table[StageNames[12] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[12] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[12] + "Room 7 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 4
for i in range(1,3+1):
    flower_table[StageNames[13] + "Room 8 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
one_up_table = {}
one_up_table[StageNames[0] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[2] + "Room 3 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[3] + "Room 6 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[5] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[6] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[7] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[7] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[8] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[10] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[10] + "Room 7 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[10] + "Room 8 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[11] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[12] + "Room 3 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[13] + "Room 7 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
    
health_pickup_table = {}
#Cookie Country 1
for i in range(1,5+1):
    health_pickup_table[StageNames[0] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    health_pickup_table[StageNames[0] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[0] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Cookie Country 2
health_pickup_table[StageNames[1] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[1] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[1] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[1] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 3
for i in range(1,5+1):
    health_pickup_table[StageNames[2] + "Room " + str(i) + " - Food"] = BaseLocationID + locationincrement
    locationincrement += 1
#Cookie Country 4
for i in range(1,3+1):
    health_pickup_table[StageNames[3] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    health_pickup_table[StageNames[3] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[3] + "Room 7 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 1
for i in range(1,2+1):
    health_pickup_table[StageNames[5] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[5] + "Room 3 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[5] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[5] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[5] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 2
for i in range(1,2+1):
    health_pickup_table[StageNames[6] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[6] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[6] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[6] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[6] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Raisin Ruins 3
health_pickup_table[StageNames[7] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[7] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[7] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(4,6+1):
    health_pickup_table[StageNames[7] + "Room " + str(i) + " - Food"] = BaseLocationID + locationincrement
    locationincrement += 1
#Raisin Ruins 4
for i in range(1,2+1):
    health_pickup_table[StageNames[8] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[8] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[8] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[8] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[8] + "Room 9 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[8] + "Room 10 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Onion Ocean 1
for i in range(1,3+1):
    health_pickup_table[StageNames[10] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[10] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[10] + "Room 3 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[10] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[10] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[10] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[10] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[10] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Onion Ocean 2
for i in range(1,2+1):
    health_pickup_table[StageNames[11] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[11] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[11] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[11] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[11] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Onion Ocean 3
for i in range(1,2+1):
    health_pickup_table[StageNames[12] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[12] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[12] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[12] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[12] + "Room 6 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[12] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    health_pickup_table[StageNames[12] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[12] + "Room 10 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Onion Ocean 4
for i in range(1,2+1):
    health_pickup_table[StageNames[13] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[13] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[13] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[13] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[13] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    health_pickup_table[StageNames[13] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

maxim_tomato_table = {}
maxim_tomato_table[StageNames[0] + "Room 5 - M-Tomato"] = BaseLocationID + locationincrement 
locationincrement += 1
maxim_tomato_table[StageNames[1] + "Room 4 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[3] + "Room 2 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[3] + "Room 3 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[3] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[4] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[6] + "Room 8 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[6] + "Room 10 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[7] + "Room 5 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[8] + "Room 10 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[9] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[10] + "Room 9 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[12] + "Room 5 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[12] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[12] + "Room 10 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[13] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[14] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
    
ChallengeNames = ["Sword Challenge ","Whip Challenge ","Hi-Jump Challenge ","Bomb Challenge ","Water Challenge ","Wing Challenge ","Item Challenge "]
challenge_table = {}
for i in ChallengeNames:
    challenge_table[i + "- Bronze"] = BaseLocationID + locationincrement
    locationincrement += 1
    challenge_table[i + "- Silver"] = BaseLocationID + locationincrement
    locationincrement += 1
    challenge_table[i + "- Gold"] = BaseLocationID + locationincrement
    locationincrement += 1
    challenge_table[i + "- Platinum"] = BaseLocationID + locationincrement
    locationincrement += 1
    
SubgameNames = ["Ninja Dojo ","Scope Shot "]
subgame_table = {}
for i in SubgameNames:
    subgame_table[i + "- Level 1"] = BaseLocationID + locationincrement
    locationincrement += 1
    subgame_table[i + "- Level 2"] = BaseLocationID + locationincrement
    locationincrement += 1
    subgame_table[i + "- Level 3"] = BaseLocationID + locationincrement
    locationincrement += 1
    
extra_sanity_table = {}
for i in energy_sphere_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in part_sphere_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in gold_star_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in red_star_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in blue_star_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in flower_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in one_up_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in health_pickup_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in maxim_tomato_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in challenge_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
for i in subgame_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1
    
composite_location: dict[str, int] = {
    **stage_completion_table,
    **energy_sphere_table,
    **part_sphere_table,
    **gold_star_table,
    **red_star_table,
    **blue_star_table,
    **flower_table,
    **one_up_table,
    **health_pickup_table,
    **maxim_tomato_table,
    **challenge_table,
    **subgame_table,
    **extra_sanity_table
}

def create_all_regions(world: "KRtDLWorld") -> None:
    regions = []

    regions.append(Region("Menu", world.player, world.multiworld))

    regions.append(Region("Popstar Map", world.player, world.multiworld))
    regions.append(Region("Halcandra Map", world.player, world.multiworld))

    regions.append(Region("Lor Starcutter", world.player, world.multiworld))

    regions.append(Region("Cookie Country Hub", world.player, world.multiworld))
    regions.append(Region("Raisin Ruins Hub", world.player, world.multiworld))
    regions.append(Region("Onion Ocean Hub", world.player, world.multiworld))
    regions.append(Region("White Wafers Hub", world.player, world.multiworld))
    regions.append(Region("Nutty Noon Hub", world.player, world.multiworld))
    regions.append(Region("Egg Engines Hub", world.player, world.multiworld))
    regions.append(Region("Dangerous Dinner Hub", world.player, world.multiworld))
    
    for i in range(1,5+1):
        regions.append(Region(StageNames[0] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(StageNames[1] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,5+1):
        regions.append(Region(StageNames[2] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,7+1):
        regions.append(Region(StageNames[3] + "Room " + str(i), world.player, world.multiworld))

    regions.append(Region(StageNames[4] + "Room 1", world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(StageNames[5] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(StageNames[6] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(StageNames[7] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(StageNames[8] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,9+1):
        regions.append(Region(StageNames[10] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(StageNames[11] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(StageNames[12] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(StageNames[13] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(StageNames[14] + "Room " + str(i), world.player, world.multiworld))
    world.multiworld.regions += regions

#def connect_regions(world: KRtDLWorld) -> None:
    

def create_regular_locations(world: "KRtDLWorld") -> None:
    MenuRegion = world.get_region("Menu")
    PopstarMapRegion = world.get_region("Popstar Map")
    HalcandraMapRegion = world.get_region("Halcandra Map")

    CookieCountryHub = world.get_region("Cookie Country Hub")
    RaisinRuinsHub = world.get_region("Raisin Ruins Hub")
    OnionOceanHub = world.get_region("Onion Ocean Hub")
    WhiteWafersHub = world.get_region("White Wafers Hub")
    NuttyNoonHub = world.get_region("Nutty Noon Hub")
    EggEnginesHub = world.get_region("Egg Engines Hub")
    DangerousDinnerHub = world.get_region("Dangerous Dinner Hub")
    
    MenuRegion.connect(PopstarMapRegion, "Menu To Popstar Map")
    MenuRegion.connect(HalcandraMapRegion, "Menu To Halcandra Map")
    PopstarMapRegion.connect(HalcandraMapRegion, "Popstar Map To Halcandra Map")
    HalcandraMapRegion.connect(PopstarMapRegion, "Halcandra Map To Popstar Map")

    PopstarMapRegion.connect(CookieCountryHub, "Popstar Map To Cookie Country Hub")
    PopstarMapRegion.connect(RaisinRuinsHub, "Popstar Map To Raisin Ruins Hub")
    PopstarMapRegion.connect(OnionOceanHub, "Popstar Map To Onion Ocean Hub")
    PopstarMapRegion.connect(WhiteWafersHub, "Popstar Map To White Wafers Hub")
    PopstarMapRegion.connect(NuttyNoonHub, "Popstar Map To Nutty Noon Hub")

    HalcandraMapRegion.connect(EggEnginesHub, "Halcandra Map To Egg Engines Hub")
    HalcandraMapRegion.connect(DangerousDinnerHub, "Halcandra Map To Dangerous Dinner Hub")
    
    OneOneRooms = [world.get_region("Cookie Country Stage 1 Room 1"),
                   world.get_region("Cookie Country Stage 1 Room 2"),
                   world.get_region("Cookie Country Stage 1 Room 3"),
                   world.get_region("Cookie Country Stage 1 Room 4"),
                  world.get_region("Cookie Country Stage 1 Room 5")]

    CookieCountryHub.connect(OneOneRooms[0], "Cookie Country Hub To Cookie Country Stage 1 Room 1")
    OneOneRooms[0].connect(OneOneRooms[1], "Cookie Country Stage 1 Room 1-2")
    OneOneRooms[1].connect(OneOneRooms[2], "Cookie Country Stage 1 Room 2-3")
    OneOneRooms[2].connect(OneOneRooms[3], "Cookie Country Stage 1 Room 3-4")
    OneOneRooms[3].connect(OneOneRooms[4], "Cookie Country Stage 1 Room 4-5")

    OneTwoRooms = [world.get_region("Cookie Country Stage 2 Room 1"),
                   world.get_region("Cookie Country Stage 2 Room 2"),
                   world.get_region("Cookie Country Stage 2 Room 3"),
                   world.get_region("Cookie Country Stage 2 Room 4"),
                   world.get_region("Cookie Country Stage 2 Room 5"),
                  world.get_region("Cookie Country Stage 2 Room 6")]

    CookieCountryHub.connect(OneTwoRooms[0], "Cookie Country Hub To Cookie Country Stage 2 Room 1")
    OneTwoRooms[0].connect(OneTwoRooms[1], "Cookie Country Stage 2 Room 1-2")
    OneTwoRooms[1].connect(OneTwoRooms[2], "Cookie Country Stage 2 Room 2-3")
    OneTwoRooms[2].connect(OneTwoRooms[3], "Cookie Country Stage 2 Room 3-4")
    OneTwoRooms[3].connect(OneTwoRooms[4], "Cookie Country Stage 2 Room 4-5")
    OneTwoRooms[3].connect(OneTwoRooms[5], "Cookie Country Stage 2 Room 4-6")
    
    OneThreeRooms = [world.get_region("Cookie Country Stage 3 Room 1"),
                   world.get_region("Cookie Country Stage 3 Room 2"),
                   world.get_region("Cookie Country Stage 3 Room 3"),
                   world.get_region("Cookie Country Stage 3 Room 4"),
                  world.get_region("Cookie Country Stage 3 Room 5")]

    CookieCountryHub.connect(OneThreeRooms[0], "Cookie Country Hub To Cookie Country Stage 3 Room 1")
    OneThreeRooms[0].connect(OneThreeRooms[1], "Cookie Country Stage 3 Room 1-2")
    OneThreeRooms[1].connect(OneThreeRooms[2], "Cookie Country Stage 3 Room 2-3")
    OneThreeRooms[2].connect(OneThreeRooms[3], "Cookie Country Stage 3 Room 3-4")
    OneThreeRooms[3].connect(OneThreeRooms[4], "Cookie Country Stage 3 Room 4-5")
    
    OneFourRooms = [world.get_region("Cookie Country Stage 4 Room 1"),
                   world.get_region("Cookie Country Stage 4 Room 2"),
                   world.get_region("Cookie Country Stage 4 Room 3"),
                   world.get_region("Cookie Country Stage 4 Room 4"),
                   world.get_region("Cookie Country Stage 4 Room 5"),
                   world.get_region("Cookie Country Stage 4 Room 6"),
                   world.get_region("Cookie Country Stage 4 Room 7")]

    CookieCountryHub.connect(OneFourRooms[0], "Cookie Country Hub To Cookie Country Stage 4 Room 1")
    OneFourRooms[0].connect(OneFourRooms[1], "Cookie Country Stage 4 Room 1-2")
    OneFourRooms[0].connect(OneFourRooms[2], "Cookie Country Stage 4 Room 1-3")
    OneFourRooms[1].connect(OneFourRooms[2], "Cookie Country Stage 4 Room 2-3")
    OneFourRooms[2].connect(OneFourRooms[3], "Cookie Country Stage 4 Room 3-4")
    OneFourRooms[3].connect(OneFourRooms[4], "Cookie Country Stage 4 Room 4-5")
    OneFourRooms[4].connect(OneFourRooms[5], "Cookie Country Stage 4 Room 5-6")
    OneFourRooms[5].connect(OneFourRooms[6], "Cookie Country Stage 4 Room 6-7")
    
    OneFiveRegion = world.get_region("Cookie Country Stage 5 Room 1")

    CookieCountryHub.connect(OneFiveRegion, "Cookie Country Hub To Cookie Country Stage 5")
    
    TwoOneRooms = [world.get_region("Raisin Ruins Stage 1 Room 1"),
                   world.get_region("Raisin Ruins Stage 1 Room 2"),
                   world.get_region("Raisin Ruins Stage 1 Room 3"),
                   world.get_region("Raisin Ruins Stage 1 Room 4"),
                   world.get_region("Raisin Ruins Stage 1 Room 5"),
                   world.get_region("Raisin Ruins Stage 1 Room 6"),
                   world.get_region("Raisin Ruins Stage 1 Room 7"),
                  world.get_region("Raisin Ruins Stage 1 Room 8")]

    RaisinRuinsHub.connect(TwoOneRooms[0], "Raisin Ruins Hub To Raisin Ruins Stage 1 Room 1")
    TwoOneRooms[0].connect(TwoOneRooms[1], "Raisin Ruins Stage 1 Room 1-2")
    TwoOneRooms[0].connect(TwoOneRooms[2], "Raisin Ruins Stage 1 Room 1-3")
    TwoOneRooms[2].connect(TwoOneRooms[3], "Raisin Ruins Stage 1 Room 3-4")
    TwoOneRooms[2].connect(TwoOneRooms[4], "Raisin Ruins Stage 1 Room 3-5")
    TwoOneRooms[4].connect(TwoOneRooms[5], "Raisin Ruins Stage 1 Room 5-6")
    TwoOneRooms[5].connect(TwoOneRooms[6], "Raisin Ruins Stage 1 Room 6-7")
    TwoOneRooms[6].connect(TwoOneRooms[7], "Raisin Ruins Stage 1 Room 7-8")
    
    TwoTwoRooms = [world.get_region("Raisin Ruins Stage 2 Room 1"),
                   world.get_region("Raisin Ruins Stage 2 Room 2"),
                   world.get_region("Raisin Ruins Stage 2 Room 3"),
                   world.get_region("Raisin Ruins Stage 2 Room 4"),
                   world.get_region("Raisin Ruins Stage 2 Room 5"),
                   world.get_region("Raisin Ruins Stage 2 Room 6"),
                   world.get_region("Raisin Ruins Stage 2 Room 7"),
                   world.get_region("Raisin Ruins Stage 2 Room 8"),
                   world.get_region("Raisin Ruins Stage 2 Room 9"),
                  world.get_region("Raisin Ruins Stage 2 Room 10")]

    RaisinRuinsHub.connect(TwoTwoRooms[0], "Raisin Ruins Hub To Raisin Ruins Stage 2 Room 1")
    TwoTwoRooms[0].connect(TwoTwoRooms[1], "Raisin Ruins Stage 2 Room 1-2")
    TwoTwoRooms[1].connect(TwoTwoRooms[2], "Raisin Ruins Stage 2 Room 2-3")
    TwoTwoRooms[1].connect(TwoTwoRooms[3], "Raisin Ruins Stage 2 Room 2-4")
    TwoTwoRooms[3].connect(TwoTwoRooms[4], "Raisin Ruins Stage 2 Room 4-5")
    TwoTwoRooms[3].connect(TwoTwoRooms[5], "Raisin Ruins Stage 2 Room 4-6")
    TwoTwoRooms[3].connect(TwoTwoRooms[6], "Raisin Ruins Stage 2 Room 4-7")
    TwoTwoRooms[6].connect(TwoTwoRooms[7], "Raisin Ruins Stage 2 Room 7-8")
    TwoTwoRooms[7].connect(TwoTwoRooms[8], "Raisin Ruins Stage 2 Room 8-9")
    TwoTwoRooms[8].connect(TwoTwoRooms[9], "Raisin Ruins Stage 2 Room 9-10")

    TwoThreeRooms = [world.get_region("Raisin Ruins Stage 3 Room 1"),
                   world.get_region("Raisin Ruins Stage 3 Room 2"),
                   world.get_region("Raisin Ruins Stage 3 Room 3"),
                   world.get_region("Raisin Ruins Stage 3 Room 4"),
                   world.get_region("Raisin Ruins Stage 3 Room 5"),
                   world.get_region("Raisin Ruins Stage 3 Room 6")]

    RaisinRuinsHub.connect(TwoThreeRooms[0], "Raisin Ruins Hub To Raisin Ruins Stage 3 Room 1")
    TwoThreeRooms[0].connect(TwoThreeRooms[1], "Raisin Ruins Stage 3 Room 1-2")
    TwoThreeRooms[1].connect(TwoThreeRooms[2], "Raisin Ruins Stage 3 Room 2-3")
    TwoThreeRooms[2].connect(TwoThreeRooms[3], "Raisin Ruins Stage 3 Room 3-4")
    TwoThreeRooms[3].connect(TwoThreeRooms[4], "Raisin Ruins Stage 3 Room 4-5")
    TwoThreeRooms[4].connect(TwoThreeRooms[5], "Raisin Ruins Stage 3 Room 5-6")
    
    TwoFourRooms = [world.get_region("Raisin Ruins Stage 4 Room 1"),
                   world.get_region("Raisin Ruins Stage 4 Room 2"),
                   world.get_region("Raisin Ruins Stage 4 Room 3"),
                   world.get_region("Raisin Ruins Stage 4 Room 4"),
                   world.get_region("Raisin Ruins Stage 4 Room 5"),
                   world.get_region("Raisin Ruins Stage 4 Room 6"),
                   world.get_region("Raisin Ruins Stage 4 Room 7"),
                   world.get_region("Raisin Ruins Stage 4 Room 8"),
                   world.get_region("Raisin Ruins Stage 4 Room 9"),
                  world.get_region("Raisin Ruins Stage 4 Room 10")]

    RaisinRuinsHub.connect(TwoFourRooms[0], "Raisin Ruins Hub To Raisin Ruins Stage 4 Room 1")
    TwoFourRooms[0].connect(TwoFourRooms[1], "Raisin Ruins Stage 4 Room 1-2")
    TwoFourRooms[1].connect(TwoFourRooms[2], "Raisin Ruins Stage 4 Room 2-3")
    TwoFourRooms[1].connect(TwoFourRooms[3], "Raisin Ruins Stage 4 Room 2-4")
    TwoFourRooms[3].connect(TwoFourRooms[4], "Raisin Ruins Stage 4 Room 4-5")
    TwoFourRooms[4].connect(TwoFourRooms[5], "Raisin Ruins Stage 4 Room 5-6")
    TwoFourRooms[5].connect(TwoFourRooms[6], "Raisin Ruins Stage 4 Room 6-7")
    TwoFourRooms[5].connect(TwoFourRooms[7], "Raisin Ruins Stage 4 Room 6-8")
    TwoFourRooms[7].connect(TwoFourRooms[8], "Raisin Ruins Stage 4 Room 8-9")
    TwoFourRooms[8].connect(TwoFourRooms[9], "Raisin Ruins Stage 4 Room 9-10")
    
    TwoFiveRooms = [world.get_region("Raisin Ruins Stage 5 Room 1"),
                   world.get_region("Raisin Ruins Stage 5 Room 2")]

    RaisinRuinsHub.connect(TwoFiveRooms[0], "Raisin Ruins Hub To Raisin Ruins Stage 5 Room 1")
    TwoFiveRooms[0].connect(TwoFiveRooms[1], "Raisin Ruins Stage 5 Room 1-2")
    
    ThreeOneRooms = [world.get_region("Onion Ocean Stage 1 Room 1"),
                   world.get_region("Onion Ocean Stage 1 Room 2"),
                   world.get_region("Onion Ocean Stage 1 Room 3"),
                   world.get_region("Onion Ocean Stage 1 Room 4"),
                   world.get_region("Onion Ocean Stage 1 Room 5"),
                   world.get_region("Onion Ocean Stage 1 Room 6"),
                   world.get_region("Onion Ocean Stage 1 Room 7"),
                   world.get_region("Onion Ocean Stage 1 Room 8"),
                   world.get_region("Onion Ocean Stage 1 Room 9")]

    OnionOceanHub.connect(ThreeOneRooms[0], "Onion Ocean Hub To Raisin Ocean Stage 1 Room 1")
    ThreeOneRooms[0].connect(ThreeOneRooms[1], "Onion Ocean Stage 1 Room 1-2")
    ThreeOneRooms[1].connect(ThreeOneRooms[2], "Onion Ocean Stage 1 Room 2-3")
    ThreeOneRooms[2].connect(ThreeOneRooms[3], "Onion Ocean Stage 1 Room 3-4")
    ThreeOneRooms[3].connect(ThreeOneRooms[4], "Onion Ocean Stage 1 Room 4-5")
    ThreeOneRooms[3].connect(ThreeOneRooms[5], "Onion Ocean Stage 1 Room 4-6")
    ThreeOneRooms[5].connect(ThreeOneRooms[6], "Onion Ocean Stage 1 Room 6-7")
    ThreeOneRooms[6].connect(ThreeOneRooms[7], "Onion Ocean Stage 1 Room 7-8")
    ThreeOneRooms[7].connect(ThreeOneRooms[8], "Onion Ocean Stage 1 Room 8-9")
    
    ThreeTwoRooms = [world.get_region("Onion Ocean Stage 2 Room 1"),
                   world.get_region("Onion Ocean Stage 2 Room 2"),
                   world.get_region("Onion Ocean Stage 2 Room 3"),
                   world.get_region("Onion Ocean Stage 2 Room 4"),
                   world.get_region("Onion Ocean Stage 2 Room 5"),
                   world.get_region("Onion Ocean Stage 2 Room 6")]

    OnionOceanHub.connect(ThreeTwoRooms[0], "Onion Ocean Hub To Raisin Ocean Stage 2 Room 1")
    ThreeTwoRooms[0].connect(ThreeTwoRooms[1], "Onion Ocean Stage 2 Room 1-2")
    ThreeTwoRooms[1].connect(ThreeTwoRooms[2], "Onion Ocean Stage 2 Room 2-3")
    ThreeTwoRooms[2].connect(ThreeTwoRooms[3], "Onion Ocean Stage 2 Room 3-4")
    ThreeTwoRooms[2].connect(ThreeTwoRooms[4], "Onion Ocean Stage 2 Room 3-5")
    ThreeTwoRooms[4].connect(ThreeTwoRooms[5], "Onion Ocean Stage 2 Room 5-6")

    ThreeThreeRooms = [world.get_region("Onion Ocean Stage 3 Room 1"),
                   world.get_region("Onion Ocean Stage 3 Room 2"),
                   world.get_region("Onion Ocean Stage 3 Room 3"),
                   world.get_region("Onion Ocean Stage 3 Room 4"),
                   world.get_region("Onion Ocean Stage 3 Room 5"),
                   world.get_region("Onion Ocean Stage 3 Room 6"),
                   world.get_region("Onion Ocean Stage 3 Room 7"),
                   world.get_region("Onion Ocean Stage 3 Room 8"),
                   world.get_region("Onion Ocean Stage 3 Room 9"),
                   world.get_region("Onion Ocean Stage 3 Room 10")]

    OnionOceanHub.connect(ThreeThreeRooms[0], "Onion Ocean Hub To Raisin Ocean Stage 3 Room 1")
    ThreeThreeRooms[0].connect(ThreeThreeRooms[1], "Onion Ocean Stage 3 Room 1-2")
    ThreeThreeRooms[1].connect(ThreeThreeRooms[2], "Onion Ocean Stage 3 Room 2-3")
    ThreeThreeRooms[1].connect(ThreeThreeRooms[3], "Onion Ocean Stage 3 Room 2-4")
    ThreeThreeRooms[3].connect(ThreeThreeRooms[4], "Onion Ocean Stage 3 Room 4-5")
    ThreeThreeRooms[4].connect(ThreeThreeRooms[5], "Onion Ocean Stage 3 Room 5-6")
    ThreeThreeRooms[5].connect(ThreeThreeRooms[6], "Onion Ocean Stage 3 Room 6-7")
    ThreeThreeRooms[6].connect(ThreeThreeRooms[7], "Onion Ocean Stage 3 Room 7-8")
    ThreeThreeRooms[7].connect(ThreeThreeRooms[8], "Onion Ocean Stage 3 Room 8-9")
    ThreeThreeRooms[8].connect(ThreeThreeRooms[9], "Onion Ocean Stage 3 Room 9-10")
    
    ThreeFourRooms = [world.get_region("Onion Ocean Stage 4 Room 1"),
                   world.get_region("Onion Ocean Stage 4 Room 2"),
                   world.get_region("Onion Ocean Stage 4 Room 3"),
                   world.get_region("Onion Ocean Stage 4 Room 4"),
                   world.get_region("Onion Ocean Stage 4 Room 5"),
                   world.get_region("Onion Ocean Stage 4 Room 6"),
                   world.get_region("Onion Ocean Stage 4 Room 7"),
                   world.get_region("Onion Ocean Stage 4 Room 8")]

    OnionOceanHub.connect(ThreeFourRooms[0], "Onion Ocean Hub To Raisin Ocean Stage 4 Room 1")
    ThreeFourRooms[0].connect(ThreeFourRooms[1], "Onion Ocean Stage 4 Room 1-2")
    ThreeFourRooms[1].connect(ThreeFourRooms[2], "Onion Ocean Stage 4 Room 2-3")
    ThreeFourRooms[1].connect(ThreeFourRooms[3], "Onion Ocean Stage 4 Room 2-4")
    ThreeFourRooms[3].connect(ThreeFourRooms[4], "Onion Ocean Stage 4 Room 4-5")
    ThreeFourRooms[3].connect(ThreeFourRooms[5], "Onion Ocean Stage 4 Room 4-6")
    ThreeFourRooms[5].connect(ThreeFourRooms[6], "Onion Ocean Stage 4 Room 6-7")
    ThreeFourRooms[6].connect(ThreeFourRooms[7], "Onion Ocean Stage 4 Room 7-8")

    ThreeFiveRooms = [world.get_region("Onion Ocean Stage 5 Room 1"),
                   world.get_region("Onion Ocean Stage 5 Room 2")]

    OnionOceanHub.connect(ThreeFiveRooms[0], "Onion Ocean Hub To Raisin Ocean Stage 5 Room 1")
    ThreeFiveRooms[0].connect(ThreeFiveRooms[1], "Onion Ocean Stage 5 Room 1-2")
    
    #NinjaDojoRegion = world.get_region("Ninja Dojo")
    #ScopeShotRegion = world.get_region("Scope Shot")
    
    if world.options.shuffle_energy_spheres:
        OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 2 - Energy Sphere"]), KRtDLLocation)
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 5 - Energy Sphere #1"]), KRtDLLocation)
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 5 - Energy Sphere #2"]), KRtDLLocation) 

        OneTwoRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)
        OneTwoRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 4 - Energy Sphere"]), KRtDLLocation)
        OneTwoRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 6 - Energy Sphere"]), KRtDLLocation) 

        OneThreeRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 2 - Energy Sphere"]), KRtDLLocation)
        OneThreeRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 4 - Energy Sphere"]), KRtDLLocation)
        OneThreeRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation) 

        OneFourRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 1 - Energy Sphere"]), KRtDLLocation)
        OneFourRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)
        OneFourRooms[6].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 7 - Energy Sphere #1"]), KRtDLLocation) 
        OneFourRooms[6].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 7 - Energy Sphere #2"]), KRtDLLocation) 


        TwoOneRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 4 - Energy Sphere"]), KRtDLLocation)
        TwoOneRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)
        TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 8 - Energy Sphere"]), KRtDLLocation) 

        TwoTwoRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)
        TwoTwoRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 6 - Energy Sphere"]), KRtDLLocation)
        TwoTwoRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
        TwoTwoRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 10 - Energy Sphere #2"]), KRtDLLocation) 

        TwoThreeRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 3 - Energy Sphere"]), KRtDLLocation)
        TwoThreeRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 4 - Energy Sphere"]), KRtDLLocation)
        TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation) 
        TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation) 

        TwoFourRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 3 - Energy Sphere"]), KRtDLLocation)
        TwoFourRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)
        TwoFourRooms[6].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 7 - Energy Sphere"]), KRtDLLocation) 
        TwoFourRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
        TwoFourRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 10 - Energy Sphere #2"]), KRtDLLocation) 


        ThreeOneRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)
        ThreeOneRooms[8].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 9 - Energy Sphere #1"]), KRtDLLocation)
        ThreeOneRooms[8].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 9 - Energy Sphere #2"]), KRtDLLocation) 

        ThreeTwoRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 2 - Energy Sphere"]), KRtDLLocation)
        ThreeTwoRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 4 - Energy Sphere"]), KRtDLLocation)
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Energy Sphere #1"]), KRtDLLocation) 
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Energy Sphere #2"]), KRtDLLocation) 

        ThreeThreeRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation)
        ThreeThreeRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation)
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 10 - Energy Sphere #2"]), KRtDLLocation) 

        ThreeFourRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 3 - Energy Sphere"]), KRtDLLocation)
        ThreeFourRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 5 - Energy Sphere"]), KRtDLLocation)
        ThreeFourRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 6 - Energy Sphere"]), KRtDLLocation) 
        ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - Energy Sphere"]), KRtDLLocation) 
        ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 8 - Energy Sphere"]), KRtDLLocation) 

    
    #if world.options.shuffle_part_spheres:
        #OneFiveRegion.add_locations(get_location_names_with_ids(["Cookie Country Stage 5 Room 1 - Part Sphere"]), KRtDLLocation)
        #TwoFiveRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 5 Room 2 - Part Sphere"]), KRtDLLocation)
        #ThreeFiveRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 5 Room 3 - Part Sphere"]), KRtDLLocation)

    
    if world.options.star_sanity:
        for i in range(1,13+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,7+1):
            OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,25+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,12+1):
            OneOneRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)    

        for i in range(1,3+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,10+1):
            OneTwoRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,11+1):
            OneTwoRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,7+1):
            OneTwoRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        OneTwoRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 6 - Gold Star"]), KRtDLLocation)

        for i in range(1,3+1):
            OneThreeRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,8+1):
            OneThreeRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,17+1):
            OneThreeRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,12+1):
            OneThreeRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            OneThreeRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            OneFourRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,4+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            OneFourRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,55+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,5+1):
            OneFourRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,12+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            TwoOneRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,10+1):
            TwoOneRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,5+1):
            TwoOneRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,20+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,19+1):
            TwoTwoRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,16+1):
            TwoTwoRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            TwoTwoRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,41+1):
            TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,35+1):
            TwoTwoRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            TwoThreeRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,15+1):
            TwoThreeRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,18+1):
            TwoThreeRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,18+1):
            TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,17+1):
            TwoFourRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,6+1):
            TwoFourRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            TwoFourRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,4+1):
            TwoFourRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,12+1):
            TwoFourRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,28+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,21+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,18+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,27+1):
            ThreeOneRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            ThreeOneRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,15+1):
            ThreeOneRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,21+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,12+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,19+1):
            ThreeOneRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,7+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,15+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,28+1):
            ThreeTwoRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,45+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,19+1):
            ThreeThreeRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,14+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,16+1):
            ThreeThreeRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,69+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,55+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,23+1):
            ThreeThreeRooms[8].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            ThreeFourRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,11+1):
            ThreeFourRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,10+1):
            ThreeFourRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,21+1):
            ThreeFourRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,15+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(1,27+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
    
    
    if world.options.red_star_sanity:
        OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 1 - Red Star"]), KRtDLLocation)  
        for i in range(1,3+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 3 - Red Star #" + str(i)]), KRtDLLocation)

        OneTwoRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 2 - Red Star"]), KRtDLLocation)  
        OneTwoRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 3 - Red Star"]), KRtDLLocation)  

        OneThreeRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 2 - Red Star"]), KRtDLLocation) 
        for i in range(1,2+1):
            OneThreeRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 4 - Red Star #" + str(i)]), KRtDLLocation)
        OneThreeRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 5 - Red Star"]), KRtDLLocation)

        for i in range(1,5+1):
            OneFourRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 2 - Red Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 3 - Red Star #" + str(i)]), KRtDLLocation)
        OneFourRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 5 - Red Star"]), KRtDLLocation)

        
        TwoOneRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 1 - Red Star"]), KRtDLLocation)
        TwoOneRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 3 - Red Star"]), KRtDLLocation)

        TwoTwoRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 1 - Red Star"]), KRtDLLocation)
        for i in range(1,6+1):
            TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 8 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 1 - Red Star #" + str(i)]), KRtDLLocation)
        TwoThreeRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 3 - Red Star"]), KRtDLLocation)
        TwoThreeRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 4 - Red Star"]), KRtDLLocation)
        TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - Red Star"]), KRtDLLocation)
        for i in range(1,2+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        TwoFourRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 5 - Red Star"]), KRtDLLocation)
        for i in range(1,4+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 8 - Red Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 9 - Red Star #" + str(i)]), KRtDLLocation)

        
        ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 1 - Red Star"]), KRtDLLocation)
        ThreeOneRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 3 - Red Star"]), KRtDLLocation)
        ThreeOneRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 4 - Red Star"]), KRtDLLocation)
        ThreeOneRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 6 - Red Star"]), KRtDLLocation)
        ThreeOneRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 8 - Red Star"]), KRtDLLocation)

        ThreeTwoRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 3 - Red Star"]), KRtDLLocation)
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Red Star"]), KRtDLLocation)

        for i in range(1,2+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 1 - Red Star #" + str(i)]), KRtDLLocation)
        ThreeThreeRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 2 - Red Star"]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 4 - Red Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeThreeRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 5 - Red Star #" + str(i)]), KRtDLLocation)
        ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - Red Star"]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 8 - Red Star #" + str(i)]), KRtDLLocation)
        for i in range(1,5+1):
            ThreeThreeRooms[8].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 9 - Red Star #" + str(i)]), KRtDLLocation)

        ThreeFourRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 1 - Red Star"]), KRtDLLocation)
        ThreeFourRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 4 - Red Star"]), KRtDLLocation)
        ThreeFourRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 6 - Red Star"]), KRtDLLocation)
        for i in range(1,4+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - Red Star #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 8 - Red Star #" + str(i)]), KRtDLLocation)


    if world.options.blue_star_sanity:
        OneTwoRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 2 - Blue Star"]), KRtDLLocation)


        TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 8 - Blue Star"]), KRtDLLocation)

        TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 8 - Blue Star"]), KRtDLLocation)



        ThreeOneRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 2 - Blue Star"]), KRtDLLocation)
        ThreeOneRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 7 - Blue Star"]), KRtDLLocation)

        ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - Blue Star"]), KRtDLLocation)
                                         
    
    if world.options.flower_sanity:
        for i in range(1,6+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation)
        for i in range(1,10+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation)           

        for i in range(1,4+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation)  

        for i in range(1,2+1):
            OneThreeRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation)  
        for i in range(1,2+1):
            OneThreeRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 5 - Flower #" + str(i)]), KRtDLLocation)  

        for i in range(1,8+1):
            OneFourRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,15+1):
            OneFourRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,3+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,7+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 5 - Flower #" + str(i)]), KRtDLLocation) 


        for i in range(1,2+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            TwoOneRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        TwoOneRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 5 - Flower"]), KRtDLLocation)
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 7 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 8 - Flower #" + str(i)]), KRtDLLocation) 

        for i in range(1,7+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            TwoTwoRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,4+1):
            TwoTwoRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 4 - Flower #" + str(i)]), KRtDLLocation) 

        for i in range(1,2+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 6 - Flower #" + str(i)]), KRtDLLocation) 


        for i in range(1,8+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,3+1):
            ThreeOneRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,5+1):
            ThreeOneRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,9+1):
            ThreeOneRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 4 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,7+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,3+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 7 - Flower #" + str(i)]), KRtDLLocation) 

        for i in range(1,2+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,7+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,13+1):
            ThreeTwoRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 5 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,8+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Flower #" + str(i)]), KRtDLLocation) 

        for i in range(1,8+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,3+1):
            ThreeThreeRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
        ThreeThreeRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 4 - Flower"]), KRtDLLocation)
        for i in range(1,9+1):
            ThreeThreeRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 5 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,2+1):
            ThreeThreeRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
        for i in range(1,4+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - Flower #" + str(i)]), KRtDLLocation) 

        for i in range(1,3+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 8 - Flower #" + str(i)]), KRtDLLocation) 


    if world.options.one_up_sanity:
        OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 2 - 1-up"]), KRtDLLocation)

        OneThreeRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room 3 - 1-up"]), KRtDLLocation)

        OneFourRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 6 - 1-up"]), KRtDLLocation)


        TwoOneRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 2 - 1-up"]), KRtDLLocation)

        TwoTwoRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 5 - 1-up"]), KRtDLLocation)

        TwoThreeRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 2 - 1-up"]), KRtDLLocation)
        TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - 1-up"]), KRtDLLocation)

        TwoFourRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 5 - 1-up"]), KRtDLLocation)


        ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 1 - 1-up"]), KRtDLLocation)
        ThreeOneRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 7 - 1-up"]), KRtDLLocation)
        ThreeOneRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 8 - 1-up"]), KRtDLLocation)

        ThreeTwoRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 5 - 1-up"]), KRtDLLocation)

        ThreeThreeRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 3 - 1-up"]), KRtDLLocation)

        ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - 1-up"]), KRtDLLocation)

    
    if world.options.food_sanity:
        OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 1 - Food"]), KRtDLLocation)
        for i in range(1,4+1):
            OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 2 - Food #" + str(i)]), KRtDLLocation) 
        for i in range(1,5+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 3 - Food #" + str(i)]), KRtDLLocation) 
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 5 - Food"]), KRtDLLocation)

        OneTwoRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 1 - Food"]), KRtDLLocation)
        for i in range(1,2+1):
            OneTwoRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation) 
        OneTwoRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 4 - Food"]), KRtDLLocation)
        for i in range(1,2+1):
            OneTwoRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            OneThreeRooms[i-1].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 Room " + str(i) + " - Food" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            OneFourRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,5+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)
        OneFourRooms[6].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 7 - Food"]), KRtDLLocation)


        for i in range(1,2+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)
        TwoOneRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 3 - Food"]), KRtDLLocation)
        TwoOneRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 5 - Food"]), KRtDLLocation)
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 7 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 Room 8 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)
        TwoTwoRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 2 - Food"]), KRtDLLocation)
        TwoTwoRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 4 - Food"]), KRtDLLocation)
        TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 8 - Food"]), KRtDLLocation)
        TwoTwoRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 9 - Food"]), KRtDLLocation)

        TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 1 - Food"]), KRtDLLocation)
        TwoThreeRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 2 - Food"]), KRtDLLocation)
        for i in range(1,3+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 3 - Food #" + str(i)]), KRtDLLocation)
        TwoThreeRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 4 - Food"]), KRtDLLocation)
        TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - Food"]), KRtDLLocation)
        TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 6 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            TwoFourRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,4+1):
            TwoFourRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            TwoFourRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,4+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 8 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 9 - Food #" + str(i)]), KRtDLLocation)
        TwoFourRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 10 - Food"]), KRtDLLocation)


        for i in range(1,3+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)
        ThreeOneRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 2 - Food"]), KRtDLLocation)
        ThreeOneRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 3 - Food"]), KRtDLLocation)
        ThreeOneRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 4 - Food"]), KRtDLLocation)
        for i in range(1,3+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 Room 6 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 3 - Food #" + str(i)]), KRtDLLocation)
        ThreeTwoRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 5 - Food"]), KRtDLLocation)
        for i in range(1,4+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 1 - Food #" + str(i)]), KRtDLLocation)
        ThreeThreeRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 2 - Food"]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 4 - Food #" + str(i)]), KRtDLLocation)
        ThreeThreeRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 5 - Food"]), KRtDLLocation)
        ThreeThreeRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 6 - Food"]), KRtDLLocation)
        for i in range(1,4+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,9+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 8 - Food #" + str(i)]), KRtDLLocation)
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 10 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            ThreeFourRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 2 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,2+1):
            ThreeFourRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 3 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            ThreeFourRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,4+1):
            ThreeFourRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - Food #" + str(i)]), KRtDLLocation)
        for i in range(1,5+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 8 - Food #" + str(i)]), KRtDLLocation)
    
    
    if world.options.maxim_sanity:
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 Room 5 - M-Tomato"]), KRtDLLocation)

        OneTwoRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 Room 4 - M-Tomato"]), KRtDLLocation)

        OneFourRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 2 - M-Tomato"]), KRtDLLocation)
        OneFourRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 3 - M-Tomato"]), KRtDLLocation)
        OneFourRooms[6].add_locations(get_location_names_with_ids(["Cookie Country Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)

        OneFiveRegion.add_locations(get_location_names_with_ids(["Cookie Country Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)


        TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 8 - M-Tomato"]), KRtDLLocation)
        TwoTwoRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 Room 10 - M-Tomato"]), KRtDLLocation)

        TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 Room 5 - M-Tomato"]), KRtDLLocation)

        TwoFourRooms[9].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 Room 10 - M-Tomato"]), KRtDLLocation)

        TwoFiveRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)


        ThreeThreeRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 5 - M-Tomato"]), KRtDLLocation)
        ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 7 - M-Tomato"]), KRtDLLocation)
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 Room 10 - M-Tomato"]), KRtDLLocation)

        ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)
        
        ThreeFiveRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)

        

    #if world.options.shuffle_challenges != 0:



    #if world.options.shuffle_challenges == 2:
        


    #if world.options.shuffle_subgames:
        #for i in range(1,4);
            #NinjaDojoRegion.add_locations(get_location_names_with_ids(["Ninja Dojo - Level " + str(i)]), KRtDLLocation)
        #for i in range(1,4);
            #ScopeShotRegion.add_locations(get_location_names_with_ids(["Scope Shot - Level " + str(i)]), KRtDLLocation)
                                          

#def create_events(world: KRtDLWorld) -> None:
    
