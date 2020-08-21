from enum import Enum


class GameMode(Enum):
    SURVIVAL = 0,
    HAMLET = 1,
    SHIPWRECKED = 2,
    DT_TOGETHER = 3


GAMEMODE_NAMES = {
    GameMode.SURVIVAL: 'Survival',
    GameMode.HAMLET: 'Hamlet',
    GameMode.SHIPWRECKED: 'Shipwrecked',
    GameMode.DT_TOGETHER: "Don't Starve Together"
}

GAMEMODE_NAMES_TO_ENUM = {
    "Survival": GameMode.SURVIVAL,
    "Hamlet": GameMode.HAMLET,
    "Shipwrecked": GameMode.SHIPWRECKED,
    "Don't Starve Together": GameMode.DT_TOGETHER
}

GAMEMODE_NAMES_TO_ICONS = {
    "Survival": 'rog_icon',
    "Hamlet": 'hamlet_icon',
    "Shipwrecked": 'shipwrecked_icon',
    "Don't Starve Together": 'dst_icon'
}