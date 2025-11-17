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
    "Another Dimension Part 1 ",
    "Another Dimension Part 2 ",
    "Another Dimension Boss ",
    "Another Dimension Final Boss "
]

def create_all_regions(world: "KRtDLWorld") -> None:
    regions = []

    regions.append(Region("Menu", world.player, world.multiworld))
    
    for i in range(1,5+1):
        print(StageNames[0] + "Room " + str(i))
        regions.append(Region(StageNames[0] + "Room " + str(i), world.player, world.multiworld))
    
    world.multiworld.regions += regions

#def connect_regions(world: KRtDLWorld) -> None:
    

def create_regular_locations(world: "KRtDLWorld") -> None:
    OneOneRoomOne = world.get_region("Cookie Country Stage 1 Room 1")
    OneOneRoomTwo = world.get_region("Cookie Country Stage 1 Room 2")
    OneOneRoomThree = world.get_region("Cookie Country Stage 1 Room 3")
    OneOneRoomFour = world.get_region("Cookie Country Stage 1 Room 4")
    OneOneRoomFive = world.get_region("Cookie Country Stage 1 Room 5")

    if world.options.shuffle_energy_spheres:
        OneOneRoomTwo.add_locations(get_location_names_with_ids(energy_sphere_table[0]), KRtDLLocation)
        OneOneRoomFive.add_locations(get_location_names_with_ids(energy_sphere_table[1]), KRtDLLocation)
        OneOneRoomFive.add_locations(get_location_names_with_ids(energy_sphere_table[2]), KRtDLLocation)                        

    #if world.options.shuffle_part_spheres:
        
                                     
    if world.options.star_sanity:
        for i in range(0,13):
            OneOneRoomOne.add_locations(get_location_names_with_ids(staridlookupbase + i), KRtDLLocation)
        for i in range(13,20):
            OneOneRoomTwo.add_locations(get_location_names_with_ids(staridlookupbase + i), KRtDLLocation)
        for i in range(20,45):
            OneOneRoomThree.add_locations(get_location_names_with_ids(staridlookupbase + i), KRtDLLocation)
        for i in range(45,57):
            OneOneRoomFour.add_locations(get_location_names_with_ids(staridlookupbase + i), KRtDLLocation)                            

    #if world.options.red_star_sanity:
                                    

    #if world.options.blue_star_sanity:
                                   
                                         
    if world.options.flower_sanity:
        for i in range(1,6+1):
            OneOneRoomOne.add_locations(get_location_names_with_ids(flower_table[i]), KRtDLLocation)
        for i in range(7,16+1):
            OneOneRoomThree.add_locations(get_location_names_with_ids(flower_table[i]), KRtDLLocation)                             

    #if world.options.one_up_sanity:

                                          
    #if world.options.food_sanity:


    #if world.options.maxim_sanity:


    #if world.options.shuffle_challenges != 0:


    #if world.options.shuffle_challenges == 2:
        

    #if world.options.shuffle_subgames:
                                          
                                          
    #for i in range(1,13):
        #testregion.add_locations(get_location_names_with_ids(gold_star_table.keys()), KRtDLLocation)
        #get_location_names_with_ids
        #testregion.locations.append(KRtDLLocation(world.player, ("GoldStarTest " + str(i)), world.location_name_to_id["Bottom Left Chest"], overworld)
#def create_events(world: KRtDLWorld) -> None:
    

locationincrement = 0
stage_completion_table = {}
for i in StageNames:
    if i != "Another Dimension Part 1" and i != "Another Dimension Part 2":
        stage_completion_table[i + " - Complete"] = BaseLocationID + locationincrement
        locationincrement += 1
        stage_completion_table["EX " + i + " - Complete"] = BaseLocationID + locationincrement
        locationincrement += 1
#should end at ID 68
    
energy_sphere_table = {}
for i in range(1,3+1): #Cookie Country 1
    energy_sphere_table[StageNames[0] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[0] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1): #Cookie Country 2
    energy_sphere_table[StageNames[1] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[1] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1): #Cookie Country 3
    energy_sphere_table[StageNames[2] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[2] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,4+1): #Cookie Country 4
    energy_sphere_table[StageNames[3] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[3] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,3+1): #Raisin Ruins 1
    energy_sphere_table[StageNames[5] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[5] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Raisin Ruins 2
    energy_sphere_table[StageNames[6] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[6] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Raisin Ruins 3
    energy_sphere_table[StageNames[7] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[7] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,5+1): #Raisin Ruins 4
    energy_sphere_table[StageNames[8] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[8] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,3+1): #Onion Ocean 1
    energy_sphere_table[StageNames[10] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[10] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Onion Ocean 2
    energy_sphere_table[StageNames[11] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[11] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Onion Ocean 3
    energy_sphere_table[StageNames[12] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[12] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,5+1): #Onion Ocean 4
    energy_sphere_table[StageNames[13] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[13] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,3+1): #White Wafers 1
    energy_sphere_table[StageNames[15] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[15] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #White Wafers 2
    energy_sphere_table[StageNames[16] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[16] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #White Wafers 3
    energy_sphere_table[StageNames[17] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[17] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #White Wafers 4
    energy_sphere_table[StageNames[18] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[18] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #White Wafers 5
    energy_sphere_table[StageNames[19] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[19] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Nutty Noon 1
    energy_sphere_table[StageNames[21] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[21] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Nutty Noon 2
    energy_sphere_table[StageNames[22] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[22] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Nutty Noon 3
    energy_sphere_table[StageNames[23] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[23] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1   
for i in range(1,4+1): #Nutty Noon 4
    energy_sphere_table[StageNames[24] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[24] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,4+1): #Nutty Noon 5
    energy_sphere_table[StageNames[25] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[25] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1  
for i in range(1,3+1): #Egg Engines 1
    energy_sphere_table[StageNames[27] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[27] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Egg Engines 2
    energy_sphere_table[StageNames[28] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[28] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1): #Egg Engines 3
    energy_sphere_table[StageNames[29] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[29] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1    
for i in range(1,5+1): #Egg Engines 4
    energy_sphere_table[StageNames[30] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[30] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1): #Egg Engines 5
    energy_sphere_table[StageNames[31] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[31] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1): #Dangerous Dinner 1
    energy_sphere_table[StageNames[33] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[33] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1): #Dangerous Dinner 2
    energy_sphere_table[StageNames[34] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[34] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1): #Dangerous Dinner 3
    energy_sphere_table[StageNames[35] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    energy_sphere_table["EX " + StageNames[35] + "- Energy Sphere " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
#should end at ID 309
    
SimplificationArray = [4,9,14,20,26]
part_sphere_table = {}
for i in SimplificationArray:
    part_sphere_table[StageNames[i] + "- Part Sphere"] = BaseLocationID + locationincrement
    locationincrement += 1
    part_sphere_table["EX " + StageNames[i] + "- Part Sphere"] = BaseLocationID + locationincrement
    locationincrement += 1

staridlookupbase = BaseLocationID + locationincrement
gold_star_table = {}
for i in range(1,57+1): #Cookie Country 1
    gold_star_table[StageNames[0] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
#for i in range(1,32):
    #gold_star_table[StageNames[1] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,49):
    #gold_star_table[StageNames[2] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,82):
    #gold_star_table[StageNames[3] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,47): #Raisin Ruins 1
    #gold_star_table[StageNames[5] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,133):
    #gold_star_table[StageNames[6] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,66):
    #gold_star_table[StageNames[7] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,97):
    #gold_star_table[StageNames[8] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,117): #Onion Ocean 1
    #gold_star_table[StageNames[10] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,107): #Onion Ocean 2
    #gold_star_table[StageNames[11] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,200): #Onion Ocean 3
    #gold_star_table[StageNames[12] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
#for i in range(1,96): #Onion Ocean 4
    #gold_star_table[StageNames[13] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    #locationincrement += 1
    
red_star_table = {}
for i in range(1,4): #Cookie Country 1
    red_star_table[StageNames[0] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2):
    red_star_table[StageNames[1] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4):
    red_star_table[StageNames[2] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8):
    red_star_table[StageNames[3] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2): #Raisin Ruins 1
    red_star_table[StageNames[5] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7):
    red_star_table[StageNames[6] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8):
    red_star_table[StageNames[7] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7):
    red_star_table[StageNames[8] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5): #Onion Ocean 1
    red_star_table[StageNames[10] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2): #Onion Ocean 2
    red_star_table[StageNames[11] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15): #Onion Ocean 3
    red_star_table[StageNames[12] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9): #Onion Ocean 4
    red_star_table[StageNames[13] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
blue_star_table = {}
blue_star_table[StageNames[1] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[5] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2): #Onion Ocean 1
    blue_star_table[StageNames[10] + "- Blue Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
blue_star_table[StageNames[12] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
    
flower_table = {}
for i in range(1,16):
    flower_table[StageNames[0] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4):
    flower_table[StageNames[1] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4):
    flower_table[StageNames[2] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,33):
    flower_table[StageNames[3] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9):
    flower_table[StageNames[5] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13):
    flower_table[StageNames[6] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4):
    flower_table[StageNames[7] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,35):
    flower_table[StageNames[10] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,32):
    flower_table[StageNames[11] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,27):
    flower_table[StageNames[12] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3):
    flower_table[StageNames[13] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
one_up_table = {}
one_up_table[StageNames[0] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[2] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[3] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[5] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[6] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2):
    one_up_table[StageNames[7] + "- 1-up " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
one_up_table[StageNames[8] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3):
    one_up_table[StageNames[10] + "- 1-up " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
one_up_table[StageNames[11] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[12] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[13] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
    
health_pickup_table = {}
for i in range(1,11): #Cookie Country 1
    health_pickup_table[StageNames[0] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6):
    health_pickup_table[StageNames[1] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5):
    health_pickup_table[StageNames[2] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9):
    health_pickup_table[StageNames[3] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9): #Raisin Ruins 1
    health_pickup_table[StageNames[5] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6):
    health_pickup_table[StageNames[6] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8):
    health_pickup_table[StageNames[7] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15):
    health_pickup_table[StageNames[8] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15): #Onion Ocean 1
    health_pickup_table[StageNames[10] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,12):
    health_pickup_table[StageNames[11] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,21):
    health_pickup_table[StageNames[12] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,19):
    health_pickup_table[StageNames[13] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
maxim_tomato_table = {}
maxim_tomato_table[StageNames[0] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[1] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3):
    maxim_tomato_table[StageNames[3] + "- M-Tomato " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
maxim_tomato_table[StageNames[4] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2):
    maxim_tomato_table[StageNames[6] + "- M-Tomato " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
maxim_tomato_table[StageNames[7] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[8] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[9] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[10] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3):
    maxim_tomato_table[StageNames[12] + "- M-Tomato " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
maxim_tomato_table[StageNames[13] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[14] + "- M-Tomato"] = BaseLocationID + locationincrement
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
