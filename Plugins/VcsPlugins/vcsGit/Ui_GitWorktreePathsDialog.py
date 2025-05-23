# Form implementation generated from reading ui file 'src/eric7/Plugins/VcsPlugins/vcsGit/GitWorktreePathsDialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GitWorktreePathsDialog(object):
    def setupUi(self, GitWorktreePathsDialog):
        GitWorktreePathsDialog.setObjectName("GitWorktreePathsDialog")
        GitWorktreePathsDialog.resize(600, 400)
        GitWorktreePathsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(GitWorktreePathsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pathsList = QtWidgets.QListWidget(parent=GitWorktreePathsDialog)
        self.pathsList.setAlternatingRowColors(True)
        self.pathsList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.pathsList.setObjectName("pathsList")
        self.gridLayout.addWidget(self.pathsList, 0, 0, 5, 1)
        self.addButton = QtWidgets.QPushButton(parent=GitWorktreePathsDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.addLine = QtWidgets.QFrame(parent=GitWorktreePathsDialog)
        self.addLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.addLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.addLine.setObjectName("addLine")
        self.gridLayout.addWidget(self.addLine, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(parent=GitWorktreePathsDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(parent=GitWorktreePathsDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=GitWorktreePathsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GitWorktreePathsDialog)
        self.buttonBox.accepted.connect(GitWorktreePathsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(GitWorktreePathsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(GitWorktreePathsDialog)

    def retranslateUi(self, GitWorktreePathsDialog):
        _translate = QtCore.QCoreApplication.translate
        GitWorktreePathsDialog.setWindowTitle(_translate("GitWorktreePathsDialog", "Git Worktree Paths"))
        self.pathsList.setSortingEnabled(True)
        self.addButton.setToolTip(_translate("GitWorktreePathsDialog", "Press to add an entry"))
        self.addButton.setText(_translate("GitWorktreePathsDialog", "&Add..."))
        self.removeButton.setToolTip(_translate("GitWorktreePathsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("GitWorktreePathsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("GitWorktreePathsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("GitWorktreePathsDialog", "R&emove All"))
