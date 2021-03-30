from PyQt5 import QtCore, QtGui, QtWidgets

import FileBrowserGUI


class Data:
    file_path = "No file selected"


class MyFileBrowser(FileBrowserGUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.model = QtWidgets.QFileSystemModel()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

    def populate(self):
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setColumnWidth(0, 400)
        self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open_pdf = menu.addAction("Select file")
        open_pdf.triggered.connect(self.open_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        Data.file_path = self.model.filePath(index)
        self.close()


def get_file_path():
    return Data.file_path


if __name__ == "__main__":
    file_path = ""
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
