import os

from PyQt5 import QtCore, QtGui, QtWidgets

import FileBrowser
import EditPDF


class Ui_Dialog(object):
    def __init__(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.fb = FileBrowser.MyFileBrowser()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(225, 235)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PDFEditor.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        # Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setStyleSheet("background-color: rgb(145, 8, 3);")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 161, 229))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 87 10pt \"Arial Black\";\n"
                                      "    color: #333;\n"
                                      "    border: 15px solid #b30b00;\n"
                                      "    border-radius: 20px;\n"
                                      "    border-style: outset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                      "        radius: 1.35, stop: 0 #b30b00, stop: 1 #ff1c0d\n"
                                      "        );\n"
                                      "    padding: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                      "        radius: 1.35, stop: 0 #ff1c0d, stop: 1 #b30b00\n"
                                      "        );\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: inset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                      "        radius: 1.35, stop: 0 #4cf4ff, stop: 1 #ddd\n"
                                      "        );\n"
                                      "    }")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 87 10pt \"Arial Black\";\n"
                                        "    color: #333;\n"
                                        "    border: 15px solid #b30b00;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #b30b00, stop: 1 #ff1c0d\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #ff1c0d, stop: 1 #b30b00\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #4cf4ff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.getFileBrowser)
        self.pushButton_2.clicked.connect(self.Edit_Selected_PDF)

    def getFileBrowser(self):
        try:
            self.fb.closeEvent = self.CloseEvent
            self.fb.show()
        except:
            print("failed")

    def CloseEvent(self, event):
        self.set_Text_Browser()

    def set_Text_Browser(self):
        self.textBrowser.clear()
        self.textBrowser.insertPlainText(os.path.basename(FileBrowser.Data.file_path))

    def Edit_Selected_PDF(self):
        if FileBrowser.Data.file_path.endswith('.pdf') | FileBrowser.Data.file_path.endswith('.PDF'):
            EditPDF.convert_pfd_to_pngs(FileBrowser.Data.file_path)
        else:
            self.error_dialog.showMessage('Selected file is not PDF')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PDF Editor"))
        self.pushButton.setText(_translate("Dialog", "Select File"))
        self.pushButton_2.setText(_translate("Dialog", "Execute"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint |
                               QtCore.Qt.WindowTitleHint |
                               QtCore.Qt.WindowMinimizeButtonHint |
                               QtCore.Qt.WindowCloseButtonHint |
                               QtCore.Qt.WindowStaysOnTopHint)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
