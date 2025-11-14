from .GameNames import ItemNames
from BaseClasses import Item, ItemClassification

BaseID = 24102011

class KRtDLItems(Item):
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

    # trap items
    ItemNames.sleep_trap.value: ItemData(ItemNames.sleep_trap.value, 57, ItemClassification.trap),
    ItemNames.eject_trap.value: ItemData(ItemNames.eject_trap.value, 58, ItemClassification.trap),
    ItemNames.mouthful_trap.value: ItemData(ItemNames.mouthful_trap.value, 59, ItemClassification.trap),
}
