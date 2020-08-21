from ApplicationGlobals import ApplicationGlobals
from GameMode import GameMode


class CharacterDeath:
    def __init__(self, name='Wilson', daysSurvived=0, causeOfDeath='', gameMode=GameMode.SURVIVAL):
        if not name in ApplicationGlobals.getInstance().characterNames:
            raise ValueError("Cannot use non existing character's name")
        if not causeOfDeath in ApplicationGlobals.getInstance().causesOfDeath:
            raise ValueError(f"Cause of death named {causeOfDeath} does not exist")
        self._name = name
        self._daysSurvived = daysSurvived
        self._causeOfDeath = causeOfDeath
        self._gameMode = gameMode

    @property
    def name(self) -> str:
        return self._name
    @property
    def daysSurvived(self) -> int:
        return self._daysSurvived
    @property
    def causeOfDeath(self) -> str:
        return self._causeOfDeath
    @property
    def gameMode(self) -> GameMode:
        return self._gameMode
