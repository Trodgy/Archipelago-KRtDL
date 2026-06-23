from typing import TYPE_CHECKING

from BaseClasses import CollectionState

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

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
    world.set_rule(SixOneEntrance, Has("Egg Engines Stage 1 - Complete"))
    SixThreeEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 3 Room 1")
    world.set_rule(SixOneEntrance, Has("Egg Engines Stage 2 - Complete"))
    SixFourEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 4 Room 1")
    world.set_rule(SixOneEntrance, Has("Egg Engines Stage 3 - Complete"))
    SixFiveEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 5 Room 1")
    world.set_rule(SixOneEntrance, Has("Egg Engines Stage 4 - Complete"))
    SixSixEntrance = world.get_entrance("Egg Engines Hub To Egg Engines Stage 6 Room 1")
    world.set_rule(SixOneEntrance, Has("Egg Engines Stage 5 - Complete"))
    
    SevenOneEntrance = world.get_entrance("Halcandra Map To Dangerous Dinner Hub")
    world.set_rule(SevenOneEntrance, Has("Egg Engines Stage 6 - Complete"))
    SevenTwoEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 2 Room 1")
    world.set_rule(SevenTwoEntrance, Has("Dangerous Dinner Stage 1 - Complete"))
    SevenThreeEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 3 Room 1")
    world.set_rule(SevenThreeEntrance, Has("Dangerous Dinner Stage 2 - Complete"))
    SevenFourEntrance = world.get_entrance("Dangerous Dinner Hub To Dangerous Dinner Stage 4 Room 1")
    world.set_rule(SevenFourEntrance, Has("Dangerous Dinner Stage 3 - Complete"))
    
    AnotherDimensionEntrance = world.get_entrance("Dangerous Dinner Stage 4 To Another Dimension")
    world.set_rule(SevenOneEntrance, Has("Dangerous Dinner Stage 4 - Complete"))
    
    #if world.options.extra_sanity:
        
