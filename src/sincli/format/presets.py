from typing import Literal

DEFAULT_FONT = "ansi_shadow"

PresetName = Literal[
    "rose",
    "doppler",
    "pink",
    "mauve",
    "gray",
    "sunset",
    "cherry",
    "lush",
    "kashmir",
    "tranquil",
    "wood",
    "ocean",
    "frost",
    "violet",
    "river",
    "blood",
    "steel",
    "electric",
    "venice",
    "mystic",
]

presets = {
    "rose": {"start_color": (255, 175, 189), "end_color": (255, 195, 160)},
    "doppler": {"start_color": (204, 43, 94), "end_color": (117, 58, 136)},
    "pink": {"start_color": (238, 156, 167), "end_color": (255, 221, 225)},
    "mauve": {"start_color": (66, 39, 90), "end_color": (115, 75, 109)},
    "gray": {"start_color": (189, 195, 199), "end_color": (44, 62, 80)},
    "sunset": {"start_color": (222, 98, 98), "end_color": (255, 184, 140)},
    "cherry": {"start_color": (235, 51, 73), "end_color": (244, 92, 67)},
    "lush": {"start_color": (86, 171, 47), "end_color": (168, 224, 99)},
    "kashmir": {"start_color": (97, 67, 133), "end_color": (81, 99, 149)},
    "tranquil": {"start_color": (238, 205, 163), "end_color": (239, 98, 159)},
    "wood": {"start_color": (234, 205, 163), "end_color": (214, 174, 123)},
    "ocean": {"start_color": (2, 170, 176), "end_color": (0, 205, 172)},
    "frost": {"start_color": (0, 4, 40), "end_color": (0, 78, 146)},
    "violet": {"start_color": (123, 67, 151), "end_color": (220, 36, 48)},
    "river": {"start_color": (67, 206, 162), "end_color": (24, 90, 157)},
    "blood": {"start_color": (255, 81, 47), "end_color": (221, 36, 118)},
    "steel": {"start_color": (31, 28, 44), "end_color": (146, 141, 171)},
    "electric": {"start_color": (71, 118, 230), "end_color": (142, 84, 233)},
    "venice": {"start_color": (8, 80, 120), "end_color": (133, 216, 206)},
    "mystic": {"start_color": (117, 127, 154), "end_color": (215, 221, 232)},
}