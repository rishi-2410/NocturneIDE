# Form implementation generated from reading ui file 'src/eric7/Plugins/VcsPlugins/vcsMercurial/HgBookmarkRenameDialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HgBookmarkRenameDialog(object):
    def setupUi(self, HgBookmarkRenameDialog):
        HgBookmarkRenameDialog.setObjectName("HgBookmarkRenameDialog")
        HgBookmarkRenameDialog.resize(400, 102)
        HgBookmarkRenameDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgBookmarkRenameDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=HgBookmarkRenameDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(parent=HgBookmarkRenameDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=HgBookmarkRenameDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.bookmarkCombo = QtWidgets.QComboBox(parent=HgBookmarkRenameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmarkCombo.sizePolicy().hasHeightForWidth())
        self.bookmarkCombo.setSizePolicy(sizePolicy)
        self.bookmarkCombo.setEditable(True)
        self.bookmarkCombo.setObjectName("bookmarkCombo")
        self.gridLayout.addWidget(self.bookmarkCombo, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=HgBookmarkRenameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(HgBookmarkRenameDialog)
        self.buttonBox.accepted.connect(HgBookmarkRenameDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(HgBookmarkRenameDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(HgBookmarkRenameDialog)
        HgBookmarkRenameDialog.setTabOrder(self.nameEdit, self.bookmarkCombo)
        HgBookmarkRenameDialog.setTabOrder(self.bookmarkCombo, self.buttonBox)

    def retranslateUi(self, HgBookmarkRenameDialog):
        _translate = QtCore.QCoreApplication.translate
        HgBookmarkRenameDialog.setWindowTitle(_translate("HgBookmarkRenameDialog", "Rename Bookmark"))
        self.label.setText(_translate("HgBookmarkRenameDialog", "New Name:"))
        self.nameEdit.setToolTip(_translate("HgBookmarkRenameDialog", "Enter the bookmark name"))
        self.label_2.setText(_translate("HgBookmarkRenameDialog", "Bookmark:"))
        self.bookmarkCombo.setToolTip(_translate("HgBookmarkRenameDialog", "Enter the bookmark name to be renamed"))
