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
        regions.append(Region(StageNames[0] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(StageNames[1] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,5+1):
        regions.append(Region(StageNames[2] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,7+1):
        regions.append(Region(StageNames[3] + "Room " + str(i), world.player, world.multiworld))

    regions.append(Region(StageNames[4] + "Region", world.player, world.multiworld))

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
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,6+1):
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,10+1):
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,8+1):
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))

    for i in range(1,2+1):
        regions.append(Region(StageNames[9] + "Room " + str(i), world.player, world.multiworld))
    world.multiworld.regions += regions

#def connect_regions(world: KRtDLWorld) -> None:
    

def create_regular_locations(world: "KRtDLWorld") -> None:
    OneOneRooms = [world.get_region("Cookie Country Stage 1 Room 1"),
                   world.get_region("Cookie Country Stage 1 Room 2"),
                   world.get_region("Cookie Country Stage 1 Room 3"),
                   world.get_region("Cookie Country Stage 1 Room 4"),
                  world.get_region("Cookie Country Stage 1 Room 5")]

    OneTwoRooms = [world.get_region("Cookie Country Stage 2 Room 1"),
                   world.get_region("Cookie Country Stage 2 Room 2"),
                   world.get_region("Cookie Country Stage 2 Room 3"),
                   world.get_region("Cookie Country Stage 2 Room 4"),
                   world.get_region("Cookie Country Stage 2 Room 5"),
                  world.get_region("Cookie Country Stage 2 Room 6")]

    OneThreeRooms = [world.get_region("Cookie Country Stage 3 Room 1"),
                   world.get_region("Cookie Country Stage 3 Room 2"),
                   world.get_region("Cookie Country Stage 3 Room 3"),
                   world.get_region("Cookie Country Stage 3 Room 4"),
                  world.get_region("Cookie Country Stage 3 Room 5")]

    OneFourRooms = [world.get_region("Cookie Country Stage 4 Room 1"),
                   world.get_region("Cookie Country Stage 4 Room 2"),
                   world.get_region("Cookie Country Stage 4 Room 3"),
                   world.get_region("Cookie Country Stage 4 Room 4"),
                   world.get_region("Cookie Country Stage 4 Room 5"),
                   world.get_region("Cookie Country Stage 4 Room 6"),
                   world.get_region("Cookie Country Stage 4 Room 7")]

    OneFiveRegion = world.get_region("Cookie Country Stage 5 Region")

    TwoOneRooms = [world.get_region("Raisin Ruins Stage 1 Room 1"),
                   world.get_region("Raisin Ruins Stage 1 Room 2"),
                   world.get_region("Raisin Ruins Stage 1 Room 3"),
                   world.get_region("Raisin Ruins Stage 1 Room 4"),
                   world.get_region("Raisin Ruins Stage 1 Room 5"),
                   world.get_region("Raisin Ruins Stage 1 Room 6"),
                   world.get_region("Raisin Ruins Stage 1 Room 7"),
                  world.get_region("Raisin Ruins Stage 1 Room 8")]

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

    TwoThreeRooms = [world.get_region("Raisin Ruins Stage 3 Room 1"),
                   world.get_region("Raisin Ruins Stage 3 Room 2"),
                   world.get_region("Raisin Ruins Stage 3 Room 3"),
                   world.get_region("Raisin Ruins Stage 3 Room 4"),
                   world.get_region("Raisin Ruins Stage 3 Room 5"),
                   world.get_region("Raisin Ruins Stage 3 Room 6")]

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

    TwoFiveRooms = [world.get_region("Raisin Ruins Stage 5 Room 1"),
                   world.get_region("Raisin Ruins Stage 5 Room 2")]
    
    ThreeOneRooms = [world.get_region("Onion Ocean Stage 1 Room 1"),
                   world.get_region("Onion Ocean Stage 1 Room 2"),
                   world.get_region("Onion Ocean Stage 1 Room 3"),
                   world.get_region("Onion Ocean Stage 1 Room 4"),
                   world.get_region("Onion Ocean Stage 1 Room 5"),
                   world.get_region("Onion Ocean Stage 1 Room 6"),
                   world.get_region("Onion Ocean Stage 1 Room 7"),
                   world.get_region("Onion Ocean Stage 1 Room 8"),
                   world.get_region("Onion Ocean Stage 1 Room 9")]

    ThreeTwoRooms = [world.get_region("Onion Ocean Stage 2 Room 1"),
                   world.get_region("Onion Ocean Stage 2 Room 2"),
                   world.get_region("Onion Ocean Stage 2 Room 3"),
                   world.get_region("Onion Ocean Stage 2 Room 4"),
                   world.get_region("Onion Ocean Stage 2 Room 5"),
                   world.get_region("Onion Ocean Stage 2 Room 6")]


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

    ThreeFourRooms = [world.get_region("Onion Ocean Stage 4 Room 1"),
                   world.get_region("Onion Ocean Stage 4 Room 2"),
                   world.get_region("Onion Ocean Stage 4 Room 3"),
                   world.get_region("Onion Ocean Stage 4 Room 4"),
                   world.get_region("Onion Ocean Stage 4 Room 5"),
                   world.get_region("Onion Ocean Stage 4 Room 6"),
                   world.get_region("Onion Ocean Stage 4 Room 7"),
                   world.get_region("Onion Ocean Stage 4 Room 8")]

    ThreeFiveRooms = [world.get_region("Onion Ocean Stage 5 Room 1"),
                   world.get_region("Onion Ocean Stage 5 Room 2")]
    
    #NinjaDojoRegion = world.get_region("Ninja Dojo")
    #ScopeShotRegion = world.get_region("Scope Shot")
    
    if world.options.shuffle_energy_spheres:
        OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Energy Sphere #1"]), KRtDLLocation)
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Energy Sphere #2"]), KRtDLLocation)
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Energy Sphere #3"]), KRtDLLocation) 
        
        

    #if world.options.shuffle_part_spheres:
        #OneFiveRegion.add_locations(get_location_names_with_ids(["Cookie Country Stage 5 - Part Sphere"]), KRtDLLocation)
        #TwoFiveRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 5 - Part Sphere"]), KRtDLLocation)
        #ThreeFiveRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 5 - Part Sphere"]), KRtDLLocation)
                                     
    if world.options.star_sanity:
        for i in range(1,13+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(14,20+1):
            OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(21,45+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(46,57+1):
            OneOneRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)    

        for i in range(1,3+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(4,13+1):
            OneTwoRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(14,24+1):
            OneTwoRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(25,31+1):
            OneTwoRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        OneTwoRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Gold Star #32"]), KRtDLLocation)

        for i in range(1,3+1):
            OneThreeRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(4,11+1):
            OneThreeRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(12,28+1):
            OneThreeRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(29,40+1):
            OneThreeRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(41,49+1):
            OneThreeRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            OneFourRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(10,13+1):
            OneFourRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(14,22+1):
            OneFourRooms[3].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(23,77+1):
            OneFourRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(78,82+1):
            OneFourRooms[5].add_locations(get_location_names_with_ids(["Cookie Country Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,12+1):
            TwoOneRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(13,21+1):
            TwoOneRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(22,31+1):
            TwoOneRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(32,36+1):
            TwoOneRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(37,38+1):
            TwoOneRooms[6].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(39,47+1):
            TwoOneRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,20+1):
            TwoTwoRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(21,39+1):
            TwoTwoRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(40,55+1):
            TwoTwoRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(56,57+1):
            TwoTwoRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(58,98+1):
            TwoTwoRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(99,133+1):
            TwoTwoRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,9+1):
            TwoThreeRooms[0].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(10,12+1):
            TwoThreeRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(13,27+1):
            TwoThreeRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(28,45+1):
            TwoThreeRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(46,63+1):
            TwoThreeRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(64,66+1):
            TwoThreeRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,8+1):
            TwoFourRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(9,14+1):
            TwoFourRooms[2].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(15,23+1):
            TwoFourRooms[1].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(24,32+1):
            TwoFourRooms[3].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(33,36+1):
            TwoFourRooms[4].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(37,48+1):
            TwoFourRooms[5].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(49,76+1):
            TwoFourRooms[7].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(77,97+1):
            TwoFourRooms[8].add_locations(get_location_names_with_ids(["Raisin Ruins Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)


        for i in range(1,18+1):
            ThreeOneRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(19,45+1):
            ThreeOneRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(46,48+1):
            ThreeOneRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(49,63+1):
            ThreeOneRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(64,84+1):
            ThreeOneRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(85,96+1):
            ThreeOneRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(97,115+1):
            ThreeOneRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 1 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            ThreeTwoRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(13,19+1):
            ThreeTwoRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(20,34+1):
            ThreeTwoRooms[2].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(35,62+1):
            ThreeTwoRooms[4].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(63,107+1):
            ThreeTwoRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 2 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,4+1):
            ThreeThreeRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(5,23+1):
            ThreeThreeRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(24,37+1):
            ThreeThreeRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(38,53+1):
            ThreeThreeRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(54,122+1):
            ThreeThreeRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(123,177+1):
            ThreeThreeRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(178,200+1):
            ThreeThreeRooms[8].add_locations(get_location_names_with_ids(["Onion Ocean Stage 3 - Gold Star #" + str(i)]), KRtDLLocation)

        for i in range(1,12+1):
            ThreeFourRooms[0].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(13,23+1):
            ThreeFourRooms[1].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(24,33+1):
            ThreeFourRooms[3].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(34,54+1):
            ThreeFourRooms[5].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(55,69+1):
            ThreeFourRooms[6].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
        for i in range(70,96+1):
            ThreeFourRooms[7].add_locations(get_location_names_with_ids(["Onion Ocean Stage 4 - Gold Star #" + str(i)]), KRtDLLocation)
    #if world.options.red_star_sanity:
                                    

    #if world.options.blue_star_sanity:
                                   
                                         
    if world.options.flower_sanity:
        for i in range(1,6+1):
            OneOneRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Flower #" + str(i)]), KRtDLLocation)
        for i in range(7,16+1):
            OneOneRooms[2].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - Flower #" + str(i)]), KRtDLLocation)           

        for i in range(1,4+1):
            OneTwoRooms[0].add_locations(get_location_names_with_ids(["Cookie Country Stage 2 - Flower #" + str(i)]), KRtDLLocation)  

        

    if world.options.one_up_sanity:
        OneOneRooms[1].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - 1-up"]), KRtDLLocation)

        
                                          
    #if world.options.food_sanity:


    if world.options.maxim_sanity:
        OneOneRooms[4].add_locations(get_location_names_with_ids(["Cookie Country Stage 1 - 1-up"]), KRtDLLocation)

        

    #if world.options.shuffle_challenges != 0:


    #if world.options.shuffle_challenges == 2:
        

    #if world.options.shuffle_subgames:
        #for i in range(1,4);
            #NinjaDojoRegion.add_locations(get_location_names_with_ids(["Ninja Dojo - Level " + str(i)]), KRtDLLocation)
        #for i in range(1,4);
            #ScopeShotRegion.add_locations(get_location_names_with_ids(["Scope Shot - Level " + str(i)]), KRtDLLocation)
                                          

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

gold_star_table = {}
for i in range(1,57+1): #Cookie Country 1
    gold_star_table[StageNames[0] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,32+1):
    gold_star_table[StageNames[1] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,49+1):
    gold_star_table[StageNames[2] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,82+1):
    gold_star_table[StageNames[3] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,47+1): #Raisin Ruins 1
    gold_star_table[StageNames[5] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,133+1):
    gold_star_table[StageNames[6] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,66+1):
    gold_star_table[StageNames[7] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,97+1):
    gold_star_table[StageNames[8] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,115+1): #Onion Ocean 1
    gold_star_table[StageNames[10] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,107+1): #Onion Ocean 2
    gold_star_table[StageNames[11] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,200+1): #Onion Ocean 3
    gold_star_table[StageNames[12] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,96+1): #Onion Ocean 4
    gold_star_table[StageNames[13] + "- Gold Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
red_star_table = {}
for i in range(1,4+1): #Cookie Country 1
    red_star_table[StageNames[0] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1):
    red_star_table[StageNames[1] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    red_star_table[StageNames[2] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    red_star_table[StageNames[3] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1): #Raisin Ruins 1
    red_star_table[StageNames[5] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    red_star_table[StageNames[6] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    red_star_table[StageNames[7] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,7+1):
    red_star_table[StageNames[8] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1): #Onion Ocean 1
    red_star_table[StageNames[10] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,2+1): #Onion Ocean 2
    red_star_table[StageNames[11] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15+1): #Onion Ocean 3
    red_star_table[StageNames[12] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1): #Onion Ocean 4
    red_star_table[StageNames[13] + "- Red Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
blue_star_table = {}
blue_star_table[StageNames[1] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[5] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
blue_star_table[StageNames[6] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1): #Onion Ocean 1
    blue_star_table[StageNames[10] + "- Blue Star " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
blue_star_table[StageNames[12] + "- Blue Star"] = BaseLocationID + locationincrement
locationincrement += 1
    
flower_table = {}
for i in range(1,16+1):
    flower_table[StageNames[0] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[1] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[2] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,33+1):
    flower_table[StageNames[3] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    flower_table[StageNames[5] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1):
    flower_table[StageNames[6] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,4+1):
    flower_table[StageNames[7] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,35+1):
    flower_table[StageNames[10] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,32+1):
    flower_table[StageNames[11] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,27+1):
    flower_table[StageNames[12] + "- Flower " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,3+1):
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
for i in range(1,2+1):
    one_up_table[StageNames[7] + "- 1-up " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
one_up_table[StageNames[8] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    one_up_table[StageNames[10] + "- 1-up " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
one_up_table[StageNames[11] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[12] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
one_up_table[StageNames[13] + "- 1-up"] = BaseLocationID + locationincrement
locationincrement += 1
    
health_pickup_table = {}
for i in range(1,11+1): #Cookie Country 1
    health_pickup_table[StageNames[0] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6+1):
    health_pickup_table[StageNames[1] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,5+1):
    health_pickup_table[StageNames[2] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1):
    health_pickup_table[StageNames[3] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,9+1): #Raisin Ruins 1
    health_pickup_table[StageNames[5] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,6+1):
    health_pickup_table[StageNames[6] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,8+1):
    health_pickup_table[StageNames[7] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,15+1):
    health_pickup_table[StageNames[8] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,13+1): #Onion Ocean 1
    health_pickup_table[StageNames[10] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,12+1):
    health_pickup_table[StageNames[11] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,21+1):
    health_pickup_table[StageNames[12] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
for i in range(1,19+1):
    health_pickup_table[StageNames[13] + "- Food " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
    
maxim_tomato_table = {}
maxim_tomato_table[StageNames[0] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
maxim_tomato_table[StageNames[1] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,3+1):
    maxim_tomato_table[StageNames[3] + "- M-Tomato " + "#" + str(i)] = BaseLocationID + locationincrement
    locationincrement += 1
maxim_tomato_table[StageNames[4] + "- M-Tomato"] = BaseLocationID + locationincrement
locationincrement += 1
for i in range(1,2+1):
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
for i in range(1,3+1):
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
