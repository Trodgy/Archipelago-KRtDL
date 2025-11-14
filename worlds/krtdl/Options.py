from typing import List
from dataclasses import dataclass
from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionSet, OptionGroup, PerGameCommonOptions

class Goal(Choice):
    """Determines the goal for your run.
    
    Main Complete - Complete the Main mode by defeating the final boss.
    Extra Complete - Complete the Extra mode by defeating the EX final boss.

    The Arena - Complete The Arena.
    The True Arena - Complete The True Arena.
    
    Energy Sphere Hunt - Collect a set number of Energy Spheres.
    
    Perfectionist - Obtain every possible check. [Adapts to Sanity options]
    [REALLY LONG, SEEDS MAY BE IMPOSSIBLE WITHOUT CONSOLE USAGE]"""
    display_name = "Goal"
    default = 0
    option_main_complete = 0
    option_extra_complete = 1
    option_the_arena = 2
    option_the_true_arena = 3
    option_energy_sphere_hunt = 4
    option_perfectionist = 5

class EnergySphereHuntRequirement(Range):
    """Determines how many Energy Spheres are necessary to achieve the Energy Sphere Hunt goal.
    [Note that setting the goal over 120 will require playing through Extra mode]
    [Will force Energy Spheres in Extra mode to become checks if over 120 regardless of Extrasanity status if this is the case]"""
    display_name = "Energy Sphere Hunt Requirement"
    range_start = 1
    range_end = 240
    default = 80

class ShuffleEnergySpheres(DefaultOnToggle):
    """Shuffles all Energy Spheres into other locations.
    [Total checks added: 120]"""
    display_name = "Shuffle Energy Spheres"

class ShufflePartSpheres(DefaultOnToggle):
    """Shuffles all Part Spheres into other locations.
    [May cause BKs related to the Lor Starcutter]
    [Total checks added: 5]"""
    display_name = "Shuffle Part Spheres"

class ShuffleEnemies(Choice):
    """Shuffles the game's enemies around excluding Another Dimension.
    
    Light - Enemies will be shuffled with eachother within a given stage's pool.
    Intense - Enemies will be shuffled with eachother within the entire game's pool.
    Anomalous - Randomizes enemies out of the game's possible ones. [CREATES HARDER SEEDS]"""
    display_name = "Shuffle Enemies"
    default = 0
    option_off = 0
    option_light = 1
    option_intense = 2
    option_anomalous = 3

class RandomizeEnemyAbilities(Toggle):
    """Randomizes which enemies give what copy ability."""
    display_name = "Randomize Enemy Abilities"

class ShuffleBosses(Choice):
    """Shuffles the game's bosses around excluding the two in Another Dimension.
    
    Light - Bosses will be shuffled with eachother.
    Anomalous - Randomizes boss fights out of the game's possible ones."""
    display_name = "Shuffle Bosses"
    default = 0
    option_off = 0
    option_light = 1
    option_anomalous = 2

class StartingWorld(Choice):
    """Determines the first world of your run. Default is Cookie Country."""
    display_name = "Starting World"
    default = 0
    option_cookie_country = 0
    option_raisin_ruins = 1
    option_onion_ocean = 2
    option_white_wafers = 3
    option_nutty_noon = 4
    option_egg_engines = 5
    option_dangerous_dinner = 6

class StartWithAllWorlds(Toggle):
    """Unlocks all of the worlds and their Stage 1s from the start.
    [Some worlds may be locked out by Lor Starcutter access]"""
    display_name = "Start with all Worlds"

class StartWithAllStages(Toggle):
    """Unlocks all of the non-boss stages from the start. 
    Beating all of a level's stages unlocks the boss stage slot."""
    display_name = "Start with all Stages"

class StartWithLor(Toggle):
    """Unlocks the Lor Starcutter from the start (all 5 parts), allowing you to travel between Popstar and Halcandra immediately."""
    display_name = "Start with Lor Starcutter" 

class StartInExtraGame(Toggle):
    """Choose whether or not the run starts in Extra Mode"""
    display_name = "Start in Extra Mode"




class ShuffleChallenges(Choice):
    """Turns challenge medals into checks. 
    One for Bronze, Silver and Gold. Bonus checks also available for Platinums.
    
    Off - No checks from challenges.
    On - Checks from challenges.
    Platinum - Platinum ranks give checks."""    
    display_name = "Shuffle Challenges"
    default = 0
    option_challenges_off = 0
    option_challenges_on = 1
    option_challenges_platinum = 2
    
class ChallengeEnergySphereRange(Range):
    """Determines the maximum Energy Spheres needed for a challenge."""
    display_name = "Challenge max Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 120

class ShuffleSubgames(Toggle):
    """Turns Subgame level completions into checks. 
    One for levels 1, 2 and 3."""  
    display_name = "Shuffle Subgames"
    
class SubgameEnergySphereRange(Range):
    """Determines the maximum Energy Spheres needed for a Subgame."""
    display_name = "Subgame max Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 30

class CopyAbilityRoomEnergySphereRange(Range):
    """Determines the maximum Energy Spheres needed for a Copy Ability room."""
    display_name = "Copy Ability room max Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 80




class ShuffleCookieCountry(DefaultOnToggle):
    """If enabled, allows Cookie Country to be shuffled with other worlds."""
    display_name = "Shuffle Cookie Country"

class ShuffleRaisinRuins(DefaultOnToggle):
    """If enabled, allows Raisin Ruins to be shuffled with other worlds."""
    display_name = "Shuffle Raisin Ruins"

class ShuffleOnionOcean(DefaultOnToggle):
    """If enabled, allows Onion Ocean to be shuffled with other worlds."""
    display_name = "Shuffle Onion Ocean"

class ShuffleWhiteWafers(DefaultOnToggle):
    """If enabled, allows White Wafers to be shuffled with other worlds."""
    display_name = "Shuffle White Wafers"

class ShuffleNuttyNoon(DefaultOnToggle):
    """If enabled, allows Nutty Noon to be shuffled with other worlds."""
    display_name = "Shuffle Nutty Noon"

class ShuffleEggEngines(DefaultOnToggle):
    """If enabled, allows Egg Engines to be shuffled with other worlds."""
    display_name = "Shuffle Egg Engines"

class ShuffleDangerousDinner(DefaultOnToggle):
    """If enabled, allows Dangerous Dinner to be shuffled with other worlds."""
    display_name = "Shuffle Dangerous Dinner"

class ShuffleStages(Choice):
    """Shuffles the game's stages around.
    
    Light - Shuffles stages within a given world.
    Intense - Shuffles all of the game's stages with eachother."""
    display_name = "Shuffle Stages"
    default = 0
    option_off = 0
    option_light = 1
    option_intense = 2

class ShuffleBossStages(Toggle):
    """Shuffles the game's boss stages around.
    [If Shuffle Stages is turned on to Intense then worlds may have no or multiple boss stages]"""
    display_name = "Shuffle Boss Stages"

class LockBossStages(Toggle):
    """Makes Boss Stages require Energy Spheres to unlock instead of stage completions."""
    display_name = "Boss Stage locks"   

class BossOneEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 1."""
    display_name = "Boss 1 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 5

class BossTwoEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 2."""
    display_name = "Boss 2 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 12

class BossThreeEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 3."""
    display_name = "Boss 3 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 20

class BossFourEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 4."""
    display_name = "Boss 4 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 30

class BossFiveEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 5."""
    display_name = "Boss 5 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 45

class BossSixEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 6."""
    display_name = "Boss 6 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 60

class BossSevenEnergySphereRequirement(Range):
    """Determines the number of Energy Spheres needed for Boss 7."""
    display_name = "Boss 7 Energy Sphere requirement"
    range_start = 1
    range_end = 120
    default = 80




class ShuffleCopyAbilities(DefaultOnToggle):
    """Requires individual Copy Abilities to be unlocked to be able to obtain them."""
    display_name = "Shuffle Copy Abilities"

class ShuffleLandia(Toggle):
    """Requires you to find Landia in order to enter Another Dimension."""
    display_name = "Shuffle Landia"

class ShuffleMoves(Toggle):
    """If enabled, requires some of Kirby's basic moves to be unlocked to be able to use them."""
    display_name = "Shuffle Moves"

class ShuffleLevelItems(DefaultOnToggle):
    """Requires objects such as Buttons, Invincibility Candy or Crackler to be unlocked to be able to find them in levels."""
    display_name = "Shuffle Items"




class StarSanity(Toggle):
    """Turns all guaranteed Gold Stars (ones not gained from Flowers) into checks.
    [WARNING: ADDS [total number] CHECKS AND CREATES SOME VERY HARD SEEDS]
    [MAY RESULT IN FRIENDS YELLING AT YOU FROM PICKING UP HUNDREDS OF VERY UNHELPFUL STARS IN THEIR WORLD]"""
    display_name = "Star Sanity"

class RedStarSanity(Toggle):
    """Turns all Red Stars into checks.
    [Total checks added: x]"""
    display_name = "Red Star Sanity"

class BlueStarSanity(Toggle):
    """Turns all Blue Stars into checks.
    [Total checks added: x]"""
    display_name = "Blue Star Sanity"

class FoodSanity(Toggle):
    """Turns all guaranteed Food items (ones not gained from Flowers and exluding Maxim Tomatoes) into checks.
    [Total checks added: x]"""
    display_name = "Food Sanity"

class FlowerSanity(Toggle):
    """Turns all flower pickups into checks.
    [Total checks added: x]"""
    display_name = "Flower Sanity"

class OneUpSanity(Toggle):
    """Turns all 1-Ups into checks.
    [Total checks added: x]"""
    display_name = "1-Up Sanity"

class MaximSanity(Toggle):
    """Turns all Maxim Tomatoes into checks.
    [Total checks added: x]"""
    display_name = "Maxim Sanity"

class ExtraSanity(Toggle):
    """Basically doubles the number of checks by making all pickups in Extra Mode have unique checks to Normal Mode.
    [WARNING: ADDS AN OBSCENE NUMBER OF EXTRA CHECKS AND WILL LIKELY REQUIRE TWO FULL PLAYTHROUGHS OF THE GAME]
    [MAY RESULT IN A GRUELING ENDURANCE TEST]"""
    display_name = "EX-tra Sanity"




class TrapChance(Range):
    """The chance for any junk item in the pool to be replaced by a trap."""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 5

class SleepWeight(Range):
    """The weight of Sleep traps in the trap pool.
    Forces all players to use the Sleep ability if possible."""
    display_name = "Sleep Weight"
    range_start = 0
    range_end = 100
    default = 50

class EjectWeight(Range):
    """The weight of Eject traps in the trap pool.
    Forces all players to eject their abilities."""
    display_name = "Eject Weight"
    range_start = 0
    range_end = 100
    default = 10

class MouthfulWeight(Range):
    """The weight of Mouthful traps in the trap pool.
    Puts a junk item in Kirby's mouth which disables some of his moves."""
    display_name = "Mouthful Weight"
    range_start = 0
    range_end = 100
    default = 40




@dataclass
class KRtDLOptions(PerGameCommonOptions):
    """Options for Kirby's Return to Dream Land."""
    
    goal: Goal
    energy_sphere_hunt_requirement: EnergySphereHuntRequirement
    shuffle_energy_spheres: ShuffleEnergySpheres
    shuffle_part_spheres: ShufflePartSpheres
    shuffle_enemies: ShuffleEnemies
    randomize_enemy_abilities: RandomizeEnemyAbilities
    shuffle_bosses: ShuffleBosses
    starting_world: StartingWorld
    start_with_all_worlds: StartWithAllWorlds
    start_with_all_stages: StartWithAllStages
    start_in_extra_game: StartInExtraGame

    shuffle_stages: ShuffleStages
    shuffle_boss_stages: ShuffleBossStages
    shuffle_cookie_country: ShuffleCookieCountry
    shuffle_raisin_ruins: ShuffleRaisinRuins
    shuffle_onion_ocean: ShuffleOnionOcean
    shuffle_white_wafers: ShuffleWhiteWafers
    shuffle_nutty_noon: ShuffleNuttyNoon
    shuffle_egg_engines: ShuffleEggEngines
    shuffle_dangerous_dinner: ShuffleDangerousDinner
    
    shuffle_copy_abilities: ShuffleCopyAbilities
    shuffle_landia: ShuffleLandia
    shuffle_moves: ShuffleMoves
    shuffle_level_items: ShuffleLevelItems

    star_sanity: StarSanity
    red_star_sanity: RedStarSanity
    blue_star_sanity: BlueStarSanity
    food_sanity: FoodSanity
    flower_sanity: FlowerSanity
    one_up_sanity: OneUpSanity
    maxim_sanity: MaximSanity
    extra_sanity: ExtraSanity

    trap_chance: TrapChance
    sleep_weight: SleepWeight
    eject_weight: EjectWeight
    mouthful_weight: MouthfulWeight

    death_link: DeathLink

krtdl_option_groups = [
    OptionGroup(
        "Basic Options", 
        [Goal, 
         EnergySphereHuntRequirement, 
         ShuffleEnergySpheres,
         ShufflePartSpheres,
         ShuffleEnemies,
         RandomizeEnemyAbilities,
         ShuffleBosses,
         StartingWorld, 
         StartWithAllWorlds,
         StartWithAllStages,
         StartWithLor,
         StartInExtraGame],
    ),
    
    OptionGroup(
        "Stage Options",
        [ShuffleCookieCountry, 
         ShuffleRaisinRuins, 
         ShuffleOnionOcean, 
         ShuffleWhiteWafers, 
         ShuffleNuttyNoon, 
         ShuffleEggEngines, 
         ShuffleDangerousDinner,
         ShuffleStages, 
         ShuffleBossStages,
         LockBossStages,
         BossOneEnergySphereRequirement,
         BossTwoEnergySphereRequirement,
         BossThreeEnergySphereRequirement,
         BossFourEnergySphereRequirement,
         BossFiveEnergySphereRequirement,
         BossSixEnergySphereRequirement,
         BossSevenEnergySphereRequirement],
    ),

    OptionGroup(
        "Item Options", 
        [ShuffleCopyAbilities, 
         ShuffleMoves, 
         ShuffleLandia, 
         ShuffleLevelItems],
    ),

    OptionGroup(
        "Side Content Options",
        [ShuffleChallenges, 
         ChallengeEnergySphereRange, 
         ShuffleSubgames, 
         SubgameEnergySphereRange, 
         CopyAbilityRoomEnergySphereRange],
    ),
    
    OptionGroup(
        "Sanity Options", 
        [StarSanity, 
         RedStarSanity, 
         BlueStarSanity, 
         FoodSanity, 
         FlowerSanity,
         OneUpSanity, 
         MaximSanity,
         ExtraSanity],
    ),

    OptionGroup(
        "Trap Options", 
        [TrapChance, 
         SleepWeight, 
         EjectWeight, 
         MouthfulWeight],
    ),
]
