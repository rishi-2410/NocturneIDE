# Form implementation generated from reading ui file 'src/eric7/UI/VersionsDialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VersionsDialog(object):
    def setupUi(self, VersionsDialog):
        VersionsDialog.setObjectName("VersionsDialog")
        VersionsDialog.resize(550, 600)
        VersionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(VersionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.iconLabel = QtWidgets.QLabel(parent=VersionsDialog)
        self.iconLabel.setText("")
        self.iconLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.textLabel = QtWidgets.QLabel(parent=VersionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel.sizePolicy().hasHeightForWidth())
        self.textLabel.setSizePolicy(sizePolicy)
        self.textLabel.setText("")
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setObjectName("textLabel")
        self.gridLayout.addWidget(self.textLabel, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=VersionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(VersionsDialog)
        self.buttonBox.accepted.connect(VersionsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(VersionsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(VersionsDialog)

    def retranslateUi(self, VersionsDialog):
        pass
