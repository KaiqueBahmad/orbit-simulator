# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtViewIPlDIB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1396, 924)
        self.background = QFrame(Dialog)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1401, 931))
        self.background.setAcceptDrops(False)
        self.background.setStyleSheet(u"QFrame#background {\n"
"	background-repeat: no-repet;\n"
"	background-position: center;\n"
"	border-image: url(:/imgs/assets/bg2.jpg) 0 0 0 0 stretch stretch;\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.containerInputs = QFrame(self.background)
        self.containerInputs.setObjectName(u"containerInputs")
        self.containerInputs.setGeometry(QRect(0, 764, 341, 161))
        self.containerInputs.setStyleSheet(u"QFrame#containerInputs{\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: white;\n"
"}")
        self.containerInputs.setFrameShape(QFrame.StyledPanel)
        self.containerInputs.setFrameShadow(QFrame.Raised)
        self.X = QLabel(self.containerInputs)
        self.X.setObjectName(u"X")
        self.X.setGeometry(QRect(20, 20, 16, 20))
        self.X.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.Y = QLabel(self.containerInputs)
        self.Y.setObjectName(u"Y")
        self.Y.setGeometry(QRect(20, 50, 16, 20))
        self.Y.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.Massa = QLabel(self.containerInputs)
        self.Massa.setObjectName(u"Massa")
        self.Massa.setGeometry(QRect(20, 80, 41, 20))
        self.Massa.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.VelocidadeX = QLabel(self.containerInputs)
        self.VelocidadeX.setObjectName(u"VelocidadeX")
        self.VelocidadeX.setGeometry(QRect(160, 20, 81, 20))
        self.VelocidadeX.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.VelocidadeY = QLabel(self.containerInputs)
        self.VelocidadeY.setObjectName(u"VelocidadeY")
        self.VelocidadeY.setGeometry(QRect(160, 50, 81, 20))
        self.VelocidadeY.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.valorX = QTextEdit(self.containerInputs)
        self.valorX.setObjectName(u"valorX")
        self.valorX.setGeometry(QRect(70, 20, 71, 21))
        self.valorX.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorX.setAcceptDrops(True)
        self.valorX.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorX.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.valorX.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.criarPlaneta = QPushButton(self.containerInputs)
        self.criarPlaneta.setObjectName(u"criarPlaneta")
        self.criarPlaneta.setGeometry(QRect(130, 120, 75, 23))
        self.criarPlaneta.setCursor(QCursor(Qt.PointingHandCursor))
        self.criarPlaneta.setStyleSheet(u"background-color: \"#5bc400\";\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;")
        self.valorY = QTextEdit(self.containerInputs)
        self.valorY.setObjectName(u"valorY")
        self.valorY.setGeometry(QRect(70, 50, 71, 21))
        self.valorY.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorY.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorY.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.valorY.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.valorMassa = QTextEdit(self.containerInputs)
        self.valorMassa.setObjectName(u"valorMassa")
        self.valorMassa.setGeometry(QRect(70, 80, 71, 21))
        self.valorMassa.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorMassa.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorMassa.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.valorMassa.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ValorVeloX = QTextEdit(self.containerInputs)
        self.ValorVeloX.setObjectName(u"ValorVeloX")
        self.ValorVeloX.setGeometry(QRect(250, 20, 71, 21))
        self.ValorVeloX.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ValorVeloX.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.ValorVeloX.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ValorVeloX.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ValorVeloY = QTextEdit(self.containerInputs)
        self.ValorVeloY.setObjectName(u"ValorVeloY")
        self.ValorVeloY.setGeometry(QRect(250, 50, 71, 21))
        self.ValorVeloY.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ValorVeloY.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.ValorVeloY.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ValorVeloY.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.zoomIn = QPushButton(self.background)
        self.zoomIn.setObjectName(u"zoomIn")
        self.zoomIn.setGeometry(QRect(1330, 800, 21, 23))
        self.zoomIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomIn.setContextMenuPolicy(Qt.PreventContextMenu)
        self.zoomIn.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.zoomOut = QPushButton(self.background)
        self.zoomOut.setObjectName(u"zoomOut")
        self.zoomOut.setGeometry(QRect(1330, 830, 21, 23))
        self.zoomOut.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomOut.setContextMenuPolicy(Qt.PreventContextMenu)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.X.setText(QCoreApplication.translate("Dialog", u"X:", None))
        self.Y.setText(QCoreApplication.translate("Dialog", u"Y:", None))
        self.Massa.setText(QCoreApplication.translate("Dialog", u"Massa:", None))
        self.VelocidadeX.setText(QCoreApplication.translate("Dialog", u"VelocidadeX:", None))
        self.VelocidadeY.setText(QCoreApplication.translate("Dialog", u"VelocidadeY:", None))
        self.criarPlaneta.setText(QCoreApplication.translate("Dialog", u"Criar Planeta", None))
        self.zoomIn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.zoomOut.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: \"#c2c2c2\";", None))
        self.zoomOut.setText(QCoreApplication.translate("Dialog", u"-", None))
    # retranslateUi

