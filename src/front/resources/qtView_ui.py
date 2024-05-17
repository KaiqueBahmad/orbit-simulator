# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.background = QFrame(Dialog)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 800, 600))
        self.background.setAcceptDrops(False)
        self.background.setStyleSheet(u"QFrame#background {\n"
"	background-repeat: no-repet;\n"
"	background-position: center;\n"
"	border-image: url(:/back-sky/back-sky.jpg) 0 0 0 0 stretch stretch;\n"
"}")
        self.background.setFrameShape(QFrame.Shape.NoFrame)
        self.containerInputs_3 = QFrame(self.background)
        self.containerInputs_3.setObjectName(u"containerInputs_3")
        self.containerInputs_3.setGeometry(QRect(20, 400, 330, 160))
        self.containerInputs_3.setStyleSheet(u"QFrame#containerInputs{\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: white;\n"
"}")
        self.containerInputs_3.setFrameShape(QFrame.Shape.NoFrame)
        self.X_3 = QLabel(self.containerInputs_3)
        self.X_3.setObjectName(u"X_3")
        self.X_3.setGeometry(QRect(20, 20, 16, 20))
        self.X_3.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.Y_3 = QLabel(self.containerInputs_3)
        self.Y_3.setObjectName(u"Y_3")
        self.Y_3.setGeometry(QRect(20, 50, 16, 20))
        self.Y_3.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.Massa_3 = QLabel(self.containerInputs_3)
        self.Massa_3.setObjectName(u"Massa_3")
        self.Massa_3.setGeometry(QRect(20, 80, 41, 20))
        self.Massa_3.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.VelocidadeX_3 = QLabel(self.containerInputs_3)
        self.VelocidadeX_3.setObjectName(u"VelocidadeX_3")
        self.VelocidadeX_3.setGeometry(QRect(160, 20, 81, 20))
        self.VelocidadeX_3.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.VelocidadeY_3 = QLabel(self.containerInputs_3)
        self.VelocidadeY_3.setObjectName(u"VelocidadeY_3")
        self.VelocidadeY_3.setGeometry(QRect(160, 50, 81, 20))
        self.VelocidadeY_3.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.valorX_3 = QTextEdit(self.containerInputs_3)
        self.valorX_3.setObjectName(u"valorX_3")
        self.valorX_3.setGeometry(QRect(70, 20, 71, 21))
        self.valorX_3.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorX_3.setAcceptDrops(True)
        self.valorX_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorX_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorX_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.criarPlaneta_3 = QPushButton(self.containerInputs_3)
        self.criarPlaneta_3.setObjectName(u"criarPlaneta_3")
        self.criarPlaneta_3.setGeometry(QRect(130, 120, 75, 23))
        self.criarPlaneta_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.criarPlaneta_3.setStyleSheet(u"background-color: \"#5bc400\";\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;")
        self.valorY_3 = QTextEdit(self.containerInputs_3)
        self.valorY_3.setObjectName(u"valorY_3")
        self.valorY_3.setGeometry(QRect(70, 50, 71, 21))
        self.valorY_3.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorY_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorY_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorY_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorMassa_3 = QTextEdit(self.containerInputs_3)
        self.valorMassa_3.setObjectName(u"valorMassa_3")
        self.valorMassa_3.setGeometry(QRect(70, 80, 71, 21))
        self.valorMassa_3.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.valorMassa_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.valorMassa_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorMassa_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloX_3 = QTextEdit(self.containerInputs_3)
        self.ValorVeloX_3.setObjectName(u"ValorVeloX_3")
        self.ValorVeloX_3.setGeometry(QRect(250, 20, 71, 21))
        self.ValorVeloX_3.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ValorVeloX_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.ValorVeloX_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloX_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloY_3 = QTextEdit(self.containerInputs_3)
        self.ValorVeloY_3.setObjectName(u"ValorVeloY_3")
        self.ValorVeloY_3.setGeometry(QRect(250, 50, 71, 21))
        self.ValorVeloY_3.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ValorVeloY_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;\n"
"height: 20px;\n"
"background-color: white;\n"
"color: black;")
        self.ValorVeloY_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloY_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.zoomIn_3 = QPushButton(self.background)
        self.zoomIn_3.setObjectName(u"zoomIn_3")
        self.zoomIn_3.setGeometry(QRect(700, 435, 21, 23))
        self.zoomIn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomIn_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.zoomIn_3.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.zoomOut_3 = QPushButton(self.background)
        self.zoomOut_3.setObjectName(u"zoomOut_3")
        self.zoomOut_3.setGeometry(QRect(700, 480, 21, 23))
        self.zoomOut_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomOut_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.X_3.setText(QCoreApplication.translate("Dialog", u"X:", None))
        self.Y_3.setText(QCoreApplication.translate("Dialog", u"Y:", None))
        self.Massa_3.setText(QCoreApplication.translate("Dialog", u"Massa:", None))
        self.VelocidadeX_3.setText(QCoreApplication.translate("Dialog", u"VelocidadeX:", None))
        self.VelocidadeY_3.setText(QCoreApplication.translate("Dialog", u"VelocidadeY:", None))
        self.criarPlaneta_3.setText(QCoreApplication.translate("Dialog", u"Criar Planeta", None))
        self.zoomIn_3.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.zoomOut_3.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: \"#c2c2c2\";", None))
        self.zoomOut_3.setText(QCoreApplication.translate("Dialog", u"-", None))
    # retranslateUi

