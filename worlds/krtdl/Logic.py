from typing import TYPE_CHECKING

from BaseClasses import CollectionState

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, Rule

from .Options import Goal

if TYPE_CHECKING:
    from . import KRtDLWorld

def InitiateRules(world: "KRtDLWorld") -> None:
    if world.options.goal == Goal.option_magolor:
        world.set_completion_rule(Has("Another Dimension Final Boss - Complete"))
    elif world.options.goal == Goal.option_landia:
        world.set_completion_rule(Has("Dangerous Dinner Stage 4 - Complete"))
    elif world.options.goal == Goal.option_grand_doomer:
        world.set_completion_rule(Has("Nutty Noon Stage 6 - Complete"))
    elif world.options.goal == Goal.option_the_arena:
        world.set_completion_rule(Has("The Arena - Complete"))
    elif world.options.goal == Goal.option_the_true_arena:
        world.set_completion_rule(Has("The True Arena - Complete"))

    CanHover = True
    CanSlide = True
    CanSwim = True
    CanInhale = True
    CanSuperInhale = True
    if world.options.shuffle_moves:
        CanHover = Has("Hover")
        CanSlide = Has("Slide")
        CanSlide = Has("Swim")
        CanInhale = Has("Progressive Inhale")
        CanSuperInhale = Has("Progressive Inhale", count=2)
    
    #this gets INSANELY complicated, for simplicity's sake these will be True for now
    CanAccessSword = True
    CanAccessCutter = True
    CanAccessLeaf = True
    CanAccessWhip = True
    CanAccessFire = True
    CanAccessNeedle = True
    CanAccessBeam = True
    CanAccessSpark = True
    CanAccessStone = True
    CanAccessParasol = True
    CanAccessWater = True
    CanAccessHiJump = True
    CanAccessTornado = True
    CanAccessBomb = True
    CanAccessSpear = True
    CanAccessHammer = True
    CanAccessIce = True
    CanAccessWing = True
    CanAccessNinja = True
    CanAccessFighter = True
    #if world.options.shuffle_copy_abilities:

    HasStarcutterAccess = HasAll("Lor Starcutter Oars", "Lor Starcutter Right Wing", "Lor Starcutter Left Wing", "Lor Starcutter Emblem", "Lor Starcutter Mast")
    HasStarcutterAccessEX = HasAll("EX Lor Starcutter Oars", "EX Lor Starcutter Right Wing", "EX Lor Starcutter Left Wing", "EX Lor Starcutter Emblem", "EX Lor Starcutter Mast")
    if world.options.start_with_lor:
        HasStarcutterAccess = True
        HasStarcutterAccessEX = True

    HasLandia = True
    if world.options.shuffle_landia:
        HasLandia = Has("Landia")

    CanFightBosses = True
    if world.options.shuffle_moves and not world.options.shuffle_copy_abilities:
        CanFightBosses = Has("Progressive Inhale")
    elif world.options.shuffle_copy_abilities:
        CanFightBosses = CanAccessSword | CanAccessCutter | CanAccessLeaf | CanAccessWhip | CanAccessFire | CanAccessNeedle | CanAccessBeam | CanAccessSpark | CanAccessStone | CanAccessParasol | CanAccessWater | CanAccessHiJump | CanAccessTornado | CanAccessBomb | CanAccessSpear | CanAccessHammer | CanAccessIce | CanAccessWing | CanAccessNinja | CanAccessFighter
        if world.options.shuffle_moves:
            CanFightBosses = CanFightBosses | Has("Progressive Inhale")

    CookieCountryHubEntrance = world.get_entrance("Map To Cookie Country Hub")
    if world.world_gen["WorldDef"][0] != 0:
        if not world.options.start_in_halcandra:
            if world.world_gen["WorldDef"][5] == 0:
                world.set_rule(CookieCountryHubEntrance, HasStarcutterAccess)
            elif world.world_gen["WorldDef"][6] == 0:
                world.set_rule(CookieCountryHubEntrance, Has("World Unlock - Cookie Country") & HasStarcutterAccess)
            else:
                world.set_rule(CookieCountryHubEntrance, Has("World Unlock - Cookie Country"))
        else:
            if world.world_gen["WorldDef"][2] == 0:
                world.set_rule(CookieCountryHubEntrance, HasStarcutterAccess)
            elif world.world_gen["WorldDef"][1] == 0:
                world.set_rule(CookieCountryHubEntrance, Has("World Unlock - Cookie Country"))
            else:
                world.set_rule(CookieCountryHubEntrance, Has("World Unlock - Cookie Country") & HasStarcutterAccess)

    TwoOneEntrance = world.get_entrance("Map To Raisin Ruins Hub")
    #world.set_rule(TwoOneEntrance, Has("Cookie Country Stage 5 - Complete"))
    if world.world_gen["WorldDef"][0] != 1:
        world.set_rule(TwoOneEntrance, Has("World Unlock - Raisin Ruins"))

    ThreeOneEntrance = world.get_entrance("Map To Onion Ocean Hub")
    if world.world_gen["WorldDef"][0] != 2:
        world.set_rule(ThreeOneEntrance, Has("World Unlock - Onion Ocean"))

    FourOneEntrance = world.get_entrance("Map To White Wafers Hub")
    if world.world_gen["WorldDef"][0] != 3:
        world.set_rule(FourOneEntrance, Has("World Unlock - White Wafers"))

    FiveOneEntrance = world.get_entrance("Map To Nutty Noon Hub")
    if world.world_gen["WorldDef"][0] != 4:
        world.set_rule(FiveOneEntrance, Has("World Unlock - Nutty Noon"))

    SixOneEntrance = world.get_entrance("Map To Egg Engines Hub")
    if world.world_gen["WorldDef"][0] != 5:
        world.set_rule(SixOneEntrance, Has("World Unlock - Egg Engines"))

    SevenOneEntrance = world.get_entrance("Map To Dangerous Dinner Hub")
    if world.world_gen["WorldDef"][0] != 6:
        world.set_rule(SevenOneEntrance, Has("World Unlock - Dangerous Dinner"))

    AnotherDimensionEntrance = world.get_entrance("Dangerous Dinner Stage 4 To Another Dimension")
    world.set_rule(AnotherDimensionEntrance, Has("Dangerous Dinner Stage 4 - Complete") & HasLandia) 

    #extra conditions needed for this
    #EX Dangerous Dinner needs to only connect to Another Dimension/EX when Extra Sanity is enabled
    #Dangerous Dinner should connect to Another Dimension/EX if Extra/Both Modes is on
    
    #if world.options.start_in_extra_game != 0:
        #EXAnotherDimensionEntranceOne = world.get_entrance("EX Dangerous Dinner Stage 4 To Another Dimension")
        #EXAnotherDimensionEntranceTwo = world.get_entrance("EX Dangerous Dinner Stage 4 To EX Another Dimension")   
        #world.set_rule(EXAnotherDimensionEntranceOne, Has("EX Dangerous Dinner Stage 4 - Complete") & HasLandia)
        #world.set_rule(EXAnotherDimensionEntranceTwo, Has("EX Dangerous Dinner Stage 4 - Complete") & HasLandia)

    
    #these only account for non-plando'd spheres through Shuffle Part Spheres, need to write more logic for this elsewhere
    OneFivePartSphere = world.get_location("Cookie Country Stage 5 Room 1 - Part Sphere")
    TwoFivePartSphere = world.get_location("Raisin Ruins Stage 5 Room 2 - Part Sphere")
    ThreeFivePartSphere = world.get_location("Onion Ocean Stage 5 Room 2 - Part Sphere")
    FourSixPartSphere = world.get_location("White Wafers Stage 6 Room 2 - Part Sphere")
    FiveSixPartSphere = world.get_location("Nutty Noon Stage 6 Room 2 - Part Sphere")
    world.set_rule(OneFivePartSphere, CanFightBosses)
    world.set_rule(TwoFivePartSphere, CanFightBosses)
    world.set_rule(ThreeFivePartSphere, CanFightBosses)
    world.set_rule(FourSixPartSphere, CanFightBosses)
    world.set_rule(FiveSixPartSphere, CanFightBosses)
    
    OneFiveComplete = world.get_location("Cookie Country Stage 5 - Complete")
    world.set_rule(OneFiveComplete, CanFightBosses)
    TwoFiveComplete = world.get_location("Raisin Ruins Stage 5 - Complete")
    world.set_rule(TwoFiveComplete, CanFightBosses)
    ThreeFiveComplete = world.get_location("Onion Ocean Stage 5 - Complete")
    world.set_rule(ThreeFiveComplete, CanFightBosses)
    FourSixComplete = world.get_location("White Wafers Stage 6 - Complete")
    world.set_rule(FourSixComplete, CanFightBosses)
    FiveSixComplete = world.get_location("Nutty Noon Stage 6 - Complete")
    world.set_rule(FiveSixComplete, CanFightBosses)
    SixSixComplete = world.get_location("Egg Engines Stage 6 - Complete")
    world.set_rule(SixSixComplete, CanFightBosses)
    SevenFourComplete = world.get_location("Dangerous Dinner Stage 4 - Complete")
    world.set_rule(SevenFourComplete, CanFightBosses)




    

    OneTwoEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 2 Room 1")
    world.set_rule(OneTwoEntrance, Has("Cookie Country Stage 1 - Complete"))
    OneThreeEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 3 Room 1")
    world.set_rule(OneThreeEntrance, Has("Cookie Country Stage 2 - Complete"))
    OneFourEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 4 Room 1")
    world.set_rule(OneFourEntrance, Has("Cookie Country Stage 3 - Complete"))
    OneFiveEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 5")
    world.set_rule(OneFiveEntrance, Has("Cookie Country Stage 4 - Complete"))
    
    TwoTwoEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 2 Room 1")
    world.set_rule(TwoTwoEntrance, Has("Raisin Ruins Stage 1 - Complete"))
    TwoThreeEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 3 Room 1")
    world.set_rule(TwoThreeEntrance, Has("Raisin Ruins Stage 2 - Complete"))
    TwoFourEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 4 Room 1")
    world.set_rule(TwoFourEntrance, Has("Raisin Ruins Stage 3 - Complete"))
    TwoFiveEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 5 Room 1")
    world.set_rule(TwoFiveEntrance, Has("Raisin Ruins Stage 4 - Complete"))
    
    ThreeTwoEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 2 Room 1")
    world.set_rule(ThreeTwoEntrance, Has("Onion Ocean Stage 1 - Complete"))
    ThreeThreeEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 3 Room 1")
    world.set_rule(ThreeThreeEntrance, Has("Onion Ocean Stage 2 - Complete"))
    ThreeFourEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 4 Room 1")
    world.set_rule(ThreeFourEntrance, Has("Onion Ocean Stage 3 - Complete"))
    ThreeFiveEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 5 Room 1")
    world.set_rule(ThreeFiveEntrance, Has("Onion Ocean Stage 4 - Complete"))
    
    FourTwoEntrance = world.get_entrance("White Wafers Hub To White Wafers Stage 2 Room 1")
    world.set_rule(FourTwoEntrance, Has("White Wafers Stage 1 - Complete"))
    FourThreeEntrance = world.get_entrance("White Wafers Hub To White Wafers Stage 3 Room 1")
    world.set_rule(FourThreeEntrance, Has("White Wafers Stage 2 - Complete"))
    FourFourEntrance = world.get_entrance("White Wafers Hub To White Wafers Stage 4 Room 1")
    world.set_rule(FourFourEntrance, Has("White Wafers Stage 3 - Complete"))
    FourFiveEntrance = world.get_entrance("White Wafers Hub To White Wafers Stage 5 Room 1")
    world.set_rule(FourFiveEntrance, Has("White Wafers Stage 4 - Complete"))
    FourSixEntrance = world.get_entrance("White Wafers Hub To White Wafers Stage 6 Room 1")
    world.set_rule(FourSixEntrance, Has("White Wafers Stage 5 - Complete"))
    
    FiveTwoEntrance = world.get_entrance("Nutty Noon Hub To Nutty Noon Stage 2 Room 1")
    world.set_rule(FiveTwoEntrance, Has("Nutty Noon Stage 1 - Complete"))
    FiveThreeEntrance = world.get_entrance("Nutty Noon Hub To Nutty Noon Stage 3 Room 1")
    world.set_rule(FiveThreeEntrance, Has("Nutty Noon Stage 2 - Complete"))
    FiveFourEntrance = world.get_entrance("Nutty Noon Hub To Nutty Noon Stage 4 Room 1")
    world.set_rule(FiveFourEntrance, Has("Nutty Noon Stage 3 - Complete"))
    FiveFiveEntrance = world.get_entrance("Nutty Noon Hub To Nutty Noon Stage 5 Room 1")
    world.set_rule(FiveFiveEntrance, Has("Nutty Noon Stage 4 - Complete"))
    FiveSixEntrance = world.get_entrance("Nutty Noon Hub To Nutty Noon Stage 6 Room 1")
    world.set_rule(FiveSixEntrance, Has("Nutty Noon Stage 5 - Complete"))
    
    SixTwoEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 2 Room 1")
    world.set_rule(SixTwoEntrance, Has("Egg Engines Stage 1 - Complete"))
    SixThreeEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 3 Room 1")
    world.set_rule(SixThreeEntrance, Has("Egg Engines Stage 2 - Complete"))
    SixFourEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 4 Room 1")
    world.set_rule(SixFourEntrance, Has("Egg Engines Stage 3 - Complete"))
    SixFiveEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 5 Room 1")
    world.set_rule(SixFiveEntrance, Has("Egg Engines Stage 4 - Complete"))
    SixSixEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 6 Room 1")
    world.set_rule(SixSixEntrance, Has("Egg Engines Stage 5 - Complete"))
    
    SevenTwoEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 2 Room 1")
    world.set_rule(SevenTwoEntrance, Has("Dangerous Dinner Stage 1 - Complete"))
    SevenThreeEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 3 Room 1")
    world.set_rule(SevenThreeEntrance, Has("Dangerous Dinner Stage 2 - Complete"))
    SevenFourEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 4 Room 1")
    world.set_rule(SevenFourEntrance, Has("Dangerous Dinner Stage 3 - Complete"))
    
    if world.options.extra_sanity:
        OneTwoEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 2 Room 1")
        world.set_rule(OneTwoEntrance, Has("EX Cookie Country Stage 1 - Complete"))
        OneThreeEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 3 Room 1")
        world.set_rule(OneThreeEntrance, Has("EX Cookie Country Stage 2 - Complete"))
        OneFourEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 4 Room 1")
        world.set_rule(OneFourEntrance, Has("EX Cookie Country Stage 3 - Complete"))
        OneFiveEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 5")
        world.set_rule(OneFiveEntrance, Has("EX Cookie Country Stage 4 - Complete"))
        
        TwoTwoEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 2 Room 1")
        world.set_rule(TwoTwoEntrance, Has("EX Raisin Ruins Stage 1 - Complete"))
        TwoThreeEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 3 Room 1")
        world.set_rule(TwoThreeEntrance, Has("EX Raisin Ruins Stage 2 - Complete"))
        TwoFourEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 4 Room 1")
        world.set_rule(TwoFourEntrance, Has("EX Raisin Ruins Stage 3 - Complete"))
        TwoFiveEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 5 Room 1")
        world.set_rule(TwoFiveEntrance, Has("EX Raisin Ruins Stage 4 - Complete"))
        
        ThreeTwoEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 2 Room 1")
        world.set_rule(ThreeTwoEntrance, Has("EX Onion Ocean Stage 1 - Complete"))
        ThreeThreeEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 3 Room 1")
        world.set_rule(ThreeThreeEntrance, Has("EX Onion Ocean Stage 2 - Complete"))
        ThreeFourEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 4 Room 1")
        world.set_rule(ThreeFourEntrance, Has("EX Onion Ocean Stage 3 - Complete"))
        ThreeFiveEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 5 Room 1")
        world.set_rule(ThreeFiveEntrance, Has("EX Onion Ocean Stage 4 - Complete"))
        
        FourTwoEntrance = world.get_entrance("EX White Wafers Hub To EX White Wafers Stage 2 Room 1")
        world.set_rule(FourTwoEntrance, Has("EX White Wafers Stage 1 - Complete"))
        FourThreeEntrance = world.get_entrance("EX White Wafers Hub To EX White Wafers Stage 3 Room 1")
        world.set_rule(FourThreeEntrance, Has("EX White Wafers Stage 2 - Complete"))
        FourFourEntrance = world.get_entrance("EX White Wafers Hub To EX White Wafers Stage 4 Room 1")
        world.set_rule(FourFourEntrance, Has("EX White Wafers Stage 3 - Complete"))
        FourFiveEntrance = world.get_entrance("EX White Wafers Hub To EX White Wafers Stage 5 Room 1")
        world.set_rule(FourFiveEntrance, Has("EX White Wafers Stage 4 - Complete"))
        FourSixEntrance = world.get_entrance("EX White Wafers Hub To EX White Wafers Stage 6 Room 1")
        world.set_rule(FourSixEntrance, Has("EX White Wafers Stage 5 - Complete"))
        
        FiveTwoEntrance = world.get_entrance("EX Nutty Noon Hub To EX Nutty Noon Stage 2 Room 1")
        world.set_rule(FiveTwoEntrance, Has("EX Nutty Noon Stage 1 - Complete"))
        FiveThreeEntrance = world.get_entrance("EX Nutty Noon Hub To EX Nutty Noon Stage 3 Room 1")
        world.set_rule(FiveThreeEntrance, Has("EX Nutty Noon Stage 2 - Complete"))
        FiveFourEntrance = world.get_entrance("EX Nutty Noon Hub To EX Nutty Noon Stage 4 Room 1")
        world.set_rule(FiveFourEntrance, Has("EX Nutty Noon Stage 3 - Complete"))
        FiveFiveEntrance = world.get_entrance("EX Nutty Noon Hub To EX Nutty Noon Stage 5 Room 1")
        world.set_rule(FiveFiveEntrance, Has("EX Nutty Noon Stage 4 - Complete"))
        FiveSixEntrance = world.get_entrance("EX Nutty Noon Hub To EX Nutty Noon Stage 6 Room 1")
        world.set_rule(FiveSixEntrance, Has("EX Nutty Noon Stage 5 - Complete"))
        
        SixTwoEntrance = world.get_entrance("EX Egg Engines Hub To EX Egg Engines Stage 2 Room 1")
        world.set_rule(SixTwoEntrance, Has("EX Egg Engines Stage 1 - Complete"))
        SixThreeEntrance = world.get_entrance("EX Egg Engines Hub To EX Egg Engines Stage 3 Room 1")
        world.set_rule(SixThreeEntrance, Has("EX Egg Engines Stage 2 - Complete"))
        SixFourEntrance = world.get_entrance("EX Egg Engines Hub To EX Egg Engines Stage 4 Room 1")
        world.set_rule(SixFourEntrance, Has("EX Egg Engines Stage 3 - Complete"))
        SixFiveEntrance = world.get_entrance("EX Egg Engines Hub To EX Egg Engines Stage 5 Room 1")
        world.set_rule(SixFiveEntrance, Has("EX Egg Engines Stage 4 - Complete"))
        SixSixEntrance = world.get_entrance("EX Egg Engines Hub To EX Egg Engines Stage 6 Room 1")
        world.set_rule(SixSixEntrance, Has("EX Egg Engines Stage 5 - Complete"))
        
        SevenTwoEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 2 Room 1")
        world.set_rule(SevenTwoEntrance, Has("EX Dangerous Dinner Stage 1 - Complete"))
        SevenThreeEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 3 Room 1")
        world.set_rule(SevenThreeEntrance, Has("EX Dangerous Dinner Stage 2 - Complete"))
        SevenFourEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 4 Room 1")
        world.set_rule(SevenFourEntrance, Has("EX Dangerous Dinner Stage 3 - Complete"))
        
        AnotherDimensionEntrance = world.get_entrance("EX Dangerous Dinner Stage 4 To Another Dimension")
        AnotherDimensionEntrance = world.get_entrance("EX Dangerous Dinner Stage 4 To EX Another Dimension")    
        world.set_rule(AnotherDimensionEntrance, Has("EX Dangerous Dinner Stage 4 - Complete"))
