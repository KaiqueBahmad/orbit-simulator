# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QThreadPool,QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
from Receiver import Receiver
import resources.resources_rc as resources_rc
import json
from math import log
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
        self.containerInputs.setGeometry(QRect(0, 440, 330, 160))
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
        self.VelocidadeX.setGeometry(QRect(160, 18, 81, 20))
        self.VelocidadeX.setStyleSheet(u"font: bold 12px;\n"
"color: white;")
        self.VelocidadeY = QLabel(self.containerInputs)
        self.VelocidadeY.setObjectName(u"VelocidadeY")
        self.VelocidadeY.setGeometry(QRect(160, 48, 81, 20))
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
        self.ValorVeloX.setGeometry(QRect(250, 18, 71, 21))
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
        self.ValorVeloY.setGeometry(QRect(250, 48, 71, 21))
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
        self.containerControls.setGeometry(QRect(645, 480, 155, 120))
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
        self.zoomOut.setGeometry(QRect(125, 65, 23, 23))
        self.zoomOut.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomOut.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.zoomIn = QPushButton(self.containerControls)
        self.zoomIn.setObjectName(u"zoomIn")
        self.zoomIn.setGeometry(QRect(125, 35, 23, 23))
        self.zoomIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoomIn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.zoomIn.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Right = QPushButton(self.containerControls)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(70, 50, 25, 25))
        self.Right.setAutoFillBackground(False)
        self.Right.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Up = QPushButton(self.containerControls)
        self.Up.setObjectName(u"Up")
        self.Up.setGeometry(QRect(41, 20, 25, 25))
        self.Up.setAutoFillBackground(False)
        self.Up.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Left = QPushButton(self.containerControls)
        self.Left.setObjectName(u"Left")
        self.Left.setGeometry(QRect(11, 50, 25, 25))
        self.Left.setAutoFillBackground(False)
        self.Left.setStyleSheet(u"background-color: \"#c2c2c2\";")
        self.Down = QPushButton(self.containerControls)
        self.Down.setObjectName(u"Down")
        self.Down.setGeometry(QRect(41, 80, 25, 25))
        self.Down.setAutoFillBackground(False)
        self.Down.setStyleSheet(u"background-color: \"#c2c2c2\";")

        self.planets_queue = []
        receiverInstance = Receiver(self)
        self.planetsOnScreen = []
        self.planetsIncoming = []
        receiverInstance.signals.addPlanetsSignal.connect(self.handlePlanetsUpdate)
        
        
        self.newPlanetForm = {
            "X": self.valorX,
            "Y": self.valorY,
            "Massa": self.valorMassa,
            "Velocidade X": self.ValorVeloX,
            "Velocidade Y": self.ValorVeloY
        }

        self.criarPlaneta.clicked.connect(lambda: self.criarPlanet(self.parseNewPlanetForm(self.newPlanetForm)))
        self.retranslateUi(Dialog)
        self.variationX = 0
        self.variationY = 0
        self.scale      = 1
        
        QMetaObject.connectSlotsByName(Dialog)
        self.threadpool = QThreadPool()
        self.threadpool.start(receiverInstance)
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

        self.zoomOut.clicked.connect(lambda: self.mexerTela("zoomOut"))
        self.zoomIn.clicked.connect(lambda: self.mexerTela("zoomIn"))
        self.Right.clicked.connect(lambda: self.mexerTela("Right"))
        self.Up.clicked.connect(lambda: self.mexerTela("Up"))
        self.Left.clicked.connect(lambda: self.mexerTela("Left"))
        self.Down.clicked.connect(lambda: self.mexerTela("Down"))
    
    def parseNewPlanetForm(self, fields):
        response = {}
        for field_name in fields:
            response.update(
                {field_name: fields[field_name].toPlainText()}
            )
        print(response)
        return response
    # def newPlanetForm(self, planetForm):
    #     for attribute in planetForm:
    #         if not planetForm[attribute] or not planetForm.replace(".","").isnumeric() and planetForm.count(".") <= 1:
    #             return [False]
    #     newForm = {
    #         "mass" : planetForm["Massa"],
    #         "x"    : planetForm["X"],
    #         "y"    : planetForm["Y"],
    #         "vx"   : planetForm["Velocidade X"],
    #         "vy"   : planetForm["Velocidade Y"]
    #     }
    #     return [True, newForm]


    def handlePlanetsUpdate(self, planets_str):
        print("recebi o evento")
        planetsParsed = json.loads(planets_str)
        #print(planetsParsed)
        self.planetsIncoming = [self.mountPlanetInstance(x) for x in planetsParsed]
        for i in self.planetsOnScreen:
            i.deleteLater()
        self.planetsOnScreen = self.planetsIncoming

#    def criarPlanet(self, formDict, Dialog):
#        try:
#            dadosDoPlaneta = {x:int(formDict[x].toPlainText()) for x in formDict}
#        except Exception as ex:
#            return
#        novoPlaneta = QLabel(self.background)
#        novoPlaneta.setObjectName(u"planeta1")
#        novoPlaneta.setGeometry(QRect(30, 30, 30, 30))
#        novoPlaneta.setStyleSheet(u"background-color: #ffffff")
#        novoPlaneta.show()
#    
    def criarPlanet(self, planetForm):
        # for attribute in planetForm:
        #     if not planetForm[attribute] or not planetForm[attribute].replace(".","").isnumeric() and planetForm[attribute].count(".") <= 1:
        #         return [False]
        newForm = {
            "mass" : planetForm["Massa"],
            "x"    : planetForm["X"],
            "y"    : planetForm["Y"],
            "vx"   : planetForm["Velocidade X"],
            "vy"   : planetForm["Velocidade Y"]
        }

        self.planets_queue.append(newForm)

    def replacePlanetsOnScreen(self, planetsData):
        self.addThose(planetsData)
        self.planetsIncoming = [self.mountPlanetInstance(planet) for planet in planetsData]
        for i in self.planetsOnScreen:
            i.deleteLater()
        self.planetsOnScreen = self.planetsIncoming
    
    def mountPlanetInstance(self, planet):
        novoPlaneta = QLabel(self.background)
        novoPlaneta.setGeometry(int((planet["x"]+ self.variationX)*self.scale), int((planet["y"]+ self.variationY)*self.scale), 30, 30)
        novoPlaneta.setStyleSheet("background-color: white")
        novoPlaneta.show()
        print(f"montado em ({planet['x']}, {planet['y']})")
        return novoPlaneta

#this is how to delete a planet
#self.novoPlaneta.deleteLater()

#    [ DEBUG ]
    def mexerTela(self, movimento):
        if movimento == "zoomOut":
            self.scale /= 2
            self.variationX *= 1/2
            self.variationY *= 1/2
        elif movimento == "zoomIn":
            self.scale *= 2
            self.variationX *= 2
            self.variationY *= 2
        elif movimento == "Right":
            self.variationX -= 20 * (1/self.scale)
            print("Right")
        elif movimento == "Up":
            self.variationY += 20 * (1/self.scale)
            print("Up")
        elif movimento == "Left":
            self.variationX += 20 * (1/self.scale)
            print("Left")
        elif movimento == "Down":
            self.variationY -= 20 * (1/self.scale)
            print("Down")
