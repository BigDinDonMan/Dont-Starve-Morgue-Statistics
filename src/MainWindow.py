from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QHeaderView, QTableWidget, QTableWidgetItem, QLabel, \
    QMenuBar, QAction

from ApplicationGlobals import ApplicationGlobals
from CharacterDeath import CharacterDeath
from CustomWidgets import CharacterDeathFormWidget
from GameMode import *
from Morgue import Morgue
from StatisticsWindow import StatisticsWindow


class MainWindow(QMainWindow):
    def __init__(self, title: str):
        super(MainWindow, self).__init__()
        self.dataTable = QTableWidget()
        self.form = CharacterDeathFormWidget(owningWindow=self)
        self._initUI(title=title)
        self._initTableView()

    def _initUI(self, title: str) -> None:
        self.setWindowTitle(title)
        self.resize(600, 600)
        self.setFixedSize(self.width(), self.height())
        widget, layout = QWidget(), QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(self.form, 0, 0)
        layout.addWidget(self.dataTable, 1, 0)
        self.setCentralWidget(widget)
        statisticsAction = QAction('Show game statistics', self)
        statisticsAction.setStatusTip('Calculates the game statistics (favourite characters, most deaths etc.)')
        statisticsAction.triggered.connect(self.showStatisticsModalWindow)
        saveDeathsAction = QAction('Save data', self)
        saveDeathsAction.setStatusTip('Saves player deaths')
        saveDeathsAction.triggered.connect(Morgue.getInstance().save)
        menuBar: QMenuBar = self.menuBar()
        menuBar.addAction(saveDeathsAction)
        menuBar.addAction(statisticsAction)



    def _initTableView(self):
        # temp = CharacterDeath(name='Wilson', daysSurvived=10, causeOfDeath='Pengull', gameMode=GameMode.SURVIVAL)
        # Morgue.getInstance().deaths.append(temp)
        self.dataTable.setColumnCount(4)
        self.dataTable.setHorizontalHeaderLabels(['Character', 'Days survived', 'Cause of death', 'Game mode'])
        header: QHeaderView = self.dataTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        for death in Morgue.getInstance().deaths:
            self._insertItemToDataTable(death)

    def _insertItemToDataTable(self, death: CharacterDeath):
        def addItem(row, col, i):
            i.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i.setFlags(i.flags() ^ Qt.ItemIsEditable)
            self.dataTable.setItem(row, col, i)
        rowCount = self.dataTable.rowCount()
        self.dataTable.insertRow(rowCount)
        label = QLabel('')
        label.setPixmap(QPixmap(ApplicationGlobals.getInstance().characterImages[death.name]))
        label.setAlignment(Qt.AlignCenter)
        self.dataTable.setCellWidget(rowCount, 0, label)
        addItem(rowCount, 1, QTableWidgetItem(str(death.daysSurvived)))
        addItem(rowCount, 2, QTableWidgetItem(death.causeOfDeath))
        addItem(rowCount, 3, QTableWidgetItem(GAMEMODE_NAMES[death.gameMode]))
        self.dataTable.setRowHeight(rowCount, 150)

    def addNewDeathToTable(self, death: CharacterDeath):
        self._insertItemToDataTable(death)
        self.form.clear()

    def showStatisticsModalWindow(self):
        dialog = StatisticsWindow()
        dialog.setModal(True)
        dialog.exec()