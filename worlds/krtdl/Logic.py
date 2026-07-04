from typing import TYPE_CHECKING

from BaseClasses import CollectionState

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .Options import Goal

if TYPE_CHECKING:
    from . import KRtDLWorld

WorldOrderDefinition = [0, 1, 2, 3, 4, 5, 6] #Cookie Country to Dangerous Dinner

#need to make this function return stuff instead of defining the bits above ^
#as if there are multiple slots with the game they end up inheriting the previous one's world shuffles which is not right
def DefineWorldOrder(world: "KRtDLWorld") -> None:
    WorldsDef = WorldOrderDefinition.copy()
    WorldsDefEX = WorldOrderDefinition.copy()
    #print(WorldsDef)
    ShuffleableWorlds = []
    if world.options.shuffle_cookie_country:
        ShuffleableWorlds.append(0)
    if world.options.shuffle_raisin_ruins:
        ShuffleableWorlds.append(1)
    if world.options.shuffle_onion_ocean:
        ShuffleableWorlds.append(2)
    if world.options.shuffle_white_wafers:
        ShuffleableWorlds.append(3)
    if world.options.shuffle_nutty_noon:
        ShuffleableWorlds.append(4)
    if world.options.shuffle_egg_engines:
        ShuffleableWorlds.append(5)
    if world.options.shuffle_dangerous_dinner:
        ShuffleableWorlds.append(6)

    ExtraCheckingShuffleableWorlds = ShuffleableWorlds.copy()
    EXShuffleableWorlds = ShuffleableWorlds.copy()
    
    if len(ShuffleableWorlds) > 1:
        for i in range(0,7):
            if i in ExtraCheckingShuffleableWorlds:
                RandomIndex = world.random.randrange(0,len(ShuffleableWorlds))
                WorldsDef[i] = ShuffleableWorlds[RandomIndex]
                ShuffleableWorlds.pop(RandomIndex)
    if len(EXShuffleableWorlds) > 1:
        for i in range(0,7):
            if i in ExtraCheckingShuffleableWorlds:
                RandomIndex = world.random.randrange(0,len(EXShuffleableWorlds))
                WorldsDefEX[i] = EXShuffleableWorlds[RandomIndex]
                EXShuffleableWorlds.pop(RandomIndex)
    print(WorldsDef)
    print(WorldsDefEX)

    OneOneEntrance = world.get_entrance("Popstar Map To Cookie Country Hub")
    if WorldsDef[0] != 0:
        world.set_rule(OneOneEntrance, Has("World Unlock - Cookie Country"))


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
    
    DefineWorldOrder(world)
    
    #"Popstar Map To Cookie Country Hub")

    OneTwoEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 2 Room 1")
    world.set_rule(OneTwoEntrance, Has("Cookie Country Stage 1 - Complete"))
    OneThreeEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 3 Room 1")
    world.set_rule(OneThreeEntrance, Has("Cookie Country Stage 2 - Complete"))
    OneFourEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 4 Room 1")
    world.set_rule(OneFourEntrance, Has("Cookie Country Stage 3 - Complete"))
    OneFiveEntrance = world.get_entrance("Cookie Country Hub To Cookie Country Stage 5")
    world.set_rule(OneFiveEntrance, Has("Cookie Country Stage 4 - Complete"))
    
    TwoOneEntrance = world.get_entrance("Popstar Map To Raisin Ruins Hub")
    world.set_rule(TwoOneEntrance, Has("Cookie Country Stage 5 - Complete"))
    TwoTwoEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 2 Room 1")
    world.set_rule(TwoTwoEntrance, Has("Raisin Ruins Stage 1 - Complete"))
    TwoThreeEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 3 Room 1")
    world.set_rule(TwoThreeEntrance, Has("Raisin Ruins Stage 2 - Complete"))
    TwoFourEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 4 Room 1")
    world.set_rule(TwoFourEntrance, Has("Raisin Ruins Stage 3 - Complete"))
    TwoFiveEntrance = world.get_entrance("Raisin Ruins Hub To Raisin Ruins Stage 5 Room 1")
    world.set_rule(TwoFiveEntrance, Has("Raisin Ruins Stage 4 - Complete"))
    
    ThreeOneEntrance = world.get_entrance("Popstar Map To Onion Ocean Hub")
    world.set_rule(ThreeOneEntrance, Has("Raisin Ruins Stage 5 - Complete"))
    ThreeTwoEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 2 Room 1")
    world.set_rule(ThreeTwoEntrance, Has("Onion Ocean Stage 1 - Complete"))
    ThreeThreeEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 3 Room 1")
    world.set_rule(ThreeThreeEntrance, Has("Onion Ocean Stage 2 - Complete"))
    ThreeFourEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 4 Room 1")
    world.set_rule(ThreeFourEntrance, Has("Onion Ocean Stage 3 - Complete"))
    ThreeFiveEntrance = world.get_entrance("Onion Ocean Hub To Onion Ocean Stage 5 Room 1")
    world.set_rule(ThreeFiveEntrance, Has("Onion Ocean Stage 4 - Complete"))
    
    FourOneEntrance = world.get_entrance("Popstar Map To White Wafers Hub")
    world.set_rule(FourOneEntrance, Has("Onion Ocean Stage 5 - Complete"))
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
    
    FiveOneEntrance = world.get_entrance("Popstar Map To Nutty Noon Hub")
    world.set_rule(FiveOneEntrance, Has("White Wafers Stage 6 - Complete"))
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
    
    SixOneEntrance = world.get_entrance("Halcandra Map To Egg Engines Hub")
    world.set_rule(SixOneEntrance, Has("Nutty Noon Stage 6 - Complete"))
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
    
    SevenOneEntrance = world.get_entrance("Halcandra Map To Dangerous Dinner Hub")
    world.set_rule(SevenOneEntrance, Has("Egg Engines Stage 6 - Complete"))
    SevenTwoEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 2 Room 1")
    world.set_rule(SevenTwoEntrance, Has("Dangerous Dinner Stage 1 - Complete"))
    SevenThreeEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 3 Room 1")
    world.set_rule(SevenThreeEntrance, Has("Dangerous Dinner Stage 2 - Complete"))
    SevenFourEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 4 Room 1")
    world.set_rule(SevenFourEntrance, Has("Dangerous Dinner Stage 3 - Complete"))
    
    AnotherDimensionEntrance = world.get_entrance("Dangerous Dinner Stage 4 To Another Dimension")
    world.set_rule(AnotherDimensionEntrance, Has("Dangerous Dinner Stage 4 - Complete"))
    
    if world.options.extra_sanity:
        OneTwoEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 2 Room 1")
        world.set_rule(OneTwoEntrance, Has("EX Cookie Country Stage 1 - Complete"))
        OneThreeEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 3 Room 1")
        world.set_rule(OneThreeEntrance, Has("EX Cookie Country Stage 2 - Complete"))
        OneFourEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 4 Room 1")
        world.set_rule(OneFourEntrance, Has("EX Cookie Country Stage 3 - Complete"))
        OneFiveEntrance = world.get_entrance("EX Cookie Country Hub To EX Cookie Country Stage 5")
        world.set_rule(OneFiveEntrance, Has("EX Cookie Country Stage 4 - Complete"))
        
        TwoOneEntrance = world.get_entrance("EX Popstar Map To EX Raisin Ruins Hub")
        world.set_rule(TwoOneEntrance, Has("EX Cookie Country Stage 5 - Complete"))
        TwoTwoEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 2 Room 1")
        world.set_rule(TwoTwoEntrance, Has("EX Raisin Ruins Stage 1 - Complete"))
        TwoThreeEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 3 Room 1")
        world.set_rule(TwoThreeEntrance, Has("EX Raisin Ruins Stage 2 - Complete"))
        TwoFourEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 4 Room 1")
        world.set_rule(TwoFourEntrance, Has("EX Raisin Ruins Stage 3 - Complete"))
        TwoFiveEntrance = world.get_entrance("EX Raisin Ruins Hub To EX Raisin Ruins Stage 5 Room 1")
        world.set_rule(TwoFiveEntrance, Has("EX Raisin Ruins Stage 4 - Complete"))
        
        ThreeOneEntrance = world.get_entrance("EX Popstar Map To EX Onion Ocean Hub")
        world.set_rule(ThreeOneEntrance, Has("EX Raisin Ruins Stage 5 - Complete"))
        ThreeTwoEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 2 Room 1")
        world.set_rule(ThreeTwoEntrance, Has("EX Onion Ocean Stage 1 - Complete"))
        ThreeThreeEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 3 Room 1")
        world.set_rule(ThreeThreeEntrance, Has("EX Onion Ocean Stage 2 - Complete"))
        ThreeFourEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 4 Room 1")
        world.set_rule(ThreeFourEntrance, Has("EX Onion Ocean Stage 3 - Complete"))
        ThreeFiveEntrance = world.get_entrance("EX Onion Ocean Hub To EX Onion Ocean Stage 5 Room 1")
        world.set_rule(ThreeFiveEntrance, Has("EX Onion Ocean Stage 4 - Complete"))
        
        FourOneEntrance = world.get_entrance("EX Popstar Map To EX White Wafers Hub")
        world.set_rule(FourOneEntrance, Has("EX Onion Ocean Stage 5 - Complete"))
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
        
        FiveOneEntrance = world.get_entrance("EX Popstar Map To EX Nutty Noon Hub")
        world.set_rule(FiveOneEntrance, Has("EX White Wafers Stage 6 - Complete"))
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
        
        SixOneEntrance = world.get_entrance("EX Halcandra Map To EX Egg Engines Hub")
        world.set_rule(SixOneEntrance, Has("EX Nutty Noon Stage 6 - Complete"))
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
        
        SevenOneEntrance = world.get_entrance("EX Halcandra Map To EX Dangerous Dinner Hub")
        world.set_rule(SevenOneEntrance, Has("EX Egg Engines Stage 6 - Complete"))
        SevenTwoEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 2 Room 1")
        world.set_rule(SevenTwoEntrance, Has("EX Dangerous Dinner Stage 1 - Complete"))
        SevenThreeEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 3 Room 1")
        world.set_rule(SevenThreeEntrance, Has("EX Dangerous Dinner Stage 2 - Complete"))
        SevenFourEntrance = world.get_entrance("EX Dangerous Dinner Hub To EX Dangerous Dinner Stage 4 Room 1")
        world.set_rule(SevenFourEntrance, Has("EX Dangerous Dinner Stage 3 - Complete"))
        
        AnotherDimensionEntrance = world.get_entrance("EX Dangerous Dinner Stage 4 To Another Dimension")
        AnotherDimensionEntrance = world.get_entrance("EX Dangerous Dinner Stage 4 To EX Another Dimension")    
        world.set_rule(AnotherDimensionEntrance, Has("EX Dangerous Dinner Stage 4 - Complete"))
