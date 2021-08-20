from enum import Enum
from os import path

import pygame

from core.assets.asset import Asset
from settings import GAMEDIR


class Assets(Enum):
	# Column 0
	EMPTY = Asset("Empty", "empty", 0)
	TREE_0 = Asset("Tree 0", "tree_0", 1)
	FERN = Asset("Fern", "fern", 2)
	FENCE_RED_LOW = Asset("Low red fence", "fence_red_low", 3)
	FENCE_WHITE_LOW = Asset("Low white fence", "fence_white_low", 4)
	RAILS_01000100 = Asset("Rails", "rails_01000100", 5)
	METAL_CONSTRUCTION_0 = Asset("Metal construction", "metal_construction_0", 6)
	SIGN_0 = Asset("Sign", "sign_0", 7)

	DOOR_BLUE_LOCKED = Asset("Locked blue door", "door_blue_locked", 9)
	LOCK_BLUE_LOCKED = Asset("Lock blue locked", "lock_blue_locked", 10)
	BUTTON_BLUE_LOCKED = Asset("Button blue locked", "button_blue_locked", 11)
	CHIMNEY = Asset("Chimney", "chimney", 12)
	BRICK_WHITE = Asset("Brick white", "brick_white", 13)
	GRAVESTONE_0 = Asset("Gravestone 0", "gravestone_0", 14)
	SKULL_HUMAN = Asset("Skull human", "skull_human", 15)
	ROOF_PART_00011100 = Asset("Roof part 00011100", "roof_part_00011100", 16)
	ROOF_PART_01111100 = Asset("Roof part 01111100", "roof_part_01111100", 17)
	ROOF_PART_01110000 = Asset("Roof part 01110000", "roof_part_01110000", 18)
	HOUSE_RED_0 = Asset("House red 0", "house_red_0", 19)
	HOUSE_RED_2 = Asset("House red 2", "house_red_2", 20)
	HOUSE_WHITE_0 = Asset("House white 0", "house_white_0", 21)
	# Column 1
	PATH_STONE_0 = Asset("Path stone 0", "path_stone_0", 22)
	TREE_1 = Asset("Tree 1", "tree_1", 23)
	PLANT_0 = Asset("Plant 0", "plant_0", 24)
	FENCE = Asset("Fence", "fence", 25)
	FENCE_WHITE_1 = Asset("Fence white 1", "fence_white_1", 26)
	RAILS_WHITE_00010100 = Asset("Rails white 00010100", "rails_white_00010100", 27)
	METAL_CONSTRUCTION_1 = Asset("Metal construction 1", "metal_construction_1", 28)
	SIGN_1 = Asset("Sign 1", "sign_1", 29)
	CART_RED_0 = Asset("Cart red 0", "cart_red_0", 30)
	DOOR_BLUE_FADING = Asset("Door blue fading", "door_blue_fading", 31)
	PLATE_BLUE_UP = Asset("Plate blue up", "plate_blue_up", 32)
	STAIRS_BRICK = Asset("Stairs brick", "stairs_brick", 33)
	ROOF_WHITE = Asset("Roof white", "roof_white", 34)
	WALL_WINDOW_BARRED = Asset("Wall window barred", "wall_window_barred", 35)
	GRAVESTONE_1 = Asset("Gravestone 1", "gravestone_1", 36)
	SKULL_ANIMAL = Asset("Skull animal", "skull_animal", 37)
	ROOF_PART_00011111 = Asset("Roof part 00011111", "roof_part_00011111", 38)
	ROOF_PART_11111111 = Asset("Roof part 11111111", "roof_part_11111111", 39)
	ROOF_PART_11110001 = Asset("Roof part 11110001", "roof_part_11110001", 40)
	HOUSE_RED_1 = Asset("House red 1", "house_red_1", 41)
	HOUSE_RED_3 = Asset("House red 3", "house_red_3", 42)
	HOUSE_WHITE_1 = Asset("House white 1", "house_white_1", 43)
	# Column 2
	PATH_STONE_1 = Asset("Path stone 1", "path_stone_1", 44)
	TREE_2 = Asset("Tree 2", "tree_2", 45)
	PLANT_1 = Asset("Plant 1", "plant_1", 46)
	FENCE_HIGH = Asset("Fence high", "fence_high", 47)
	FENCE_WHITE_BROKEN = Asset("Fence white broken", "fence_white_broken", 48)
	RAILS_WHITE_01010100 = Asset("Rails white 01010100", "rails_white_01010100", 49)
	STAIRS_RED_0 = Asset("Stairs red 0", "stairs_red_0", 50)
	MAIL_BOX = Asset("Mail box", "mail_box", 51)
	CART_RED_1 = Asset("Cart red 1", "cart_red_1", 52)
	DOOR_BLUE_OPEN = Asset("Door blue open", "door_blue_open", 53)
	PLATE_BLUE_DOWN = Asset("Plate blue down", "plate_blue_down", 54)
	BRICK_HALF = Asset("Brick half", "brick_half", 55)
	ROOF_TOP_DOWN = Asset("Roof top down", "roof_top_down", 56)
	WALL_WINDOW = Asset("Wall window", "wall_window", 57)
	GRAVESTONE_2 = Asset("Gravestone 2", "gravestone_2", 58)
	WEB = Asset("Web", "web", 59)
	ROOF_PART_00000111 = Asset("Roof part 00000111", "roof_part_00000111", 60)
	ROOF_PART_11000111 = Asset("Roof part 11000111", "roof_part_11000111", 61)
	ROOF_PART_11000001 = Asset("Roof part 11000001", "roof_part_11000001", 62)
	CASTLE_0 = Asset("Castle 0", "castle_0", 63)
	PYRAMID = Asset("Pyramid", "pyramid", 64)
	HOUSE_WHITE_2 = Asset("House white 2", "house_white_2", 65)
	# Column 3
	PATH_STONE_2 = Asset("Path stone 2", "path_stone_2", 66)
	FOREST_0 = Asset("Forest 0", "forest_0", 67)
	FOREST_1 = Asset("Forest 1", "forest_1", 68)
	FENCE_RED_GATE = Asset("Fence red gate", "fence_red_gate", 69)
	FENCE_WHITE_GATE = Asset("Fence white gate", "fence_white_gate", 70)
	RAILS_1111 = Asset("Rails 1111", "rails_1111", 71)
	STAIRS_RED_1 = Asset("Stairs red 1", "stairs_red_1", 72)
	BOOKSHELF = Asset("Bookshelf", "bookshelf", 73)
	CART_HALF = Asset("Cart half", "cart_half", 74)
	DOOR_RED_0 = Asset("Door red 0", "door_red_0", 75)
	LEVER_LEFT = Asset("Lever left", "lever_left", 76)
	PILLAR_TOP = Asset("Pillar top", "pillar_top", 77)
	PILLAR_MID = Asset("Pillar mid", "pillar_mid", 78)
	PILLAR_BOTTOM = Asset("Pillar bottom", "pillar_bottom", 79)
	BARS_FLOOR = Asset("Bars floor", "bars_floor", 80)
	CANDLE_RED = Asset("Candle red", "candle_red", 81)
	ROOF_POINT_0110 = Asset("Roof point 0110", "roof_point_0110", 82)
	ROOF_POINT_1100 = Asset("Roof point 1100", "roof_point_1100", 83)
	ROOF_POINT_0 = Asset("Roof point 0", "roof_point_0", 84)
	CASTLE_WHITE_1 = Asset("Castle white 1", "castle_white_1", 85)
	SCHOOL = Asset("School", "school", 86)
	APARTMENT_0 = Asset("Apartment 0", "apartment_0", 87)
	# Column 4
	PATH_STONE_3 = Asset("Path stone 3", "path_stone_3", 88)
	TREE_3 = Asset("Tree 3", "tree_3", 89)
	TREE_4 = Asset("Tree 4", "tree_4", 90)
	FENCE_RED_GATE_OPEN = Asset("Fence red gate open", "fence_red_gate_open", 91)
	FENCE_WHITE_GATE_OPEN = Asset("Fence white gate open", "fence_white_gate_open", 92)
	RAILS_WHITE_BROKEN = Asset("Rails white broken", "rails_white_broken", 93)
	STAIRS_RED_2 = Asset("Stairs red 2", "stairs_red_2", 94)
	BOOKSHELF_SKULL = Asset("Bookshelf skull", "bookshelf_skull", 95)
	CART_RED_MID = Asset("Cart red mid", "cart_red_mid", 96)
	DOOR_RED_1 = Asset("Door red 1", "door_red_1", 97)
	LEVER_RIGHT = Asset("Lever right", "lever_right", 98)
	BARS_BLUE_LOCKED = Asset("Bars blue locked", "bars_blue_locked", 99)
	COFFIN = Asset("Coffin", "coffin", 100)
	BRICK_OPEN = Asset("Brick open", "brick_open", 101)
	FIREPLACE = Asset("Fireplace", "fireplace", 102)
	TORCH_YELLOW = Asset("Torch yellow", "torch_yellow", 103)
	ROOF_POINT_0011 = Asset("Roof point 0011", "roof_point_0011", 104)
	ROOF_POINT_1001 = Asset("Roof point 1001", "roof_point_1001", 105)
	ROOF_POINT_1 = Asset("Roof point 1", "roof_point_1", 106)
	CASTLE_WHITE_2 = Asset("Castle white 2", "castle_white_2", 107)
	HOUSE_WHITE_3 = Asset("House white 3", "house_white_3", 108)
	APARTMENT_1 = Asset("Apartment 1", "apartment_1", 109)
	# Column 5
	GRASS_0 = Asset("Grass 0", "grass_0", 110)
	TREE_5 = Asset("Tree 5", "tree_5", 111)
	STONES = Asset("Stones", "stones", 112)
	FENCE_WHITE_BARRED = Asset("Fence white barred", "fence_white_barred", 113)
	FENCE_WHITE_BARRED_GATE = Asset("Fence white barred gate", "fence_white_barred_gate", 114)
	FENCE_WHITE_BARRED_GROUND = Asset("Fence white barred ground", "fence_white_barred_ground", 115)
	SHELF_WITH_BOOKS = Asset("Shelf with books", "shelf_with_books", 116)
	CABINET_RED_0 = Asset("Cabinet red 0", "cabinet_red_0", 117)
	BED_RED = Asset("Bed red", "bed_red", 118)
	DOOR_RED_2 = Asset("Door red 2", "door_red_2", 119)
	DOOR_WHITE_0 = Asset("Door white 0", "door_white_0", 120)
	ROOF_RED_0 = Asset("Roof red 0", "roof_red_0", 121)
	ROOF_RED_LEFT = Asset("Roof red left", "roof_red_left", 122)
	ROOF_RED_TOP_0 = Asset("Roof red top 0", "roof_red_top_0", 123)
	CAULDRON = Asset("Cauldron", "cauldron", 124)
	CANDLES_YELLOW = Asset("Candles yellow", "candles_yellow", 125)
	WALL_FIREPLACE_0 = Asset("Wall fireplace 0", "wall_fireplace_0", 126)
	WALL_FIREPLACE_1 = Asset("Wall fireplace 1", "wall_fireplace_1", 127)
	WALL_FIREPLACE_2 = Asset("Wall fireplace 2", "wall_fireplace_2", 128)
	CASTLE_WHITE_3 = Asset("Castle white 3", "castle_white_3", 129)
	HOUSE_WHITE_4 = Asset("House white 4", "house_white_4", 130)
	APARTMENT_2 = Asset("Apartment 2", "apartment_2", 131)
	# Column 6
	GRASS_1 = Asset("Grass 1", "grass_1", 132)
	CACTUS = Asset("Cactus", "cactus", 133)
	BUSH = Asset("Bush", "bush", 134)
	FENCE_WHITE_BARRED_BROKEN = Asset("Fence white barred broken", "fence_white_barred_broken", 135)
	BRIDGE_WHITE_0 = Asset("Bridge white 0", "bridge_white_0", 136)
	BRIDGE_RED_0 = Asset("Bridge red 0", "bridge_red_0", 137)
	PILLARS_RED = Asset("Pillars red", "pillars_red", 138)
	CABINET_RED_1 = Asset("Cabinet red 1", "cabinet_red_1", 139)
	BED_RED_LEFT = Asset("Bed red left", "bed_red_left", 140)
	DOOR_RED_3 = Asset("Door red 3", "door_red_3", 141)
	DOOR_WHITE_1 = Asset("Door white 1", "door_white_1", 142)
	ROOF_RED_1 = Asset("Roof red 1", "roof_red_1", 143)
	ROOF_RED_TOP = Asset("Roof red top", "roof_red_top", 144)
	WALL_RED_0 = Asset("Wall red 0", "wall_red_0", 145)
	WALL_RED_TOP_0 = Asset("Wall red top 0", "wall_red_top_0", 146)
	WALL_RED_BROKEN = Asset("Wall red broken", "wall_red_broken", 147)
	WALL_DOOR_0 = Asset("Wall door 0", "wall_door_0", 148)
	WALL_DOOR_1 = Asset("Wall door 1", "wall_door_1", 149)
	WALL_DOOR_2 = Asset("Wall door 2", "wall_door_2", 150)
	CASTLE_WHITE_4 = Asset("Castle white 4", "castle_white_4", 151)
	TENT_WHITE = Asset("Tent white", "tent_white", 152)
	APARTMENT_3 = Asset("Apartment 3", "apartment_3", 153)
	# Column 7
	GRASS_3 = Asset("Grass 3", "grass_3", 154)
	CACTI = Asset("Cacti", "cacti", 155)
	PALM_TREE = Asset("Palm tree", "palm_tree", 156)
	METAL_BAR_10000011 = Asset("Metal bar 10000011", "metal_bar_10000011", 157)
	BRIDGE_WHITE_1 = Asset("Bridge white 1", "bridge_white_1", 158)
	BRIDGE_RED_1 = Asset("Bridge red 1", "bridge_red_1", 159)
	HOLE = Asset("Hole", "hole", 160)
	CABINET_RED_2 = Asset("Cabinet red 2", "cabinet_red_2", 161)
	BED_RED_RIGHT = Asset("Bed red right", "bed_red_right", 162)
	DOOR_RED_4 = Asset("Door red 4", "door_red_4", 163)
	DOOR_WHITE_2 = Asset("Door white 2", "door_white_2", 164)
	ROOF_RED_2 = Asset("Roof red 2", "roof_red_2", 165)
	ROOF_RED_RIGHT = Asset("Roof red right", "roof_red_right", 166)
	ROOF_RED_TOP_1 = Asset("Roof red top 1", "roof_red_top_1", 167)
	WALL_RED_TOP_1 = Asset("Wall red top 1", "wall_red_top_1", 168)
	WALL_RED_1 = Asset("Wall red 1", "wall_red_1", 169)
	WHITE_WALL_PART_1011 = Asset("White wall part 1011", "white_wall_part_1011", 170)
	WHITE_WALL_PART_1111 = Asset("White wall part 1111", "white_wall_part_1111", 171)
	WHITE_WALL_THICK = Asset("White wall thick", "white_wall_thick", 172)
	CASTLE_WHITE_5 = Asset("Castle white 5", "castle_white_5", 173)
	TENT_RED = Asset("Tent red", "tent_red", 174)
	APARTMENT_4 = Asset("Apartment 4", "apartment_4", 175)
	# Column 8
	# path_{type}_{upleft}{up}{upright}{right}{bottomright}{bottom}{bottomleft}{left}
	PATH_ROAD_01000100 = Asset("Path road 01000100", "path_road_01000100", 176)
	PATH_DIRT_01000100 = Asset("Path dirt 01000100", "path_dirt_01000100", 177)
	PATH_RAILED_01000100 = Asset("Path railed 01000100", "path_railed_01000100", 178)
	METAL_BAR_11100011 = Asset("Metal bar 11100011", "metal_bar_11100011", 179)
	# water_{upleft}{up}{upright}{right}{bottomright}{bottom}{bottomleft}{left}
	WATER_01000100 = Asset("Water 01000100", "water_01000100", 180)
	WATER_11111111 = Asset("Water 11111111", "water_11111111", 181)
	CHEST_RED_0 = Asset("Chest red 0", "chest_red_0", 182)
	CABINET_RED_3 = Asset("Cabinet red 3", "cabinet_red_3", 183)
	CHIMNEY_WHITE_FUME = Asset("Chimney white fume", "chimney_white_fume", 184)
	DOOR_RED_5 = Asset("Door red 5", "door_red_5", 185)
	DOOR_WHITE_3 = Asset("Door white 3", "door_white_3", 186)
	DOOR_WHITE_7 = Asset("Door white 7", "door_white_7", 187)
	PIPE_RED_0 = Asset("Pipe red 0", "pipe_red_0", 188)
	PILLAR_WHITE_0 = Asset("Pillar white 0", "pillar_white_0", 189)
	CABINET_WHITE_0 = Asset("Cabinet white 0", "cabinet_white_0", 190)
	WALL_WHITE_OPEN_0 = Asset("Wall white open 0", "wall_white_open_0", 191)
	WALL_WHITE_PART_1010 = Asset("Wall white part 1010", "wall_white_part_1010", 192)
	WALL_DOOR_3 = Asset("Wall door 3", "wall_door_3", 193)
	WALL_DOOR_4 = Asset("Wall door 4", "wall_door_4", 194)
	CASTLE_WHITE_6 = Asset("Castle white 6", "castle_white_6", 195)
	HOUSE_RED_4 = Asset("House red 4", "house_red_4", 196)
	HOUSE_RED_5 = Asset("House red 5", "house_red_5", 197)
	# Column 9
	PATH_ROAD_00010100 = Asset("Path road 00010100", "path_road_00010100", 198)
	PATH_DIRT_00010100 = Asset("Path dirt 00010100", "path_dirt_00010100", 199)
	PATH_RAILED_00010100 = Asset("Path railed 00010100", "path_railed_00010100", 200)
	METAL_BAR_00000010 = Asset("Metal bar 00000010", "metal_bar_00000010", 201)
	WATER_00010100 = Asset("Water 00010100", "water_00010100", 202)
	WATER_01111100 = Asset("Water 01111100", "water_01111100", 203)
	CHEST_RED_1 = Asset("Chest red 1", "chest_red_1", 204)
	CABINET_RED_4 = Asset("Cabinet red 4", "cabinet_red_4", 205)
	CHIMNEY_WHITE_THICK_FUME = Asset("Chimney white thick fume", "chimney_white_thick_fume", 206)
	DOOR_RED_6 = Asset("Door red 6", "door_red_6", 207)
	DOOR_WHITE_4 = Asset("Door white 4", "door_white_4", 208)
	DOOR_WHITE_8 = Asset("Door white 8", "door_white_8", 209)
	PIPE_RED_1 = Asset("Pipe red 1", "pipe_red_1", 210)
	PILLAR_WHITE_1 = Asset("Pillar white 1", "pillar_white_1", 211)
	CABINET_WHITE_1 = Asset("Cabinet white 1", "cabinet_white_1", 212)
	WALL_WHITE_OPEN_1 = Asset("Wall white open 1", "wall_white_open_1", 213)
	WALL_WHITE_PART_1101 = Asset("Wall white part 1101", "wall_white_part_1101", 214)
	WALL_WHITE_PART_0101 = Asset("Wall white part 0101", "wall_white_part_0101", 215)
	WALL_WHITE_PART_0111 = Asset("Wall white part 0111", "wall_white_part_0111", 216)
	BOAT_RED_0 = Asset("Boat red 0", "boat_red_0", 217)
	TANK_WHITE_0 = Asset("Tank white 0", "tank_white_0", 218)
	CART_RED_SMALL_0 = Asset("Cart red small 0", "cart_red_small_0", 219)
	# Column 10
	PATH_ROAD_01010100 = Asset("Path road 01010100", "path_road_01010100", 220)
	PATH_DIRT_01010100 = Asset("Path dirt 01010100", "path_dirt_01010100", 221)
	PATH_RAILED_01010100 = Asset("Path railed 01010100", "path_railed_01010100", 222)
	METAL_BAR_10111011 = Asset("Metal bar 10111011", "metal_bar_10111011", 223)
	WATER_01010100 = Asset("Water 01010100", "water_01010100", 224)
	WATER_00011100 = Asset("Water 00011100", "water_00011100", 225)
	CHEST_WHITE_0 = Asset("Chest white 0", "chest_white_0", 226)
	CABINET_RED_5 = Asset("Cabinet red 5", "cabinet_red_5", 227)
	UNKNOWN_0 = Asset("Unknown 0", "unknown_0", 228)
	DOOR_RED_7 = Asset("Door red 7", "door_red_7", 229)
	DOOR_WHITE_5 = Asset("Door white 5", "door_white_5", 230)
	DOOR_WHITE_9 = Asset("Door white 9", "door_white_9", 231)
	PIPE_RED_2 = Asset("Pipe red 2", "pipe_red_2", 232)
	BOX_RED = Asset("Box red", "box_red", 233)
	CABINET_WHITE_2 = Asset("Cabinet white 2", "cabinet_white_2", 234)
	ROOF_WOOD_LEFT = Asset("Roof wood left", "roof_wood_left", 235)
	WALL_WOOD_PILLAR_RIGHT = Asset("Wall wood pillar right", "wall_wood_pillar_right", 236)
	WALL_WHITE = Asset("Wall white", "wall_white", 237)
	WALL_WHITE_PILLAR_MID = Asset("Wall white pillar mid", "wall_white_pillar_mid", 238)
	BOAT_RED_1 = Asset("Boat red 1", "boat_red_1", 239)
	TANK_WHITE_1 = Asset("Tank white 1", "tank_white_1", 240)
	# Column 11
	CART_RED_SMALL_1 = Asset("Cart red small 1", "cart_red_small_1", 241)
	PATH_ROAD_01010101 = Asset("Path road 01010101", "path_road_01010101", 242)
	PATH_DIRT_01010101 = Asset("Path dirt 01010101", "path_dirt_01010101", 243)
	PATH_RAILED_01010101 = Asset("Path railed 01010101", "path_railed_01010101", 244)
	METAL_BAR_11111011 = Asset("Metal bar 11111011", "metal_bar_11111011", 245)
	WATER_01010101 = Asset("Water 01010101", "water_01010101", 246)
	WATER_01111111 = Asset("Water 01111111", "water_01111111", 247)
	CHEST_WHITE_1 = Asset("Chest white 1", "chest_white_1", 248)
	SINK_WHITE = Asset("Sink white", "sink_white", 249)
	FURNACE_WHITE = Asset("Furnace white", "furnace_white", 250)
	CHAIR_WHITE_0 = Asset("Chair white 0", "chair_white_0", 251)
	DOOR_WHITE_6 = Asset("Door white 6", "door_white_6", 252)
	DOOR_WHITE_10 = Asset("Door white 10", "door_white_10", 253)
	PIPE_RED_3 = Asset("Pipe red 3", "pipe_red_3", 254)
	PILLAR_WHITE_FILLED = Asset("Pillar white filled", "pillar_white_filled", 255)
	ROPE = Asset("Rope", "rope", 256)
	ROOF_WOOD_TOP = Asset("Roof wood top", "roof_wood_top", 257)
	WALL_WOOD_PILLAR_SIDES = Asset("Wall wood pillar sides", "wall_wood_pillar_sides", 258)
	WALL_WHITE_WINDOW = Asset("Wall white window", "wall_white_window", 259)
	WALL_WHITE_PILLAR_SIDES = Asset("Wall white pillar sides", "wall_white_pillar_sides", 260)
	BOAT_RED_2 = Asset("Boat red 2", "boat_red_2", 261)
	TANK_WHITE_2 = Asset("Tank white 2", "tank_white_2", 262)
	# Column 12
	CART_RED_SMALL_2 = Asset("Cart red small 2", "cart_red_small_2", 263)
	PATH_ROAD_00000100 = Asset("Path road 00000100", "path_road_00000100", 264)
	PATH_DIRT_00000100 = Asset("Path dirt 00000100", "path_dirt_00000100", 265)
	PATH_RAILED_00000100 = Asset("Path railed 00000100", "path_railed_00000100", 266)
	METAL_BAR_00111010 = Asset("Metal bar 00111010", "metal_bar_00111010", 267)
	WATER_00000100 = Asset("Water 00000100", "water_00000100", 268)
	WATER_THIN_01000100 = Asset("Water thin 01000100", "water_thin_01000100", 269)
	FARMLAND = Asset("Farmland", "farmland", 270)
	CABINET_WHITE_3 = Asset("Cabinet white 3", "cabinet_white_3", 271)
	OVEN_WHITE = Asset("Oven white", "oven_white", 272)
	CHAIR_WHITE_1 = Asset("Chair white 1", "chair_white_1", 273)
	TOILET_WHITE_0 = Asset("Toilet white 0", "toilet_white_0", 274)
	DOOR_WHITE_11 = Asset("Door white 11", "door_white_11", 275)
	CHAIN = Asset("Chain", "chain", 276)
	CHAIN_HOOK = Asset("Chain hook", "chain_hook", 277)
	CONVEYOR_0 = Asset("Conveyor 0", "conveyor_0", 278)
	ROOF_WOOD_RIGHT = Asset("Roof wood right", "roof_wood_right", 279)
	WALL_WOOD_PILLAR_LEFT = Asset("Wall wood pillar left", "wall_wood_pillar_left", 280)
	WALL_WHITE_WINDOW_BARRED = Asset("Wall white window barred", "wall_white_window_barred", 281)
	CHECKERBOARD_RED = Asset("Checkerboard red", "checkerboard_red", 282)
	TRUCK_LEFT_0 = Asset("Truck left 0", "truck_left_0", 283)
	TRUCK_LEFT_1 = Asset("Truck left 1", "truck_left_1", 284)
	# Column 13
	SUBMARINE_0 = Asset("Submarine 0", "submarine_0", 285)
	LINE_RED_0 = Asset("Line red 0", "line_red_0", 286)
	STRIPES_RED_1010 = Asset("Stripes red 1010", "stripes_red_1010", 287)
	PIPE_WHITE_0_0010 = Asset("Pipe white 0 0010", "pipe_white_0_0010", 288)
	PIPE_WHITE_1_0010 = Asset("Pipe white 1 0010", "pipe_white_1_0010", 289)
	PIPE_WHITE_2_0010 = Asset("Pipe white 2 0010", "pipe_white_2_0010", 290)
	WATER_THIN_00010100 = Asset("Water thin 00010100", "water_thin_00010100", 291)
	CROP_0 = Asset("Crop 0", "crop_0", 292)
	CABINET_WHITE_4 = Asset("Cabinet white 4", "cabinet_white_4", 293)
	SINK_WHITE_SMALL = Asset("Sink white small", "sink_white_small", 294)
	TOILET_WHITE_1 = Asset("Toilet white 1", "toilet_white_1", 295)
	BATH = Asset("Bath", "bath", 296)
	DOOR_WHITE_12 = Asset("Door white 12", "door_white_12", 297)
	FIRE_HYDRANT = Asset("Fire hydrant", "fire_hydrant", 298)
	DISH_RED_0 = Asset("Dish red 0", "dish_red_0", 299)
	CONVEYOR_1 = Asset("Conveyor 1", "conveyor_1", 300)
	WALL_WOOD_WINDOW = Asset("Wall wood window", "wall_wood_window", 301)
	WALL_WOOD = Asset("Wall wood", "wall_wood", 302)
	WALL_WHITE_HOLE = Asset("Wall white hole", "wall_white_hole", 303)
	BOX_CROSS_RED = Asset("Box cross red", "box_cross_red", 304)
	TRUCK_RIGHT_0 = Asset("Truck right 0", "truck_right_0", 305)
	TRUCK_RIGHT_1 = Asset("Truck right 1", "truck_right_1", 306)
	# Column 14
	SUBMARINE_1 = Asset("Submarine 1", "submarine_1", 307)
	LINE_RED_1 = Asset("Line red 1", "line_red_1", 308)
	STRIPES_RED_1100 = Asset("Stripes red 1100", "stripes_red_1100", 309)
	PIPE_WHITE_0_1010 = Asset("Pipe white 0 1010", "pipe_white_0_1010", 310)
	PIPE_WHITE_1_1010 = Asset("Pipe white 1 1010", "pipe_white_1_1010", 311)
	PIPE_WHITE_2_1010 = Asset("Pipe white 2 1010", "pipe_white_2_1010", 312)
	WATER_BLOB = Asset("Water blob", "water_blob", 313)
	CROP_1 = Asset("Crop 1", "crop_1", 314)
	SIGN_BED = Asset("Sign bed", "sign_bed", 315)
	SIGN_HANGING_BED = Asset("Sign hanging bed", "sign_hanging_bed", 316)
	CART_WHITE_0 = Asset("Cart white 0", "cart_white_0", 317)
	FIREPLACE_FIRE = Asset("Fireplace fire", "fireplace_fire", 318)
	ROADWORK_FENCE = Asset("Roadwork fence", "roadwork_fence", 319)
	UNKNOWN_1 = Asset("Unknown 1", "unknown_1", 320)
	DISH_RED_1 = Asset("Dish red 1", "dish_red_1", 321)
	PILLAR_WOOD_0 = Asset("Pillar wood 0", "pillar_wood_0", 322)
	PILLAR_METAL_0 = Asset("Pillar metal 0", "pillar_metal_0", 323)
	WALL_WOOD_WINDOW_BARRED = Asset("Wall wood window barred", "wall_wood_window_barred", 324)
	WALL_RED_WINDOW = Asset("Wall red window", "wall_red_window", 325)
	COMET_BLUE = Asset("Comet blue", "comet_blue", 326)
	UFO_0 = Asset("Ufo 0", "ufo_0", 327)
	UFO_1 = Asset("Ufo 1", "ufo_1", 328)
	# Column 15
	SUBMARINE_2 = Asset("Submarine 2", "submarine_2", 329)
	LINE_RED_2 = Asset("Line red 2", "line_red_2", 330)
	STRIPES_RED_1101 = Asset("Stripes red 1101", "stripes_red_1101", 331)
	PIPE_WHITE_0_0110 = Asset("Pipe white 0 0110", "pipe_white_0_0110", 332)
	PIPE_WHITE_1_0110 = Asset("Pipe white 1 0110", "pipe_white_1_0110", 333)
	PIPE_WHITE_2_0110 = Asset("Pipe white 2 0110", "pipe_white_2_0110", 334)
	BRIDGE_WOOD_LEFT = Asset("Bridge wood left", "bridge_wood_left", 335)
	CROP_2 = Asset("Crop 2", "crop_2", 336)
	SIGN_DRINK = Asset("Sign drink", "sign_drink", 337)
	SIGN_HANGING_DRINK = Asset("Sign hanging drink", "sign_hanging_drink", 338)
	CART_WHITE_1 = Asset("Cart white 1", "cart_white_1", 339)
	FIRE = Asset("Fire", "fire", 340)
	DISH_WHITE_0 = Asset("Dish white 0", "dish_white_0", 341)
	COMET_BLUE_0 = Asset("Comet blue 0", "comet_blue_0", 342)
	CART_WHITE_2 = Asset("Cart white 2", "cart_white_2", 343)
	PILLAR_WOOD_1 = Asset("Pillar wood 1", "pillar_wood_1", 344)
	PILLAR_METAL_1 = Asset("Pillar metal 1", "pillar_metal_1", 345)
	WALL_WOOD_WINDOW_CLOSED = Asset("Wall wood window closed", "wall_wood_window_closed", 346)
	WALL_RED_WINDOW_OPEN = Asset("Wall red window open", "wall_red_window_open", 347)
	COMET_BLUE_1 = Asset("Comet blue 1", "comet_blue_1", 348)
	JETPACK_BLUE = Asset("Jetpack blue", "jetpack_blue", 349)
	FUME_PILLAR_TOP = Asset("Fume pillar top", "fume_pillar_top", 350)
	FUME_PILLAR_MID = Asset("Fume pillar mid", "fume_pillar_mid", 351)
	# Column 16
	FLOOR_PATTERN_0 = Asset("Floor pattern 0", "floor_pattern_0", 352)
	STRIPES_RED_1111 = Asset("Stripes red 1111", "stripes_red_1111", 353)
	PIPE_WHITE_0_1111 = Asset("Pipe white 0 1111", "pipe_white_0_1111", 354)
	PIPE_WHITE_1_1111 = Asset("Pipe white 1 1111", "pipe_white_1_1111", 355)
	PIPE_WHITE_2_1111 = Asset("Pipe white 2 1111", "pipe_white_2_1111", 356)
	BRIDGE_WOOD_MID = Asset("Bridge wood mid", "bridge_wood_mid", 357)
	CROP_3 = Asset("Crop 3", "crop_3", 358)
	SIGN_SQUARE = Asset("Sign square", "sign_square", 359)
	LINES_WOOD_1101 = Asset("Lines wood 1101", "lines_wood_1101", 360)
	LINES_WOOD_0101 = Asset("Lines wood 0101", "lines_wood_0101", 361)
	CART_WOOD_0 = Asset("Cart wood 0", "cart_wood_0", 362)
	PILLAR_WOOD_2 = Asset("Pillar wood 2", "pillar_wood_2", 363)
	BRICKS_0 = Asset("Bricks 0", "bricks_0", 364)
	CASTLE_PART_11100011 = Asset("Castle part 11100011", "castle_part_11100011", 365)
	CASTLE_PART_10000011 = Asset("Castle part 10000011", "castle_part_10000011", 366)
	CASTLE_PART_10001111 = Asset("Castle part 10001111", "castle_part_10001111", 367)
	WALL_PART_0_11100011 = Asset("Wall part 0 11100011", "wall_part_0_11100011", 368)
	WALL_PART_0_10000011 = Asset("Wall part 0 10000011", "wall_part_0_10000011", 369)
	WALL_PART_0_10001111 = Asset("Wall part 0 10001111", "wall_part_0_10001111", 370)
	WALL_PART_1_11100011 = Asset("Wall part 1 11100011", "wall_part_1_11100011", 371)
	WALL_PART_1_10000011 = Asset("Wall part 1 10000011", "wall_part_1_10000011", 372)
	WALL_PART_1_10001111 = Asset("Wall part 1 10001111", "wall_part_1_10001111", 373)
	# Column 17
	FLOOR_PATTERN_1 = Asset("Floor pattern 1", "floor_pattern_1", 374)
	STRIPES_RED_1110 = Asset("Stripes red 1110", "stripes_red_1110", 375)
	PIPE_WHITE_0_1110 = Asset("Pipe white 0 1110", "pipe_white_0_1110", 376)
	PIPE_WHITE_1_1110 = Asset("Pipe white 1 1110", "pipe_white_1_1110", 377)
	PIPE_WHITE_2_1110 = Asset("Pipe white 2 1110", "pipe_white_2_1110", 378)
	BRIDGE_WOOD_BROKEN = Asset("Bridge wood broken", "bridge_wood_broken", 379)
	CROP_4 = Asset("Crop 4", "crop_4", 380)
	FINISH_RED = Asset("Finish red", "finish_red", 381)
	FLAG_RED_0 = Asset("Flag red 0", "flag_red_0", 382)
	FLAG_RED_1 = Asset("Flag red 1", "flag_red_1", 383)
	CART_WOOD_1 = Asset("Cart wood 1", "cart_wood_1", 384)
	PILLAR_WOOD_3 = Asset("Pillar wood 3", "pillar_wood_3", 385)
	BRICKS_1 = Asset("Bricks 1", "bricks_1", 386)
	CASTLE_PART_11100000 = Asset("Castle part 11100000", "castle_part_11100000", 387)
	CASTLE_PART_11111111 = Asset("Castle part 11111111", "castle_part_11111111", 388)
	CASTLE_PART_00001110 = Asset("Castle part 00001110", "castle_part_00001110", 389)
	WALL_PART_0_11100000 = Asset("Wall part 0 11100000", "wall_part_0_11100000", 390)
	WALL_PART_0_11111111 = Asset("Wall part 0 11111111", "wall_part_0_11111111", 391)
	WALL_PART_0_00001110 = Asset("Wall part 0 00001110", "wall_part_0_00001110", 392)
	WALL_PART_1_11100000 = Asset("Wall part 1 11100000", "wall_part_1_11100000", 393)
	WALL_PART_1_11111111 = Asset("Wall part 1 11111111", "wall_part_1_11111111", 394)
	WALL_PART_1_00001110 = Asset("Wall part 1 00001110", "wall_part_1_00001110", 395)
	# Column 19
	BRICK_WALL_PART_11100011 = Asset("Brick wall part 11100011", "brick_wall_part_11100011", 396)
	BRICK_WALL_PART_10000011 = Asset("Brick wall part 10000011", "brick_wall_part_10000011", 397)
	BRICK_WALL_PART_10001111 = Asset("Brick wall part 10001111", "brick_wall_part_10001111", 398)
	BRICK_PART_00001000 = Asset("Brick part 00001000", "brick_part_00001000", 399)
	BRICK_PART_00100000 = Asset("Brick part 00100000", "brick_part_00100000", 400)
	BRICK_PART_01000000 = Asset("Brick part 01000000", "brick_part_01000000", 401)
	TRUNK_0 = Asset("Trunk 0", "trunk_0", 402)
	BLOB_BLUE_0 = Asset("Blob blue 0", "blob_blue_0", 403)
	BLOB_YELLOW_0 = Asset("Blob yellow 0", "blob_yellow_0", 404)
	BLOB_GREEN_0 = Asset("Blob green 0", "blob_green_0", 405)
	HOUSE_GREEN_0 = Asset("House green 0", "house_green_0", 406)
	ROOF_GREEN_LEFT = Asset("Roof green left", "roof_green_left", 407)
	WOOD_CORNER = Asset("Wood corner", "wood_corner", 408)
	CASTLE_PART_11111000 = Asset("Castle part 11111000", "castle_part_11111000", 409)
	CASTLE_PART_00111000 = Asset("Castle part 00111000", "castle_part_00111000", 410)
	CASTLE_PART_00111110 = Asset("Castle part 00111110", "castle_part_00111110", 411)
	WALL_PART_0_11111000 = Asset("Wall part 0 11111000", "wall_part_0_11111000", 412)
	WALL_PART_0_00111000 = Asset("Wall part 0 00111000", "wall_part_0_00111000", 413)
	WALL_PART_0_00111110 = Asset("Wall part 0 00111110", "wall_part_0_00111110", 414)
	WALL_PART_1_11111000 = Asset("Wall part 1 11111000", "wall_part_1_11111000", 415)
	WALL_PART_1_00111000 = Asset("Wall part 1 00111000", "wall_part_1_00111000", 416)
	WALL_PART_1_00111110 = Asset("Wall part 1 00111110", "wall_part_1_00111110", 417)
	# Column 18
	BRICK_WALL_PART_11100000 = Asset("Brick wall part 11100000", "brick_wall_part_11100000", 418)
	BRICK_WALL_PART_11111111 = Asset("Brick wall part 11111111", "brick_wall_part_11111111", 419)
	BRICK_WALL_PART_00001110 = Asset("Brick wall part 00001110", "brick_wall_part_00001110", 420)
	BRICK_PART_00000010 = Asset("Brick part 00000010", "brick_part_00000010", 421)
	BRICK_PART_10000000 = Asset("Brick part 10000000", "brick_part_10000000", 422)
	TREE_6 = Asset("Tree 6", "tree_6", 423)
	TRUNK_1 = Asset("Trunk 1", "trunk_1", 424)
	BLOB_BLUE_1 = Asset("Blob blue 1", "blob_blue_1", 425)
	BLOB_YELLOW_1 = Asset("Blob yellow 1", "blob_yellow_1", 426)
	BLOB_GREEN_1 = Asset("Blob green 1", "blob_green_1", 427)
	HOUSE_GREEN_1 = Asset("House green 1", "house_green_1", 428)
	ROOF_GREEN_TOP = Asset("Roof green top", "roof_green_top", 429)
	WOOD_BARRED_BOX = Asset("Wood barred box", "wood_barred_box", 430)
	CASTLE_PART_11101111 = Asset("Castle part 11101111", "castle_part_11101111", 431)
	SCOPE_0 = Asset("Scope 0", "scope_0", 432)
	SLIDER_0 = Asset("Slider 0", "slider_0", 433)
	CARD_0_0 = Asset("Card 0 0", "card_0_0", 434)
	CARD_1_0 = Asset("Card 1 0", "card_1_0", 435)
	CARD_2_0 = Asset("Card 2 0", "card_2_0", 436)
	CARD_3_0 = Asset("Card 3 0", "card_3_0", 437)
	ARROW_POINTING_0 = Asset("Arrow pointing 0", "arrow_pointing_0", 438)
	ARROW_POINTING_1 = Asset("Arrow pointing 1", "arrow_pointing_1", 439)
	# Column 20
	BRICK_WALL_PART_11111000 = Asset("Brick wall part 11111000", "brick_wall_part_11111000", 440)
	BRICK_WALL_PART_00111000 = Asset("Brick wall part 00111000", "brick_wall_part_00111000", 441)
	BRICK_WALL_PART_00111110 = Asset("Brick wall part 00111110", "brick_wall_part_00111110", 442)
	# Column 24
	MAGE1 = Asset("Mage1", "mage1", 528)
	MAGE2 = Asset("Mage2", "mage2", 529)
	MAGE3 = Asset("Mage3", "mage3", 530)
	# Column 25
	PLAYER1 = Asset("Player1", "player1", 550)
	PLAYER2 = Asset("Player2", "player2", 551)
	PLAYER3 = Asset("Player3", "player3", 552)
	# ?
	NUMBER0 = Asset("Number0", "number0", 787)
	IRON_AXE = Asset("Iron axe", "iron_axe", 931)

	# CUSTOM ASSETS AREA
	OAK_LOG = Asset("Oak log", "items/oak_log", 47685225)

	@staticmethod
	def getAsset(iden):
		"""
		:param int iden: the identifier of the entity type
		:return: Returns entity or None
		:rtype: Item
		"""
		for ass in Assets:
			if ass.value.id == iden:
				return ass.value
		return None

	@staticmethod
	def load():
		# Define list with image chunks
		assets = []
		# Open the tilesheet
		# colored_packed.png is 16x16, currently is hardcoded to this file
		sheet = pygame.image.load(
			path.join(GAMEDIR, 'assets/visual/Tilesheet/colored_transparent_packed.png'))
		# index = 0  # is used to know how many iterations we have done (x*22+y = index)
		for x in range(48):
			for y in range(22):
				# list(Assets)[x * 22 + y].image = sheet.subsurface(pygame.Rect((16 * x, 16 * y), (16, 16)))
				ass = Assets.getAsset(x * 22 + y)
				# ass = list(Assets)[x * 22 + y]
				if ass is not None:
					ass.image = sheet.subsurface(pygame.Rect((16 * x, 16 * y), (16, 16)))

		# Load the rest
		""" Can this somehow work?
		for i, asset in enumerate(Assets, 449):
			# print(f"{asset.value.image=}")
			# print(len(list(Assets)))
			asset.value.image = pygame.image.load(path.join(GAMEDIR, 'assets/visual/items/oak_log.png'))
		"""
		# TODO: change this hardcoded number when new assets get added to the tilesheet area
		for i in range(450, len(Assets)):
			print(f"{list(Assets)[i].value.image=}")
			list(Assets)[i].value.image = pygame.image.load(path.join(GAMEDIR, 'assets/visual/items/oak_log.png'))
			print(f"{list(Assets)[i].value.image=}")


