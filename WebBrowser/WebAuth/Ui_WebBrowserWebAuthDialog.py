# Form implementation generated from reading ui file 'src/eric7/WebBrowser/WebAuth/WebBrowserWebAuthDialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WebBrowserWebAuthDialog(object):
    def setupUi(self, WebBrowserWebAuthDialog):
        WebBrowserWebAuthDialog.setObjectName("WebBrowserWebAuthDialog")
        WebBrowserWebAuthDialog.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WebBrowserWebAuthDialog.sizePolicy().hasHeightForWidth())
        WebBrowserWebAuthDialog.setSizePolicy(sizePolicy)
        WebBrowserWebAuthDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(WebBrowserWebAuthDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(parent=WebBrowserWebAuthDialog)
        self.headerLabel.setText("Header")
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.descriptionLabel = QtWidgets.QLabel(parent=WebBrowserWebAuthDialog)
        self.descriptionLabel.setText("Description")
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.verticalLayout.addWidget(self.descriptionLabel)
        self.pinGroupBox = QtWidgets.QGroupBox(parent=WebBrowserWebAuthDialog)
        self.pinGroupBox.setFlat(True)
        self.pinGroupBox.setObjectName("pinGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.pinGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pinLabel = QtWidgets.QLabel(parent=self.pinGroupBox)
        self.pinLabel.setObjectName("pinLabel")
        self.gridLayout.addWidget(self.pinLabel, 0, 0, 1, 1)
        self.pinEdit = QtWidgets.QLineEdit(parent=self.pinGroupBox)
        self.pinEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pinEdit.setObjectName("pinEdit")
        self.gridLayout.addWidget(self.pinEdit, 0, 1, 1, 1)
        self.pinButton = QtWidgets.QToolButton(parent=self.pinGroupBox)
        self.pinButton.setCheckable(True)
        self.pinButton.setObjectName("pinButton")
        self.gridLayout.addWidget(self.pinButton, 0, 2, 1, 1)
        self.confirmPinLabel = QtWidgets.QLabel(parent=self.pinGroupBox)
        self.confirmPinLabel.setObjectName("confirmPinLabel")
        self.gridLayout.addWidget(self.confirmPinLabel, 1, 0, 1, 1)
        self.confirmPinEdit = QtWidgets.QLineEdit(parent=self.pinGroupBox)
        self.confirmPinEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirmPinEdit.setObjectName("confirmPinEdit")
        self.gridLayout.addWidget(self.confirmPinEdit, 1, 1, 1, 1)
        self.confirmPinErrorLabel = QtWidgets.QLabel(parent=self.pinGroupBox)
        self.confirmPinErrorLabel.setObjectName("confirmPinErrorLabel")
        self.gridLayout.addWidget(self.confirmPinErrorLabel, 2, 1, 1, 2)
        self.pinErrorLabel = QtWidgets.QLabel(parent=self.pinGroupBox)
        self.pinErrorLabel.setText("PIN Error")
        self.pinErrorLabel.setWordWrap(True)
        self.pinErrorLabel.setObjectName("pinErrorLabel")
        self.gridLayout.addWidget(self.pinErrorLabel, 3, 0, 1, 3)
        self.verticalLayout.addWidget(self.pinGroupBox)
        self.selectAccountArea = QtWidgets.QScrollArea(parent=WebBrowserWebAuthDialog)
        self.selectAccountArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.selectAccountArea.setObjectName("selectAccountArea")
        self.selectAccountWidget = QtWidgets.QWidget()
        self.selectAccountWidget.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.selectAccountWidget.setObjectName("selectAccountWidget")
        self.selectAccountArea.setWidget(self.selectAccountWidget)
        self.verticalLayout.addWidget(self.selectAccountArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=WebBrowserWebAuthDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok|QtWidgets.QDialogButtonBox.StandardButton.Retry)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(WebBrowserWebAuthDialog)
        QtCore.QMetaObject.connectSlotsByName(WebBrowserWebAuthDialog)
        WebBrowserWebAuthDialog.setTabOrder(self.pinEdit, self.pinButton)
        WebBrowserWebAuthDialog.setTabOrder(self.pinButton, self.confirmPinEdit)
        WebBrowserWebAuthDialog.setTabOrder(self.confirmPinEdit, self.selectAccountArea)

    def retranslateUi(self, WebBrowserWebAuthDialog):
        _translate = QtCore.QCoreApplication.translate
        WebBrowserWebAuthDialog.setWindowTitle(_translate("WebBrowserWebAuthDialog", "Web Authentication"))
        self.pinLabel.setText(_translate("WebBrowserWebAuthDialog", "PIN:"))
        self.pinEdit.setToolTip(_translate("WebBrowserWebAuthDialog", "Enter the PIN"))
        self.pinButton.setToolTip(_translate("WebBrowserWebAuthDialog", "Press to show or hide the PIN."))
        self.confirmPinLabel.setText(_translate("WebBrowserWebAuthDialog", "Confirm PIN:"))
        self.confirmPinEdit.setToolTip(_translate("WebBrowserWebAuthDialog", "Enter the same PIN again."))
        self.confirmPinErrorLabel.setText(_translate("WebBrowserWebAuthDialog", "PINs do not match!"))
