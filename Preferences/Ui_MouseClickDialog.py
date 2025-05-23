# Form implementation generated from reading ui file 'src/eric7/Preferences/MouseClickDialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MouseClickDialog(object):
    def setupUi(self, MouseClickDialog):
        MouseClickDialog.setObjectName("MouseClickDialog")
        MouseClickDialog.resize(550, 137)
        MouseClickDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MouseClickDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clickGroup = QtWidgets.QGroupBox(parent=MouseClickDialog)
        self.clickGroup.setTitle("")
        self.clickGroup.setObjectName("clickGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.clickGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.clearButton = QtWidgets.QPushButton(parent=self.clickGroup)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 0, 1, 1)
        self.clickEdit = QtWidgets.QLineEdit(parent=self.clickGroup)
        self.clickEdit.setReadOnly(True)
        self.clickEdit.setObjectName("clickEdit")
        self.gridLayout.addWidget(self.clickEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.clickGroup)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.clickGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=MouseClickDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MouseClickDialog)
        self.buttonBox.accepted.connect(MouseClickDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(MouseClickDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MouseClickDialog)

    def retranslateUi(self, MouseClickDialog):
        _translate = QtCore.QCoreApplication.translate
        MouseClickDialog.setWindowTitle(_translate("MouseClickDialog", "Edit Mouse Click"))
        self.clearButton.setToolTip(_translate("MouseClickDialog", "Press to clear the mouse click sequence."))
        self.clearButton.setText(_translate("MouseClickDialog", "Clear"))
        self.label.setText(_translate("MouseClickDialog", "Press the desired modifier keys and then click the desired mouse button."))
