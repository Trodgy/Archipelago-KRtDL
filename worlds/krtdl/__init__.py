import Utils
import os
import settings
import struct
import zipfile
import typing
import json
import logging
from logging import info
from typing import TYPE_CHECKING, Any, Dict, List, Optional, ClassVar, cast
from collections.abc import Mapping
from pathlib import Path
from .GameNames import ItemNames
from .Items import KRtDLItem, item_table, generate_item_pool
from .Locations import KRtDLLocation, composite_location, create_all_regions, create_regular_locations, gold_star_table, get_stage_complete_location_names_with_ids, stage_completion_table
from .Options import KRtDLOptions, krtdl_option_groups
from .Logic import InitiateRules
from worlds.AutoWorld import World, WebWorld
from worlds.Files import APPlayerContainer
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, icon_paths, components, launch_subprocess
from BaseClasses import MultiWorld, Region, Location, Entrance, Item, Tutorial, ItemClassification
from Utils import local_path

BaseID = 24102011

if TYPE_CHECKING:
    from ppc_asm.assembler.ppc import GeneralRegister  # type: ignore

class MultiworldWithPassthrough(MultiWorld):
    re_gen_passthrough: Dict[str, Dict[str, Any]] = {}

def run_client(url: Optional[str] = None):
    from .KRtDLClient import launch
    launch_subprocess(launch, name="KRtDLClient")

components.append(
    Component("Kirby's Return to Dream Land Client", func=run_client, component_type=Type.CLIENT, icon='krtdlicon',
              file_identifier=SuffixIdentifier(".apkrtdl"))
)

icon_paths['krtdlicon'] = f"ap:{__name__}/krtdlicon.png"

class KRtDLSettings(settings.Group):
    class DolphinToolPath(settings.UserFilePath):
        """
        This determines a file path for where DolphinTool.exe is. It is necessary for the patching process.
        It should be in the same folder Dolphin.exe is.
        """
    dolphin_tool_path: DolphinToolPath = DolphinToolPath(Path.home())

    class GamePath(settings.UserFilePath):
        """
        This determines a file path for where your copy of Kirby's Return to Dream Land is.
        It must be the US version in one of the following formats:
        .iso 
        .wbfs
        .rvz
        """
    game_path: GamePath = GamePath(Path.home())

    #class PatchOutputPath(settings.UserFilePath):
        #"""
        #This determines the directory where patch outputs will be put.
        #"""
    #patch_output_path: PatchOutputPath = PatchOutputPath(Path.home())

class KRtDLWeb(WebWorld):
    theme = "grassFlowers"
    rich_text_options_doc = True
    option_groups = krtdl_option_groups
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Kirby's Return to Dream Land for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Trodgy"]
    )]

class KRtDLContainer(APPlayerContainer):
    game: str = "Kirby's Return to Dream Land"
    patch_file_ending = ".apkrtdl"

    def __init__(
        self, 
        config_json: str, 
        #options_json: str, 
        outfile_name: str, 
        output_directory: str,
        player: Optional[int] = None, 
        player_name: str = "", 
        server: str = ""):
            
        self.config_json = config_json
        self.config_path = "config.json"
        #self.options_path = "options.json"
        #self.options_json = options_json

        logging.info(msg = outfile_name + ".apkrtdl")
            
        container_path = os.path.join(output_directory, outfile_name + ".apkrtdl")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr(self.config_path, self.config_json)
        #opened_zipfile.writestr(self.options_path, self.options_json)
        super().write_contents(opened_zipfile)

class KRtDLWorld(World):
    """
    Also known as Kirby's Adventure Wii in PAL regions.
    
    The tough puff Kirby is back for a 1-4 player platforming adventure across Planet Popstar. 
    Help the mysterious far-flung traveler Magolor rebuild his ship and return to his home planet of Halcandra.
    """

    game = "Kirby's Return to Dream Land"
    web = KRtDLWeb()
    required_client_version = (0, 0, 0)
    options_dataclass = KRtDLOptions
    options: KRtDLOptions
    topology_present = True
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = composite_location
    prefilled_item_map: Dict[str, str] = {}  # Dict of location name to item name
    origin_region_name = "Menu"
    settings_key = "krtdl_settings"
    settings: ClassVar[KRtDLSettings]

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        if hasattr(self.multiworld, "re_gen_passthrough"):
            self.init_tracker_data()
            
        # Select Start Room
       # init_starting_room_data(self)

        # Randomize Door Colors
        #if (
        #    self.options.door_color_randomization != DoorColorRandomization.option_none
        #    and not self.door_color_mapping
        #):
        #    self.door_color_mapping = get_world_door_mapping(self)

        #init_starting_beam(self)

        # Reconcile starting beam with door color mapping, if applicable
        #remap_doors_to_power_beam_if_necessary(self)

        # Set starting loadout
        #init_starting_loadout(self)

        # Randomize Blast Shields
        #if (
        #    self.options.blast_shield_randomization.value
        #    != BlastShieldRandomization.option_none
        #    or self.options.locked_door_count > 0
        #) and not self.blast_shield_mapping:
        #    self.blast_shield_mapping = get_world_blast_shield_mapping(self)

        #if self.blast_shield_mapping:
        #    apply_blast_shield_mapping(self)

        # Randomize Elevators
        #if self.options.elevator_randomization:
        #    if not len(self.elevator_mapping):
        #       self.elevator_mapping = get_random_elevator_mapping(self)
        #else:
        #    self.elevator_mapping = default_elevator_mappings

        # Init starting inventory
        #starting_items = generate_base_start_inventory(self)
        #option_filled_items = [
        #    *[item for item in self.options.start_inventory.value.keys()],
        #    *[item for item in self.options.start_inventory_from_pool.value.keys()],
        #]

        #for item in [item for item in starting_items if item not in option_filled_items]:
            #self.multiworld.push_precollected(self.create_item(item, ItemClassification.progression))

    def create_regions(self) -> None:
        #print("test")
        create_all_regions(self)
        create_regular_locations(self)

    def set_rules(self) -> None:
        InitiateRules(self)
    
    def create_item(self, name: str, override: Optional[ItemClassification] = None) -> "KRtDLItem":
        createdthing = item_table[name]

        if hasattr(self.multiworld, "generation_is_fake"):
            # All items should be progression for the Universal Tracker
            override = ItemClassification.progression
        if override:
            return KRtDLItem(name, override, createdthing.code, self.player)
        return KRtDLItem(name, createdthing.classification, createdthing.code, self.player)

    def create_items(self) -> None:
        precollected_item_names = [
            item.name for item in self.multiworld.precollected_items[self.player]
        ]
        new_map: Dict[str, str] = {}

        for location, item in self.prefilled_item_map.items():
            if item not in precollected_item_names:
                # Prefilled items affect what goes into the item pool. If we already have collected something, we won't need to prefill it
                new_map[location] = item
        
        #temp code for now, make a prettier solution later
        new_map[ItemNames.stage1_1.value] = ItemNames.stage1_1.value
        new_map[ItemNames.stage1_2.value] = ItemNames.stage1_2.value
        new_map[ItemNames.stage1_3.value] = ItemNames.stage1_3.value
        new_map[ItemNames.stage1_4.value] = ItemNames.stage1_4.value
        new_map[ItemNames.stage1_5.value] = ItemNames.stage1_5.value
        new_map[ItemNames.stage2_1.value] = ItemNames.stage2_1.value
        new_map[ItemNames.stage2_2.value] = ItemNames.stage2_2.value
        new_map[ItemNames.stage2_3.value] = ItemNames.stage2_3.value
        new_map[ItemNames.stage2_4.value] = ItemNames.stage2_4.value
        new_map[ItemNames.stage2_5.value] = ItemNames.stage2_5.value
        new_map[ItemNames.stage3_1.value] = ItemNames.stage3_1.value
        new_map[ItemNames.stage3_2.value] = ItemNames.stage3_2.value
        new_map[ItemNames.stage3_3.value] = ItemNames.stage3_3.value
        new_map[ItemNames.stage3_4.value] = ItemNames.stage3_4.value
        new_map[ItemNames.stage3_5.value] = ItemNames.stage3_5.value
        new_map[ItemNames.stage4_1.value] = ItemNames.stage4_1.value
        new_map[ItemNames.stage4_2.value] = ItemNames.stage4_2.value
        new_map[ItemNames.stage4_3.value] = ItemNames.stage4_3.value
        new_map[ItemNames.stage4_4.value] = ItemNames.stage4_4.value
        new_map[ItemNames.stage4_5.value] = ItemNames.stage4_5.value
        new_map[ItemNames.stage4_6.value] = ItemNames.stage4_6.value
        new_map[ItemNames.stage5_1.value] = ItemNames.stage5_1.value
        new_map[ItemNames.stage5_2.value] = ItemNames.stage5_2.value
        new_map[ItemNames.stage5_3.value] = ItemNames.stage5_3.value
        new_map[ItemNames.stage5_4.value] = ItemNames.stage5_4.value
        new_map[ItemNames.stage5_5.value] = ItemNames.stage5_5.value
        new_map[ItemNames.stage5_6.value] = ItemNames.stage5_6.value
        new_map[ItemNames.stage6_1.value] = ItemNames.stage6_1.value
        new_map[ItemNames.stage6_2.value] = ItemNames.stage6_2.value
        new_map[ItemNames.stage6_3.value] = ItemNames.stage6_3.value
        new_map[ItemNames.stage6_4.value] = ItemNames.stage6_4.value
        new_map[ItemNames.stage6_5.value] = ItemNames.stage6_5.value
        new_map[ItemNames.stage6_6.value] = ItemNames.stage6_6.value
        new_map[ItemNames.stage7_1.value] = ItemNames.stage7_1.value
        new_map[ItemNames.stage7_2.value] = ItemNames.stage7_2.value
        new_map[ItemNames.stage7_3.value] = ItemNames.stage7_3.value
        new_map[ItemNames.stage7_4.value] = ItemNames.stage7_4.value
        new_map[ItemNames.stage8_4.value] = ItemNames.stage8_4.value

        if self.options.goal == 3 or (self.options.shuffle_arena and (self.options.extra_sanity or not self.options.start_in_extra_game)):
            new_map[ItemNames.arena_completion.value] = ItemNames.arena_completion.value
        if self.options.goal == 4 or (self.options.shuffle_arena and (self.options.extra_sanity or self.options.start_in_extra_game)):
            new_map[ItemNames.true_arena_completion.value] = ItemNames.true_arena_completion.value

        if self.options.extra_sanity:
            new_map[ItemNames.ex_stage1_1.value] = ItemNames.ex_stage1_1.value
            new_map[ItemNames.ex_stage1_2.value] = ItemNames.ex_stage1_2.value
            new_map[ItemNames.ex_stage1_3.value] = ItemNames.ex_stage1_3.value
            new_map[ItemNames.ex_stage1_4.value] = ItemNames.ex_stage1_4.value
            new_map[ItemNames.ex_stage1_5.value] = ItemNames.ex_stage1_5.value
            new_map[ItemNames.ex_stage2_1.value] = ItemNames.ex_stage2_1.value
            new_map[ItemNames.ex_stage2_2.value] = ItemNames.ex_stage2_2.value
            new_map[ItemNames.ex_stage2_3.value] = ItemNames.ex_stage2_3.value
            new_map[ItemNames.ex_stage2_4.value] = ItemNames.ex_stage2_4.value
            new_map[ItemNames.ex_stage2_5.value] = ItemNames.ex_stage2_5.value
            new_map[ItemNames.ex_stage3_1.value] = ItemNames.ex_stage3_1.value
            new_map[ItemNames.ex_stage3_2.value] = ItemNames.ex_stage3_2.value
            new_map[ItemNames.ex_stage3_3.value] = ItemNames.ex_stage3_3.value
            new_map[ItemNames.ex_stage3_4.value] = ItemNames.ex_stage3_4.value
            new_map[ItemNames.ex_stage3_5.value] = ItemNames.ex_stage3_5.value
            new_map[ItemNames.ex_stage4_1.value] = ItemNames.ex_stage4_1.value
            new_map[ItemNames.ex_stage4_2.value] = ItemNames.ex_stage4_2.value
            new_map[ItemNames.ex_stage4_3.value] = ItemNames.ex_stage4_3.value
            new_map[ItemNames.ex_stage4_4.value] = ItemNames.ex_stage4_4.value
            new_map[ItemNames.ex_stage4_5.value] = ItemNames.ex_stage4_5.value
            new_map[ItemNames.ex_stage4_6.value] = ItemNames.ex_stage4_6.value
            new_map[ItemNames.ex_stage5_1.value] = ItemNames.ex_stage5_1.value
            new_map[ItemNames.ex_stage5_2.value] = ItemNames.ex_stage5_2.value
            new_map[ItemNames.ex_stage5_3.value] = ItemNames.ex_stage5_3.value
            new_map[ItemNames.ex_stage5_4.value] = ItemNames.ex_stage5_4.value
            new_map[ItemNames.ex_stage5_5.value] = ItemNames.ex_stage5_5.value
            new_map[ItemNames.ex_stage5_6.value] = ItemNames.ex_stage5_6.value
            new_map[ItemNames.ex_stage6_1.value] = ItemNames.ex_stage6_1.value
            new_map[ItemNames.ex_stage6_2.value] = ItemNames.ex_stage6_2.value
            new_map[ItemNames.ex_stage6_3.value] = ItemNames.ex_stage6_3.value
            new_map[ItemNames.ex_stage6_4.value] = ItemNames.ex_stage6_4.value
            new_map[ItemNames.ex_stage6_5.value] = ItemNames.ex_stage6_5.value
            new_map[ItemNames.ex_stage6_6.value] = ItemNames.ex_stage6_6.value
            new_map[ItemNames.ex_stage7_1.value] = ItemNames.ex_stage7_1.value
            new_map[ItemNames.ex_stage7_2.value] = ItemNames.ex_stage7_2.value
            new_map[ItemNames.ex_stage7_3.value] = ItemNames.ex_stage7_3.value
            new_map[ItemNames.ex_stage7_4.value] = ItemNames.ex_stage7_4.value
            new_map[ItemNames.ex_stage8_4.value] = ItemNames.ex_stage8_4.value
        
        self.prefilled_item_map = new_map

        item_pool = generate_item_pool(self)
        self.multiworld.itempool += item_pool

    def pre_fill(self) -> None:
        for location_name, item_name in self.prefilled_item_map.items():
            self.multiworld.get_location(location_name, self.player).place_locked_item(self.create_item(item_name))
    
    def generate_output(self, output_directory: str) -> None:
        config: Dict[str, Union[int, str]] = {
            "seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "slot": self.multiworld.player_name[self.player],  # to connect to server
            "items": {location.name if "#" in location.name else location.name + " #1": 
                      location.item.name if location.item.player == self.player else "Remote" 
                      for location in self.multiworld.get_filled_locations(self.player)},
            # store start_inventory from player's .yaml
            # make sure to mark as not remote_start_inventory when connecting if stored in rom/mod
            "starter_items": [item.name for item in self.multiworld.precollected_items[self.player]],
        }
        configjsons = json.dumps(config, indent=4)

        #"inputIso": "Kirby's Return to Dream Land (USA) (En,Fr,Es).rvz",
        #"outputIso": "KRtDLArchipelagoPatch.rvz",
        
        #logging.info(msg = data)
        
        # Check if the environment variable 'DEBUG' is set to 'True'
        #if os.environ.get('DEBUG') == 'True':
        #    with open("test_config.json", "w") as f:
        #        f.write(configjsons)

        #options_dict: Dict[str, Union[int, str]] = {
            #"progressive_beam_upgrades": self.options.progressive_beam_upgrades.value,
            #"player_name": self.player_name,
        #}
        #options_json = json.dumps(options_dict, indent=4)
        outfile_name = self.multiworld.get_out_file_name_base(self.player)
        
        #krtdl = KRtDLContainer(configjsons, options_json, outfile_name, output_directory, player=self.player, player_name=self.player_name)
        outputfile = KRtDLContainer(configjsons, outfile_name, output_directory, player=self.player, player_name=self.player_name)
        outputfile.write()

    #def fill_slot_data(self) -> Mapping[str, Any]:
        #print("test")
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        #return self.options.as_dict(
        #    "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
        #)
