from typing import TYPE_CHECKING, Any, Dict
from dataclasses import dataclass

if TYPE_CHECKING:
    from . import KRtDLWorld

WorldOrderDefinition = [0, 1, 2, 3, 4, 5, 6] #Cookie Country to Dangerous Dinner

#need to make this function return stuff instead of defining the bits above ^
#as if there are multiple slots with the game they end up inheriting the previous one's world shuffles which is not right
def DefineWorldOrder(world: "KRtDLWorld") -> None:
    FinalGenExport: Dict[str, Any] = {}
    
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
    
    FinalGenExport["WorldsShuffled"] = len(ShuffleableWorlds)
    FinalGenExport["EXWorldsShuffled"] = len(EXShuffleableWorlds)
    
    ShufflingIndex = 0
    if world.options.starting_world != 0:
        WorldsDef[0] = world.options.starting_world - 1
        WorldsDef[world.options.starting_world - 1] = 0
        WorldsDefEX[0] = world.options.starting_world - 1
        WorldsDefEX[world.options.starting_world - 1] = 0
        ShufflingIndex = 1
    
    if len(ShuffleableWorlds) > 1:
        for i in range(ShufflingIndex,7):
            if i in ExtraCheckingShuffleableWorlds:
                RandomIndex = world.random.randrange(0,len(ShuffleableWorlds))
                WorldsDef[i] = ShuffleableWorlds[RandomIndex]
                ShuffleableWorlds.pop(RandomIndex)
    if len(EXShuffleableWorlds) > 1:
        for i in range(ShufflingIndex,7):
            if i in ExtraCheckingShuffleableWorlds:
                RandomIndex = world.random.randrange(0,len(EXShuffleableWorlds))
                WorldsDefEX[i] = EXShuffleableWorlds[RandomIndex]
                EXShuffleableWorlds.pop(RandomIndex)
    print(WorldsDef)
    print(WorldsDefEX)
    
    
    #something is wrong with how this is implemented as is overwritten by other RTDL slots, strange as other world settings are still individual
    
    #possible fault of Dictionaries?
    #confirmed not to be caused by a lack of .copy()
    #there is really no rhyme or reason I can see that this shouldn't just work as intended given other variables like this can be set individually from other slots in basically this same manner
    #strange
    
    FinalGenExport["WorldDef"] = WorldsDef
    FinalGenExport["EXWorldDef"] = WorldsDefEX
    
    return FinalGenExport.copy()
