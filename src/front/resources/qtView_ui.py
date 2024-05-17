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
        self.containerInputs = QFrame(self.background)
        self.containerInputs.setObjectName(u"containerInputs")
        self.containerInputs.setGeometry(QRect(20, 400, 330, 160))
        self.containerInputs.setAutoFillBackground(False)
        self.containerInputs.setStyleSheet(u"QFrame#containerInputs{\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: white;\n"
"}")
        self.containerInputs.setFrameShape(QFrame.Shape.NoFrame)
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
        self.valorX.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorX.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
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
        self.valorY.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorY.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
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
        self.valorMassa.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.valorMassa.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
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
        self.ValorVeloX.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloX.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
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
        self.ValorVeloY.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ValorVeloY.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.containerControls = QFrame(self.background)
        self.containerControls.setObjectName(u"containerControls")
        self.containerControls.setEnabled(True)
        self.containerControls.setGeometry(QRect(580, 410, 155, 120))
        self.containerControls.setAutoFillBackground(False)
        self.containerControls.setStyleSheet(u"QFrame#containerControls\n"
"{\n"
"	background-color: black;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: white;\n"
"}")
        self.containerControls.setFrameShape(QFrame.Shape.StyledPanel)
        self.containerControls.setFrameShadow(QFrame.Shadow.Raised)
        self.zoomOut = QPushButton(self.containerControls)
        self.zoomOut.setObjectName(u"zoomOut")
        self.zoomOut.setGeometry(QRect(130, 90, 21, 23))
        self.zoomOut.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomOut.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.zoomIn = QPushButton(self.containerControls)
        self.zoomIn.setObjectName(u"zoomIn")
        self.zoomIn.setGeometry(QRect(130, 55, 23, 23))
        self.zoomIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomIn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.zoomIn.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Right = QPushButton(self.containerControls)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(94, 45, 25, 25))
        self.Right.setAutoFillBackground(False)
        self.Right.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Up = QPushButton(self.containerControls)
        self.Up.setObjectName(u"Up")
        self.Up.setGeometry(QRect(65, 15, 25, 25))
        self.Up.setAutoFillBackground(False)
        self.Up.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Left = QPushButton(self.containerControls)
        self.Left.setObjectName(u"Left")
        self.Left.setGeometry(QRect(35, 45, 25, 25))
        self.Left.setAutoFillBackground(False)
        self.Left.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Down = QPushButton(self.containerControls)
        self.Down.setObjectName(u"Down")
        self.Down.setGeometry(QRect(65, 75, 25, 25))
        self.Down.setAutoFillBackground(False)
        self.Down.setStyleSheet(u"background-color: \"#c2c2c2\";")

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
        self.zoomOut.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color: \"#c2c2c2\";", None))
        self.zoomOut.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.zoomIn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.Right.setText(QCoreApplication.translate("Dialog", u"+X", None))
        self.Up.setText(QCoreApplication.translate("Dialog", u"+Y", None))
        self.Left.setText(QCoreApplication.translate("Dialog", u"-X", None))
        self.Down.setText(QCoreApplication.translate("Dialog", u"-Y", None))
    # retranslateUi

