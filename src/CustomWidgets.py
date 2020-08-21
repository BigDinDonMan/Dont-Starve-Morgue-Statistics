from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QPixmap, QPainter, QIntValidator, QIcon
from PyQt5.QtWidgets import QWidget, QStyledItemDelegate, QStyleOptionViewItem, QPushButton, QLineEdit, \
    QComboBox, QLabel, QVBoxLayout, QMessageBox, QCompleter, QSpacerItem, QHBoxLayout, QSizePolicy

from ApplicationGlobals import ApplicationGlobals
from CharacterDeath import CharacterDeath
from GameMode import *


class ImageWidget(QWidget):
    def __init__(self, imagePath: str, parent):
        super(ImageWidget, self).__init__(parent)
        self.image = QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QPainter(self)
        x, y = self.x(), self.y()
        painter.drawPixmap(x,y,self.image)

    def width(self):
        return self.image.width()

    def height(self):
        return self.image.height()


class AlignCenterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignCenterDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter
        option.decorationAlignment = Qt.AlignCenter
        option.decorationPosition = QStyleOptionViewItem.Top


class CharacterDeathFormWidget(QWidget):
    def __init__(self, owningWindow):
        super(CharacterDeathFormWidget, self).__init__()
        self.owningWindow = owningWindow
        self.addButton = QPushButton('Add player death')
        self.addButton.clicked.connect(self.addDeath)
        self.causeOfDeathTextBox = QLineEdit()
        self.autoCompleteModel = QStringListModel()
        self.gameModeComboBox = QComboBox()
        self.characterComboBox = QComboBox()
        self.daysSurvivedTextBox = QLineEdit()
        self.daysSurvivedTextBox.setValidator(QIntValidator(0, 10000000))
        self._initFormLayout()
        self._initAutoCompleter()
        self._initComboBoxes()

    def _initAutoCompleter(self):
        completer = QCompleter()
        completer.setModel(self.autoCompleteModel)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.autoCompleteModel.setStringList(ApplicationGlobals.getInstance().causesOfDeath)
        self.causeOfDeathTextBox.setCompleter(completer)

    def _initFormLayout(self):
        def addItemsToVBox(vbox, *args):
            for arg in args:
                vbox.addWidget(arg)
        formLayout = QVBoxLayout()
        self.setLayout(formLayout)
        comboboxVbox, lineEditsVbox = QVBoxLayout(), QVBoxLayout()
        addItemsToVBox(comboboxVbox, QLabel('Character'), self.characterComboBox, QLabel('Game mode'), self.gameModeComboBox)
        addItemsToVBox(lineEditsVbox, QLabel('Cause of death'), self.causeOfDeathTextBox, QLabel('Days survived'), self.daysSurvivedTextBox)
        widget1, widget2 = QWidget(), QWidget()
        widget1.setLayout(comboboxVbox)
        widget2.setLayout(lineEditsVbox)
        widget, hbox = QWidget(), QHBoxLayout()
        widget.setLayout(hbox)
        hbox.addWidget(widget1)
        hbox.addItem(QSpacerItem(25, 0))
        hbox.addWidget(widget2)
        formLayout.addWidget(widget)
        formLayout.addWidget(self.addButton)
        formLayout.setAlignment(self.addButton, Qt.AlignHCenter)
        self.addButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        widget1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _initComboBoxes(self):
        for name in ApplicationGlobals.getInstance().characterNames:
            self.characterComboBox.addItem(QIcon('../resources/images/characters/{0}.png'.format(name.lower())), name)
        for gameModeName in GAMEMODE_NAMES.values():
            self.gameModeComboBox.addItem(QIcon('../resources/images/gamemodes/{0}.png'.format(GAMEMODE_NAMES_TO_ICONS[gameModeName])), gameModeName)

    def isValid(self):
        daysSurvivedValid = self.daysSurvivedTextBox.text()
        causeOfDeath = self.causeOfDeathTextBox.text()
        causeOfDeathValid = causeOfDeath and causeOfDeath in ApplicationGlobals.getInstance().causesOfDeath
        characterName = self.characterComboBox.currentText()
        characterNameValid = characterName and characterName in ApplicationGlobals.getInstance().characterNames
        gamemodeValid = self.gameModeComboBox.currentText()
        return (daysSurvivedValid and causeOfDeathValid and characterNameValid and gamemodeValid)

    def addDeath(self):
        if self.isValid():
            gamemode = GAMEMODE_NAMES_TO_ENUM[str(self.gameModeComboBox.currentText())]
            charName, causeOfDeath = str(self.characterComboBox.currentText()), str(self.causeOfDeathTextBox.text())
            daysSurvived = int(self.daysSurvivedTextBox.text())
            death = CharacterDeath(name=charName, daysSurvived=daysSurvived, causeOfDeath=causeOfDeath, gameMode=gamemode)
            from Morgue import Morgue
            Morgue.getInstance().deaths.append(death)
            self.owningWindow.addNewDeathToTable(death)
        else:
            messageBox = QMessageBox()
            messageBox.setText("Please fill in correct information in the form")
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setModal(True)
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec_()

    def clear(self):
        self.gameModeComboBox.setCurrentIndex(0)
        self.characterComboBox.setCurrentIndex(0)
        self.daysSurvivedTextBox.setText('')
        self.causeOfDeathTextBox.setText('')
