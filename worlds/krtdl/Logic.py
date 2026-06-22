from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule
from .Options import Goal

if TYPE_CHECKING:
    from . import KRtDLWorld

def InitiateRules(world: "KRtDLWorld") -> None:
    if world.options.goal == Goal.option_magolor:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Another Dimension Final Boss - Complete", world.player)
    elif world.options.goal == Goal.option_landia:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Dangerous Dinner Stage 4 - Complete", world.player)
    elif world.options.goal == Goal.option_grand_doomer:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Nutty Noon Stage 6 - Complete", world.player)
    elif world.options.goal == Goal.option_the_arena:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("The Arena - Complete", world.player)
    elif world.options.goal == Goal.option_the_true_arena:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("The True Arena - Complete", world.player)
