from typing import TYPE_CHECKING
from BaseClasses import Location, Region, CollectionState

if TYPE_CHECKING:
    from . import KRtDLWorld

BaseLocationID = 24102011 + 98

class KRtDLLocation(Location):
    game: str = "Kirby's Return to Dream Land"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: composite_location[location_name] for location_name in location_names}

def get_stage_complete_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: compound_stage_completion_table[location_name] for location_name in location_names}

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

NonStageNames = [
    "The Arena ",
    "The True Arena "
]

locationincrement = 0
stage_completion_table = {}
compound_stage_completion_table = {}
for i in StageNames:
    if i != "Another Dimension ":
        stage_completion_table[i + "- Complete"] = BaseLocationID + locationincrement
        compound_stage_completion_table[i + "- Complete"] = BaseLocationID + locationincrement
        locationincrement += 1
stage_completion_table["Another Dimension Final Boss - Complete"] = BaseLocationID + locationincrement
compound_stage_completion_table["Another Dimension Final Boss - Complete"] = BaseLocationID + locationincrement
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
energy_sphere_table[StageNames[15] + "Room 1 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[15] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[15] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 2
energy_sphere_table[StageNames[16] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[16] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[16] + "Room 9 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 3
energy_sphere_table[StageNames[17] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[17] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[17] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[17] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 4
energy_sphere_table[StageNames[18] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[18] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[18] + "Room 7 - Energy Sphere #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 5
energy_sphere_table[StageNames[19] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[19] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[19] + "Room 9 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[19] + "Room 10 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
energy_sphere_table[StageNames[21] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[21] + "Room 7 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[21] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[21] + "Room 9 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 2
energy_sphere_table[StageNames[22] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[22] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[22] + "Room 8 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 3
energy_sphere_table[StageNames[23] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[23] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[23] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[23] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
energy_sphere_table[StageNames[24] + "Room 1 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[24] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[24] + "Room 7 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 5
energy_sphere_table[StageNames[25] + "Room 4/16 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[25] + "Room 7/20 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[25] + "Room 10/23 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[25] + "Room 13/26 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 1
energy_sphere_table[StageNames[27] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[27] + "Room 11 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 2
energy_sphere_table[StageNames[28] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[28] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[28] + "Room 12 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[28] + "Room 13 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 3
energy_sphere_table[StageNames[29] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[29] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[29] + "Room 8 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
#Egg Engines 4
energy_sphere_table[StageNames[30] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[30] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[30] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[30] + "Room 5 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[30] + "Room 7 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 5
energy_sphere_table[StageNames[31] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[31] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[31] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[31] + "Room 7 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[31] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 1
energy_sphere_table[StageNames[33] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[33] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[33] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[33] + "Room 9 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 2
energy_sphere_table[StageNames[34] + "Room 1 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[34] + "Room 2 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[34] + "Room 4 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[34] + "Room 9 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 3
energy_sphere_table[StageNames[35] + "Room 3 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[35] + "Room 6 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
energy_sphere_table[StageNames[35] + "Room 8 - Energy Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    energy_sphere_table[StageNames[35] + "Room 11 - Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

#print(len(energy_sphere_table))
    
#should end at ID 309
    
SimplificationArray = [9,14,20,26]
part_sphere_table = {}
part_sphere_table[StageNames[4] + "Room 1 - Part Sphere"] = BaseLocationID + locationincrement
locationincrement += 1
for i in SimplificationArray:
    part_sphere_table[StageNames[i] + "Room 2 - Part Sphere"] = BaseLocationID + locationincrement
    locationincrement += 1

#print(len(part_sphere_table))

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
#White Wafers 1
for i in range(1,8+1):
    gold_star_table[StageNames[15] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,6+1):
    gold_star_table[StageNames[15] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,10+1):
    gold_star_table[StageNames[15] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[15] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[15] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#White Wafers 2
for i in range(1,10+1):
    gold_star_table[StageNames[16] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,6+1):
    gold_star_table[StageNames[16] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,12+1):
    gold_star_table[StageNames[16] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,4+1):
    gold_star_table[StageNames[16] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,11+1):
    gold_star_table[StageNames[16] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,66+1):
    gold_star_table[StageNames[16] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,17+1):
    gold_star_table[StageNames[16] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#White Wafers 3
for i in range(1,5+1):
    gold_star_table[StageNames[17] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,11+1):
    gold_star_table[StageNames[17] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[17] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,16+1):
    gold_star_table[StageNames[17] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,4+1):
    gold_star_table[StageNames[17] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,12+1):
    gold_star_table[StageNames[17] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#White Wafers 4
for i in range(1,16+1):
    gold_star_table[StageNames[18] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,23+1):
    gold_star_table[StageNames[18] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,18+1):
    gold_star_table[StageNames[18] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    gold_star_table[StageNames[18] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,27+1):
    gold_star_table[StageNames[18] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,30+1):
    gold_star_table[StageNames[18] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#White Wafers 5
for i in range(1,2+1):
    gold_star_table[StageNames[19] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,12+1):
    gold_star_table[StageNames[19] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,8+1):
    gold_star_table[StageNames[19] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[19] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    gold_star_table[StageNames[19] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
gold_star_table[StageNames[19] + "Room 7 - Gold Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,45+1):
    gold_star_table[StageNames[19] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,3+1):
    gold_star_table[StageNames[19] + "Room 10 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Nutty Noon 1
for i in range(1,14+1):
    gold_star_table[StageNames[21] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,14+1):
    gold_star_table[StageNames[21] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,15+1):
    gold_star_table[StageNames[21] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,19+1):
    gold_star_table[StageNames[21] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,16+1):
    gold_star_table[StageNames[21] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Nutty Noon 2
for i in range(1,17+1):
    gold_star_table[StageNames[22] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,9+1):
    gold_star_table[StageNames[22] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,5+1):
    gold_star_table[StageNames[22] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,18+1):
    gold_star_table[StageNames[22] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 3
for i in range(1,18+1):
    gold_star_table[StageNames[23] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    gold_star_table[StageNames[23] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[23] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    gold_star_table[StageNames[23] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1):
    gold_star_table[StageNames[23] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
gold_star_table[StageNames[23] + "Room 8 - Gold Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
for i in range(1,16+1):
    gold_star_table[StageNames[24] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    gold_star_table[StageNames[24] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,63+1):
    gold_star_table[StageNames[24] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[24] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    gold_star_table[StageNames[24] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 5
for i in range(1,4+1):
    gold_star_table[StageNames[25] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[25] + "Room 13 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[25] + "Room 26 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[25] + "Room 27 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 1
for i in range(1,20+1):
    gold_star_table[StageNames[27] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    gold_star_table[StageNames[27] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,12+1):
    gold_star_table[StageNames[27] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[27] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15+1):
    gold_star_table[StageNames[27] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1):
    gold_star_table[StageNames[27] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,16+1):
    gold_star_table[StageNames[27] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    gold_star_table[StageNames[27] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,69+1):
    gold_star_table[StageNames[27] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,34+1):
    gold_star_table[StageNames[27] + "Room 10 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 2
for i in range(1,6+1):
    gold_star_table[StageNames[28] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[28] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[28] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[28] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6+1):
    gold_star_table[StageNames[28] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6+1):
    gold_star_table[StageNames[28] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[28] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,17+1):
    gold_star_table[StageNames[28] + "Room 10 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[28] + "Room 12 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    gold_star_table[StageNames[28] + "Room 13 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 3
for i in range(1,21+1):
    gold_star_table[StageNames[29] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,22+1):
    gold_star_table[StageNames[29] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    gold_star_table[StageNames[29] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[29] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,39+1):
    gold_star_table[StageNames[29] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[29] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,26+1):
    gold_star_table[StageNames[29] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 4
for i in range(1,23+1):
    gold_star_table[StageNames[30] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[30] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,31+1):
    gold_star_table[StageNames[30] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    gold_star_table[StageNames[30] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,22+1):
    gold_star_table[StageNames[30] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,42+1):
    gold_star_table[StageNames[30] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 5
for i in range(1,16+1):
    gold_star_table[StageNames[31] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[31] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    gold_star_table[StageNames[31] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[31] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,44+1):
    gold_star_table[StageNames[31] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6+1):
    gold_star_table[StageNames[31] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,18+1):
    gold_star_table[StageNames[31] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[31] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 1
for i in range(1,6+1):
    gold_star_table[StageNames[33] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,16+1):
    gold_star_table[StageNames[33] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[33] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    gold_star_table[StageNames[33] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,37+1):
    gold_star_table[StageNames[33] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,17+1):
    gold_star_table[StageNames[33] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 2
for i in range(1,5+1):
    gold_star_table[StageNames[34] + "Room 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[34] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    gold_star_table[StageNames[34] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    gold_star_table[StageNames[34] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,61+1):
    gold_star_table[StageNames[34] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,31+1):
    gold_star_table[StageNames[34] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    gold_star_table[StageNames[34] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 3
for i in range(1,15+1):
    gold_star_table[StageNames[35] + "Room 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,16+1):
    gold_star_table[StageNames[35] + "Room 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    gold_star_table[StageNames[35] + "Room 4 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1):
    gold_star_table[StageNames[35] + "Room 5 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,16+1):
    gold_star_table[StageNames[35] + "Room 6 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    gold_star_table[StageNames[35] + "Room 7 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,17+1):
    gold_star_table[StageNames[35] + "Room 8 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,83+1):
    gold_star_table[StageNames[35] + "Room 9 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,29+1):
    gold_star_table[StageNames[35] + "Room 10 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,60+1):
    gold_star_table[StageNames[35] + "Room 13 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

extra_excluded_gold_star_table = {}
#Another Dimension
for i in range(1,26+1):
    extra_excluded_gold_star_table[StageNames[37] + "Section 1 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,39+1):
    gold_star_table[StageNames[37] + "Section 2 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15+1):
    extra_excluded_gold_star_table[StageNames[37] + "Section 3 - Gold Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

#print(len(gold_star_table))

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
#White Wafers 1
for i in range(1,2+1):
    red_star_table[StageNames[15] + "Room 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 2
for i in range(1,2+1):
    red_star_table[StageNames[16] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[16] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    red_star_table[StageNames[16] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 3
for i in range(1,3+1):
    red_star_table[StageNames[17] + "Room " + str(i) + " - Red Star"] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 4
red_star_table[StageNames[18] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[18] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[18] + "Room 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[18] + "Room 5 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[18] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 5
red_star_table[StageNames[19] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[19] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[19] + "Room 8 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
red_star_table[StageNames[21] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[21] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[21] + "Room 7 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[21] + "Room 8 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 2
for i in range(1,5+1):
    red_star_table[StageNames[22] + "Room 1 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[22] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 3
for i in range(1,2+1):
    red_star_table[StageNames[23] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[23] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
for i in range(1,2+1):
    red_star_table[StageNames[24] + "Room 1 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    red_star_table[StageNames[24] + "Room 4 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[24] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 5
red_star_table[StageNames[25] + "Room 7 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[25] + "Room 26 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[25] + "Room 28 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 1
red_star_table[StageNames[27] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[27] + "Room 4 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[27] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[27] + "Room 9 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[27] + "Room 10 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 2
for i in range(1,3+1):
    red_star_table[StageNames[28] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[28] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[28] + "Room 13 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 3
red_star_table[StageNames[29] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[29] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    red_star_table[StageNames[29] + "Room 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[29] + "Room 5 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 4
red_star_table[StageNames[30] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[30] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[30] + "Room 6 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 5
red_star_table[StageNames[31] + "Room 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[31] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    red_star_table[StageNames[31] + "Room 5 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    red_star_table[StageNames[31] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
red_star_table[StageNames[31] + "Room 8 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1  
#Dangerous Dinner 1
for i in range(1,3+1):
    red_star_table[StageNames[33] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
red_star_table[StageNames[33] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[33] + "Room 7 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
for i in range(1,2+1):
    red_star_table[StageNames[33] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1 
#Dangerous Dinner 2
for i in range(1,2+1):
    red_star_table[StageNames[34] + "Room 2 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    red_star_table[StageNames[34] + "Room 4 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[34] + "Room 5 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[34] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[34] + "Room 7 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,5+1):
    red_star_table[StageNames[34] + "Room 8 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 3
red_star_table[StageNames[35] + "Room 2 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[35] + "Room 3 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,5+1):
    red_star_table[StageNames[35] + "Room 6 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[35] + "Room 8 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,17+1):
    red_star_table[StageNames[35] + "Room 9 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
red_star_table[StageNames[35] + "Room 10 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
red_star_table[StageNames[35] + "Room 13 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1

extra_excluded_red_star_table = {}
#Another Dimension
extra_excluded_red_star_table[StageNames[37] + "Section 1 - Red Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    extra_excluded_red_star_table[StageNames[37] + "Section 3 - Red Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

#print(len(red_star_table))

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
#White Wafers 1
blue_star_table[StageNames[15] + "Room 1 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[15] + "Room 3 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 2
for i in range(1,7+1):
    blue_star_table[StageNames[16] + "Room 7 - Blue Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 4
blue_star_table[StageNames[18] + "Room 3 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 5
blue_star_table[StageNames[19] + "Room 3 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
blue_star_table[StageNames[21] + "Room 1 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 2
for i in range(1,2+1):
    blue_star_table[StageNames[22] + "Room 6 - Blue Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 3
blue_star_table[StageNames[23] + "Room 5 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
blue_star_table[StageNames[24] + "Room 1 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[24] + "Room 4 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 1
blue_star_table[StageNames[27] + "Room 3 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[27] + "Room 6 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 3
blue_star_table[StageNames[29] + "Room 1 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    blue_star_table[StageNames[29] + "Room 5 - Blue Star #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
blue_star_table[StageNames[29] + "Room 6 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 5
blue_star_table[StageNames[31] + "Room 7 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 2
blue_star_table[StageNames[34] + "Room 1 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[34] + "Room 7 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 3
blue_star_table[StageNames[35] + "Room 5 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[35] + "Room 8 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[35] + "Room 10 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[35] + "Room 13 - Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1

#print(len(blue_star_table))
    
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
#White Wafers 1
for i in range(1,5+1):
    flower_table[StageNames[15] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[15] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,11+1):
    flower_table[StageNames[15] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[15] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 2
for i in range(1,5+1):
    flower_table[StageNames[16] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[16] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[16] + "Room 7 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 3
for i in range(1,3+1):
    flower_table[StageNames[17] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[17] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 4
for i in range(1,3+1):
    flower_table[StageNames[18] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[18] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    flower_table[StageNames[18] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 5
for i in range(1,2+1):
    flower_table[StageNames[19] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[19] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[19] + "Room 10 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 1
for i in range(1,5+1):
    flower_table[StageNames[21] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[21] + "Room 8 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 4
for i in range(1,8+1):
    flower_table[StageNames[24] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 1
for i in range(1,2+1):
    flower_table[StageNames[27] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[27] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
flower_table[StageNames[27] + "Room 4 - Flower"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,5+1):
    flower_table[StageNames[27] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 3
for i in range(1,2+1):
    flower_table[StageNames[29] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[29] + "Room 4 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[29] + "Room 6 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 5
for i in range(1,5+1):
    flower_table[StageNames[31] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 1
for i in range(1,9+1):
    flower_table[StageNames[33] + "Room 1 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[33] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    flower_table[StageNames[33] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    flower_table[StageNames[33] + "Room 5 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[33] + "Room 7 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Dangerous Dinner 2
flower_table[StageNames[34] + "Room 10 - Flower"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 3
for i in range(1,4+1):
    flower_table[StageNames[35] + "Room 2 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[35] + "Room 3 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[35] + "Room 8 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[35] + "Room 9 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    flower_table[StageNames[35] + "Room 13 - Flower #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

#print(len(flower_table))
    
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
#White Wafers 1
one_up_table[StageNames[15] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[15] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 2
one_up_table[StageNames[16] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 3
one_up_table[StageNames[17] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 4
one_up_table[StageNames[18] + "Room 6 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 5
one_up_table[StageNames[19] + "Room 4 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
one_up_table[StageNames[21] + "Room 3 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 3
one_up_table[StageNames[23] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
one_up_table[StageNames[24] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[24] + "Room 4 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 5
for i in range(1,4+1):
    one_up_table[StageNames[25] + "Room 26 - 1-up #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 1
one_up_table[StageNames[27] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[27] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[27] + "Room 8 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 2
one_up_table[StageNames[28] + "Room 12 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 5
one_up_table[StageNames[31] + "Room 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    one_up_table[StageNames[31] + "Room 5 - 1-up #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
one_up_table[StageNames[31] + "Room 8 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 1
one_up_table[StageNames[33] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[33] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[33] + "Room 6 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 2
one_up_table[StageNames[34] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[34] + "Room 7 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[34] + "Room 8 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 3
one_up_table[StageNames[35] + "Room 2 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[35] + "Room 5 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[35] + "Room 13 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1

extra_excluded_one_up_table = {}
#Another Dimension
extra_excluded_one_up_table[StageNames[37] + "Section 1 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
extra_excluded_one_up_table[StageNames[37] + "Section 3 - 1-up"] = BaseLocationID + locationincrement
locationincrement += 1

#print(len(one_up_table))
    
health_pickup_table = {}
#Cookie Country 1
health_pickup_table[StageNames[0] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
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
#White Wafers 1
for i in range(1,2+1):
    health_pickup_table[StageNames[15] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[15] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    health_pickup_table[StageNames[15] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[15] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[15] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 2
for i in range(1,4+1):
    health_pickup_table[StageNames[16] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[16] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[16] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[16] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[16] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,10+1):
    health_pickup_table[StageNames[16] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[16] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 3
health_pickup_table[StageNames[17] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[17] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[17] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[17] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[17] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#White Wafers 4
for i in range(1,2+1):
    health_pickup_table[StageNames[18] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[18] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[18] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[18] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[18] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[18] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[18] + "Room 7 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 5
for i in range(1,2+1):
    health_pickup_table[StageNames[19] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[19] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[19] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[19] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[19] + "Room 10 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
health_pickup_table[StageNames[21] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[21] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[21] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[21] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 2
health_pickup_table[StageNames[22] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[22] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[22] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[22] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[22] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[22] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 3
for i in range(1,2+1):
    health_pickup_table[StageNames[23] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[23] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[23] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[23] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[23] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 4
for i in range(1,3+1):
    health_pickup_table[StageNames[24] + "Room 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    health_pickup_table[StageNames[24] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[24] + "Room 7 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[24] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Nutty Noon 5
health_pickup_table[StageNames[25] + "Room 4 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[25] + "Room 7 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[25] + "Room 10 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[25] + "Room 16 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[25] + "Room 20 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[25] + "Room 23 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 1
for i in range(1,3+1):
    health_pickup_table[StageNames[27] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[27] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[27] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    health_pickup_table[StageNames[27] + "Room 9 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[27] + "Room 10 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[27] + "Room 11 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 2
health_pickup_table[StageNames[28] + "Room 3 - Food"] = BaseLocationID + locationincrement
locationincrement += 1  
health_pickup_table[StageNames[28] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1  
for i in range(1,2+1):
    health_pickup_table[StageNames[28] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[28] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1  
health_pickup_table[StageNames[28] + "Room 10 - Food"] = BaseLocationID + locationincrement
locationincrement += 1  
health_pickup_table[StageNames[28] + "Room 11 - Food"] = BaseLocationID + locationincrement
locationincrement += 1  
#Egg Engines 3
health_pickup_table[StageNames[29] + "Room 1 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[29] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[29] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[29] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[29] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[29] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1    
#Egg Engines 4
health_pickup_table[StageNames[30] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[30] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[30] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[30] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[30] + "Room 6 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#Egg Engines 5
for i in range(1,2+1):
    health_pickup_table[StageNames[31] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[31] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[31] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[31] + "Room 6 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[31] + "Room 7 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 1
for i in range(1,2+1):
    health_pickup_table[StageNames[33] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[33] + "Room 3 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[33] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    health_pickup_table[StageNames[33] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[33] + "Room 8 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[33] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 2
for i in range(1,2+1):
    health_pickup_table[StageNames[34] + "Room 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[34] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[34] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[34] + "Room 5 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
health_pickup_table[StageNames[34] + "Room 6 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,14+1):
    health_pickup_table[StageNames[34] + "Room 7 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[34] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[34] + "Room 9 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 3
health_pickup_table[StageNames[35] + "Room 2 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[35] + "Room 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[35] + "Room 4 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[35] + "Room 5 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[35] + "Room 6 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
    health_pickup_table[StageNames[35] + "Room 8 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    health_pickup_table[StageNames[35] + "Room 9 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
    health_pickup_table[StageNames[35] + "Room 10 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
health_pickup_table[StageNames[35] + "Room 11 - Food"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,4+1):
    health_pickup_table[StageNames[35] + "Room 13 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1

extra_excluded_health_pickup_table = {}
#Another Dimension
for i in range(1,5+1):
    extra_excluded_health_pickup_table[StageNames[37] + "Section 1 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    health_pickup_table[StageNames[37] + "Section 2 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    extra_excluded_health_pickup_table[StageNames[37] + "Section 3 - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#The Arena
for i in range(1,5+1):
    extra_excluded_health_pickup_table[NonStageNames[0] + "Intermission Room - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#The True Arena
for i in range(1,3+1):
    extra_excluded_health_pickup_table[NonStageNames[1] + "Intermission Room - Food #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
#health_pickup_table[StageNames[16] + "Room 2 - Food"] = BaseLocationID + locationincrement
#locationincrement += 1

#print(len(health_pickup_table))

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
#White Wafers 2
maxim_tomato_table[StageNames[16] + "Room 9 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 3
maxim_tomato_table[StageNames[17] + "Room 3 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[17] + "Room 6 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 4
maxim_tomato_table[StageNames[18] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#White Wafers 6
maxim_tomato_table[StageNames[20] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 1
maxim_tomato_table[StageNames[21] + "Room 8 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 2
maxim_tomato_table[StageNames[22] + "Room 8 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 4
maxim_tomato_table[StageNames[24] + "Room 4 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[24] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 5
maxim_tomato_table[StageNames[25] + "Room 2 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[25] + "Room 14 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[25] + "Room 27 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[25] + "Room 28 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Nutty Noon 6
maxim_tomato_table[StageNames[26] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 1
maxim_tomato_table[StageNames[27] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[27] + "Room 11 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 2
maxim_tomato_table[StageNames[28] + "Room 7 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[28] + "Room 12 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 3
maxim_tomato_table[StageNames[29] + "Room 3 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[29] + "Room 6 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[29] + "Room 8 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 5
maxim_tomato_table[StageNames[31] + "Room 2 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[31] + "Room 5 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Egg Engines 6
maxim_tomato_table[StageNames[32] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 1
maxim_tomato_table[StageNames[33] + "Room 2 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[33] + "Room 4 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[33] + "Room 9 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 2
maxim_tomato_table[StageNames[34] + "Room 5 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[34] + "Room 9 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 3
maxim_tomato_table[StageNames[35] + "Room 2 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[35] + "Room 4 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[35] + "Room 11 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[35] + "Room 13 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
#Dangerous Dinner 4
maxim_tomato_table[StageNames[36] + "Room 1 - M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1

extra_excluded_maxim_tomato_table = {}
#The Arena
for i in range(1,5+1):
    extra_excluded_maxim_tomato_table[NonStageNames[0] + "Intermission Room - M-Tomato #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#The True Arena
for i in range(1,3+1):
    extra_excluded_maxim_tomato_table[NonStageNames[1] + "Intermission Room - M-Tomato #" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1


#print(len(maxim_tomato_table))
    
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


arenas_table = {}
for i in range(1,12+1):
    arenas_table["The Arena - Round " + str(i) + " Clear"] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,14+1):
    arenas_table["The True Arena - Round " + str(i) + " Clear"] = BaseLocationID + locationincrement
    locationincrement += 1


extra_sanity_table = {}
for i in stage_completion_table.keys():
    extra_sanity_table["EX " + i] = BaseLocationID + locationincrement
    compound_stage_completion_table["EX " + i] = BaseLocationID + locationincrement
    locationincrement += 1

stage_completion_table["The Arena - Complete"] = BaseLocationID + locationincrement
compound_stage_completion_table["The Arena - Complete"] = BaseLocationID + locationincrement
locationincrement += 1
stage_completion_table["The True Arena - Complete"] = BaseLocationID + locationincrement
compound_stage_completion_table["The True Arena - Complete"] = BaseLocationID + locationincrement
locationincrement += 1

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

#still need to separate the unique checks from the extra pool so it doesn't make dupes!!!



composite_location: dict[str, int] = {
    **stage_completion_table,
    **energy_sphere_table,
    **part_sphere_table,
    **gold_star_table,
    **extra_excluded_gold_star_table,
    **red_star_table,
    **extra_excluded_red_star_table,
    **blue_star_table,
    **flower_table,
    **one_up_table,
    **extra_excluded_one_up_table,
    **health_pickup_table,
    **extra_excluded_health_pickup_table,
    **maxim_tomato_table,
    **extra_excluded_maxim_tomato_table,
    **challenge_table,
    **subgame_table,
    **arenas_table,
    **extra_sanity_table
}

def AllRegionsWhichCanBeSplitForEXtraSanityMoreEasily(world: "KRtDLWorld", EXStatus: str) -> None:
    regions = []

    regions.append(Region(EXStatus + "Popstar Map", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Halcandra Map", world.player, world.multiworld))

    regions.append(Region(EXStatus + "Lor Starcutter", world.player, world.multiworld))

    regions.append(Region(EXStatus + "Cookie Country Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Raisin Ruins Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Onion Ocean Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "White Wafers Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Nutty Noon Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Egg Engines Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Dangerous Dinner Hub", world.player, world.multiworld))
    regions.append(Region(EXStatus + "Another Dimension", world.player, world.multiworld))
    
    for i in range(1,5+1):
        regions.append(Region(EXStatus + StageNames[0] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(EXStatus + StageNames[1] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,5+1):
        regions.append(Region(EXStatus + StageNames[2] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,7+1):
        regions.append(Region(EXStatus + StageNames[3] + "Room " + str(i), world.player, world.multiworld))

    regions.append(Region(EXStatus + StageNames[4] + "Room 1", world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[5] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(EXStatus + StageNames[6] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(EXStatus + StageNames[7] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(EXStatus + StageNames[8] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,9+1):
        regions.append(Region(EXStatus + StageNames[10] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(EXStatus + StageNames[11] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(EXStatus + StageNames[12] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[13] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[14] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,5+1):
        regions.append(Region(EXStatus + StageNames[15] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,9+1):
        regions.append(Region(EXStatus + StageNames[16] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(EXStatus + StageNames[17] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,7+1):
        regions.append(Region(EXStatus + StageNames[18] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(EXStatus + StageNames[19] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[20] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,9+1):
        regions.append(Region(EXStatus + StageNames[21] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[22] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[23] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[24] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,28+1):
        regions.append(Region(EXStatus + StageNames[25] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,4+1):
        regions.append(Region(EXStatus + StageNames[25] + "Energy Sphere Region #" + str(i), world.player, world.multiworld))

    regions.append(Region(EXStatus + StageNames[25] + "Goal Region", world.player, world.multiworld))
    
    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[26] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,11+1):
        regions.append(Region(EXStatus + StageNames[27] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,13+1):
        regions.append(Region(EXStatus + StageNames[28] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[29] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,7+1):
        regions.append(Region(EXStatus + StageNames[30] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(EXStatus + StageNames[31] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[32] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,9+1):
        regions.append(Region(EXStatus + StageNames[33] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(EXStatus + StageNames[34] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,13+1):
        regions.append(Region(EXStatus + StageNames[35] + "Room " + str(i), world.player, world.multiworld))
    #NOTE DANGEROUS DINNER 7-3 ROOM 12 IS 13, ROOM 13 IS 14 ON THE SPREADSHEET
    #NUMBERING GOT CONFUSING THANKS TO THAT USELESS WARP STAR TRANSITION ROOM

    for i in range(1,2+1):
        regions.append(Region(EXStatus + StageNames[36] + "Room " + str(i), world.player, world.multiworld))
                              
    world.multiworld.regions += regions

def create_all_regions(world: "KRtDLWorld") -> None:
    if world.options.extra_sanity:
        AllRegionsWhichCanBeSplitForEXtraSanityMoreEasily(world, "EX ")
    AllRegionsWhichCanBeSplitForEXtraSanityMoreEasily(world, "")

def AddLocationsButAMoreCallableFunctionSoEXtraSanityCanWork(world: "KRtDLWorld", EXStatus: str) -> None:
    MenuRegion = world.get_region("Menu")
    PopstarMapRegion = world.get_region(EXStatus + "Popstar Map")
    HalcandraMapRegion = world.get_region(EXStatus + "Halcandra Map")
    LorStarcutterRegion = world.get_region(EXStatus + "Lor Starcutter")
    
    CookieCountryHub = world.get_region(EXStatus + "Cookie Country Hub")
    RaisinRuinsHub = world.get_region(EXStatus + "Raisin Ruins Hub")
    OnionOceanHub = world.get_region(EXStatus + "Onion Ocean Hub")
    WhiteWafersHub = world.get_region(EXStatus + "White Wafers Hub")
    NuttyNoonHub = world.get_region(EXStatus + "Nutty Noon Hub")
    EggEnginesHub = world.get_region(EXStatus + "Egg Engines Hub")
    DangerousDinnerHub = world.get_region(EXStatus + "Dangerous Dinner Hub")
    AnotherDimension = world.get_region(EXStatus + "Another Dimension")
    
    OneOneRooms = [world.get_region(EXStatus + "Cookie Country Stage 1 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 4"),
                  world.get_region(EXStatus + "Cookie Country Stage 1 Room 5")]

    OneTwoRooms = [world.get_region(EXStatus + "Cookie Country Stage 2 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 4"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 5"),
                  world.get_region(EXStatus + "Cookie Country Stage 2 Room 6")]
    
    OneThreeRooms = [world.get_region(EXStatus + "Cookie Country Stage 3 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 4"),
                  world.get_region(EXStatus + "Cookie Country Stage 3 Room 5")]
    
    OneFourRooms = [world.get_region(EXStatus + "Cookie Country Stage 4 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 4"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 5"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 6"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 7")]
    
    OneFiveRegion = world.get_region(EXStatus + "Cookie Country Stage 5 Room 1")
    
    TwoOneRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 7"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 8")]
    
    TwoTwoRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 7"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 8"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 9"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 10")]

    TwoThreeRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 6")]
    
    TwoFourRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 7"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 8"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 9"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 10")]
    
    TwoFiveRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 5 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 5 Room 2")]
    
    ThreeOneRooms = [world.get_region(EXStatus + "Onion Ocean Stage 1 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 8"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 9")]
    
    ThreeTwoRooms = [world.get_region(EXStatus + "Onion Ocean Stage 2 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 6")]

    ThreeThreeRooms = [world.get_region(EXStatus + "Onion Ocean Stage 3 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 8"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 9"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 10")]
    
    ThreeFourRooms = [world.get_region(EXStatus + "Onion Ocean Stage 4 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 8")]

    ThreeFiveRooms = [world.get_region(EXStatus + "Onion Ocean Stage 5 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 5 Room 2")]

    FourOneRooms = [world.get_region(EXStatus + "White Wafers Stage 1 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 5")]

    FourTwoRooms = [world.get_region(EXStatus + "White Wafers Stage 2 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 7"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 8"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 9")]

    FourThreeRooms = [world.get_region(EXStatus + "White Wafers Stage 3 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 6")]

    FourFourRooms = [world.get_region(EXStatus + "White Wafers Stage 4 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 7")]

    FourFiveRooms = [world.get_region(EXStatus + "White Wafers Stage 5 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 7"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 8"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 9"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 10")]

    FourSixRooms = [world.get_region(EXStatus + "White Wafers Stage 6 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 6 Room 2")]

    FiveOneRooms = [world.get_region(EXStatus + "Nutty Noon Stage 1 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 8"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 9")]

    FiveTwoRooms = [world.get_region(EXStatus + "Nutty Noon Stage 2 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 8")]

    FiveThreeRooms = [world.get_region(EXStatus + "Nutty Noon Stage 3 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 8")]

    FiveFourRooms = [world.get_region(EXStatus + "Nutty Noon Stage 4 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 8")]

    FiveFiveRooms = [world.get_region(EXStatus + "Nutty Noon Stage 5 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 8"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 9"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 10"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 11"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 12"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 13"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 14"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 15"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 16"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 17"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 18"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 19"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 20"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 21"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 22"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 23"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 24"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 25"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 26"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 27"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 28")]
    FiveFiveGoalRegion = world.get_region(EXStatus + "Nutty Noon Stage 5 Goal Region")

    FiveSixRooms = [world.get_region(EXStatus + "Nutty Noon Stage 6 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 6 Room 2")]

    SixOneRooms = [world.get_region(EXStatus + "Egg Engines Stage 1 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 8"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 9"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 10"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 11")]

    SixTwoRooms = [world.get_region(EXStatus + "Egg Engines Stage 2 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 8"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 9"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 10"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 11"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 12"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 13")]

    SixThreeRooms = [world.get_region(EXStatus + "Egg Engines Stage 3 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 8")]

    SixFourRooms = [world.get_region(EXStatus + "Egg Engines Stage 4 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 7")]

    SixFiveRooms = [world.get_region(EXStatus + "Egg Engines Stage 5 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 8")]

    SixSixRooms = [world.get_region(EXStatus + "Egg Engines Stage 6 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 6 Room 2")]
    
    SevenOneRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 9")]

    SevenTwoRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 9"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 10")]

    SevenThreeRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 9"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 10"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 11"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 12"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 13")]

    SevenFourRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 4 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 4 Room 2")]
    
    OneOneRooms[2].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Cookie Country Stage 1 - Complete"]), KRtDLLocation)
    OneTwoRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Cookie Country Stage 2 - Complete"]), KRtDLLocation)
    OneThreeRooms[4].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Cookie Country Stage 3 - Complete"]), KRtDLLocation)
    OneFourRooms[4].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Cookie Country Stage 4 - Complete"]), KRtDLLocation)
    OneFiveRegion.add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Cookie Country Stage 5 - Complete"]), KRtDLLocation)
    TwoOneRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 - Complete"]), KRtDLLocation)
    TwoTwoRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 - Complete"]), KRtDLLocation)
    TwoThreeRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 - Complete"]), KRtDLLocation)
    TwoFourRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 - Complete"]), KRtDLLocation)
    TwoFiveRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Raisin Ruins Stage 5 - Complete"]), KRtDLLocation)
    ThreeOneRooms[6].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 - Complete"]), KRtDLLocation)
    ThreeTwoRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 - Complete"]), KRtDLLocation)
    ThreeThreeRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 - Complete"]), KRtDLLocation)
    ThreeFourRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 - Complete"]), KRtDLLocation)
    ThreeFiveRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Onion Ocean Stage 5 - Complete"]), KRtDLLocation)
    FourOneRooms[4].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 1 - Complete"]), KRtDLLocation)
    FourTwoRooms[6].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 2 - Complete"]), KRtDLLocation)
    FourThreeRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 3 - Complete"]), KRtDLLocation)
    FourFourRooms[4].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 4 - Complete"]), KRtDLLocation)
    FourFiveRooms[9].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 5 - Complete"]), KRtDLLocation)
    FourSixRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "White Wafers Stage 6 - Complete"]), KRtDLLocation)
    FiveOneRooms[8].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 - Complete"]), KRtDLLocation)
    FiveTwoRooms[6].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 - Complete"]), KRtDLLocation)
    FiveThreeRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 - Complete"]), KRtDLLocation)
    FiveFourRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 - Complete"]), KRtDLLocation)
    FiveFiveGoalRegion.add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 - Complete"]), KRtDLLocation)
    FiveSixRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Nutty Noon Stage 6 - Complete"]), KRtDLLocation)
    SixOneRooms[8].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 1 - Complete"]), KRtDLLocation)
    SixTwoRooms[12].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 2 - Complete"]), KRtDLLocation)
    SixThreeRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 3 - Complete"]), KRtDLLocation)
    SixFourRooms[5].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 4 - Complete"]), KRtDLLocation)
    SixFiveRooms[7].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 5 - Complete"]), KRtDLLocation)
    SixSixRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Egg Engines Stage 6 - Complete"]), KRtDLLocation)
    SevenOneRooms[6].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 - Complete"]), KRtDLLocation)
    SevenTwoRooms[9].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 - Complete"]), KRtDLLocation)
    SevenThreeRooms[11].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 - Complete"]), KRtDLLocation)
    SevenFourRooms[1].add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 4 - Complete"]), KRtDLLocation)
    AnotherDimension.add_locations(get_stage_complete_location_names_with_ids([EXStatus + "Another Dimension Final Boss - Complete"]), KRtDLLocation)
    
    
    if world.options.shuffle_energy_spheres:
        OneOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 2 - Energy Sphere"]), KRtDLLocation)
         
        OneOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 5 - Energy Sphere #1"]), KRtDLLocation)
         
        OneOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 5 - Energy Sphere #2"]), KRtDLLocation) 
         

        OneTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        OneTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        OneTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 6 - Energy Sphere"]), KRtDLLocation) 
         

        OneThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 2 - Energy Sphere"]), KRtDLLocation)
         
        OneThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        OneThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation) 
         

        OneFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 1 - Energy Sphere"]), KRtDLLocation)
         
        OneFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        OneFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 7 - Energy Sphere #1"]), KRtDLLocation) 
         
        OneFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 7 - Energy Sphere #2"]), KRtDLLocation) 
         


        TwoOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        TwoOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)
         
        TwoOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 8 - Energy Sphere"]), KRtDLLocation) 
         

        TwoTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        TwoTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 6 - Energy Sphere"]), KRtDLLocation)
         
        TwoTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
         
        TwoTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 10 - Energy Sphere #2"]), KRtDLLocation) 
         

        TwoThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        TwoThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation) 
         
        TwoThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation) 
         

        TwoFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        TwoFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        TwoFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 7 - Energy Sphere"]), KRtDLLocation) 
         
        TwoFourRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
         
        TwoFourRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 10 - Energy Sphere #2"]), KRtDLLocation) 
         


        ThreeOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)
         
        ThreeOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 9 - Energy Sphere #1"]), KRtDLLocation)
         
        ThreeOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 9 - Energy Sphere #2"]), KRtDLLocation) 
         

        ThreeTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 2 - Energy Sphere"]), KRtDLLocation)
         
        ThreeTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Energy Sphere #1"]), KRtDLLocation) 
         
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Energy Sphere #2"]), KRtDLLocation) 
         

        ThreeThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation)
         
        ThreeThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation)
         
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 10 - Energy Sphere #1"]), KRtDLLocation) 
         
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 10 - Energy Sphere #2"]), KRtDLLocation) 
         

        ThreeFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        ThreeFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 5 - Energy Sphere"]), KRtDLLocation)
         
        ThreeFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 6 - Energy Sphere"]), KRtDLLocation) 
         
        ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - Energy Sphere"]), KRtDLLocation) 
         
        ThreeFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 8 - Energy Sphere"]), KRtDLLocation)



        FourOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 1 - Energy Sphere"]), KRtDLLocation)
         
        FourOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        FourOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 4 - Energy Sphere"]), KRtDLLocation) 


        FourTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        FourTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 5 - Energy Sphere"]), KRtDLLocation)
         
        FourTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 9 - Energy Sphere #1"]), KRtDLLocation) 

        FourTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 9 - Energy Sphere #2"]), KRtDLLocation) 


        FourThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 2 - Energy Sphere"]), KRtDLLocation)
         
        FourThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 3 - Energy Sphere"]), KRtDLLocation)
         
        FourThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation) 

        FourThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation) 


        FourFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 2 - Energy Sphere"]), KRtDLLocation)
         
        FourFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        FourFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 7 - Energy Sphere #1"]), KRtDLLocation) 

        FourFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 7 - Energy Sphere #2"]), KRtDLLocation) 


        FourFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 4 - Energy Sphere"]), KRtDLLocation)
         
        FourFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 6 - Energy Sphere"]), KRtDLLocation)
         
        FourFiveRooms[8].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 9 - Energy Sphere"]), KRtDLLocation) 

        FourFiveRooms[9].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 10 - Energy Sphere"]), KRtDLLocation) 

        

        FiveOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)

        FiveOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 7 - Energy Sphere"]), KRtDLLocation)

        FiveOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 8 - Energy Sphere"]), KRtDLLocation)

        FiveOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 9 - Energy Sphere"]), KRtDLLocation)


        FiveTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 3 - Energy Sphere"]), KRtDLLocation)

        FiveTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 5 - Energy Sphere"]), KRtDLLocation)

        FiveTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 8 - Energy Sphere #1"]), KRtDLLocation)

        FiveTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 8 - Energy Sphere #2"]), KRtDLLocation)


        FiveThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 3 - Energy Sphere"]), KRtDLLocation)

        FiveThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 5 - Energy Sphere"]), KRtDLLocation)

        FiveThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation)

        FiveThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 8 - Energy Sphere"]), KRtDLLocation)
        

        FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - Energy Sphere"]), KRtDLLocation)

        FiveFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 2 - Energy Sphere"]), KRtDLLocation)

        FiveFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 7 - Energy Sphere #1"]), KRtDLLocation)

        FiveFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 7 - Energy Sphere #2"]), KRtDLLocation)
        
        
        world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #1").add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 4/16 - Energy Sphere"]), KRtDLLocation)

        world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #2").add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 7/20 - Energy Sphere"]), KRtDLLocation)

        world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #3").add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 10/23 - Energy Sphere"]), KRtDLLocation)

        world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #4").add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 13/26 - Energy Sphere"]), KRtDLLocation)
        

        SixOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 5 - Energy Sphere"]), KRtDLLocation)

        SixOneRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 11 - Energy Sphere #1"]), KRtDLLocation)

        SixOneRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 11 - Energy Sphere #2"]), KRtDLLocation)


        SixTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 6 - Energy Sphere"]), KRtDLLocation)

        SixTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 8 - Energy Sphere"]), KRtDLLocation)

        SixTwoRooms[11].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 12 - Energy Sphere"]), KRtDLLocation)

        SixTwoRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 13 - Energy Sphere"]), KRtDLLocation)


        SixThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 2 - Energy Sphere"]), KRtDLLocation)

        SixThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 4 - Energy Sphere"]), KRtDLLocation)

        SixThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 8 - Energy Sphere #1"]), KRtDLLocation)

        SixThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 8 - Energy Sphere #2"]), KRtDLLocation)


        SixFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 2 - Energy Sphere"]), KRtDLLocation)

        SixFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 3 - Energy Sphere"]), KRtDLLocation)

        SixFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 4 - Energy Sphere"]), KRtDLLocation)

        SixFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 5 - Energy Sphere"]), KRtDLLocation)
        
        SixFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 7 - Energy Sphere"]), KRtDLLocation)


        SixFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 2 - Energy Sphere"]), KRtDLLocation)

        SixFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 4 - Energy Sphere"]), KRtDLLocation)

        SixFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 6 - Energy Sphere"]), KRtDLLocation)

        SixFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 7 - Energy Sphere"]), KRtDLLocation)
        
        SixFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 8 - Energy Sphere"]), KRtDLLocation)


        SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - Energy Sphere"]), KRtDLLocation)

        SevenOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 4 - Energy Sphere"]), KRtDLLocation)
        
        SevenOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 6 - Energy Sphere"]), KRtDLLocation)

        SevenOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 9 - Energy Sphere #1"]), KRtDLLocation)

        SevenOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 9 - Energy Sphere #2"]), KRtDLLocation)


        SevenTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 1 - Energy Sphere"]), KRtDLLocation)

        SevenTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 2 - Energy Sphere"]), KRtDLLocation)
        
        SevenTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 4 - Energy Sphere"]), KRtDLLocation)

        SevenTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 9 - Energy Sphere #1"]), KRtDLLocation)

        SevenTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 9 - Energy Sphere #2"]), KRtDLLocation)


        SevenThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 3 - Energy Sphere"]), KRtDLLocation)

        SevenThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 6 - Energy Sphere"]), KRtDLLocation)
        
        SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Energy Sphere"]), KRtDLLocation)

        SevenThreeRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 11 - Energy Sphere #1"]), KRtDLLocation)

        SevenThreeRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 11 - Energy Sphere #2"]), KRtDLLocation)
    
        
    
    if world.options.shuffle_part_spheres:
        OneFiveRegion.add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 5 Room 1 - Part Sphere"]), KRtDLLocation)
         
        TwoFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 5 Room 2 - Part Sphere"]), KRtDLLocation)
         
        ThreeFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 5 Room 2 - Part Sphere"]), KRtDLLocation)

        FourSixRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 6 Room 2 - Part Sphere"]), KRtDLLocation)

        FiveSixRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 6 Room 2 - Part Sphere"]), KRtDLLocation)
         

   
    
    
    if world.options.star_sanity:
        for i in range(1,13+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,7+1):
            OneOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,25+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,12+1):
            OneOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)    
             

        for i in range(1,3+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,10+1):
            OneTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,11+1):
            OneTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,7+1):
            OneTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        OneTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 6 - Gold Star"]), KRtDLLocation)
         

        for i in range(1,3+1):
            OneThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,8+1):
            OneThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,17+1):
            OneThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,12+1):
            OneThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            OneThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,9+1):
            OneFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,4+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            OneFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,55+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,5+1):
            OneFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             


        for i in range(1,12+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            TwoOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,10+1):
            TwoOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,5+1):
            TwoOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,20+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,19+1):
            TwoTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,16+1):
            TwoTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            TwoTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,41+1):
            TwoTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,35+1):
            TwoTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,9+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            TwoThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,15+1):
            TwoThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,18+1):
            TwoThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,18+1):
            TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,17+1):
            TwoFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,6+1):
            TwoFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            TwoFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,4+1):
            TwoFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,12+1):
            TwoFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,28+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,21+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
             


        for i in range(1,18+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,27+1):
            ThreeOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            ThreeOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,15+1):
            ThreeOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,21+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,12+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,19+1):
            ThreeOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,12+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,7+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,15+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,28+1):
            ThreeTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,45+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,4+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,19+1):
            ThreeThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,14+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,16+1):
            ThreeThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,69+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,55+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,23+1):
            ThreeThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,12+1):
            ThreeFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,11+1):
            ThreeFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,10+1):
            ThreeFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,21+1):
            ThreeFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,15+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,27+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)



        for i in range(1,8+1):
            FourOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,6+1):
            FourOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,10+1):
            FourOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            FourOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FourOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,10+1):
            FourTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,6+1):
            FourTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            FourTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FourTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            FourTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,66+1):
            FourTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,17+1):
            FourTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,5+1):
            FourThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            FourThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            FourThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,16+1):
            FourThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FourThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            FourThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,16+1):
            FourFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)    

        for i in range(1,23+1):
            FourFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)   

        for i in range(1,18+1):
            FourFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation) 

        for i in range(1,2+1):
            FourFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,27+1):
            FourFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,30+1):
            FourFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            FourFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            FourFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            FourFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FourFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        FourFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 7 - Gold Star"]), KRtDLLocation)

        for i in range(1,45+1):
            FourFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FourFiveRooms[9].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 10 - Gold Star #" + str(i)]), KRtDLLocation)



        for i in range(1,14+1):
            FiveOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,14+1):
            FiveOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,15+1):
            FiveOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,19+1):
            FiveOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,16+1):
            FiveOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)
        

        for i in range(1,17+1):
            FiveTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,9+1):
            FiveTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            FiveTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,18+1):
            FiveTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,18+1):
            FiveThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,10+1):
            FiveThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            FiveThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            FiveThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,13+1):
            FiveThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        FiveThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 8 - Gold Star"]), KRtDLLocation)


        for i in range(1,16+1):
            FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            FiveFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,63+1):
            FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            FiveFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FiveFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,4+1):
            FiveFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            FiveFiveRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 13 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveFiveRooms[25].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 26 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveFiveRooms[26].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 27 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,20+1):
            SixOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            SixOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            SixOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,15+1):
            SixOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,13+1):
            SixOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,16+1):
            SixOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            SixOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,69+1):
            SixOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,34+1):
            SixOneRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 10 - Gold Star #" + str(i)]), KRtDLLocation)
    

        for i in range(1,6+1):
            SixTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,6+1):
            SixTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,6+1):
            SixTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)
        
        for i in range(1,9+1):
            SixTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,17+1):
            SixTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 10 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixTwoRooms[11].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 12 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            SixTwoRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 13 - Gold Star #" + str(i)]), KRtDLLocation)



        for i in range(1,21+1):
            SixThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,22+1):
            SixThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,7+1):
            SixThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            SixThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,39+1):
            SixThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,26+1):
            SixThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,23+1):
            SixFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            SixFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,31+1):
            SixFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,7+1):
            SixFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,22+1):
            SixFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,42+1):
            SixFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,16+1):
            SixFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            SixFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,10+1):
            SixFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,44+1):
            SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,6+1):
            SixFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,18+1):
            SixFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,6+1):
            SevenOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,16+1):
            SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,7+1):
            SevenOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,37+1):
            SevenOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,17+1):
            SevenOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,5+1):
            SevenTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            SevenTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            SevenTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            SevenTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,61+1):
            SevenTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,31+1):
            SevenTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            SevenTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,15+1):
            SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,16+1):
            SevenThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            SevenThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 4 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,13+1):
            SevenThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 5 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,16+1):
            SevenThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 6 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 7 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,17+1):
            SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,83+1):
            SevenThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 9 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,29+1):
            SevenThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 10 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,60+1):
            SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,39+1):
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 2 - Gold Star #" + str(i)]), KRtDLLocation)
            
    
    

    
    if world.options.red_star_sanity:
        OneOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 1 - Red Star"]), KRtDLLocation)
         
        for i in range(1,3+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 3 - Red Star #" + str(i)]), KRtDLLocation)
             

        OneTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 2 - Red Star"]), KRtDLLocation)  
         
        OneTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 3 - Red Star"]), KRtDLLocation)  
         

        OneThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 2 - Red Star"]), KRtDLLocation) 
         
        for i in range(1,2+1):
            OneThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 4 - Red Star #" + str(i)]), KRtDLLocation)
             
        OneThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 5 - Red Star"]), KRtDLLocation)
         

        for i in range(1,5+1):
            OneFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 2 - Red Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 3 - Red Star #" + str(i)]), KRtDLLocation)
             
        OneFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 5 - Red Star"]), KRtDLLocation)
         

        
        TwoOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 1 - Red Star"]), KRtDLLocation)
         
        TwoOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 3 - Red Star"]), KRtDLLocation)
         

        TwoTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 1 - Red Star"]), KRtDLLocation)
         
        for i in range(1,6+1):
            TwoTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 8 - Red Star #" + str(i)]), KRtDLLocation)
             

        for i in range(1,3+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 1 - Red Star #" + str(i)]), KRtDLLocation)
             
        TwoThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 3 - Red Star"]), KRtDLLocation)
         
        TwoThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 4 - Red Star"]), KRtDLLocation)
         
        TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - Red Star"]), KRtDLLocation)
         
        for i in range(1,2+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 6 - Red Star #" + str(i)]), KRtDLLocation)
             

        TwoFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 5 - Red Star"]), KRtDLLocation)
         
        for i in range(1,4+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 8 - Red Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 9 - Red Star #" + str(i)]), KRtDLLocation)
             

        
        ThreeOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 1 - Red Star"]), KRtDLLocation)
         
        ThreeOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 3 - Red Star"]), KRtDLLocation)
         
        ThreeOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 4 - Red Star"]), KRtDLLocation)
         
        ThreeOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 6 - Red Star"]), KRtDLLocation)
         
        ThreeOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 8 - Red Star"]), KRtDLLocation)
         

        ThreeTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 3 - Red Star"]), KRtDLLocation)
         
        ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Red Star"]), KRtDLLocation)
         

        for i in range(1,2+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 1 - Red Star #" + str(i)]), KRtDLLocation)
             
        ThreeThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 2 - Red Star"]), KRtDLLocation)
         
        for i in range(1,2+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 4 - Red Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            ThreeThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 5 - Red Star #" + str(i)]), KRtDLLocation)
             
        ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - Red Star"]), KRtDLLocation)
         
        for i in range(1,2+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 8 - Red Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,5+1):
            ThreeThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 9 - Red Star #" + str(i)]), KRtDLLocation)
             

        ThreeFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 1 - Red Star"]), KRtDLLocation)
         
        ThreeFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 4 - Red Star"]), KRtDLLocation)
         
        ThreeFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 6 - Red Star"]), KRtDLLocation)
         
        for i in range(1,4+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - Red Star #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 8 - Red Star #" + str(i)]), KRtDLLocation)


        
        for i in range(1,2+1):
            FourOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 3 - Red Star #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            FourTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FourTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,7+1):
            FourTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 8 - Red Star #" + str(i)]), KRtDLLocation)


        for i in range(0,3):
            FourThreeRooms[i].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room " + str(i + 1) + " - Red Star"]), KRtDLLocation)


        FourFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 1 - Red Star"]), KRtDLLocation)

        FourFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 2 - Red Star"]), KRtDLLocation)

        for i in range(1,3+1):
            FourFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 3 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FourFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 5 - Red Star #" + str(i)]), KRtDLLocation)

        FourFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 6 - Red Star"]), KRtDLLocation)


        FourFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 3 - Red Star"]), KRtDLLocation)

        for i in range(1,3+1):
            FourFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        FourFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 8 - Red Star"]), KRtDLLocation)



        FiveOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 2 - Red Star"]), KRtDLLocation)

        FiveOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 6 - Red Star"]), KRtDLLocation)

        FiveOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 7 - Red Star"]), KRtDLLocation)

        FiveOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 8 - Red Star"]), KRtDLLocation)


        for i in range(1,5+1):
            FiveTwoRooms[0 ].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 1 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 6 - Red Star #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            FiveThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        FiveThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 6 - Red Star"]), KRtDLLocation)


        for i in range(1,2+1):
            FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FiveFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 6 - Red Star #" + str(i)]), KRtDLLocation)


        FiveFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 7 - Red Star"]), KRtDLLocation)

        FiveFiveRooms[25].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 26 - Red Star"]), KRtDLLocation)
        
        for i in range(1,3+1):
            FiveFiveRooms[27].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 28 - Red Star #" + str(i)]), KRtDLLocation) 



        SixOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 2 - Red Star"]), KRtDLLocation)
        
        for i in range(1,2+1):
            SixOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 4 - Red Star #" + str(i)]), KRtDLLocation)

        SixOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 6 - Red Star"]), KRtDLLocation)

        for i in range(1,2+1):
            SixOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 9 - Red Star #" + str(i)]), KRtDLLocation)

        SixOneRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 10 - Red Star"]), KRtDLLocation)


        for i in range(1,3+1):
            SixTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 8 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixTwoRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 13 - Red Star #" + str(i)]), KRtDLLocation)


        SixThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 1 - Red Star"]), KRtDLLocation)

        for i in range(1,4+1):
            SixThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 3 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 5 - Red Star #" + str(i)]), KRtDLLocation)


        SixFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 1 - Red Star"]), KRtDLLocation)

        SixFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 2 - Red Star"]), KRtDLLocation)

        SixFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 6 - Red Star"]), KRtDLLocation)


        SixFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 1 - Red Star"]), KRtDLLocation)

        for i in range(1,4+1):
            SixFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,10+1):
            SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        SixFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 8 - Red Star"]), KRtDLLocation)


        for i in range(1,3+1):
            SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        SevenOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 5 - Red Star"]), KRtDLLocation)

        for i in range(1,4+1):
            SevenOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 7 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 8 - Red Star #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            SevenTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 2 - Red Star #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            SevenTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 4 - Red Star #" + str(i)]), KRtDLLocation)

        SevenTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 5 - Red Star"]), KRtDLLocation)

        for i in range(1,3+1):
            SevenTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 6 - Red Star #" + str(i)]), KRtDLLocation)
        
        if world.options.hard_logic:
            SevenTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 6 - Red Star #4"]), KRtDLLocation)

        SevenTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 7 - Red Star"]), KRtDLLocation)

        for i in range(1,5+1):
            SevenTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 8 - Red Star #" + str(i)]), KRtDLLocation)


        SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - Red Star"]), KRtDLLocation)

        SevenThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 3 - Red Star"]), KRtDLLocation)

        for i in range(1,5+1):
            SevenThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 6 - Red Star #" + str(i)]), KRtDLLocation)

        SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Red Star"]), KRtDLLocation)

        for i in range(1,17+1):
            SevenThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 9 - Red Star #" + str(i)]), KRtDLLocation)

        SevenThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 10 - Red Star"]), KRtDLLocation)

        SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - Red Star"]), KRtDLLocation)




    
    if world.options.blue_star_sanity:
        OneTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 2 - Blue Star"]), KRtDLLocation)
         


        TwoOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 8 - Blue Star"]), KRtDLLocation)
         

        TwoTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 8 - Blue Star"]), KRtDLLocation)
         


        ThreeOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 2 - Blue Star"]), KRtDLLocation)
         
        ThreeOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 7 - Blue Star"]), KRtDLLocation)
         

        ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - Blue Star"]), KRtDLLocation)



        FourOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 1 - Blue Star"]), KRtDLLocation)

        FourOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 3 - Blue Star"]), KRtDLLocation)


        for i in range(1,7+1):
            FourTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 7 - Blue Star #" + str(i)]), KRtDLLocation)


        FourFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 3 - Blue Star"]), KRtDLLocation)


        FourFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 3 - Blue Star"]), KRtDLLocation)


        
        FiveOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 1 - Blue Star"]), KRtDLLocation)


        for i in range(1,2+1):
            FiveTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 6 - Blue Star #" + str(i)]), KRtDLLocation)


        FiveThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 5 - Blue Star"]), KRtDLLocation)


        FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - Blue Star"]), KRtDLLocation)

        FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - Blue Star"]), KRtDLLocation)



        SixOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 3 - Blue Star"]), KRtDLLocation)

        SixOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 6 - Blue Star"]), KRtDLLocation)


        SixThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 1 - Blue Star"]), KRtDLLocation)

        for i in range(1,2+1):
            SixThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 5 - Blue Star #" + str(i)]), KRtDLLocation)

        SixThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 6 - Blue Star"]), KRtDLLocation)


        SixFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 7 - Blue Star"]), KRtDLLocation)


        SevenTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 1 - Blue Star"]), KRtDLLocation)

        SevenTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 7 - Blue Star"]), KRtDLLocation)


        SevenThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 5 - Blue Star"]), KRtDLLocation)

        SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Blue Star"]), KRtDLLocation)

        SevenThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 10 - Blue Star"]), KRtDLLocation)

        SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - Blue Star"]), KRtDLLocation)
    
   


    
    if world.options.flower_sanity:
        for i in range(1,6+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation)
             
        for i in range(1,10+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,4+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,2+1):
            OneThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation)  
             
        for i in range(1,2+1):
            OneThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 5 - Flower #" + str(i)]), KRtDLLocation)  
             

        for i in range(1,8+1):
            OneFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,15+1):
            OneFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,3+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,7+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 5 - Flower #" + str(i)]), KRtDLLocation) 
             


        for i in range(1,2+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            TwoOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
             
        TwoOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 5 - Flower"]), KRtDLLocation)
         
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 7 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 8 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,7+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            TwoTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,4+1):
            TwoTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 4 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,2+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
             


        for i in range(1,8+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,3+1):
            ThreeOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,5+1):
            ThreeOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,9+1):
            ThreeOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 4 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,7+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,3+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 7 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,2+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,7+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 3 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,13+1):
            ThreeTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 5 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,8+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,8+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 1 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,3+1):
            ThreeThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 2 - Flower #" + str(i)]), KRtDLLocation) 
             
        ThreeThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 4 - Flower"]), KRtDLLocation)
         
        for i in range(1,9+1):
            ThreeThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 5 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,2+1):
            ThreeThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 6 - Flower #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,4+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - Flower #" + str(i)]), KRtDLLocation) 
             

        for i in range(1,3+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 8 - Flower #" + str(i)]), KRtDLLocation) 



        for i in range(1,5+1):
            FourOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,11+1):
            FourOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 4 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 5 - Flower #" + str(i)]), KRtDLLocation)


        for i in range(1,5+1):
            FourTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 1 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FourTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 4 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 7 - Flower #" + str(i)]), KRtDLLocation)


        for i in range(1,3+1):
            FourThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 4 - Flower #" + str(i)]), KRtDLLocation)


        for i in range(1,3+1):
            FourFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 3 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            FourFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 4 - Flower #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            FourFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 1 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 4 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFiveRooms[9].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 10 - Flower #" + str(i)]), KRtDLLocation)



        for i in range(1,5+1):
            FiveOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 8 - Flower #" + str(i)]), KRtDLLocation)
        

        for i in range(1,8+1):
            FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - Flower #" + str(i)]), KRtDLLocation)
    


        for i in range(1,2+1):
            SixOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation)
        
        SixOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 4 - Flower"]), KRtDLLocation)

        for i in range(1,5+1):
            SixOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 6 - Flower #" + str(i)]), KRtDLLocation)

        
        for i in range(1,2+1):
            SixThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 3 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 4 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 6 - Flower #" + str(i)]), KRtDLLocation)
        

        for i in range(1,5+1):
            SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - Flower #" + str(i)]), KRtDLLocation)


        for i in range(1,9+1):
            SevenOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 1 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 3 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,5+1):
            SevenOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 5 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 7 - Flower #" + str(i)]), KRtDLLocation)


        SevenTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 10 - Flower"]), KRtDLLocation)


        for i in range(1,4+1):
            SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 3 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 9 - Flower #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - Flower #" + str(i)]), KRtDLLocation)




    
    if world.options.one_up_sanity:
        OneOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 2 - 1-up"]), KRtDLLocation)
         

        OneThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room 3 - 1-up"]), KRtDLLocation)
         

        OneFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 6 - 1-up"]), KRtDLLocation)
         


        TwoOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 2 - 1-up"]), KRtDLLocation)
         

        TwoTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 5 - 1-up"]), KRtDLLocation)
         

        TwoThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 2 - 1-up"]), KRtDLLocation)
         
        TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - 1-up"]), KRtDLLocation)
         

        TwoFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 5 - 1-up"]), KRtDLLocation)
         


        ThreeOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 1 - 1-up"]), KRtDLLocation)
         
        ThreeOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 7 - 1-up"]), KRtDLLocation)
         
        ThreeOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 8 - 1-up"]), KRtDLLocation)
         

        ThreeTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 5 - 1-up"]), KRtDLLocation)
         

        ThreeThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 3 - 1-up"]), KRtDLLocation)
         

        ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - 1-up"]), KRtDLLocation)



        FourOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 2 - 1-up"]), KRtDLLocation)

        FourOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 5 - 1-up"]), KRtDLLocation)


        FourTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 1 - 1-up"]), KRtDLLocation)


        FourThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 1 - 1-up"]), KRtDLLocation)


        FourFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 6 - 1-up"]), KRtDLLocation)  


        FourFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 4 - 1-up"]), KRtDLLocation)
    


        FiveOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 3 - 1-up"]), KRtDLLocation)


        FiveThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 1 - 1-up"]), KRtDLLocation)


        FiveFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 1 - 1-up"]), KRtDLLocation)

        FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - 1-up"]), KRtDLLocation)


        for i in range(1,4+1):
            FiveFiveRooms[25].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 26 - 1-up #" + str(i)]), KRtDLLocation)


        SixOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 2 - 1-up"]), KRtDLLocation)

        SixOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 5 - 1-up"]), KRtDLLocation)

        SixOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 8 - 1-up"]), KRtDLLocation)


        SixTwoRooms[11].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 12 - 1-up"]), KRtDLLocation)


        SixFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 1 - 1-up"]), KRtDLLocation)

        for i in range(1,2+1):
            SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - 1-up #" + str(i)]), KRtDLLocation)

        SixFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 8 - 1-up"]), KRtDLLocation)


        SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - 1-up"]), KRtDLLocation)

        SevenOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 5 - 1-up"]), KRtDLLocation)

        SevenOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 6 - 1-up"]), KRtDLLocation)


        SevenTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 5 - 1-up"]), KRtDLLocation)

        SevenTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 7 - 1-up"]), KRtDLLocation)

        SevenTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 8 - 1-up"]), KRtDLLocation)


        SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - 1-up"]), KRtDLLocation)

        SevenThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 5 - 1-up"]), KRtDLLocation)

        SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - 1-up"]), KRtDLLocation)
        

            
        
   
    if world.options.food_sanity:
        OneOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 1 - Food"]), KRtDLLocation)
         
        for i in range(1,4+1):
            OneOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 2 - Food #" + str(i)]), KRtDLLocation) 
             
        for i in range(1,5+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 3 - Food #" + str(i)]), KRtDLLocation) 
             
        OneOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 5 - Food"]), KRtDLLocation)
         

        OneTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 1 - Food"]), KRtDLLocation)
         
        for i in range(1,2+1):
            OneTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation) 
             
        OneTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 4 - Food"]), KRtDLLocation)
         
        for i in range(1,2+1):
            OneTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)
             

        for i in range(1,5+1):
            OneThreeRooms[i-1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 3 Room " + str(i) + " - Food"]), KRtDLLocation)
             

        for i in range(1,3+1):
            OneFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,5+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)
             
        OneFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 7 - Food"]), KRtDLLocation)
         


        for i in range(1,2+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)
             
        TwoOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 3 - Food"]), KRtDLLocation)
         
        TwoOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 5 - Food"]), KRtDLLocation)
         
        for i in range(1,2+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 7 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 1 Room 8 - Food #" + str(i)]), KRtDLLocation)
             

        for i in range(1,2+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)
             
        TwoTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 2 - Food"]), KRtDLLocation)
         
        TwoTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 4 - Food"]), KRtDLLocation)
         
        TwoTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 8 - Food"]), KRtDLLocation)
         
        TwoTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 9 - Food"]), KRtDLLocation)
         

        TwoThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 1 - Food"]), KRtDLLocation)
         
        TwoThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 2 - Food"]), KRtDLLocation)
         
        for i in range(1,3+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 3 - Food #" + str(i)]), KRtDLLocation)
             
        TwoThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 4 - Food"]), KRtDLLocation)
         
        TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - Food"]), KRtDLLocation)
         
        TwoThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 6 - Food"]), KRtDLLocation)
         

        for i in range(1,2+1):
            TwoFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,4+1):
            TwoFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            TwoFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,4+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 8 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 9 - Food #" + str(i)]), KRtDLLocation)
             
        TwoFourRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 10 - Food"]), KRtDLLocation)
         


        for i in range(1,3+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 2 - Food"]), KRtDLLocation)
         
        ThreeOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 3 - Food"]), KRtDLLocation)
         
        ThreeOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 4 - Food"]), KRtDLLocation)
         
        for i in range(1,3+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 6 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 7 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 8 - Food"]), KRtDLLocation)
         
        ThreeOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 9 - Food"]), KRtDLLocation)
         

        for i in range(1,2+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 3 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 5 - Food"]), KRtDLLocation)
         
        for i in range(1,4+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)
             

        for i in range(1,2+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 1 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 2 - Food"]), KRtDLLocation)
         
        for i in range(1,2+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 4 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 5 - Food"]), KRtDLLocation)
         
        ThreeThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 6 - Food"]), KRtDLLocation)
         
        for i in range(1,4+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,9+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 8 - Food #" + str(i)]), KRtDLLocation)
             
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 10 - Food"]), KRtDLLocation)
         

        for i in range(1,2+1):
            ThreeFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 2 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,2+1):
            ThreeFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 3 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            ThreeFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,4+1):
            ThreeFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,3+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - Food #" + str(i)]), KRtDLLocation)
             
        for i in range(1,5+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 8 - Food #" + str(i)]), KRtDLLocation)



        for i in range(1,2+1):
            FourOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            FourOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 3 - Food #" + str(i)]), KRtDLLocation)
            
        for i in range(1,4+1):
            FourOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 4 - Food #" + str(i)]), KRtDLLocation)
            
        for i in range(1,2+1):
            FourOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 1 Room 5 - Food #" + str(i)]), KRtDLLocation)


        for i in range(1,4+1):
            FourTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,10+1):
            FourTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 7 - Food #" + str(i)]), KRtDLLocation)

        FourTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 9 - Food"]), KRtDLLocation)


        FourThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 1 - Food"]), KRtDLLocation)
        
        for i in range(1,2+1):
            FourThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 3 - Food #" + str(i)]), KRtDLLocation)

        FourThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 4 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            FourThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 6 - Food #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            FourFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FourFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FourFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)

        FourFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 7 - Food"]), KRtDLLocation)


        for i in range(1,2+1):
            FourFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FourFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 5 - Food #" + str(i)]), KRtDLLocation)

        FourFiveRooms[7].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 8 - Food"]), KRtDLLocation)

        FourFiveRooms[9].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 5 Room 10 - Food"]), KRtDLLocation)


        
        FiveOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 2 - Food"]), KRtDLLocation)

        for i in range(1,3+1):
            FiveOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FiveOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 6 - Food #" + str(i)]), KRtDLLocation)
        
        FiveOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 9 - Food"]), KRtDLLocation)


        FiveTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 1 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            FiveTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 2 - Food #" + str(i)]), KRtDLLocation)

        FiveTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 4 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            FiveTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)
        
        FiveTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 8 - Food"]), KRtDLLocation)


        for i in range(1,2+1):
            FiveThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            FiveThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FiveThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            FiveThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 7 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            FiveThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 3 Room 8 - Food #" + str(i)]), KRtDLLocation)


        for i in range(1,3+1):
            FiveFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 2 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)

        FiveFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 7 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            FiveFourRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 8 - Food #" + str(i)]), KRtDLLocation)


        FiveFiveRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 4 - Food"]), KRtDLLocation)

        FiveFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 7 - Food"]), KRtDLLocation)

        FiveFiveRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 10 - Food"]), KRtDLLocation)

        FiveFiveRooms[15].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 16 - Food"]), KRtDLLocation)

        FiveFiveRooms[19].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 20 - Food"]), KRtDLLocation)

        FiveFiveRooms[22].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 23 - Food"]), KRtDLLocation)



        for i in range(1,3+1):
            SixOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixOneRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 6 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            SixOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 9 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixOneRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 10 - Food #" + str(i)]), KRtDLLocation)
            
        SixOneRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 11 - Food"]), KRtDLLocation)
        
        
        SixTwoRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 3 - Food"]), KRtDLLocation)

        SixTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 5 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SixTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 6 - Food #" + str(i)]), KRtDLLocation)

        SixTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 8 - Food"]), KRtDLLocation)

        SixTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 10 - Food"]), KRtDLLocation)

        SixTwoRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 11 - Food"]), KRtDLLocation)


        SixThreeRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 1 - Food"]), KRtDLLocation)

        SixThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 2 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SixThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            SixThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            SixThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 7 - Food #" + str(i)]), KRtDLLocation)

        SixThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 8 - Food"]), KRtDLLocation)


        SixFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 2 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SixFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SixFourRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            SixFourRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 4 Room 6 - Food #" + str(i)]), KRtDLLocation)


        for i in range(1,2+1):
            SixFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 1 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixFiveRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - Food #" + str(i)]), KRtDLLocation)

        SixFiveRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 6 - Food"]), KRtDLLocation)

        SixFiveRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 7 - Food"]), KRtDLLocation)


        for i in range(1,2+1):
            SevenOneRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 1 - Food #" + str(i)]), KRtDLLocation)
        
        SevenOneRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 3 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SevenOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 5 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            SevenOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 7 - Food #" + str(i)]), KRtDLLocation)

        SevenOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 8 - Food"]), KRtDLLocation)

        SevenOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 9 - Food"]), KRtDLLocation)


        for i in range(1,2+1):
            SevenTwoRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 1 - Food #" + str(i)]), KRtDLLocation)
        
        SevenTwoRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 2 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SevenTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 4 - Food #" + str(i)]), KRtDLLocation)

        SevenTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 5 - Food"]), KRtDLLocation)

        SevenTwoRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 6 - Food"]), KRtDLLocation)

        for i in range(1,14+1):
            SevenTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 7 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 8 - Food #" + str(i)]), KRtDLLocation)

        SevenTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 9 - Food"]), KRtDLLocation)


        SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 3 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 4 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 5 - Food #" + str(i)]), KRtDLLocation)

        SevenThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 6 - Food"]), KRtDLLocation)

        for i in range(1,2+1):
            SevenThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 8 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,7+1):
            SevenThreeRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 9 - Food #" + str(i)]), KRtDLLocation)

        for i in range(1,3+1):
            SevenThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 10 - Food #" + str(i)]), KRtDLLocation)

        SevenThreeRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 11 - Food"]), KRtDLLocation)

        for i in range(1,4+1):
            SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - Food #" + str(i)]), KRtDLLocation)
        
        
        for i in range(1,7+1):
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 2 - Food #" + str(i)]), KRtDLLocation)
        
            
    

   
    if world.options.maxim_sanity:
        OneOneRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 1 Room 5 - M-Tomato"]), KRtDLLocation)
         

        OneTwoRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 2 Room 4 - M-Tomato"]), KRtDLLocation)
         

        OneFourRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 2 - M-Tomato"]), KRtDLLocation)
         
        OneFourRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 3 - M-Tomato"]), KRtDLLocation)
         
        OneFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)
         

        OneFiveRegion.add_locations(get_location_names_with_ids([EXStatus + "Cookie Country Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)
         


        TwoTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 8 - M-Tomato"]), KRtDLLocation)
         
        TwoTwoRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 2 Room 10 - M-Tomato"]), KRtDLLocation)
         

        TwoThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 3 Room 5 - M-Tomato"]), KRtDLLocation)
         

        TwoFourRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 4 Room 10 - M-Tomato"]), KRtDLLocation)
         

        TwoFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Raisin Ruins Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)
         


        ThreeOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 1 Room 9 - M-Tomato"]), KRtDLLocation)
         
        
        ThreeThreeRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 5 - M-Tomato"]), KRtDLLocation)
         
        ThreeThreeRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 7 - M-Tomato"]), KRtDLLocation)
         
        ThreeThreeRooms[9].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 3 Room 10 - M-Tomato"]), KRtDLLocation)
         

        ThreeFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)
         
        
        ThreeFiveRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Onion Ocean Stage 5 Room 1 - M-Tomato"]), KRtDLLocation)



        FourTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 2 Room 9 - M-Tomato"]), KRtDLLocation)


        FourThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 3 - M-Tomato"]), KRtDLLocation)

        FourThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 3 Room 6 - M-Tomato"]), KRtDLLocation)


        FourFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)


        FourSixRooms[0].add_locations(get_location_names_with_ids([EXStatus + "White Wafers Stage 6 Room 1 - M-Tomato"]), KRtDLLocation)



        FiveOneRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 1 Room 8 - M-Tomato"]), KRtDLLocation)


        FiveTwoRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 2 Room 8 - M-Tomato"]), KRtDLLocation)


        FiveFourRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 4 - M-Tomato"]), KRtDLLocation)

        FiveFourRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 4 Room 7 - M-Tomato"]), KRtDLLocation)


        FiveFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 2 - M-Tomato"]), KRtDLLocation)

        FiveFiveRooms[13].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 14 - M-Tomato"]), KRtDLLocation)

        FiveFiveRooms[26].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 27 - M-Tomato"]), KRtDLLocation)

        FiveFiveRooms[27].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 5 Room 28 - M-Tomato"]), KRtDLLocation)


        FiveSixRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Nutty Noon Stage 6 Room 1 - M-Tomato"]), KRtDLLocation)

    

        SixOneRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 7 - M-Tomato"]), KRtDLLocation)
        
        SixOneRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 1 Room 11 - M-Tomato"]), KRtDLLocation)


        SixTwoRooms[6].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 7 - M-Tomato"]), KRtDLLocation)
        
        SixTwoRooms[11].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 2 Room 12 - M-Tomato"]), KRtDLLocation)


        SixThreeRooms[2].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 3 - M-Tomato"]), KRtDLLocation)
        
        SixThreeRooms[5].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 6 - M-Tomato"]), KRtDLLocation)

        SixThreeRooms[7].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 3 Room 8 - M-Tomato"]), KRtDLLocation)


        SixFiveRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 2 - M-Tomato"]), KRtDLLocation)
        
        SixFiveRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 5 Room 5 - M-Tomato"]), KRtDLLocation)


        SixSixRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Egg Engines Stage 6 Room 1 - M-Tomato"]), KRtDLLocation)


        SevenOneRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 2 - M-Tomato"]), KRtDLLocation)

        SevenOneRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 4 - M-Tomato"]), KRtDLLocation)

        SevenOneRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 1 Room 9 - M-Tomato"]), KRtDLLocation)


        SevenTwoRooms[4].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 5 - M-Tomato"]), KRtDLLocation)

        SevenTwoRooms[8].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 2 Room 9 - M-Tomato"]), KRtDLLocation)

        
        SevenThreeRooms[1].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 2 - M-Tomato"]), KRtDLLocation)

        SevenThreeRooms[3].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 4 - M-Tomato"]), KRtDLLocation)

        SevenThreeRooms[10].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 11 - M-Tomato"]), KRtDLLocation)

        SevenThreeRooms[12].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 3 Room 13 - M-Tomato"]), KRtDLLocation)


        SevenFourRooms[0].add_locations(get_location_names_with_ids([EXStatus + "Dangerous Dinner Stage 4 Room 1 - M-Tomato"]), KRtDLLocation)


    
    #if world.options.shuffle_challenges != 0:



    #if world.options.shuffle_challenges == 2:
        

def CreateTheRegionConnectionsAndExtraRegions(world: "KRtDLWorld", EXStatus: str) -> None:
    MenuRegion = world.get_region("Menu")
    PopstarMapRegion = world.get_region(EXStatus + "Popstar Map")
    HalcandraMapRegion = world.get_region(EXStatus + "Halcandra Map")
    LorStarcutterRegion = world.get_region(EXStatus + "Lor Starcutter")
    
    CookieCountryHub = world.get_region(EXStatus + "Cookie Country Hub")
    RaisinRuinsHub = world.get_region(EXStatus + "Raisin Ruins Hub")
    OnionOceanHub = world.get_region(EXStatus + "Onion Ocean Hub")
    WhiteWafersHub = world.get_region(EXStatus + "White Wafers Hub")
    NuttyNoonHub = world.get_region(EXStatus + "Nutty Noon Hub")
    EggEnginesHub = world.get_region(EXStatus + "Egg Engines Hub")
    DangerousDinnerHub = world.get_region(EXStatus + "Dangerous Dinner Hub")
    AnotherDimension = world.get_region(EXStatus + "Another Dimension")
    
    MenuRegion.connect(PopstarMapRegion, "Menu To " + EXStatus + "Popstar Map")
    MenuRegion.connect(HalcandraMapRegion, "Menu To " + EXStatus + "Halcandra Map")
    
    PopstarMapRegion.connect(HalcandraMapRegion, "Popstar Map To " + EXStatus + "Halcandra Map")
    PopstarMapRegion.connect(LorStarcutterRegion, "Popstar Map To Lor Starcutter")
    HalcandraMapRegion.connect(PopstarMapRegion, "Halcandra Map To " + EXStatus + "Popstar Map")
    HalcandraMapRegion.connect(LorStarcutterRegion, "Halcandra Map To Lor Starcutter")
    
    PopstarMapRegion.connect(CookieCountryHub, "Popstar Map To " + EXStatus + "Cookie Country Hub")
    PopstarMapRegion.connect(RaisinRuinsHub, "Popstar Map To " + EXStatus + "Raisin Ruins Hub")
    PopstarMapRegion.connect(OnionOceanHub, "Popstar Map To " + EXStatus + "Onion Ocean Hub")
    PopstarMapRegion.connect(WhiteWafersHub, "Popstar Map To " + EXStatus + "White Wafers Hub")
    PopstarMapRegion.connect(NuttyNoonHub, "Popstar Map To " + EXStatus + "Nutty Noon Hub")

    HalcandraMapRegion.connect(EggEnginesHub, "Halcandra Map To " + EXStatus + "Egg Engines Hub")
    HalcandraMapRegion.connect(DangerousDinnerHub, "Halcandra Map To " + EXStatus + "Dangerous Dinner Hub")
    
    OneOneRooms = [world.get_region(EXStatus + "Cookie Country Stage 1 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 1 Room 4"),
                  world.get_region(EXStatus + "Cookie Country Stage 1 Room 5")]

    CookieCountryHub.connect(OneOneRooms[0], EXStatus + "Cookie Country Hub To " + EXStatus + "Cookie Country Stage 1 Room 1")
    OneOneRooms[0].connect(OneOneRooms[1], EXStatus + "Cookie Country Stage 1 Room 1-2")
    OneOneRooms[1].connect(OneOneRooms[2], EXStatus + "Cookie Country Stage 1 Room 2-3")
    OneOneRooms[2].connect(OneOneRooms[3], EXStatus + "Cookie Country Stage 1 Room 3-4")
    OneOneRooms[3].connect(OneOneRooms[4], EXStatus + "Cookie Country Stage 1 Room 4-5")

    OneTwoRooms = [world.get_region(EXStatus + "Cookie Country Stage 2 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 4"),
                   world.get_region(EXStatus + "Cookie Country Stage 2 Room 5"),
                  world.get_region(EXStatus + "Cookie Country Stage 2 Room 6")]

    CookieCountryHub.connect(OneTwoRooms[0], EXStatus + "Cookie Country Hub To " + EXStatus + "Cookie Country Stage 2 Room 1")
    OneTwoRooms[0].connect(OneTwoRooms[1], EXStatus + "Cookie Country Stage 2 Room 1-2")
    OneTwoRooms[1].connect(OneTwoRooms[2], EXStatus + "Cookie Country Stage 2 Room 2-3")
    OneTwoRooms[2].connect(OneTwoRooms[3], EXStatus + "Cookie Country Stage 2 Room 3-4")
    OneTwoRooms[3].connect(OneTwoRooms[4], EXStatus + "Cookie Country Stage 2 Room 4-5")
    OneTwoRooms[3].connect(OneTwoRooms[5], EXStatus + "Cookie Country Stage 2 Room 4-6")
    
    OneThreeRooms = [world.get_region(EXStatus + "Cookie Country Stage 3 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 3 Room 4"),
                  world.get_region(EXStatus + "Cookie Country Stage 3 Room 5")]

    CookieCountryHub.connect(OneThreeRooms[0], EXStatus + "Cookie Country Hub To " + EXStatus + "Cookie Country Stage 3 Room 1")
    OneThreeRooms[0].connect(OneThreeRooms[1], EXStatus + "Cookie Country Stage 3 Room 1-2")
    OneThreeRooms[1].connect(OneThreeRooms[2], EXStatus + "Cookie Country Stage 3 Room 2-3")
    OneThreeRooms[2].connect(OneThreeRooms[3], EXStatus + "Cookie Country Stage 3 Room 3-4")
    OneThreeRooms[3].connect(OneThreeRooms[4], EXStatus + "Cookie Country Stage 3 Room 4-5")
    
    OneFourRooms = [world.get_region(EXStatus + "Cookie Country Stage 4 Room 1"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 2"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 3"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 4"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 5"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 6"),
                   world.get_region(EXStatus + "Cookie Country Stage 4 Room 7")]

    CookieCountryHub.connect(OneFourRooms[0], EXStatus + "Cookie Country Hub To " + EXStatus + "Cookie Country Stage 4 Room 1")
    OneFourRooms[0].connect(OneFourRooms[1], EXStatus + "Cookie Country Stage 4 Room 1-2")
    OneFourRooms[0].connect(OneFourRooms[2], EXStatus + "Cookie Country Stage 4 Room 1-3")
    OneFourRooms[1].connect(OneFourRooms[2], EXStatus + "Cookie Country Stage 4 Room 2-3")
    OneFourRooms[2].connect(OneFourRooms[3], EXStatus + "Cookie Country Stage 4 Room 3-4")
    OneFourRooms[3].connect(OneFourRooms[4], EXStatus + "Cookie Country Stage 4 Room 4-5")
    OneFourRooms[4].connect(OneFourRooms[5], EXStatus + "Cookie Country Stage 4 Room 5-6")
    OneFourRooms[5].connect(OneFourRooms[6], EXStatus + "Cookie Country Stage 4 Room 6-7")
    
    OneFiveRegion = world.get_region(EXStatus + "Cookie Country Stage 5 Room 1")

    CookieCountryHub.connect(OneFiveRegion, "Cookie Country Hub To " + EXStatus + "Cookie Country Stage 5")

    
    TwoOneRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 7"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 1 Room 8")]

    RaisinRuinsHub.connect(TwoOneRooms[0], EXStatus + "Raisin Ruins Hub To " + EXStatus + "Raisin Ruins Stage 1 Room 1")
    TwoOneRooms[0].connect(TwoOneRooms[1], EXStatus + "Raisin Ruins Stage 1 Room 1-2")
    TwoOneRooms[0].connect(TwoOneRooms[2], EXStatus + "Raisin Ruins Stage 1 Room 1-3")
    TwoOneRooms[2].connect(TwoOneRooms[3], EXStatus + "Raisin Ruins Stage 1 Room 3-4")
    TwoOneRooms[2].connect(TwoOneRooms[4], EXStatus + "Raisin Ruins Stage 1 Room 3-5")
    TwoOneRooms[4].connect(TwoOneRooms[5], EXStatus + "Raisin Ruins Stage 1 Room 5-6")
    TwoOneRooms[5].connect(TwoOneRooms[6], EXStatus + "Raisin Ruins Stage 1 Room 6-7")
    TwoOneRooms[6].connect(TwoOneRooms[7], EXStatus + "Raisin Ruins Stage 1 Room 7-8")
    
    TwoTwoRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 7"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 8"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 9"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 2 Room 10")]

    RaisinRuinsHub.connect(TwoTwoRooms[0], EXStatus + "Raisin Ruins Hub To " + EXStatus + "Raisin Ruins Stage 2 Room 1")
    TwoTwoRooms[0].connect(TwoTwoRooms[1], EXStatus + "Raisin Ruins Stage 2 Room 1-2")
    TwoTwoRooms[1].connect(TwoTwoRooms[2], EXStatus + "Raisin Ruins Stage 2 Room 2-3")
    TwoTwoRooms[1].connect(TwoTwoRooms[3], EXStatus + "Raisin Ruins Stage 2 Room 2-4")
    TwoTwoRooms[3].connect(TwoTwoRooms[4], EXStatus + "Raisin Ruins Stage 2 Room 4-5")
    TwoTwoRooms[3].connect(TwoTwoRooms[5], EXStatus + "Raisin Ruins Stage 2 Room 4-6")
    TwoTwoRooms[3].connect(TwoTwoRooms[6], EXStatus + "Raisin Ruins Stage 2 Room 4-7")
    TwoTwoRooms[6].connect(TwoTwoRooms[7], EXStatus + "Raisin Ruins Stage 2 Room 7-8")
    TwoTwoRooms[7].connect(TwoTwoRooms[8], EXStatus + "Raisin Ruins Stage 2 Room 8-9")
    TwoTwoRooms[8].connect(TwoTwoRooms[9], EXStatus + "Raisin Ruins Stage 2 Room 9-10")

    TwoThreeRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 3 Room 6")]

    RaisinRuinsHub.connect(TwoThreeRooms[0], EXStatus + "Raisin Ruins Hub To " + EXStatus + "Raisin Ruins Stage 3 Room 1")
    TwoThreeRooms[0].connect(TwoThreeRooms[1], EXStatus + "Raisin Ruins Stage 3 Room 1-2")
    TwoThreeRooms[1].connect(TwoThreeRooms[2], EXStatus + "Raisin Ruins Stage 3 Room 2-3")
    TwoThreeRooms[2].connect(TwoThreeRooms[3], EXStatus + "Raisin Ruins Stage 3 Room 3-4")
    TwoThreeRooms[3].connect(TwoThreeRooms[4], EXStatus + "Raisin Ruins Stage 3 Room 4-5")
    TwoThreeRooms[4].connect(TwoThreeRooms[5], EXStatus + "Raisin Ruins Stage 3 Room 5-6")
    
    TwoFourRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 2"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 3"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 4"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 5"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 6"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 7"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 8"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 9"),
                  world.get_region(EXStatus + "Raisin Ruins Stage 4 Room 10")]

    RaisinRuinsHub.connect(TwoFourRooms[0], EXStatus + "Raisin Ruins Hub To " + EXStatus + "Raisin Ruins Stage 4 Room 1")
    TwoFourRooms[0].connect(TwoFourRooms[1], EXStatus + "Raisin Ruins Stage 4 Room 1-2")
    TwoFourRooms[1].connect(TwoFourRooms[2], EXStatus + "Raisin Ruins Stage 4 Room 2-3")
    TwoFourRooms[1].connect(TwoFourRooms[3], EXStatus + "Raisin Ruins Stage 4 Room 2-4")
    TwoFourRooms[3].connect(TwoFourRooms[4], EXStatus + "Raisin Ruins Stage 4 Room 4-5")
    TwoFourRooms[4].connect(TwoFourRooms[5], EXStatus + "Raisin Ruins Stage 4 Room 5-6")
    TwoFourRooms[5].connect(TwoFourRooms[6], EXStatus + "Raisin Ruins Stage 4 Room 6-7")
    TwoFourRooms[5].connect(TwoFourRooms[7], EXStatus + "Raisin Ruins Stage 4 Room 6-8")
    TwoFourRooms[7].connect(TwoFourRooms[8], EXStatus + "Raisin Ruins Stage 4 Room 8-9")
    TwoFourRooms[8].connect(TwoFourRooms[9], EXStatus + "Raisin Ruins Stage 4 Room 9-10")
    
    TwoFiveRooms = [world.get_region(EXStatus + "Raisin Ruins Stage 5 Room 1"),
                   world.get_region(EXStatus + "Raisin Ruins Stage 5 Room 2")]

    RaisinRuinsHub.connect(TwoFiveRooms[0], EXStatus + "Raisin Ruins Hub To " + EXStatus + "Raisin Ruins Stage 5 Room 1")
    TwoFiveRooms[0].connect(TwoFiveRooms[1], EXStatus + "Raisin Ruins Stage 5 Room 1-2")

    
    ThreeOneRooms = [world.get_region(EXStatus + "Onion Ocean Stage 1 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 8"),
                   world.get_region(EXStatus + "Onion Ocean Stage 1 Room 9")]

    OnionOceanHub.connect(ThreeOneRooms[0], EXStatus + "Onion Ocean Hub To " + EXStatus + "Onion Ocean Stage 1 Room 1")
    ThreeOneRooms[0].connect(ThreeOneRooms[1], EXStatus + "Onion Ocean Stage 1 Room 1-2")
    ThreeOneRooms[1].connect(ThreeOneRooms[2], EXStatus + "Onion Ocean Stage 1 Room 2-3")
    ThreeOneRooms[2].connect(ThreeOneRooms[3], EXStatus + "Onion Ocean Stage 1 Room 3-4")
    ThreeOneRooms[3].connect(ThreeOneRooms[4], EXStatus + "Onion Ocean Stage 1 Room 4-5")
    ThreeOneRooms[3].connect(ThreeOneRooms[5], EXStatus + "Onion Ocean Stage 1 Room 4-6")
    ThreeOneRooms[5].connect(ThreeOneRooms[6], EXStatus + "Onion Ocean Stage 1 Room 6-7")
    ThreeOneRooms[6].connect(ThreeOneRooms[7], EXStatus + "Onion Ocean Stage 1 Room 7-8")
    ThreeOneRooms[7].connect(ThreeOneRooms[8], EXStatus + "Onion Ocean Stage 1 Room 8-9")
    
    ThreeTwoRooms = [world.get_region(EXStatus + "Onion Ocean Stage 2 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 2 Room 6")]

    OnionOceanHub.connect(ThreeTwoRooms[0], EXStatus + "Onion Ocean Hub To " + EXStatus + "Onion Ocean Stage 2 Room 1")
    ThreeTwoRooms[0].connect(ThreeTwoRooms[1], EXStatus + "Onion Ocean Stage 2 Room 1-2")
    ThreeTwoRooms[1].connect(ThreeTwoRooms[2], EXStatus + "Onion Ocean Stage 2 Room 2-3")
    ThreeTwoRooms[2].connect(ThreeTwoRooms[3], EXStatus + "Onion Ocean Stage 2 Room 3-4")
    ThreeTwoRooms[2].connect(ThreeTwoRooms[4], EXStatus + "Onion Ocean Stage 2 Room 3-5")
    ThreeTwoRooms[4].connect(ThreeTwoRooms[5], EXStatus + "Onion Ocean Stage 2 Room 5-6")

    ThreeThreeRooms = [world.get_region(EXStatus + "Onion Ocean Stage 3 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 8"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 9"),
                   world.get_region(EXStatus + "Onion Ocean Stage 3 Room 10")]

    OnionOceanHub.connect(ThreeThreeRooms[0], EXStatus + "Onion Ocean Hub To " + EXStatus + "Onion Ocean Stage 3 Room 1")
    ThreeThreeRooms[0].connect(ThreeThreeRooms[1], EXStatus + "Onion Ocean Stage 3 Room 1-2")
    ThreeThreeRooms[1].connect(ThreeThreeRooms[2], EXStatus + "Onion Ocean Stage 3 Room 2-3")
    ThreeThreeRooms[1].connect(ThreeThreeRooms[3], EXStatus + "Onion Ocean Stage 3 Room 2-4")
    ThreeThreeRooms[3].connect(ThreeThreeRooms[4], EXStatus + "Onion Ocean Stage 3 Room 4-5")
    ThreeThreeRooms[4].connect(ThreeThreeRooms[5], EXStatus + "Onion Ocean Stage 3 Room 5-6")
    ThreeThreeRooms[5].connect(ThreeThreeRooms[6], EXStatus + "Onion Ocean Stage 3 Room 6-7")
    ThreeThreeRooms[6].connect(ThreeThreeRooms[7], EXStatus + "Onion Ocean Stage 3 Room 7-8")
    ThreeThreeRooms[7].connect(ThreeThreeRooms[8], EXStatus + "Onion Ocean Stage 3 Room 8-9")
    ThreeThreeRooms[8].connect(ThreeThreeRooms[9], EXStatus + "Onion Ocean Stage 3 Room 9-10")
    
    ThreeFourRooms = [world.get_region(EXStatus + "Onion Ocean Stage 4 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 2"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 3"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 4"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 5"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 6"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 7"),
                   world.get_region(EXStatus + "Onion Ocean Stage 4 Room 8")]

    OnionOceanHub.connect(ThreeFourRooms[0], EXStatus + "Onion Ocean Hub To " + EXStatus + "Onion Ocean Stage 4 Room 1")
    ThreeFourRooms[0].connect(ThreeFourRooms[1], EXStatus + "Onion Ocean Stage 4 Room 1-2")
    ThreeFourRooms[1].connect(ThreeFourRooms[2], EXStatus + "Onion Ocean Stage 4 Room 2-3")
    ThreeFourRooms[1].connect(ThreeFourRooms[3], EXStatus + "Onion Ocean Stage 4 Room 2-4")
    ThreeFourRooms[3].connect(ThreeFourRooms[4], EXStatus + "Onion Ocean Stage 4 Room 4-5")
    ThreeFourRooms[3].connect(ThreeFourRooms[5], EXStatus + "Onion Ocean Stage 4 Room 4-6")
    ThreeFourRooms[5].connect(ThreeFourRooms[6], EXStatus + "Onion Ocean Stage 4 Room 6-7")
    ThreeFourRooms[6].connect(ThreeFourRooms[7], EXStatus + "Onion Ocean Stage 4 Room 7-8")

    ThreeFiveRooms = [world.get_region(EXStatus + "Onion Ocean Stage 5 Room 1"),
                   world.get_region(EXStatus + "Onion Ocean Stage 5 Room 2")]

    OnionOceanHub.connect(ThreeFiveRooms[0], EXStatus + "Onion Ocean Hub To " + EXStatus + "Onion Ocean Stage 5 Room 1")
    ThreeFiveRooms[0].connect(ThreeFiveRooms[1], EXStatus + "Onion Ocean Stage 5 Room 1-2")


    FourOneRooms = [world.get_region(EXStatus + "White Wafers Stage 1 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 1 Room 5")]

    WhiteWafersHub.connect(FourOneRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 1 Room 1")
    FourOneRooms[0].connect(FourOneRooms[1], EXStatus + "White Wafers Stage 1 Room 1-2")
    FourOneRooms[1].connect(FourOneRooms[2], EXStatus + "White Wafers Stage 1 Room 2-3")
    FourOneRooms[2].connect(FourOneRooms[3], EXStatus + "White Wafers Stage 1 Room 3-4")
    FourOneRooms[3].connect(FourOneRooms[4], EXStatus + "White Wafers Stage 1 Room 4-5")

    FourTwoRooms = [world.get_region(EXStatus + "White Wafers Stage 2 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 7"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 8"),
                   world.get_region(EXStatus + "White Wafers Stage 2 Room 9")]

    WhiteWafersHub.connect(FourTwoRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 2 Room 1")
    FourTwoRooms[0].connect(FourTwoRooms[1], EXStatus + "White Wafers Stage 2 Room 1-2")
    FourTwoRooms[1].connect(FourTwoRooms[2], EXStatus + "White Wafers Stage 2 Room 2-3")
    FourTwoRooms[1].connect(FourTwoRooms[3], EXStatus + "White Wafers Stage 2 Room 2-4")
    FourTwoRooms[3].connect(FourTwoRooms[4], EXStatus + "White Wafers Stage 2 Room 4-5")
    FourTwoRooms[3].connect(FourTwoRooms[5], EXStatus + "White Wafers Stage 2 Room 4-6")
    FourTwoRooms[5].connect(FourTwoRooms[6], EXStatus + "White Wafers Stage 2 Room 6-7")
    FourTwoRooms[6].connect(FourTwoRooms[7], EXStatus + "White Wafers Stage 2 Room 7-8")
    FourTwoRooms[7].connect(FourTwoRooms[8], EXStatus + "White Wafers Stage 2 Room 8-9")

    FourThreeRooms = [world.get_region(EXStatus + "White Wafers Stage 3 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 3 Room 6")]

    WhiteWafersHub.connect(FourThreeRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 3 Room 1")
    FourThreeRooms[0].connect(FourThreeRooms[1], EXStatus + "White Wafers Stage 3 Room 1-2")
    FourThreeRooms[1].connect(FourThreeRooms[2], EXStatus + "White Wafers Stage 3 Room 2-3")
    FourThreeRooms[2].connect(FourThreeRooms[3], EXStatus + "White Wafers Stage 3 Room 3-4")
    FourThreeRooms[3].connect(FourThreeRooms[4], EXStatus + "White Wafers Stage 3 Room 4-5")
    FourThreeRooms[3].connect(FourThreeRooms[5], EXStatus + "White Wafers Stage 3 Room 4-6")

    FourFourRooms = [world.get_region(EXStatus + "White Wafers Stage 4 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 4 Room 7")]

    WhiteWafersHub.connect(FourFourRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 4 Room 1")
    FourFourRooms[0].connect(FourFourRooms[1], EXStatus + "White Wafers Stage 4 Room 1-2")
    FourFourRooms[1].connect(FourFourRooms[2], EXStatus + "White Wafers Stage 4 Room 2-3")
    FourFourRooms[2].connect(FourFourRooms[3], EXStatus + "White Wafers Stage 4 Room 3-4")
    FourFourRooms[3].connect(FourFourRooms[4], EXStatus + "White Wafers Stage 4 Room 4-5")
    FourFourRooms[4].connect(FourFourRooms[5], EXStatus + "White Wafers Stage 4 Room 5-6")
    FourFourRooms[5].connect(FourFourRooms[6], EXStatus + "White Wafers Stage 4 Room 6-7")

    FourFiveRooms = [world.get_region(EXStatus + "White Wafers Stage 5 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 2"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 3"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 4"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 5"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 6"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 7"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 8"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 9"),
                   world.get_region(EXStatus + "White Wafers Stage 5 Room 10")]

    WhiteWafersHub.connect(FourFiveRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 5 Room 1")
    FourFiveRooms[0].connect(FourFiveRooms[1], EXStatus + "White Wafers Stage 5 Room 1-2")
    FourFiveRooms[1].connect(FourFiveRooms[2], EXStatus + "White Wafers Stage 5 Room 2-3")
    FourFiveRooms[2].connect(FourFiveRooms[3], EXStatus + "White Wafers Stage 5 Room 3-4")
    FourFiveRooms[2].connect(FourFiveRooms[4], EXStatus + "White Wafers Stage 5 Room 3-5")
    FourFiveRooms[4].connect(FourFiveRooms[5], EXStatus + "White Wafers Stage 5 Room 5-6")
    FourFiveRooms[4].connect(FourFiveRooms[6], EXStatus + "White Wafers Stage 5 Room 5-7")
    FourFiveRooms[6].connect(FourFiveRooms[7], EXStatus + "White Wafers Stage 5 Room 7-8")
    FourFiveRooms[7].connect(FourFiveRooms[8], EXStatus + "White Wafers Stage 5 Room 8-9")
    FourFiveRooms[7].connect(FourFiveRooms[9], EXStatus + "White Wafers Stage 5 Room 8-10")

    FourSixRooms = [world.get_region(EXStatus + "White Wafers Stage 6 Room 1"),
                   world.get_region(EXStatus + "White Wafers Stage 6 Room 2")]

    WhiteWafersHub.connect(FourSixRooms[0], EXStatus + "White Wafers Hub To " + EXStatus + "White Wafers Stage 6 Room 1")
    FourSixRooms[0].connect(FourSixRooms[1], EXStatus + "White Wafers Stage 6 Room 1-2")

    FiveOneRooms = [world.get_region(EXStatus + "Nutty Noon Stage 1 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 8"),
                   world.get_region(EXStatus + "Nutty Noon Stage 1 Room 9")]

    NuttyNoonHub.connect(FiveOneRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 1 Room 1")
    FiveOneRooms[0].connect(FiveOneRooms[1], EXStatus + "Nutty Noon Stage 1 Room 1-2")
    FiveOneRooms[1].connect(FiveOneRooms[2], EXStatus + "Nutty Noon Stage 1 Room 2-3")
    FiveOneRooms[1].connect(FiveOneRooms[3], EXStatus + "Nutty Noon Stage 1 Room 2-4")
    FiveOneRooms[3].connect(FiveOneRooms[4], EXStatus + "Nutty Noon Stage 1 Room 4-5")
    FiveOneRooms[3].connect(FiveOneRooms[5], EXStatus + "Nutty Noon Stage 1 Room 4-6")
    FiveOneRooms[5].connect(FiveOneRooms[6], EXStatus + "Nutty Noon Stage 1 Room 6-7")
    FiveOneRooms[5].connect(FiveOneRooms[7], EXStatus + "Nutty Noon Stage 1 Room 6-8")
    FiveOneRooms[7].connect(FiveOneRooms[8], EXStatus + "Nutty Noon Stage 1 Room 8-9")

    FiveTwoRooms = [world.get_region(EXStatus + "Nutty Noon Stage 2 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 2 Room 8")]

    NuttyNoonHub.connect(FiveTwoRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 2 Room 1")
    FiveTwoRooms[0].connect(FiveTwoRooms[1], EXStatus + "Nutty Noon Stage 2 Room 1-2")
    FiveTwoRooms[1].connect(FiveTwoRooms[2], EXStatus + "Nutty Noon Stage 2 Room 2-3")
    FiveTwoRooms[1].connect(FiveTwoRooms[3], EXStatus + "Nutty Noon Stage 2 Room 2-4")
    FiveTwoRooms[3].connect(FiveTwoRooms[4], EXStatus + "Nutty Noon Stage 2 Room 4-5")
    FiveTwoRooms[4].connect(FiveTwoRooms[5], EXStatus + "Nutty Noon Stage 2 Room 5-6")
    FiveTwoRooms[5].connect(FiveTwoRooms[6], EXStatus + "Nutty Noon Stage 2 Room 6-7")
    FiveTwoRooms[6].connect(FiveTwoRooms[7], EXStatus + "Nutty Noon Stage 2 Room 7-8")

    FiveThreeRooms = [world.get_region(EXStatus + "Nutty Noon Stage 3 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 3 Room 8")]

    NuttyNoonHub.connect(FiveThreeRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 3 Room 1")
    FiveThreeRooms[0].connect(FiveThreeRooms[1], EXStatus + "Nutty Noon Stage 3 Room 1-2")
    FiveThreeRooms[1].connect(FiveThreeRooms[2], EXStatus + "Nutty Noon Stage 3 Room 2-3")
    FiveThreeRooms[2].connect(FiveThreeRooms[3], EXStatus + "Nutty Noon Stage 3 Room 3-4")
    FiveThreeRooms[3].connect(FiveThreeRooms[4], EXStatus + "Nutty Noon Stage 3 Room 4-5")
    FiveThreeRooms[3].connect(FiveThreeRooms[5], EXStatus + "Nutty Noon Stage 3 Room 4-6")
    FiveThreeRooms[5].connect(FiveThreeRooms[6], EXStatus + "Nutty Noon Stage 3 Room 6-7")
    FiveThreeRooms[6].connect(FiveThreeRooms[7], EXStatus + "Nutty Noon Stage 3 Room 7-8")

    FiveFourRooms = [world.get_region(EXStatus + "Nutty Noon Stage 4 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 4 Room 8")]

    NuttyNoonHub.connect(FiveFourRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 4 Room 1")
    FiveFourRooms[0].connect(FiveFourRooms[1], EXStatus + "Nutty Noon Stage 4 Room 1-2")
    FiveFourRooms[1].connect(FiveFourRooms[2], EXStatus + "Nutty Noon Stage 4 Room 2-3")
    FiveFourRooms[2].connect(FiveFourRooms[3], EXStatus + "Nutty Noon Stage 4 Room 3-4")
    FiveFourRooms[3].connect(FiveFourRooms[4], EXStatus + "Nutty Noon Stage 4 Room 4-5")
    FiveFourRooms[4].connect(FiveFourRooms[5], EXStatus + "Nutty Noon Stage 4 Room 5-6")
    FiveFourRooms[4].connect(FiveFourRooms[6], EXStatus + "Nutty Noon Stage 4 Room 5-7")
    FiveFourRooms[3].connect(FiveFourRooms[7], EXStatus + "Nutty Noon Stage 4 Room 4-8")

    FiveFiveRooms = [world.get_region(EXStatus + "Nutty Noon Stage 5 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 2"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 3"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 4"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 5"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 6"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 7"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 8"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 9"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 10"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 11"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 12"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 13"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 14"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 15"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 16"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 17"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 18"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 19"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 20"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 21"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 22"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 23"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 24"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 25"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 26"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 27"),
                   world.get_region(EXStatus + "Nutty Noon Stage 5 Room 28")]
    FiveFiveGoalRegion = world.get_region(EXStatus + "Nutty Noon Stage 5 Goal Region")

    NuttyNoonHub.connect(FiveFiveRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 5 Room 1")
    FiveFiveRooms[0].connect(FiveFiveRooms[1], EXStatus + "Nutty Noon Stage 5 Room 1-2")
    FiveFiveRooms[1].connect(FiveFiveRooms[2], EXStatus + "Nutty Noon Stage 5 Room 2-3")
    FiveFiveRooms[2].connect(FiveFiveRooms[3], EXStatus + "Nutty Noon Stage 5 Room 3-4")
    FiveFiveRooms[3].connect(FiveFiveRooms[4], EXStatus + "Nutty Noon Stage 5 Room 4-5")
    FiveFiveRooms[4].connect(FiveFiveRooms[5], EXStatus + "Nutty Noon Stage 5 Room 5-6")
    FiveFiveRooms[5].connect(FiveFiveRooms[6], EXStatus + "Nutty Noon Stage 5 Room 6-7")
    FiveFiveRooms[6].connect(FiveFiveRooms[7], EXStatus + "Nutty Noon Stage 5 Room 7-8")
    FiveFiveRooms[7].connect(FiveFiveRooms[8], EXStatus + "Nutty Noon Stage 5 Room 8-9")
    FiveFiveRooms[8].connect(FiveFiveRooms[9], EXStatus + "Nutty Noon Stage 5 Room 9-10")
    FiveFiveRooms[9].connect(FiveFiveRooms[10], EXStatus + "Nutty Noon Stage 5 Room 10-11")
    FiveFiveRooms[10].connect(FiveFiveRooms[11], EXStatus + "Nutty Noon Stage 5 Room 11-12")
    FiveFiveRooms[11].connect(FiveFiveRooms[12], EXStatus + "Nutty Noon Stage 5 Room 12-13")
    FiveFiveRooms[12].connect(FiveFiveRooms[26], EXStatus + "Nutty Noon Stage 5 Room 13-27")
    FiveFiveRooms[0].connect(FiveFiveRooms[13], EXStatus + "Nutty Noon Stage 5 Room 1-14")
    FiveFiveRooms[13].connect(FiveFiveRooms[14], EXStatus + "Nutty Noon Stage 5 Room 14-15")
    FiveFiveRooms[14].connect(FiveFiveRooms[15], EXStatus + "Nutty Noon Stage 5 Room 15-16")
    FiveFiveRooms[15].connect(FiveFiveRooms[16], EXStatus + "Nutty Noon Stage 5 Room 16-17")
    FiveFiveRooms[16].connect(FiveFiveRooms[17], EXStatus + "Nutty Noon Stage 5 Room 17-18")
    FiveFiveRooms[17].connect(FiveFiveRooms[18], EXStatus + "Nutty Noon Stage 5 Room 18-19")
    FiveFiveRooms[18].connect(FiveFiveRooms[19], EXStatus + "Nutty Noon Stage 5 Room 19-20")
    FiveFiveRooms[19].connect(FiveFiveRooms[20], EXStatus + "Nutty Noon Stage 5 Room 20-21")
    FiveFiveRooms[20].connect(FiveFiveRooms[21], EXStatus + "Nutty Noon Stage 5 Room 21-22")
    FiveFiveRooms[21].connect(FiveFiveRooms[22], EXStatus + "Nutty Noon Stage 5 Room 22-23")
    FiveFiveRooms[22].connect(FiveFiveRooms[23], EXStatus + "Nutty Noon Stage 5 Room 23-24")
    FiveFiveRooms[23].connect(FiveFiveRooms[24], EXStatus + "Nutty Noon Stage 5 Room 24-25")
    FiveFiveRooms[24].connect(FiveFiveRooms[25], EXStatus + "Nutty Noon Stage 5 Room 25-26")
    FiveFiveRooms[25].connect(FiveFiveRooms[27], EXStatus + "Nutty Noon Stage 5 Room 26-28")
    FiveFiveRooms[26].connect(FiveFiveGoalRegion, "Nutty Noon Stage 5 Room 27 Goal")
    FiveFiveRooms[27].connect(FiveFiveGoalRegion, "Nutty Noon Stage 5 Room 28 Goal")
    FiveFiveRooms[3].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #1"), "Nutty Noon Stage 5 Room 4 Energy Sphere")
    FiveFiveRooms[15].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #1"), "Nutty Noon Stage 5 Room 16 Energy Sphere")
    FiveFiveRooms[6].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #2"), "Nutty Noon Stage 5 Room 7 Energy Sphere")
    FiveFiveRooms[19].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #2"), "Nutty Noon Stage 5 Room 20 Energy Sphere")
    FiveFiveRooms[9].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #3"), "Nutty Noon Stage 5 Room 10 Energy Sphere")
    FiveFiveRooms[22].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #3"), "Nutty Noon Stage 5 Room 23 Energy Sphere")
    FiveFiveRooms[12].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #4"), "Nutty Noon Stage 5 Room 13 Energy Sphere")
    FiveFiveRooms[25].connect(world.get_region(EXStatus + "Nutty Noon Stage 5 Energy Sphere Region #4"), "Nutty Noon Stage 5 Room 26 Energy Sphere")

    FiveSixRooms = [world.get_region(EXStatus + "Nutty Noon Stage 6 Room 1"),
                   world.get_region(EXStatus + "Nutty Noon Stage 6 Room 2")]

    NuttyNoonHub.connect(FiveSixRooms[0], EXStatus + "Nutty Noon Hub To " + EXStatus + "Nutty Noon Stage 6 Room 1")
    FiveSixRooms[0].connect(FiveSixRooms[1], EXStatus + "Nutty Noon Stage 6 Room 1-2")

    SixOneRooms = [world.get_region(EXStatus + "Egg Engines Stage 1 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 8"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 9"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 10"),
                   world.get_region(EXStatus + "Egg Engines Stage 1 Room 11")]

    EggEnginesHub.connect(SixOneRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 1 Room 1")
    SixOneRooms[0].connect(SixOneRooms[1], EXStatus + "Egg Engines Stage 1 Room 1-2")
    SixOneRooms[0].connect(SixOneRooms[2], EXStatus + "Egg Engines Stage 1 Room 1-3")
    SixOneRooms[2].connect(SixOneRooms[3], EXStatus + "Egg Engines Stage 1 Room 3-4")
    SixOneRooms[3].connect(SixOneRooms[4], EXStatus + "Egg Engines Stage 1 Room 4-5")
    SixOneRooms[3].connect(SixOneRooms[5], EXStatus + "Egg Engines Stage 1 Room 4-6")
    SixOneRooms[5].connect(SixOneRooms[6], EXStatus + "Egg Engines Stage 1 Room 6-7")
    SixOneRooms[6].connect(SixOneRooms[7], EXStatus + "Egg Engines Stage 1 Room 7-8")
    SixOneRooms[6].connect(SixOneRooms[8], EXStatus + "Egg Engines Stage 1 Room 7-9")
    SixOneRooms[8].connect(SixOneRooms[9], EXStatus + "Egg Engines Stage 1 Room 9-10")
    SixOneRooms[9].connect(SixOneRooms[10], EXStatus + "Egg Engines Stage 1 Room 10-11")

    SixTwoRooms = [world.get_region(EXStatus + "Egg Engines Stage 2 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 8"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 9"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 10"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 11"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 12"),
                   world.get_region(EXStatus + "Egg Engines Stage 2 Room 13")]

    EggEnginesHub.connect(SixTwoRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 2 Room 1")
    SixTwoRooms[0].connect(SixTwoRooms[1], EXStatus + "Egg Engines Stage 2 Room 1-2")
    SixTwoRooms[1].connect(SixTwoRooms[2], EXStatus + "Egg Engines Stage 2 Room 2-3")
    SixTwoRooms[2].connect(SixTwoRooms[3], EXStatus + "Egg Engines Stage 2 Room 3-4")
    SixTwoRooms[3].connect(SixTwoRooms[4], EXStatus + "Egg Engines Stage 2 Room 4-5")
    SixTwoRooms[4].connect(SixTwoRooms[5], EXStatus + "Egg Engines Stage 2 Room 5-6")
    SixTwoRooms[5].connect(SixTwoRooms[6], EXStatus + "Egg Engines Stage 2 Room 6-7")
    SixTwoRooms[6].connect(SixTwoRooms[7], EXStatus + "Egg Engines Stage 2 Room 7-8")
    SixTwoRooms[7].connect(SixTwoRooms[8], EXStatus + "Egg Engines Stage 2 Room 8-9")
    SixTwoRooms[8].connect(SixTwoRooms[9], EXStatus + "Egg Engines Stage 2 Room 9-10")
    SixTwoRooms[9].connect(SixTwoRooms[10], EXStatus + "Egg Engines Stage 2 Room 10-11")
    SixTwoRooms[10].connect(SixTwoRooms[11], EXStatus + "Egg Engines Stage 2 Room 11-12")
    SixTwoRooms[11].connect(SixTwoRooms[12], EXStatus + "Egg Engines Stage 2 Room 12-13")

    SixThreeRooms = [world.get_region(EXStatus + "Egg Engines Stage 3 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 3 Room 8")]

    EggEnginesHub.connect(SixThreeRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 3 Room 1")
    SixThreeRooms[0].connect(SixThreeRooms[1], EXStatus + "Egg Engines Stage 3 Room 1-2")
    SixThreeRooms[1].connect(SixThreeRooms[2], EXStatus + "Egg Engines Stage 3 Room 2-3")
    SixThreeRooms[2].connect(SixThreeRooms[3], EXStatus + "Egg Engines Stage 3 Room 3-4")
    SixThreeRooms[3].connect(SixThreeRooms[4], EXStatus + "Egg Engines Stage 3 Room 4-5")
    SixThreeRooms[4].connect(SixThreeRooms[5], EXStatus + "Egg Engines Stage 3 Room 5-6")
    SixThreeRooms[5].connect(SixThreeRooms[6], EXStatus + "Egg Engines Stage 3 Room 6-7")
    SixThreeRooms[6].connect(SixThreeRooms[7], EXStatus + "Egg Engines Stage 3 Room 7-8")

    SixFourRooms = [world.get_region(EXStatus + "Egg Engines Stage 4 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 4 Room 7")]

    EggEnginesHub.connect(SixFourRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 4 Room 1")
    SixFourRooms[0].connect(SixFourRooms[1], EXStatus + "Egg Engines Stage 4 Room 1-2")
    SixFourRooms[1].connect(SixFourRooms[2], EXStatus + "Egg Engines Stage 4 Room 2-3")
    SixFourRooms[2].connect(SixFourRooms[3], EXStatus + "Egg Engines Stage 4 Room 3-4")
    SixFourRooms[3].connect(SixFourRooms[4], EXStatus + "Egg Engines Stage 4 Room 4-5")
    SixFourRooms[4].connect(SixFourRooms[5], EXStatus + "Egg Engines Stage 4 Room 5-6")
    SixFourRooms[5].connect(SixFourRooms[6], EXStatus + "Egg Engines Stage 4 Room 6-7")

    SixFiveRooms = [world.get_region(EXStatus + "Egg Engines Stage 5 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 2"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 3"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 4"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 5"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 6"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 7"),
                   world.get_region(EXStatus + "Egg Engines Stage 5 Room 8")]

    EggEnginesHub.connect(SixFiveRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 5 Room 1")
    SixFiveRooms[0].connect(SixFiveRooms[1], EXStatus + "Egg Engines Stage 5 Room 1-2")
    SixFiveRooms[1].connect(SixFiveRooms[2], EXStatus + "Egg Engines Stage 5 Room 2-3")
    SixFiveRooms[2].connect(SixFiveRooms[3], EXStatus + "Egg Engines Stage 5 Room 3-4")
    SixFiveRooms[3].connect(SixFiveRooms[4], EXStatus + "Egg Engines Stage 5 Room 4-5")
    SixFiveRooms[4].connect(SixFiveRooms[5], EXStatus + "Egg Engines Stage 5 Room 5-6")
    SixFiveRooms[5].connect(SixFiveRooms[6], EXStatus + "Egg Engines Stage 5 Room 6-7")
    SixFiveRooms[6].connect(SixFiveRooms[7], EXStatus + "Egg Engines Stage 5 Room 7-8")

    SixSixRooms = [world.get_region(EXStatus + "Egg Engines Stage 6 Room 1"),
                   world.get_region(EXStatus + "Egg Engines Stage 6 Room 2")]

    EggEnginesHub.connect(SixSixRooms[0], EXStatus + "Egg Engines Hub To " + EXStatus + "Egg Engines Stage 6 Room 1")
    SixSixRooms[0].connect(SixSixRooms[1], EXStatus + "Egg Engines Stage 6 Room 1-2")
    
    SevenOneRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 1 Room 9")]

    DangerousDinnerHub.connect(SevenOneRooms[0], EXStatus + "Dangerous Dinner Hub To " + EXStatus + "Dangerous Dinner Stage 1 Room 1")
    SevenOneRooms[0].connect(SevenOneRooms[1], EXStatus + "Dangerous Dinner Stage 1 Room 1-2")
    SevenOneRooms[1].connect(SevenOneRooms[2], EXStatus + "Dangerous Dinner Stage 1 Room 2-3")
    SevenOneRooms[2].connect(SevenOneRooms[3], EXStatus + "Dangerous Dinner Stage 1 Room 3-4")
    SevenOneRooms[2].connect(SevenOneRooms[4], EXStatus + "Dangerous Dinner Stage 1 Room 3-5")
    SevenOneRooms[4].connect(SevenOneRooms[5], EXStatus + "Dangerous Dinner Stage 1 Room 5-6")
    SevenOneRooms[4].connect(SevenOneRooms[6], EXStatus + "Dangerous Dinner Stage 1 Room 5-7")
    SevenOneRooms[6].connect(SevenOneRooms[7], EXStatus + "Dangerous Dinner Stage 1 Room 7-8")
    SevenOneRooms[7].connect(SevenOneRooms[8], EXStatus + "Dangerous Dinner Stage 1 Room 8-9")

    SevenTwoRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 9"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 2 Room 10")]

    DangerousDinnerHub.connect(SevenTwoRooms[0], EXStatus + "Dangerous Dinner Hub To " + EXStatus + "Dangerous Dinner Stage 2 Room 1")
    SevenTwoRooms[0].connect(SevenTwoRooms[1], EXStatus + "Dangerous Dinner Stage 2 Room 1-2")
    SevenTwoRooms[1].connect(SevenTwoRooms[2], EXStatus + "Dangerous Dinner Stage 2 Room 2-3")
    SevenTwoRooms[1].connect(SevenTwoRooms[3], EXStatus + "Dangerous Dinner Stage 2 Room 2-4")
    SevenTwoRooms[3].connect(SevenTwoRooms[4], EXStatus + "Dangerous Dinner Stage 2 Room 4-5")
    SevenTwoRooms[4].connect(SevenTwoRooms[5], EXStatus + "Dangerous Dinner Stage 2 Room 5-6")
    SevenTwoRooms[5].connect(SevenTwoRooms[6], EXStatus + "Dangerous Dinner Stage 2 Room 6-7")
    SevenTwoRooms[6].connect(SevenTwoRooms[7], EXStatus + "Dangerous Dinner Stage 2 Room 7-8")
    SevenTwoRooms[6].connect(SevenTwoRooms[9], EXStatus + "Dangerous Dinner Stage 2 Room 7-10")
    SevenTwoRooms[7].connect(SevenTwoRooms[8], EXStatus + "Dangerous Dinner Stage 2 Room 8-9")

    SevenThreeRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 2"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 3"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 4"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 5"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 6"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 7"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 8"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 9"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 10"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 11"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 12"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 3 Room 13")]

    DangerousDinnerHub.connect(SevenThreeRooms[0], EXStatus + "Dangerous Dinner Hub To " + EXStatus + "Dangerous Dinner Stage 3 Room 1")
    SevenThreeRooms[0].connect(SevenThreeRooms[1], EXStatus + "Dangerous Dinner Stage 3 Room 1-2")
    SevenThreeRooms[1].connect(SevenThreeRooms[2], EXStatus + "Dangerous Dinner Stage 3 Room 2-3")
    SevenThreeRooms[2].connect(SevenThreeRooms[3], EXStatus + "Dangerous Dinner Stage 3 Room 3-4")
    SevenThreeRooms[3].connect(SevenThreeRooms[4], EXStatus + "Dangerous Dinner Stage 3 Room 4-5")
    SevenThreeRooms[4].connect(SevenThreeRooms[5], EXStatus + "Dangerous Dinner Stage 3 Room 5-6")
    SevenThreeRooms[4].connect(SevenThreeRooms[6], EXStatus + "Dangerous Dinner Stage 3 Room 5-7")
    SevenThreeRooms[6].connect(SevenThreeRooms[7], EXStatus + "Dangerous Dinner Stage 3 Room 7-8")
    SevenThreeRooms[7].connect(SevenThreeRooms[8], EXStatus + "Dangerous Dinner Stage 3 Room 8-9")
    SevenThreeRooms[8].connect(SevenThreeRooms[9], EXStatus + "Dangerous Dinner Stage 3 Room 9-10")
    SevenThreeRooms[9].connect(SevenThreeRooms[10], EXStatus + "Dangerous Dinner Stage 3 Room 10-11")
    SevenThreeRooms[8].connect(SevenThreeRooms[11], EXStatus + "Dangerous Dinner Stage 3 Room 9-12")
    SevenThreeRooms[11].connect(SevenThreeRooms[12], EXStatus + "Dangerous Dinner Stage 3 Room 12-13")

    SevenFourRooms = [world.get_region(EXStatus + "Dangerous Dinner Stage 4 Room 1"),
                   world.get_region(EXStatus + "Dangerous Dinner Stage 4 Room 2")]

    DangerousDinnerHub.connect(SevenFourRooms[0], EXStatus + "Dangerous Dinner Hub To " + EXStatus + "Dangerous Dinner Stage 4 Room 1")
    SevenFourRooms[0].connect(SevenFourRooms[1], EXStatus + "Dangerous Dinner Stage 4 Room 1-2")




    #there's a good 1k+ connections that all need a EXStatus + 
    #in order to account for extrasanity

    #pain





def create_regular_locations(world: "KRtDLWorld") -> None:
    world.multiworld.regions.append(Region("Menu", world.player, world.multiworld))
    
    if world.options.extra_sanity:
        CreateTheRegionConnectionsAndExtraRegions(world, "EX ")
        AddLocationsButAMoreCallableFunctionSoEXtraSanityCanWork(world, "EX ")
    CreateTheRegionConnectionsAndExtraRegions(world, "")
    AddLocationsButAMoreCallableFunctionSoEXtraSanityCanWork(world, "")

    NonRepeatableRegions = []
    NonRepeatableRegions.append(Region("Ninja Dojo", world.player, world.multiworld))
    NonRepeatableRegions.append(Region("Scope Shot", world.player, world.multiworld))
    NonRepeatableRegions.append(Region("The Arena", world.player, world.multiworld))
    NonRepeatableRegions.append(Region("The True Arena", world.player, world.multiworld))                            
    world.multiworld.regions += NonRepeatableRegions
    
    MenuRegion = world.get_region("Menu")
    
    NinjaDojoRegion = world.get_region("Ninja Dojo")
    ScopeShotRegion = world.get_region("Scope Shot")

    #challenge regions here
    
    TheArenaRegion = world.get_region("The Arena")
    TheTrueArenaRegion = world.get_region("The True Arena")

    MenuRegion.connect(NinjaDojoRegion, "Menu To Ninja Dojo")
    MenuRegion.connect(ScopeShotRegion, "Menu To Scope Shot")

    MenuRegion.connect(TheArenaRegion, "Menu To The Arena")
    MenuRegion.connect(TheTrueArenaRegion, "Menu To The True Arena")

    AnotherDimension = world.get_region("Another Dimension")
    SevenFourRoomTwo = world.get_region("Dangerous Dinner Stage 4 Room 2")
    SevenFourRoomTwo.connect(AnotherDimension, "Dangerous Dinner Stage 4 To Another Dimension")
    if world.options.extra_sanity:
        EXAnotherDimension = world.get_region(EXStatus + "EX Another Dimension")
        EXSevenFourRoomTwo = world.get_region(EXStatus + "EX Dangerous Dinner Stage 4 Room 2")
        EXSevenFourRoomTwo.connect(AnotherDimension, "EX Dangerous Dinner Stage 4 To Another Dimension")
        EXSevenFourRoomTwo.connect(EXAnotherDimension, "EX Dangerous Dinner Stage 4 To EX Another Dimension")

    if world.options.extra_sanity:
        if world.options.star_sanity:
            for i in range(1,26+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Gold Star #" + str(i)]), KRtDLLocation)
            for i in range(1,15+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Gold Star #" + str(i)]), KRtDLLocation)
        if world.options.red_star_sanity:
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Red Star"]), KRtDLLocation)
            for i in range(1,3+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Red Star #" + str(i)]), KRtDLLocation)
        if world.options.food_sanity:
            for i in range(1,5+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Food #" + str(i)]), KRtDLLocation)
            for i in range(1,7+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Food #" + str(i)]), KRtDLLocation)
            if world.options.shuffle_arena:
                for i in range(1,5+1):
                    TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena Intermission Room - Food #" + str(i)]), KRtDLLocation)
                for i in range(1,3+1):
                    TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena Intermission Room - Food #" + str(i)]), KRtDLLocation)
        if world.options.one_up_sanity:
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - 1-up"]), KRtDLLocation)
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - 1-up"]), KRtDLLocation)
        if world.options.maxim_sanity and world.options.shuffle_arena:
            for i in range(1,5+1):
                TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena Intermission Room - M-Tomato #" + str(i)]), KRtDLLocation)
            for i in range(1,3+1):
                TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena Intermission Room - M-Tomato #" + str(i)]), KRtDLLocation)
        if world.options.shuffle_arena:
            for i in range(1,12+1):
                TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena - Round " + str(i) + " Clear"]), KRtDLLocation) 
            for i in range(1,14+1):
                TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena - Round " + str(i) + " Clear"]), KRtDLLocation) 
    elif world.options.start_in_extra_game:
        if world.options.star_sanity:
            for i in range(1,15+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Gold Star #" + str(i)]), KRtDLLocation)
        if world.options.red_star_sanity:
            for i in range(1,3+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Red Star #" + str(i)]), KRtDLLocation)
        if world.options.food_sanity:
            for i in range(1,7+1):
                 AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - Food #" + str(i)]), KRtDLLocation)
            if world.options.shuffle_arena:
                for i in range(1,3+1):
                    TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena Intermission Room - Food #" + str(i)]), KRtDLLocation)
        if world.options.one_up_sanity:
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 3 - 1-up"]), KRtDLLocation)
        if world.options.maxim_sanity and world.options.shuffle_arena:
            for i in range(1,3+1):
                TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena Intermission Room - M-Tomato #" + str(i)]), KRtDLLocation)
        if world.options.shuffle_arena:
            for i in range(1,14+1):
                TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena - Round " + str(i) + " Clear"]), KRtDLLocation)
    else:
        if world.options.star_sanity:
            for i in range(1,26+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Gold Star #" + str(i)]), KRtDLLocation)
        if world.options.red_star_sanity:
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Red Star"]), KRtDLLocation)
        if world.options.food_sanity:
            for i in range(1,5+1):
                AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - Food #" + str(i)]), KRtDLLocation)
            if world.options.shuffle_arena:
                for i in range(1,5+1):
                    TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena Intermission Room - Food #" + str(i)]), KRtDLLocation)
        if world.options.one_up_sanity:
            AnotherDimension.add_locations(get_location_names_with_ids([EXStatus + "Another Dimension Section 1 - 1-up"]), KRtDLLocation)
        if world.options.maxim_sanity and world.options.shuffle_arena:
            for i in range(1,5+1):
                TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena Intermission Room - M-Tomato #" + str(i)]), KRtDLLocation)
        if world.options.shuffle_arena:
            for i in range(1,12+1):
                TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena - Round " + str(i) + " Clear"]), KRtDLLocation)  
    
    if world.options.shuffle_subgames:
        for i in range(1,3+1):
            NinjaDojoRegion.add_locations(get_location_names_with_ids([EXStatus + "Ninja Dojo - Level " + str(i)]), KRtDLLocation)
        for i in range(1,3+1):
            ScopeShotRegion.add_locations(get_location_names_with_ids([EXStatus + "Scope Shot - Level " + str(i)]), KRtDLLocation)

    if world.options.shuffle_arena or world.options.goal == 3 or world.options.goal == 4:
        if world.options.extra_sanity:
            TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena - Complete"]), KRtDLLocation)
            TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena - Complete"]), KRtDLLocation)
        elif world.options.start_in_extra_game:
            TheTrueArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The True Arena - Complete"]), KRtDLLocation) 
        else:
            TheArenaRegion.add_locations(get_location_names_with_ids([EXStatus + "The Arena - Complete"]), KRtDLLocation) 

    #need to gather all of the unique checks and put them here instead of in that function since it's gonna be called twice
    #should also really just make a separate function to declare the rooms so it doesn't do that twice too
    #maybe also figure out a way to organise all of this more neatly so it doesn't require 10 bagillion little loops and individual calls for each location cuz god this would take an eternity-
    #-to edit to be EX compatible properly
