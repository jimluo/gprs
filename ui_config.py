# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gprs_config.ui'
#
# Created: Tue Mar  3 14:36:35 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_config(object):
    def setupUi(self, config):
        config.setObjectName("config")
        config.resize(664, 445)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        config.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(config)
        self.label.setGeometry(QtCore.QRect(20, 14, 54, 12))
        self.label.setObjectName("label")
        self.mail = QtWidgets.QLineEdit(config)
        self.mail.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.mail.setObjectName("mail")
        self.label_2 = QtWidgets.QLabel(config)
        self.label_2.setGeometry(QtCore.QRect(210, 14, 54, 12))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(config)
        self.name.setGeometry(QtCore.QRect(250, 10, 171, 20))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(config)
        self.label_3.setGeometry(QtCore.QRect(460, 14, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pwd = QtWidgets.QLineEdit(config)
        self.pwd.setGeometry(QtCore.QRect(490, 10, 113, 20))
        self.pwd.setObjectName("pwd")
        self.label_4 = QtWidgets.QLabel(config)
        self.label_4.setGeometry(QtCore.QRect(20, 48, 54, 12))
        self.label_4.setObjectName("label_4")
        self.current = QtWidgets.QSpinBox(config)
        self.current.setGeometry(QtCore.QRect(80, 42, 91, 22))
        self.current.setMinimum(1)
        self.current.setMaximum(8)
        self.current.setProperty("value", 5)
        self.current.setObjectName("current")
        self.wells = QtWidgets.QTableWidget(config)
        self.wells.setGeometry(QtCore.QRect(20, 100, 621, 291))
        self.wells.setAlternatingRowColors(True)
        self.wells.setObjectName("wells")
        self.wells.setColumnCount(10)
        self.wells.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.wells.setHorizontalHeaderItem(9, item)
        self.wells.horizontalHeader().setDefaultSectionSize(56)
        self.label_5 = QtWidgets.QLabel(config)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_5.setObjectName("label_5")
        self.btnOK = QtWidgets.QPushButton(config)
        self.btnOK.setGeometry(QtCore.QRect(440, 410, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnExit = QtWidgets.QPushButton(config)
        self.btnExit.setGeometry(QtCore.QRect(560, 410, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.btnAppend = QtWidgets.QToolButton(config)
        self.btnAppend.setGeometry(QtCore.QRect(490, 80, 71, 18))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/append.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAppend.setIcon(icon1)
        self.btnAppend.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnAppend.setObjectName("btnAppend")
        self.btnDelete = QtWidgets.QToolButton(config)
        self.btnDelete.setGeometry(QtCore.QRect(570, 80, 71, 18))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon2)
        self.btnDelete.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(config)
        self.btnExit.clicked.connect(config.close)
        self.btnOK.clicked.connect(config.saveCfg)
        self.btnAppend.clicked.connect(config.appendRow)
        self.btnDelete.clicked.connect(config.deleteRow)
        QtCore.QMetaObject.connectSlotsByName(config)

    def retranslateUi(self, config):
        _translate = QtCore.QCoreApplication.translate
        config.setWindowTitle(_translate("config", "配置"))
        self.label.setText(_translate("config", "邮箱"))
        self.label_2.setText(_translate("config", "用户名"))
        self.label_3.setText(_translate("config", "密码"))
        self.label_4.setText(_translate("config", "电流范围"))
        self.current.setSuffix(_translate("config", "A"))
        self.current.setPrefix(_translate("config", "±"))
        item = self.wells.horizontalHeaderItem(0)
        item.setText(_translate("config", "井区"))
        item = self.wells.horizontalHeaderItem(1)
        item.setText(_translate("config", "井组"))
        item = self.wells.horizontalHeaderItem(2)
        item.setText(_translate("config", "井场"))
        item = self.wells.horizontalHeaderItem(3)
        item.setText(_translate("config", "电话"))
        item = self.wells.horizontalHeaderItem(4)
        item.setText(_translate("config", "井号1"))
        item = self.wells.horizontalHeaderItem(5)
        item.setText(_translate("config", "井号2"))
        item = self.wells.horizontalHeaderItem(6)
        item.setText(_translate("config", "井号3"))
        item = self.wells.horizontalHeaderItem(7)
        item.setText(_translate("config", "井号4"))
        item = self.wells.horizontalHeaderItem(8)
        item.setText(_translate("config", "井号5"))
        item = self.wells.horizontalHeaderItem(9)
        item.setText(_translate("config", "井号6"))
        self.label_5.setText(_translate("config", "井区"))
        self.btnOK.setText(_translate("config", "确定"))
        self.btnExit.setText(_translate("config", "退出"))
        self.btnAppend.setText(_translate("config", "插入行"))
        self.btnDelete.setText(_translate("config", "删除行"))

import res_rc
