# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiDesigner/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 621, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(9, 9, 9, 9)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 389, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menusimulation = QtWidgets.QMenu(self.menubar)
        self.menusimulation.setObjectName("menusimulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew_system = QtWidgets.QAction(MainWindow)
        self.actionnew_system.setObjectName("actionnew_system")
        self.actionadd_reaction = QtWidgets.QAction(MainWindow)
        self.actionadd_reaction.setObjectName("actionadd_reaction")
        self.actionedit_state_state = QtWidgets.QAction(MainWindow)
        self.actionedit_state_state.setObjectName("actionedit_state_state")
        self.actionsimulate = QtWidgets.QAction(MainWindow)
        self.actionsimulate.setObjectName("actionsimulate")
        self.actionshow = QtWidgets.QAction(MainWindow)
        self.actionshow.setObjectName("actionshow")
        self.menuedit.addAction(self.actionnew_system)
        self.menuedit.addAction(self.actionadd_reaction)
        self.menuedit.addAction(self.actionedit_state_state)
        self.menusimulation.addAction(self.actionsimulate)
        self.menusimulation.addAction(self.actionshow)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menusimulation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "new system"))
        self.pushButton.setText(_translate("MainWindow", "add reaction"))
        self.pushButton_2.setText(_translate("MainWindow", "edit initial state state"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.menusimulation.setTitle(_translate("MainWindow", "simulation"))
        self.actionnew_system.setText(_translate("MainWindow", "new system"))
        self.actionadd_reaction.setText(_translate("MainWindow", "add reaction"))
        self.actionedit_state_state.setText(_translate("MainWindow", "edit state state"))
        self.actionsimulate.setText(_translate("MainWindow", "simulate"))
        self.actionshow.setText(_translate("MainWindow", "plot"))
