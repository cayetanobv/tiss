# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/ervin/.qgis2/python/plugins/tiss/indicatrix_mapper_dialog_base.ui'
#
# Created: Wed Mar 18 20:34:20 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Tiss(object):
    def setupUi(self, Tiss):
        Tiss.setObjectName(_fromUtf8("Tiss"))
        Tiss.resize(572, 300)
        self.btnRun = QtGui.QPushButton(Tiss)
        self.btnRun.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.layoutWidget = QtGui.QWidget(Tiss)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 440, 152))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 2)
        self.lblLatMin = QtGui.QLabel(self.layoutWidget)
        self.lblLatMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLatMin.setObjectName(_fromUtf8("lblLatMin"))
        self.gridLayout.addWidget(self.lblLatMin, 5, 2, 1, 1)
        self.spbLatMax = QtGui.QSpinBox(self.layoutWidget)
        self.spbLatMax.setMinimum(-89)
        self.spbLatMax.setMaximum(89)
        self.spbLatMax.setProperty("value", 60)
        self.spbLatMax.setObjectName(_fromUtf8("spbLatMax"))
        self.gridLayout.addWidget(self.spbLatMax, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 5, 1, 1)
        self.lblLatMax = QtGui.QLabel(self.layoutWidget)
        self.lblLatMax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLatMax.setObjectName(_fromUtf8("lblLatMax"))
        self.gridLayout.addWidget(self.lblLatMax, 1, 2, 1, 1)
        self.lblLongMin = QtGui.QLabel(self.layoutWidget)
        self.lblLongMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLongMin.setObjectName(_fromUtf8("lblLongMin"))
        self.gridLayout.addWidget(self.lblLongMin, 3, 0, 1, 1)
        self.lblLongMax = QtGui.QLabel(self.layoutWidget)
        self.lblLongMax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLongMax.setObjectName(_fromUtf8("lblLongMax"))
        self.gridLayout.addWidget(self.lblLongMax, 3, 4, 1, 1)
        self.lblRadius = QtGui.QLabel(self.layoutWidget)
        self.lblRadius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblRadius.setObjectName(_fromUtf8("lblRadius"))
        self.gridLayout.addWidget(self.lblRadius, 0, 0, 1, 2)
        self.lblCircleSeg = QtGui.QLabel(self.layoutWidget)
        self.lblCircleSeg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCircleSeg.setObjectName(_fromUtf8("lblCircleSeg"))
        self.gridLayout.addWidget(self.lblCircleSeg, 0, 4, 1, 2)
        self.spbLatRes = QtGui.QSpinBox(self.layoutWidget)
        self.spbLatRes.setProperty("value", 3)
        self.spbLatRes.setObjectName(_fromUtf8("spbLatRes"))
        self.gridLayout.addWidget(self.spbLatRes, 0, 2, 1, 1)
        self.spbLatMin = QtGui.QSpinBox(self.layoutWidget)
        self.spbLatMin.setMinimum(-89)
        self.spbLatMin.setMaximum(89)
        self.spbLatMin.setProperty("value", -60)
        self.spbLatMin.setObjectName(_fromUtf8("spbLatMin"))
        self.gridLayout.addWidget(self.spbLatMin, 4, 2, 1, 1)
        self.spbLongMin = QtGui.QSpinBox(self.layoutWidget)
        self.spbLongMin.setMinimum(-180)
        self.spbLongMin.setMaximum(180)
        self.spbLongMin.setProperty("value", -150)
        self.spbLongMin.setObjectName(_fromUtf8("spbLongMin"))
        self.gridLayout.addWidget(self.spbLongMin, 3, 1, 1, 1)
        self.spbLongMax = QtGui.QSpinBox(self.layoutWidget)
        self.spbLongMax.setMinimum(-180)
        self.spbLongMax.setMaximum(180)
        self.spbLongMax.setProperty("value", 150)
        self.spbLongMax.setObjectName(_fromUtf8("spbLongMax"))
        self.gridLayout.addWidget(self.spbLongMax, 3, 3, 1, 1)
        self.spbLongRes = QtGui.QSpinBox(self.layoutWidget)
        self.spbLongRes.setProperty("value", 9)
        self.spbLongRes.setObjectName(_fromUtf8("spbLongRes"))
        self.gridLayout.addWidget(self.spbLongRes, 2, 6, 1, 1)
        self.spbCircleSeg = QtGui.QSpinBox(self.layoutWidget)
        self.spbCircleSeg.setMinimum(5)
        self.spbCircleSeg.setMaximum(100)
        self.spbCircleSeg.setProperty("value", 50)
        self.spbCircleSeg.setObjectName(_fromUtf8("spbCircleSeg"))
        self.gridLayout.addWidget(self.spbCircleSeg, 0, 6, 1, 1)
        self.spbRadius = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.spbRadius.setDecimals(3)
        self.spbRadius.setMinimum(1.0)
        self.spbRadius.setMaximum(5000.0)
        self.spbRadius.setProperty("value", 800.0)
        self.spbRadius.setObjectName(_fromUtf8("spbRadius"))
        self.gridLayout.addWidget(self.spbRadius, 5, 6, 1, 1)
        self.lblCircleSeg_2 = QtGui.QLabel(self.layoutWidget)
        self.lblCircleSeg_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCircleSeg_2.setObjectName(_fromUtf8("lblCircleSeg_2"))
        self.gridLayout.addWidget(self.lblCircleSeg_2, 1, 4, 1, 2)
        self.spbLineSeg = QtGui.QSpinBox(self.layoutWidget)
        self.spbLineSeg.setMinimum(5)
        self.spbLineSeg.setMaximum(100)
        self.spbLineSeg.setProperty("value", 50)
        self.spbLineSeg.setObjectName(_fromUtf8("spbLineSeg"))
        self.gridLayout.addWidget(self.spbLineSeg, 1, 6, 1, 1)

        self.retranslateUi(Tiss)
        QtCore.QMetaObject.connectSlotsByName(Tiss)

    def retranslateUi(self, Tiss):
        Tiss.setWindowTitle(_translate("Tiss", "Tiss", None))
        self.btnRun.setText(_translate("Tiss", "Run!", None))
        self.label_6.setText(_translate("Tiss", "Longitude resolution:", None))
        self.lblLatMin.setText(_translate("Tiss", "Min. Lat", None))
        self.label_7.setText(_translate("Tiss", "Radius", None))
        self.lblLatMax.setText(_translate("Tiss", "Max. Lat", None))
        self.lblLongMin.setText(_translate("Tiss", "Min Long.", None))
        self.lblLongMax.setText(_translate("Tiss", "Max. Long.", None))
        self.lblRadius.setText(_translate("Tiss", "Latitude resolution: ", None))
        self.lblCircleSeg.setText(_translate("Tiss", "Circle segments", None))
        self.lblCircleSeg_2.setText(_translate("Tiss", "Line segments", None))

