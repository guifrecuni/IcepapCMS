# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encoders.ui'
#
# Created: Fri Mar 26 13:02:56 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_encoders(object):
    def setupUi(self, encoders):
        encoders.setObjectName("encoders")
        encoders.resize(478, 470)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(encoders.sizePolicy().hasHeightForWidth())
        encoders.setSizePolicy(sizePolicy)
        encoders.setMinimumSize(QtCore.QSize(410, 470))
        self.gridlayout = QtGui.QGridLayout(encoders)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")
        self.encoders_frame = QtGui.QFrame(encoders)
        self.encoders_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.encoders_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.encoders_frame.setObjectName("encoders_frame")
        self.gridLayout = QtGui.QGridLayout(self.encoders_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtGui.QGroupBox(self.encoders_frame)
        self.groupBox.setMinimumSize(QtCore.QSize(185, 142))
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setSpacing(10)
        self.vboxlayout1.setContentsMargins(-1, -1, 3, 10)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.cfgEINMODE = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEINMODE.sizePolicy().hasHeightForWidth())
        self.cfgEINMODE.setSizePolicy(sizePolicy)
        self.cfgEINMODE.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgEINMODE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgEINMODE.setObjectName("cfgEINMODE")
        self.gridlayout1.addWidget(self.cfgEINMODE, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 1, 0, 1, 1)
        self.cfgEINSENSE = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEINSENSE.sizePolicy().hasHeightForWidth())
        self.cfgEINSENSE.setSizePolicy(sizePolicy)
        self.cfgEINSENSE.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgEINSENSE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgEINSENSE.setObjectName("cfgEINSENSE")
        self.gridlayout1.addWidget(self.cfgEINSENSE, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem1, 0, 2, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(5)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(55, 16))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_3.setObjectName("label_3")
        self.hboxlayout.addWidget(self.label_3)
        self.line = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(5, 35))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setContentsMargins(-1, 0, -1, 0)
        self.gridlayout2.setObjectName("gridlayout2")
        self.cfgEINNSTEP = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEINNSTEP.sizePolicy().hasHeightForWidth())
        self.cfgEINNSTEP.setSizePolicy(sizePolicy)
        self.cfgEINNSTEP.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgEINNSTEP.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgEINNSTEP.setMaximum(999999999)
        self.cfgEINNSTEP.setObjectName("cfgEINNSTEP")
        self.gridlayout2.addWidget(self.cfgEINNSTEP, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 16))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_5.setObjectName("label_5")
        self.gridlayout2.addWidget(self.label_5, 0, 1, 1, 1)
        self.cfgEINNTURN = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEINNTURN.sizePolicy().hasHeightForWidth())
        self.cfgEINNTURN.setSizePolicy(sizePolicy)
        self.cfgEINNTURN.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgEINNTURN.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgEINNTURN.setMaximum(999999999)
        self.cfgEINNTURN.setObjectName("cfgEINNTURN")
        self.gridlayout2.addWidget(self.cfgEINNTURN, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 16))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_6.setObjectName("label_6")
        self.gridlayout2.addWidget(self.label_6, 1, 1, 1, 1)
        self.hboxlayout.addLayout(self.gridlayout2)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(70, 16))
        self.label_4.setMaximumSize(QtCore.QSize(80, 36))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.hboxlayout1.addWidget(self.label_4)
        self.cfgEINAUXPOL = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEINAUXPOL.sizePolicy().hasHeightForWidth())
        self.cfgEINAUXPOL.setSizePolicy(sizePolicy)
        self.cfgEINAUXPOL.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgEINAUXPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgEINAUXPOL.setFont(font)
        self.cfgEINAUXPOL.setObjectName("cfgEINAUXPOL")
        self.hboxlayout1.addWidget(self.cfgEINAUXPOL)
        spacerItem2 = QtGui.QSpacerItem(50, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.encoders_frame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(185, 142))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setSpacing(10)
        self.vboxlayout2.setContentsMargins(-1, -1, 3, -1)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setObjectName("gridlayout3")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(50, 16))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_10.setObjectName("label_10")
        self.gridlayout3.addWidget(self.label_10, 0, 0, 1, 1)
        self.cfgINPMODE = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINPMODE.sizePolicy().hasHeightForWidth())
        self.cfgINPMODE.setSizePolicy(sizePolicy)
        self.cfgINPMODE.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgINPMODE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINPMODE.setObjectName("cfgINPMODE")
        self.gridlayout3.addWidget(self.cfgINPMODE, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(50, 16))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_11.setObjectName("label_11")
        self.gridlayout3.addWidget(self.label_11, 1, 0, 1, 1)
        self.cfgINPSENSE = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINPSENSE.sizePolicy().hasHeightForWidth())
        self.cfgINPSENSE.setSizePolicy(sizePolicy)
        self.cfgINPSENSE.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgINPSENSE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINPSENSE.setObjectName("cfgINPSENSE")
        self.gridlayout3.addWidget(self.cfgINPSENSE, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem4, 0, 2, 1, 1)
        self.vboxlayout2.addLayout(self.gridlayout3)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(5)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(55, 16))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_7.setObjectName("label_7")
        self.hboxlayout2.addWidget(self.label_7)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(5, 35))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hboxlayout2.addWidget(self.line_2)
        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setSpacing(5)
        self.gridlayout4.setContentsMargins(-1, 0, -1, 0)
        self.gridlayout4.setObjectName("gridlayout4")
        self.cfgINPNSTEP = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINPNSTEP.sizePolicy().hasHeightForWidth())
        self.cfgINPNSTEP.setSizePolicy(sizePolicy)
        self.cfgINPNSTEP.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgINPNSTEP.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINPNSTEP.setMaximum(999999999)
        self.cfgINPNSTEP.setObjectName("cfgINPNSTEP")
        self.gridlayout4.addWidget(self.cfgINPNSTEP, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(50, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_8.setObjectName("label_8")
        self.gridlayout4.addWidget(self.label_8, 0, 1, 1, 1)
        self.cfgINPNTURN = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINPNTURN.sizePolicy().hasHeightForWidth())
        self.cfgINPNTURN.setSizePolicy(sizePolicy)
        self.cfgINPNTURN.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgINPNTURN.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINPNTURN.setMaximum(999999999)
        self.cfgINPNTURN.setObjectName("cfgINPNTURN")
        self.gridlayout4.addWidget(self.cfgINPNTURN, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(50, 16))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_9.setObjectName("label_9")
        self.gridlayout4.addWidget(self.label_9, 1, 1, 1, 1)
        self.hboxlayout2.addLayout(self.gridlayout4)
        self.vboxlayout2.addLayout(self.hboxlayout2)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(80, 44))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.hboxlayout3.addWidget(self.label_12)
        self.cfgINPAUXPOL = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINPAUXPOL.sizePolicy().hasHeightForWidth())
        self.cfgINPAUXPOL.setSizePolicy(sizePolicy)
        self.cfgINPAUXPOL.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgINPAUXPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgINPAUXPOL.setFont(font)
        self.cfgINPAUXPOL.setObjectName("cfgINPAUXPOL")
        self.hboxlayout3.addWidget(self.cfgINPAUXPOL)
        spacerItem5 = QtGui.QSpacerItem(50, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem5)
        self.vboxlayout2.addLayout(self.hboxlayout3)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.encoders_frame)
        self.groupBox_3.setMinimumSize(QtCore.QSize(185, 150))
        self.groupBox_3.setObjectName("groupBox_3")
        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout3.setSpacing(10)
        self.vboxlayout3.setContentsMargins(-1, -1, -1, 35)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(50, 16))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_17.setObjectName("label_17")
        self.hboxlayout4.addWidget(self.label_17)
        self.cfgABSSENSE = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgABSSENSE.sizePolicy().hasHeightForWidth())
        self.cfgABSSENSE.setSizePolicy(sizePolicy)
        self.cfgABSSENSE.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgABSSENSE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgABSSENSE.setObjectName("cfgABSSENSE")
        self.hboxlayout4.addWidget(self.cfgABSSENSE)
        spacerItem6 = QtGui.QSpacerItem(50, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem6)
        self.vboxlayout3.addLayout(self.hboxlayout4)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setSpacing(5)
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(45, 16))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_13.setObjectName("label_13")
        self.hboxlayout5.addWidget(self.label_13)
        self.line_3 = QtGui.QFrame(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(5, 35))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hboxlayout5.addWidget(self.line_3)
        self.gridlayout5 = QtGui.QGridLayout()
        self.gridlayout5.setSpacing(5)
        self.gridlayout5.setContentsMargins(-1, 0, -1, 0)
        self.gridlayout5.setObjectName("gridlayout5")
        self.cfgABSNSTEP = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgABSNSTEP.sizePolicy().hasHeightForWidth())
        self.cfgABSNSTEP.setSizePolicy(sizePolicy)
        self.cfgABSNSTEP.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgABSNSTEP.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgABSNSTEP.setMaximum(999999999)
        self.cfgABSNSTEP.setObjectName("cfgABSNSTEP")
        self.gridlayout5.addWidget(self.cfgABSNSTEP, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(50, 16))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_14.setObjectName("label_14")
        self.gridlayout5.addWidget(self.label_14, 0, 1, 1, 1)
        self.cfgABSNTURN = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgABSNTURN.sizePolicy().hasHeightForWidth())
        self.cfgABSNTURN.setSizePolicy(sizePolicy)
        self.cfgABSNTURN.setMinimumSize(QtCore.QSize(65, 22))
        self.cfgABSNTURN.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgABSNTURN.setMaximum(999999999)
        self.cfgABSNTURN.setObjectName("cfgABSNTURN")
        self.gridlayout5.addWidget(self.cfgABSNTURN, 1, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(50, 16))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_15.setObjectName("label_15")
        self.gridlayout5.addWidget(self.label_15, 1, 1, 1, 1)
        self.hboxlayout5.addLayout(self.gridlayout5)
        self.vboxlayout3.addLayout(self.hboxlayout5)
        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(50, 16))
        self.label_23.setObjectName("label_23")
        self.hboxlayout6.addWidget(self.label_23)
        self.cfgABSOFFSET = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgABSOFFSET.sizePolicy().hasHeightForWidth())
        self.cfgABSOFFSET.setSizePolicy(sizePolicy)
        self.cfgABSOFFSET.setMinimumSize(QtCore.QSize(70, 16))
        self.cfgABSOFFSET.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgABSOFFSET.setMaximum(999999999)
        self.cfgABSOFFSET.setObjectName("cfgABSOFFSET")
        self.hboxlayout6.addWidget(self.cfgABSOFFSET)
        spacerItem7 = QtGui.QSpacerItem(50, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem7)
        self.vboxlayout3.addLayout(self.hboxlayout6)
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(80, 16))
        self.label_22.setObjectName("label_22")
        self.vboxlayout3.addWidget(self.label_22)
        self.gridlayout6 = QtGui.QGridLayout()
        self.gridlayout6.setContentsMargins(15, -1, -1, -1)
        self.gridlayout6.setObjectName("gridlayout6")
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(90, 16))
        self.label_21.setObjectName("label_21")
        self.gridlayout6.addWidget(self.label_21, 0, 0, 1, 2)
        self.cfgSSIDBITS = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSSIDBITS.sizePolicy().hasHeightForWidth())
        self.cfgSSIDBITS.setSizePolicy(sizePolicy)
        self.cfgSSIDBITS.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgSSIDBITS.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSSIDBITS.setMaximum(999999999)
        self.cfgSSIDBITS.setObjectName("cfgSSIDBITS")
        self.gridlayout6.addWidget(self.cfgSSIDBITS, 0, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(90, 16))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_16.setObjectName("label_16")
        self.gridlayout6.addWidget(self.label_16, 1, 0, 1, 1)
        self.cfgSSICODE = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSSICODE.sizePolicy().hasHeightForWidth())
        self.cfgSSICODE.setSizePolicy(sizePolicy)
        self.cfgSSICODE.setMinimumSize(QtCore.QSize(60, 16))
        self.cfgSSICODE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSSICODE.setObjectName("cfgSSICODE")
        self.gridlayout6.addWidget(self.cfgSSICODE, 1, 1, 1, 2)
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(90, 16))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_18.setObjectName("label_18")
        self.gridlayout6.addWidget(self.label_18, 2, 0, 1, 1)
        self.cfgSSICLOCK = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSSICLOCK.sizePolicy().hasHeightForWidth())
        self.cfgSSICLOCK.setSizePolicy(sizePolicy)
        self.cfgSSICLOCK.setMinimumSize(QtCore.QSize(60, 16))
        self.cfgSSICLOCK.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSSICLOCK.setObjectName("cfgSSICLOCK")
        self.gridlayout6.addWidget(self.cfgSSICLOCK, 2, 1, 1, 2)
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QtCore.QSize(90, 16))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_19.setObjectName("label_19")
        self.gridlayout6.addWidget(self.label_19, 3, 0, 1, 1)
        self.cfgSSIDELAY = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSSIDELAY.sizePolicy().hasHeightForWidth())
        self.cfgSSIDELAY.setSizePolicy(sizePolicy)
        self.cfgSSIDELAY.setMinimumSize(QtCore.QSize(60, 16))
        self.cfgSSIDELAY.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSSIDELAY.setObjectName("cfgSSIDELAY")
        self.gridlayout6.addWidget(self.cfgSSIDELAY, 3, 1, 1, 2)
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(110, 16))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_20.setObjectName("label_20")
        self.gridlayout6.addWidget(self.label_20, 4, 0, 1, 1)
        self.cfgSSISTATUS = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgSSISTATUS.sizePolicy().hasHeightForWidth())
        self.cfgSSISTATUS.setSizePolicy(sizePolicy)
        self.cfgSSISTATUS.setMinimumSize(QtCore.QSize(60, 16))
        self.cfgSSISTATUS.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgSSISTATUS.setObjectName("cfgSSISTATUS")
        self.gridlayout6.addWidget(self.cfgSSISTATUS, 4, 1, 1, 2)
        self.vboxlayout3.addLayout(self.gridlayout6)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.encoders_frame, 0, 0, 1, 1)

        self.retranslateUi(encoders)
        QtCore.QMetaObject.connectSlotsByName(encoders)

    def retranslateUi(self, encoders):
        encoders.setWindowTitle(QtGui.QApplication.translate("encoders", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("encoders", "Encln (rear panel input)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("encoders", "mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("encoders", "direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("encoders", "resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("encoders", "steps in", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("encoders", "turn(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("encoders", "Aux signal polarity", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("encoders", "InPos (front panel input)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("encoders", "mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("encoders", "direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("encoders", "resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("encoders", "steps in", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("encoders", "turn(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("encoders", "Aux signal\n"
"polarity", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("encoders", "Absolute encoder (SSI)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("encoders", "direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("encoders", "resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("encoders", "steps in", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("encoders", "turn(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("encoders", "offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("encoders", "SSI parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("encoders", "data length (bits)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("encoders", "data coding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("encoders", "clock frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("encoders", "sampling delay", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("encoders", "control bit pattern", None, QtGui.QApplication.UnicodeUTF8))

