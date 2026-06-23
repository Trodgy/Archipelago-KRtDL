from typing import List
from .GameNames import ItemNames, StageNames
from BaseClasses import Item, ItemClassification

BaseID = 24102011

class KRtDLItem(Item):
    game: str = "Kirby's Return to Dream Land"

class ItemData:
    name: str
    code: int
    classification: ItemClassification
    max_capacity: int
    id: int

    def __init__(self, name: str, id: int, progression: ItemClassification, max_capacity: int = 1) -> None:
        self.name = name
        self.id = id
        self.code = id + BaseID
        self.classification = progression
        self.max_capacity = max_capacity

item_table: dict[str, ItemData] = {
    # junk items
    ItemNames.gold_star.value: ItemData(ItemNames.gold_star.value, 0, ItemClassification.filler),
    ItemNames.red_star.value: ItemData(ItemNames.red_star.value, 1, ItemClassification.filler),
    ItemNames.blue_star.value: ItemData(ItemNames.blue_star.value, 2, ItemClassification.filler),
    ItemNames.flower.value: ItemData(ItemNames.flower.value, 3, ItemClassification.filler),

    # useful items
    ItemNames.one_up.value: ItemData(ItemNames.one_up.value, 4, ItemClassification.useful),
    ItemNames.food_pickup.value: ItemData(ItemNames.food_pickup.value, 5, ItemClassification.useful),
    ItemNames.m_tomato.value: ItemData(ItemNames.m_tomato.value, 6, ItemClassification.useful),

    # progression items
    ItemNames.energy_sphere.value: ItemData(ItemNames.energy_sphere.value, 7, ItemClassification.progression, 120),
    ItemNames.energy_sphere_ex.value: ItemData(ItemNames.energy_sphere_ex.value, 8, ItemClassification.progression, 120),
    ItemNames.sword.value: ItemData(ItemNames.sword.value, 9, ItemClassification.progression, 1),
    ItemNames.cutter.value: ItemData(ItemNames.cutter.value, 10, ItemClassification.progression, 1),
    ItemNames.leaf.value: ItemData(ItemNames.leaf.value, 11, ItemClassification.progression, 1),
    ItemNames.whip.value: ItemData(ItemNames.whip.value, 12, ItemClassification.progression, 1),
    ItemNames.fire.value: ItemData(ItemNames.fire.value, 13, ItemClassification.progression, 1),
    ItemNames.needle.value: ItemData(ItemNames.needle.value, 14, ItemClassification.progression, 1),
    ItemNames.beam.value: ItemData(ItemNames.beam.value, 15, ItemClassification.progression, 1),
    ItemNames.spark.value: ItemData(ItemNames.spark.value, 16, ItemClassification.progression, 1),
    ItemNames.stone.value: ItemData(ItemNames.stone.value, 17, ItemClassification.progression, 1),
    ItemNames.parasol.value: ItemData(ItemNames.parasol.value, 18, ItemClassification.progression, 1),
    ItemNames.water.value: ItemData(ItemNames.water.value, 19, ItemClassification.progression, 1),
    ItemNames.hi_jump.value: ItemData(ItemNames.hi_jump.value, 20, ItemClassification.progression, 1),
    ItemNames.tornado.value: ItemData(ItemNames.tornado.value, 21, ItemClassification.progression, 1),
    ItemNames.bomb.value: ItemData(ItemNames.bomb.value, 22, ItemClassification.progression, 1),
    ItemNames.spear.value: ItemData(ItemNames.spear.value, 23, ItemClassification.progression, 1),
    ItemNames.hammer.value: ItemData(ItemNames.hammer.value, 24, ItemClassification.progression, 1),
    ItemNames.ice.value: ItemData(ItemNames.ice.value, 25, ItemClassification.progression, 1),
    ItemNames.wing.value: ItemData(ItemNames.wing.value, 26, ItemClassification.progression, 1),
    ItemNames.ninja.value: ItemData(ItemNames.ninja.value, 27, ItemClassification.progression, 1),
    ItemNames.fighter.value: ItemData(ItemNames.fighter.value, 28, ItemClassification.progression, 1),
    ItemNames.crash.value: ItemData(ItemNames.crash.value, 29, ItemClassification.progression, 1),
    ItemNames.mike.value: ItemData(ItemNames.mike.value, 30, ItemClassification.progression, 1),
    ItemNames.inhale.value: ItemData(ItemNames.inhale.value, 31, ItemClassification.progression, 2),
    ItemNames.hover.value: ItemData(ItemNames.hover.value, 32, ItemClassification.progression, 1),
    ItemNames.slide.value: ItemData(ItemNames.slide.value, 33, ItemClassification.progression, 1),
    ItemNames.swim.value: ItemData(ItemNames.swim.value, 34, ItemClassification.progression, 1),
    ItemNames.switch.value: ItemData(ItemNames.switch.value, 35, ItemClassification.progression, 1),
    ItemNames.pulley.value: ItemData(ItemNames.pulley.value, 36, ItemClassification.progression, 1),
    ItemNames.key.value: ItemData(ItemNames.key.value, 37, ItemClassification.progression, 1),
    ItemNames.crackler.value: ItemData(ItemNames.crackler.value, 38, ItemClassification.progression, 1),
    ItemNames.i_candy.value: ItemData(ItemNames.i_candy.value, 39, ItemClassification.progression, 1),
    ItemNames.p_shield.value: ItemData(ItemNames.p_shield.value, 40, ItemClassification.progression, 1),
    ItemNames.m_tomato_box.value: ItemData(ItemNames.m_tomato_box.value, 41, ItemClassification.progression, 1),
    ItemNames.candles.value: ItemData(ItemNames.candles.value, 42, ItemClassification.progression, 1),
    ItemNames.t_crystal.value: ItemData(ItemNames.t_crystal.value, 43, ItemClassification.progression, 1),
    ItemNames.s_boot.value: ItemData(ItemNames.s_boot.value, 44, ItemClassification.progression, 1),
    ItemNames.b_bomb.value: ItemData(ItemNames.b_bomb.value, 45, ItemClassification.progression, 1),
    ItemNames.landia.value: ItemData(ItemNames.landia.value, 46, ItemClassification.progression, 1),
    ItemNames.lor_oars.value: ItemData(ItemNames.lor_oars.value, 47, ItemClassification.progression, 1),
    ItemNames.lor_rwing.value: ItemData(ItemNames.lor_rwing.value, 48, ItemClassification.progression, 1),
    ItemNames.lor_lwing.value: ItemData(ItemNames.lor_lwing.value, 49, ItemClassification.progression, 1),
    ItemNames.lor_emblem.value: ItemData(ItemNames.lor_emblem.value, 50, ItemClassification.progression, 1),
    ItemNames.lor_mast.value: ItemData(ItemNames.lor_mast.value, 51, ItemClassification.progression, 1),
    ItemNames.lor_oars_ex.value: ItemData(ItemNames.lor_oars_ex.value, 52, ItemClassification.progression, 1),
    ItemNames.lor_rwing_ex.value: ItemData(ItemNames.lor_rwing_ex.value, 53, ItemClassification.progression, 1),
    ItemNames.lor_lwing_ex.value: ItemData(ItemNames.lor_lwing_ex.value, 54, ItemClassification.progression, 1),
    ItemNames.lor_emblem_ex.value: ItemData(ItemNames.lor_emblem_ex.value, 55, ItemClassification.progression, 1),
    ItemNames.lor_mast_ex.value: ItemData(ItemNames.lor_mast_ex.value, 56, ItemClassification.progression, 1),

    #stage completions
    ItemNames.stage1_1.value: ItemData(ItemNames.stage1_1.value, 57, ItemClassification.progression, 1),
    ItemNames.stage1_2.value: ItemData(ItemNames.stage1_2.value, 58, ItemClassification.progression, 1),
    ItemNames.stage1_3.value: ItemData(ItemNames.stage1_3.value, 59, ItemClassification.progression, 1),
    ItemNames.stage1_4.value: ItemData(ItemNames.stage1_4.value, 60, ItemClassification.progression, 1),
    ItemNames.stage1_5.value: ItemData(ItemNames.stage1_5.value, 61, ItemClassification.progression, 1),
    ItemNames.stage2_1.value: ItemData(ItemNames.stage2_1.value, 62, ItemClassification.progression, 1),
    ItemNames.stage2_2.value: ItemData(ItemNames.stage2_2.value, 63, ItemClassification.progression, 1),
    ItemNames.stage2_3.value: ItemData(ItemNames.stage2_3.value, 64, ItemClassification.progression, 1),
    ItemNames.stage2_4.value: ItemData(ItemNames.stage2_4.value, 65, ItemClassification.progression, 1),
    ItemNames.stage2_5.value: ItemData(ItemNames.stage2_5.value, 66, ItemClassification.progression, 1),
    ItemNames.stage3_1.value: ItemData(ItemNames.stage3_1.value, 67, ItemClassification.progression, 1),
    ItemNames.stage3_2.value: ItemData(ItemNames.stage3_2.value, 68, ItemClassification.progression, 1),
    ItemNames.stage3_3.value: ItemData(ItemNames.stage3_3.value, 69, ItemClassification.progression, 1),
    ItemNames.stage3_4.value: ItemData(ItemNames.stage3_4.value, 70, ItemClassification.progression, 1),
    ItemNames.stage3_5.value: ItemData(ItemNames.stage3_5.value, 71, ItemClassification.progression, 1),
    ItemNames.stage4_1.value: ItemData(ItemNames.stage4_1.value, 72, ItemClassification.progression, 1),
    ItemNames.stage4_2.value: ItemData(ItemNames.stage4_2.value, 73, ItemClassification.progression, 1),
    ItemNames.stage4_3.value: ItemData(ItemNames.stage4_3.value, 74, ItemClassification.progression, 1),
    ItemNames.stage4_4.value: ItemData(ItemNames.stage4_4.value, 75, ItemClassification.progression, 1),
    ItemNames.stage4_5.value: ItemData(ItemNames.stage4_5.value, 76, ItemClassification.progression, 1),
    ItemNames.stage4_6.value: ItemData(ItemNames.stage4_6.value, 77, ItemClassification.progression, 1),
    ItemNames.stage5_1.value: ItemData(ItemNames.stage5_1.value, 78, ItemClassification.progression, 1),
    ItemNames.stage5_2.value: ItemData(ItemNames.stage5_2.value, 79, ItemClassification.progression, 1),
    ItemNames.stage5_3.value: ItemData(ItemNames.stage5_3.value, 80, ItemClassification.progression, 1),
    ItemNames.stage5_4.value: ItemData(ItemNames.stage5_4.value, 81, ItemClassification.progression, 1),
    ItemNames.stage5_5.value: ItemData(ItemNames.stage5_5.value, 82, ItemClassification.progression, 1),
    ItemNames.stage5_6.value: ItemData(ItemNames.stage5_6.value, 83, ItemClassification.progression, 1),
    ItemNames.stage6_1.value: ItemData(ItemNames.stage6_1.value, 84, ItemClassification.progression, 1),
    ItemNames.stage6_2.value: ItemData(ItemNames.stage6_2.value, 85, ItemClassification.progression, 1),
    ItemNames.stage6_3.value: ItemData(ItemNames.stage6_3.value, 86, ItemClassification.progression, 1),
    ItemNames.stage6_4.value: ItemData(ItemNames.stage6_4.value, 87, ItemClassification.progression, 1),
    ItemNames.stage6_5.value: ItemData(ItemNames.stage6_5.value, 88, ItemClassification.progression, 1),
    ItemNames.stage6_6.value: ItemData(ItemNames.stage6_6.value, 89, ItemClassification.progression, 1),
    ItemNames.stage7_1.value: ItemData(ItemNames.stage7_1.value, 90, ItemClassification.progression, 1),
    ItemNames.stage7_2.value: ItemData(ItemNames.stage7_2.value, 91, ItemClassification.progression, 1),
    ItemNames.stage7_3.value: ItemData(ItemNames.stage7_3.value, 92, ItemClassification.progression, 1),
    ItemNames.stage7_4.value: ItemData(ItemNames.stage7_4.value, 93, ItemClassification.progression, 1),
    ItemNames.stage8_4.value: ItemData(ItemNames.stage8_4.value, 94, ItemClassification.progression, 1),

    ItemNames.ex_stage1_1.value: ItemData(ItemNames.ex_stage1_1.value, 95, ItemClassification.progression, 1),
    ItemNames.ex_stage1_2.value: ItemData(ItemNames.ex_stage1_2.value, 96, ItemClassification.progression, 1),
    ItemNames.ex_stage1_3.value: ItemData(ItemNames.ex_stage1_3.value, 97, ItemClassification.progression, 1),
    ItemNames.ex_stage1_4.value: ItemData(ItemNames.ex_stage1_4.value, 98, ItemClassification.progression, 1),
    ItemNames.ex_stage1_5.value: ItemData(ItemNames.ex_stage1_5.value, 99, ItemClassification.progression, 1),
    ItemNames.ex_stage2_1.value: ItemData(ItemNames.ex_stage2_1.value, 100, ItemClassification.progression, 1),
    ItemNames.ex_stage2_2.value: ItemData(ItemNames.ex_stage2_2.value, 101, ItemClassification.progression, 1),
    ItemNames.ex_stage2_3.value: ItemData(ItemNames.ex_stage2_3.value, 102, ItemClassification.progression, 1),
    ItemNames.ex_stage2_4.value: ItemData(ItemNames.ex_stage2_4.value, 103, ItemClassification.progression, 1),
    ItemNames.ex_stage2_5.value: ItemData(ItemNames.ex_stage2_5.value, 104, ItemClassification.progression, 1),
    ItemNames.ex_stage3_1.value: ItemData(ItemNames.ex_stage3_1.value, 105, ItemClassification.progression, 1),
    ItemNames.ex_stage3_2.value: ItemData(ItemNames.ex_stage3_2.value, 106, ItemClassification.progression, 1),
    ItemNames.ex_stage3_3.value: ItemData(ItemNames.ex_stage3_3.value, 107, ItemClassification.progression, 1),
    ItemNames.ex_stage3_4.value: ItemData(ItemNames.ex_stage3_4.value, 108, ItemClassification.progression, 1),
    ItemNames.ex_stage3_5.value: ItemData(ItemNames.ex_stage3_5.value, 109, ItemClassification.progression, 1),
    ItemNames.ex_stage4_1.value: ItemData(ItemNames.ex_stage4_1.value, 110, ItemClassification.progression, 1),
    ItemNames.ex_stage4_2.value: ItemData(ItemNames.ex_stage4_2.value, 111, ItemClassification.progression, 1),
    ItemNames.ex_stage4_3.value: ItemData(ItemNames.ex_stage4_3.value, 112, ItemClassification.progression, 1),
    ItemNames.ex_stage4_4.value: ItemData(ItemNames.ex_stage4_4.value, 113, ItemClassification.progression, 1),
    ItemNames.ex_stage4_5.value: ItemData(ItemNames.ex_stage4_5.value, 114, ItemClassification.progression, 1),
    ItemNames.ex_stage4_6.value: ItemData(ItemNames.ex_stage4_6.value, 115, ItemClassification.progression, 1),
    ItemNames.ex_stage5_1.value: ItemData(ItemNames.ex_stage5_1.value, 116, ItemClassification.progression, 1),
    ItemNames.ex_stage5_2.value: ItemData(ItemNames.ex_stage5_2.value, 117, ItemClassification.progression, 1),
    ItemNames.ex_stage5_3.value: ItemData(ItemNames.ex_stage5_3.value, 118, ItemClassification.progression, 1),
    ItemNames.ex_stage5_4.value: ItemData(ItemNames.ex_stage5_4.value, 119, ItemClassification.progression, 1),
    ItemNames.ex_stage5_5.value: ItemData(ItemNames.ex_stage5_5.value, 120, ItemClassification.progression, 1),
    ItemNames.ex_stage5_6.value: ItemData(ItemNames.ex_stage5_6.value, 121, ItemClassification.progression, 1),
    ItemNames.ex_stage6_1.value: ItemData(ItemNames.ex_stage6_1.value, 122, ItemClassification.progression, 1),
    ItemNames.ex_stage6_2.value: ItemData(ItemNames.ex_stage6_2.value, 123, ItemClassification.progression, 1),
    ItemNames.ex_stage6_3.value: ItemData(ItemNames.ex_stage6_3.value, 124, ItemClassification.progression, 1),
    ItemNames.ex_stage6_4.value: ItemData(ItemNames.ex_stage6_4.value, 125, ItemClassification.progression, 1),
    ItemNames.ex_stage6_5.value: ItemData(ItemNames.ex_stage6_5.value, 126, ItemClassification.progression, 1),
    ItemNames.ex_stage6_6.value: ItemData(ItemNames.ex_stage6_6.value, 127, ItemClassification.progression, 1),
    ItemNames.ex_stage7_1.value: ItemData(ItemNames.ex_stage7_1.value, 128, ItemClassification.progression, 1),
    ItemNames.ex_stage7_2.value: ItemData(ItemNames.ex_stage7_2.value, 129, ItemClassification.progression, 1),
    ItemNames.ex_stage7_3.value: ItemData(ItemNames.ex_stage7_3.value, 130, ItemClassification.progression, 1),
    ItemNames.ex_stage7_4.value: ItemData(ItemNames.ex_stage7_4.value, 131, ItemClassification.progression, 1),
    ItemNames.ex_stage8_4.value: ItemData(ItemNames.ex_stage8_4.value, 132, ItemClassification.progression, 1),

    ItemNames.arena_completion.value: ItemData(ItemNames.arena_completion.value, 133, ItemClassification.progression, 1),
    ItemNames.true_arena_completion.value: ItemData(ItemNames.true_arena_completion.value, 134, ItemClassification.progression, 1),
    
    # trap items
    ItemNames.sleep_trap.value: ItemData(ItemNames.sleep_trap.value, 135, ItemClassification.trap),
    ItemNames.eject_trap.value: ItemData(ItemNames.eject_trap.value, 136, ItemClassification.trap),
    ItemNames.mouthful_trap.value: ItemData(ItemNames.mouthful_trap.value, 137, ItemClassification.trap),
}

def generate_item_pool(world: "KRtDLWorld") -> List[KRtDLItem]:
    # These are items that are only added if certain options are set
    items: List[KRtDLItem] = []

    if world.options.shuffle_energy_spheres:
        #this one generates all 240 spheres
        if world.options.extra_sanity or (world.options.goal == 5 and world.options.energy_sphere_hunt_requirement > 120):
            for i in range(0,120):
                items.append(world.create_item(ItemNames.energy_sphere.value, ItemClassification.progression))
            for i in range(0,120):
                items.append(world.create_item(ItemNames.energy_sphere_ex.value, ItemClassification.progression))
        #this one generates just extra game spheres
        else:
            for i in range(0,120):
                items.append(world.create_item(ItemNames.energy_sphere.value, ItemClassification.progression))

    if world.options.shuffle_part_spheres:
        if world.options.extra_sanity:
            items.append(world.create_item(ItemNames.lor_oars.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_rwing.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_lwing.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_emblem.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_mast.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_oars_ex.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_rwing_ex.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_lwing_ex.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_emblem_ex.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_mast_ex.value, ItemClassification.progression))
        else:
            items.append(world.create_item(ItemNames.lor_oars.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_rwing.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_lwing.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_emblem.value, ItemClassification.progression))
            items.append(world.create_item(ItemNames.lor_mast.value, ItemClassification.progression))

    if world.options.star_sanity:
        if world.options.extra_sanity: #Another Dimension variance in Gold Stars between Normal and EX
            for i in range(0,2936):
                items.append(world.create_item(ItemNames.gold_star.value, ItemClassification.filler))
            for i in range(0,41):
                items.append(world.create_item(ItemNames.gold_star.value, ItemClassification.filler))
        else:
            if world.options.start_in_extra_game:
                for i in range(0,15):
                    items.append(world.create_item(ItemNames.gold_star.value, ItemClassification.filler))
            else:
                for i in range(0,26):
                    items.append(world.create_item(ItemNames.gold_star.value, ItemClassification.filler))
        for i in range(0,2936):
            items.append(world.create_item(ItemNames.gold_star.value, ItemClassification.filler))

    if world.options.red_star_sanity:
        if world.options.extra_sanity: #combined normal and EX red stars in Another Dimension
            for i in range(0,240):
                items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
            if world.options.hard_logic: #Red Star #12 in 7-2 oooooooh I hate Red Star #12 in 7-2
                for i in range(0,2):
                    items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
            for i in range(0,4):
                items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
        else:
            if world.options.hard_logic: #Red Star #12 in 7-2 oooooooh I hate Red Star #12 in 7-2
                items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
            if world.options.start_in_extra_game: #the three red stars in Another Dimension in EX
                for i in range(0,3):
                    items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
            else: #the one red star in Another Dimension in normal
                items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
        for i in range(0,240):
            items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))

    if world.options.blue_star_sanity:
        if world.options.extra_sanity:
            for i in range(0,36):
                items.append(world.create_item(ItemNames.blue_star.value, ItemClassification.filler))
        for i in range(0,36):
            items.append(world.create_item(ItemNames.blue_star.value, ItemClassification.filler))

    if world.options.food_sanity:
        if world.options.extra_sanity:
            for i in range(0,389):
                items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
            if world.options.shuffle_arena:
                for i in range(0,8):
                    items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
            for i in range(0,12):
                items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
        else:
            if world.options.start_in_extra_game:
                if world.options.shuffle_arena:
                    for i in range(0,3):
                        items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
                for i in range(0,7):
                    items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
            else:
                if world.options.shuffle_arena:
                    for i in range(0,5):
                        items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
                for i in range(0,5):
                    items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
        for i in range(0,389):
            items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))

    #todo: make it generate Gold Stars or Food at a ratio of 8/2
    if world.options.flower_sanity:
        if world.options.extra_sanity:
            for i in range(0,306):
                items.append(world.create_item(ItemNames.flower.value, ItemClassification.filler))
        for i in range(0,306):
            items.append(world.create_item(ItemNames.flower.value, ItemClassification.filler))

    if world.options.one_up_sanity:
        if world.options.extra_sanity:
            for i in range(0,45):
                items.append(world.create_item(ItemNames.one_up.value, ItemClassification.useful))
            for i in range(0,2):
                items.append(world.create_item(ItemNames.one_up.value, ItemClassification.useful))
        else:
            items.append(world.create_item(ItemNames.one_up.value, ItemClassification.useful))
        for i in range(0,45):
            items.append(world.create_item(ItemNames.one_up.value, ItemClassification.useful))

    if world.options.maxim_sanity:
        if world.options.extra_sanity:
            for i in range(0,51):
                items.append(world.create_item(ItemNames.m_tomato.value, ItemClassification.useful))
        if world.options.shuffle_arena:
            if world.options.extra_sanity:
                for i in range(0,8):
                    items.append(world.create_item(ItemNames.m_tomato.value, ItemClassification.useful))
            else:
                if world.options.start_in_extra_game:
                    for i in range(0,3):
                        items.append(world.create_item(ItemNames.m_tomato.value, ItemClassification.useful))
                else:
                    for i in range(0,5):
                        items.append(world.create_item(ItemNames.m_tomato.value, ItemClassification.useful))
        for i in range(0,51):
            items.append(world.create_item(ItemNames.m_tomato.value, ItemClassification.useful))

    if world.options.shuffle_subgames:
        for i in range(0,6):
            items.append(world.create_item(ItemNames.red_star.value, ItemClassification.filler))
    
    if world.options.shuffle_arena:
        if world.options.extra_sanity:
            for i in range(0,26):
                items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
        elif world.options.start_in_extra_game:
            for i in range(0,14):
                items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))
        else:
            for i in range(0,12):
                items.append(world.create_item(ItemNames.food_pickup.value, ItemClassification.useful))

    return items
