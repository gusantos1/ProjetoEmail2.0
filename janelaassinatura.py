# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janelaassinatura.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AssDigital(object):
    def setupUi(self, AssDigital):
        AssDigital.setObjectName("AssDigital")
        AssDigital.resize(805, 46)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AssDigital.sizePolicy().hasHeightForWidth())
        AssDigital.setSizePolicy(sizePolicy)
        AssDigital.setMinimumSize(QtCore.QSize(805, 46))
        AssDigital.setMaximumSize(QtCore.QSize(805, 46))
        self.centralwidget = QtWidgets.QWidget(AssDigital)
        self.centralwidget.setMaximumSize(QtCore.QSize(805, 46))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(805, 46))
        self.widget.setObjectName("widget")
        self.btn_box = QtWidgets.QDialogButtonBox(self.widget)
        self.btn_box.setGeometry(QtCore.QRect(610, 0, 176, 28))
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.le_assinatura = QtWidgets.QLineEdit(self.widget)
        self.le_assinatura.setGeometry(QtCore.QRect(0, 0, 601, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_assinatura.sizePolicy().hasHeightForWidth())
        self.le_assinatura.setSizePolicy(sizePolicy)
        self.le_assinatura.setObjectName("le_assinatura")
        self.horizontalLayout.addWidget(self.widget)
        AssDigital.setCentralWidget(self.centralwidget)

        self.retranslateUi(AssDigital)
        QtCore.QMetaObject.connectSlotsByName(AssDigital)

    def retranslateUi(self, AssDigital):
        _translate = QtCore.QCoreApplication.translate
        AssDigital.setWindowTitle(_translate("AssDigital", "ASSINATURA DIGITAL"))
