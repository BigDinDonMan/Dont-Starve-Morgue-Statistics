import pickle

from PyQt5.QtWidgets import QMessageBox


class Morgue(object):
    _instance = None
    @staticmethod
    def getInstance():
        if Morgue._instance is None:
            Morgue._instance = Morgue()
        return Morgue._instance

    def __init__(self):
        def loadDeaths() -> list:
            # with open('../resources/deaths.bin', mode='wb') as f:
            #     pickle.dump([], f)
            with open('../resources/deaths.bin', mode='rb') as f:
                result = pickle.load(f)
            return result
        self._deaths = loadDeaths()

    @property
    def deaths(self) -> list:
        return self._deaths

    def save(self):
        messageBox = QMessageBox()
        messageBox.setModal(True)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.setWindowTitle('Save information')
        try:
            with open('../resources/deaths.bin', mode='wb') as f:
                pickle.dump(self._deaths, f)
            messageBox.setText('Deaths saved successfully!')
            messageBox.setIcon(QMessageBox.Information)
        except Exception as e:
            messageBox.setText("Something went wrong, please see the error below:")
            messageBox.setDetailedText(str(e))
            messageBox.setIcon(QMessageBox.Warning)
        finally:
            messageBox.exec_()