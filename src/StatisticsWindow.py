from typing import List, Set

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QGridLayout, QLabel, QVBoxLayout

from collections import Counter

from GameMode import GameMode
from Morgue import Morgue
from ApplicationGlobals import ApplicationGlobals


class StatisticsWindow(QDialog):

    def __init__(self):
        super(StatisticsWindow, self).__init__()
        self._initUI()
        self._calculateStatistics()

    def _calculateStatistics(self):
        #TODO: calculate the favourite character, average number of days survived, favourite game mode and most common cause of death
        #TODO: maybe also a number of unique causes of death
        #TODO: character with most deaths
        if len(Morgue.getInstance().deaths) > 0:
            try:
                favouriteCharacter = self._getFavouriteCharacter()
                averageDaysSurvived = self._getAverageDaysSurvived()
                mostCommonCauseOfDeath = self._getMostCommonCauseOfDeath()
                uniqueCausesOfDeath = self._getUniqueCausesOfDeath()
                deathCount = len(Morgue.getInstance().deaths)
                mostCommonGameMode = None
            except Exception as e:
                print(e)

    def _getUniqueCausesOfDeath(self) -> Set[str]:
        return set([death.causeOfDeath for death in Morgue.getInstance().deaths])

    def _getMostCommonGameMode(self) -> GameMode:
        histogram = {mode: sum(1 if death.gameMode == mode else 0 for death in Morgue.getInstance().deaths) \
                     for mode in GameMode}
        return max(histogram, key=histogram.get)

    def _getFavouriteCharacter(self) -> str:
        histogram = {name: sum(1 if death.name == name else 0 for death in Morgue.getInstance().deaths) \
                     for name in ApplicationGlobals.getInstance().characterNames}
        return max(histogram, key=histogram.get)

    def _getAverageDaysSurvived(self) -> float:
        return sum(death.daysSurvived for death in Morgue.getInstance().deaths) / len(Morgue.getInstance().deaths)

    def _getMostCommonCauseOfDeath(self) -> str:
        histogram = {cause: sum(1 if death.causeOfDeath == cause else 0 for death in Morgue.getInstance().deaths) \
                     for cause in ApplicationGlobals.getInstance().causesOfDeath}
        return max(histogram, key=histogram.get)

    def _initUI(self):
        self.setWindowTitle("Game statistics")
        self.resize(450, 450)
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        mainLabel = QLabel('Gamemode and death statistics')
        mainLabel.setStyleSheet('font-size: 16px; font-family: Helvetica; font-weight: bold;')
        mainLayout.addWidget(mainLabel)
        mainLayout.setAlignment(mainLabel, Qt.AlignHCenter | Qt.AlignTop)
