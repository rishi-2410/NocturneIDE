# Form implementation generated from reading ui file 'src/eric7/Preferences/ConfigurationPages/IconsPage.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_IconsPage(object):
    def setupUi(self, IconsPage):
        IconsPage.setObjectName("IconsPage")
        IconsPage.resize(591, 606)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(IconsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(parent=IconsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line10 = QtWidgets.QFrame(parent=IconsPage)
        self.line10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line10.setObjectName("line10")
        self.verticalLayout_2.addWidget(self.line10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=IconsPage)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.iconSizeComboBox = QtWidgets.QComboBox(parent=IconsPage)
        self.iconSizeComboBox.setObjectName("iconSizeComboBox")
        self.horizontalLayout_4.addWidget(self.iconSizeComboBox)
        spacerItem = QtWidgets.QSpacerItem(396, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.TextLabel1_2_2_2 = QtWidgets.QLabel(parent=IconsPage)
        self.TextLabel1_2_2_2.setObjectName("TextLabel1_2_2_2")
        self.verticalLayout_2.addWidget(self.TextLabel1_2_2_2)
        self.vectorIconsCheckBox = QtWidgets.QCheckBox(parent=IconsPage)
        self.vectorIconsCheckBox.setObjectName("vectorIconsCheckBox")
        self.verticalLayout_2.addWidget(self.vectorIconsCheckBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=IconsPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.defaultAutomaticButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.defaultAutomaticButton.setChecked(True)
        self.defaultAutomaticButton.setObjectName("defaultAutomaticButton")
        self.horizontalLayout_3.addWidget(self.defaultAutomaticButton)
        self.defaultBreezeLightButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.defaultBreezeLightButton.setObjectName("defaultBreezeLightButton")
        self.horizontalLayout_3.addWidget(self.defaultBreezeLightButton)
        self.defaultBreezeDarkButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.defaultBreezeDarkButton.setObjectName("defaultBreezeDarkButton")
        self.horizontalLayout_3.addWidget(self.defaultBreezeDarkButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.showDefaultIconsButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.showDefaultIconsButton.setObjectName("showDefaultIconsButton")
        self.horizontalLayout_2.addWidget(self.showDefaultIconsButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(parent=IconsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.iconDirectoryList = QtWidgets.QListWidget(parent=self.groupBox)
        self.iconDirectoryList.setAlternatingRowColors(True)
        self.iconDirectoryList.setObjectName("iconDirectoryList")
        self.gridLayout.addWidget(self.iconDirectoryList, 0, 0, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxlayout.addItem(spacerItem3)
        self.upButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.vboxlayout.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.vboxlayout.addWidget(self.downButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 170, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxlayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteIconDirectoryButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.deleteIconDirectoryButton.setEnabled(False)
        self.deleteIconDirectoryButton.setObjectName("deleteIconDirectoryButton")
        self.horizontalLayout.addWidget(self.deleteIconDirectoryButton)
        self.addIconDirectoryButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.addIconDirectoryButton.setEnabled(False)
        self.addIconDirectoryButton.setObjectName("addIconDirectoryButton")
        self.horizontalLayout.addWidget(self.addIconDirectoryButton)
        self.iconDirectoryPicker = EricPathPicker(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.iconDirectoryPicker.setSizePolicy(sizePolicy)
        self.iconDirectoryPicker.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.iconDirectoryPicker.setObjectName("iconDirectoryPicker")
        self.horizontalLayout.addWidget(self.iconDirectoryPicker)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.showIconsButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.showIconsButton.setEnabled(False)
        self.showIconsButton.setObjectName("showIconsButton")
        self.gridLayout.addWidget(self.showIconsButton, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(IconsPage)
        QtCore.QMetaObject.connectSlotsByName(IconsPage)
        IconsPage.setTabOrder(self.iconSizeComboBox, self.vectorIconsCheckBox)
        IconsPage.setTabOrder(self.vectorIconsCheckBox, self.defaultAutomaticButton)
        IconsPage.setTabOrder(self.defaultAutomaticButton, self.defaultBreezeLightButton)
        IconsPage.setTabOrder(self.defaultBreezeLightButton, self.defaultBreezeDarkButton)
        IconsPage.setTabOrder(self.defaultBreezeDarkButton, self.showDefaultIconsButton)
        IconsPage.setTabOrder(self.showDefaultIconsButton, self.iconDirectoryList)
        IconsPage.setTabOrder(self.iconDirectoryList, self.iconDirectoryPicker)
        IconsPage.setTabOrder(self.iconDirectoryPicker, self.addIconDirectoryButton)
        IconsPage.setTabOrder(self.addIconDirectoryButton, self.showIconsButton)
        IconsPage.setTabOrder(self.showIconsButton, self.deleteIconDirectoryButton)
        IconsPage.setTabOrder(self.deleteIconDirectoryButton, self.upButton)
        IconsPage.setTabOrder(self.upButton, self.downButton)

    def retranslateUi(self, IconsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("IconsPage", "<b>Configure icons</b>"))
        self.label_5.setText(_translate("IconsPage", "Icon Size:"))
        self.iconSizeComboBox.setToolTip(_translate("IconsPage", "Select the icon size"))
        self.TextLabel1_2_2_2.setText(_translate("IconsPage", "<font color=\"#FF0000\"><b>Note:</b> All settings below are activated at the next startup of the application.</font>"))
        self.vectorIconsCheckBox.setToolTip(_translate("IconsPage", "Select this in order to prefer vector based SVG icons (pixel based icons as fallback). If unchecked pixel based are prefered."))
        self.vectorIconsCheckBox.setText(_translate("IconsPage", "Prefer Vector Icons (SVG Icons)"))
        self.groupBox_2.setTitle(_translate("IconsPage", "Default Icons"))
        self.defaultAutomaticButton.setToolTip(_translate("IconsPage", "Select to select between Breeze (dark) and Breeze (light) based on the window lightness"))
        self.defaultAutomaticButton.setText(_translate("IconsPage", "Automatic"))
        self.defaultBreezeLightButton.setToolTip(_translate("IconsPage", "Select to use the Breeze vector icons for light window background"))
        self.defaultBreezeLightButton.setText(_translate("IconsPage", "Breeze (light)"))
        self.defaultBreezeDarkButton.setToolTip(_translate("IconsPage", "Select to use the Breeze vector icons for dark window background"))
        self.defaultBreezeDarkButton.setText(_translate("IconsPage", "Breeze (dark)"))
        self.showDefaultIconsButton.setToolTip(_translate("IconsPage", "Press to show a dialog with a preview of the selected default icon set"))
        self.showDefaultIconsButton.setText(_translate("IconsPage", "Show"))
        self.groupBox.setTitle(_translate("IconsPage", "Custom Icon Directories"))
        self.iconDirectoryList.setToolTip(_translate("IconsPage", "List of icon directories"))
        self.upButton.setText(_translate("IconsPage", "Up"))
        self.downButton.setText(_translate("IconsPage", "Down"))
        self.deleteIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to delete the selected directory from the list"))
        self.deleteIconDirectoryButton.setText(_translate("IconsPage", "Delete"))
        self.addIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to add the entered directory to the list"))
        self.addIconDirectoryButton.setText(_translate("IconsPage", "Add"))
        self.showIconsButton.setText(_translate("IconsPage", "Show"))
from eric7.EricWidgets.EricPathPicker import EricPathPicker
