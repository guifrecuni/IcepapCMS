# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'io.ui'
#
# Created: Tue Aug  4 15:08:47 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_io(object):
    def setupUi(self, io):
        io.setObjectName("io")
        io.resize(521, 250)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(io.sizePolicy().hasHeightForWidth())
        io.setSizePolicy(sizePolicy)
        io.setMinimumSize(QtCore.QSize(410, 250))
        self.gridlayout = QtGui.QGridLayout(io)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")
        self.io_frame = QtGui.QFrame(io)
        self.io_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.io_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.io_frame.setObjectName("io_frame")
        self.gridlayout1 = QtGui.QGridLayout(self.io_frame)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_3 = QtGui.QGroupBox(self.io_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(182, 86))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout2.setObjectName("gridlayout2")
        spacerItem = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(50, 16))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridlayout2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 16))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridlayout2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(50, 16))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3, 1, 0, 1, 1)
        self.cfgINFOASRC = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOASRC.sizePolicy().hasHeightForWidth())
        self.cfgINFOASRC.setSizePolicy(sizePolicy)
        self.cfgINFOASRC.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOASRC.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOASRC.setObjectName("cfgINFOASRC")
        self.gridlayout2.addWidget(self.cfgINFOASRC, 1, 1, 1, 1)
        self.cfgINFOAPOL = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOAPOL.sizePolicy().hasHeightForWidth())
        self.cfgINFOAPOL.setSizePolicy(sizePolicy)
        self.cfgINFOAPOL.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOAPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOAPOL.setObjectName("cfgINFOAPOL")
        self.gridlayout2.addWidget(self.cfgINFOAPOL, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 16))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_4.setObjectName("label_4")
        self.gridlayout2.addWidget(self.label_4, 2, 0, 1, 1)
        self.cfgINFOBSRC = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOBSRC.sizePolicy().hasHeightForWidth())
        self.cfgINFOBSRC.setSizePolicy(sizePolicy)
        self.cfgINFOBSRC.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOBSRC.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOBSRC.setObjectName("cfgINFOBSRC")
        self.gridlayout2.addWidget(self.cfgINFOBSRC, 2, 1, 1, 1)
        self.cfgINFOBPOL = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOBPOL.sizePolicy().hasHeightForWidth())
        self.cfgINFOBPOL.setSizePolicy(sizePolicy)
        self.cfgINFOBPOL.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOBPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOBPOL.setObjectName("cfgINFOBPOL")
        self.gridlayout2.addWidget(self.cfgINFOBPOL, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 16))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_5.setObjectName("label_5")
        self.gridlayout2.addWidget(self.label_5, 3, 0, 1, 1)
        self.cfgINFOCSRC = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOCSRC.sizePolicy().hasHeightForWidth())
        self.cfgINFOCSRC.setSizePolicy(sizePolicy)
        self.cfgINFOCSRC.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOCSRC.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOCSRC.setObjectName("cfgINFOCSRC")
        self.gridlayout2.addWidget(self.cfgINFOCSRC, 3, 1, 1, 1)
        self.cfgINFOCPOL = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgINFOCPOL.sizePolicy().hasHeightForWidth())
        self.cfgINFOCPOL.setSizePolicy(sizePolicy)
        self.cfgINFOCPOL.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgINFOCPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgINFOCPOL.setObjectName("cfgINFOCPOL")
        self.gridlayout2.addWidget(self.cfgINFOCPOL, 3, 2, 1, 1)
        self.vboxlayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.io_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(182, 64))
        self.groupBox.setObjectName("groupBox")
        self.gridlayout3 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout3.setObjectName("gridlayout3")
        self.label_8 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(70, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_8.setObjectName("label_8")
        self.gridlayout3.addWidget(self.label_8, 0, 0, 1, 1)
        self.cfgEXTALARM = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEXTALARM.sizePolicy().hasHeightForWidth())
        self.cfgEXTALARM.setSizePolicy(sizePolicy)
        self.cfgEXTALARM.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgEXTALARM.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgEXTALARM.setFont(font)
        self.cfgEXTALARM.setObjectName("cfgEXTALARM")
        self.gridlayout3.addWidget(self.cfgEXTALARM, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(70, 16))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_9.setObjectName("label_9")
        self.gridlayout3.addWidget(self.label_9, 1, 0, 1, 1)
        self.cfgEXTWARNING = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgEXTWARNING.sizePolicy().hasHeightForWidth())
        self.cfgEXTWARNING.setSizePolicy(sizePolicy)
        self.cfgEXTWARNING.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgEXTWARNING.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgEXTWARNING.setFont(font)
        self.cfgEXTWARNING.setObjectName("cfgEXTWARNING")
        self.gridlayout3.addWidget(self.cfgEXTWARNING, 1, 1, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.gridlayout1.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.io_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(185, 163))
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setObjectName("gridlayout4")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(80, 16))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_10.setObjectName("label_10")
        self.gridlayout4.addWidget(self.label_10, 0, 0, 1, 1)
        self.cfgOUTPSRC = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPSRC.sizePolicy().hasHeightForWidth())
        self.cfgOUTPSRC.setSizePolicy(sizePolicy)
        self.cfgOUTPSRC.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPSRC.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgOUTPSRC.setObjectName("cfgOUTPSRC")
        self.gridlayout4.addWidget(self.cfgOUTPSRC, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(80, 16))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_11.setObjectName("label_11")
        self.gridlayout4.addWidget(self.label_11, 1, 0, 1, 1)
        self.cfgOUTPMODE = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPMODE.sizePolicy().hasHeightForWidth())
        self.cfgOUTPMODE.setSizePolicy(sizePolicy)
        self.cfgOUTPMODE.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPMODE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgOUTPMODE.setObjectName("cfgOUTPMODE")
        self.gridlayout4.addWidget(self.cfgOUTPMODE, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(80, 16))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_12.setObjectName("label_12")
        self.gridlayout4.addWidget(self.label_12, 2, 0, 1, 1)
        self.cfgOUTPSENSE = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPSENSE.sizePolicy().hasHeightForWidth())
        self.cfgOUTPSENSE.setSizePolicy(sizePolicy)
        self.cfgOUTPSENSE.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPSENSE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgOUTPSENSE.setObjectName("cfgOUTPSENSE")
        self.gridlayout4.addWidget(self.cfgOUTPSENSE, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(80, 16))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_13.setObjectName("label_13")
        self.gridlayout4.addWidget(self.label_13, 3, 0, 1, 1)
        self.cfgOUTPPULSE = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPPULSE.sizePolicy().hasHeightForWidth())
        self.cfgOUTPPULSE.setSizePolicy(sizePolicy)
        self.cfgOUTPPULSE.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPPULSE.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cfgOUTPPULSE.setObjectName("cfgOUTPPULSE")
        self.gridlayout4.addWidget(self.cfgOUTPPULSE, 3, 1, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout4)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(20, 16))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.hboxlayout1.addWidget(self.label_16)
        self.line = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(10, 30))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout1.addWidget(self.line)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(30, 16))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_14.setObjectName("label_14")
        self.vboxlayout2.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(30, 16))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_15.setObjectName("label_15")
        self.vboxlayout2.addWidget(self.label_15)
        self.hboxlayout1.addLayout(self.vboxlayout2)
        self.hboxlayout.addLayout(self.hboxlayout1)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.cfgOUTPAUXSRC = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPAUXSRC.sizePolicy().hasHeightForWidth())
        self.cfgOUTPAUXSRC.setSizePolicy(sizePolicy)
        self.cfgOUTPAUXSRC.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPAUXSRC.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgOUTPAUXSRC.setFont(font)
        self.cfgOUTPAUXSRC.setObjectName("cfgOUTPAUXSRC")
        self.vboxlayout3.addWidget(self.cfgOUTPAUXSRC)
        self.cfgOUTPAUXPOL = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfgOUTPAUXPOL.sizePolicy().hasHeightForWidth())
        self.cfgOUTPAUXPOL.setSizePolicy(sizePolicy)
        self.cfgOUTPAUXPOL.setMinimumSize(QtCore.QSize(50, 16))
        self.cfgOUTPAUXPOL.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.cfgOUTPAUXPOL.setFont(font)
        self.cfgOUTPAUXPOL.setObjectName("cfgOUTPAUXPOL")
        self.vboxlayout3.addWidget(self.cfgOUTPAUXPOL)
        self.hboxlayout.addLayout(self.vboxlayout3)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.gridlayout1.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.io_frame, 0, 0, 1, 1)

        self.retranslateUi(io)
        QtCore.QMetaObject.connectSlotsByName(io)

    def retranslateUi(self, io):
        io.setWindowTitle(QtGui.QApplication.translate("io", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("io", "Default configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("io", "source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("io", "polarity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("io", "InfoA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("io", "InfoB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("io", "InfoC", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("io", "Alarm signals", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("io", "External alarm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("io", "External warning", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("io", "OutPos (front panel output)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("io", "source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("io", "direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("io", "mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("io", "pulse width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("io", "Aux signal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("io", "source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("io", "polarity", None, QtGui.QApplication.UnicodeUTF8))

