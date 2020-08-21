from typing import List, Dict

from JsonUtils import JsonUtils

#TODO: add verification if chosen character is only available in Don't Starve Together, Shipwrecked etc.

class ApplicationGlobals(object):

    _instance = None

    def __init__(self):
        self._characterNames = JsonUtils.loadList('../resources/character_names.json')
        self._causesOfDeath = JsonUtils.loadList('../resources/causes_of_death.json')
        self._characterImages = {name: '../resources/images/characters/{0}.png'.format(name.lower()) for name in self._characterNames}

    @staticmethod
    def getInstance():
        if ApplicationGlobals._instance is None:
            ApplicationGlobals._instance = ApplicationGlobals()
        return ApplicationGlobals._instance

    @property
    def characterNames(self) -> List[str]:
        return self._characterNames

    @property
    def causesOfDeath(self) -> List[str]:
        return self._causesOfDeath

    @property
    def characterImages(self) -> Dict[str, str]:
        return self._characterImages

    def save(self):
        JsonUtils.saveList(self._characterNames, '../resources/character_names.json')
        JsonUtils.saveList(self._causesOfDeath, '../resources/causes_of_death.json')