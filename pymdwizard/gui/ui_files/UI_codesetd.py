# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codesetd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_attrdomv(object):
    def setupUi(self, fgdc_attrdomv):
        fgdc_attrdomv.setObjectName("fgdc_attrdomv")
        fgdc_attrdomv.resize(418, 442)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fgdc_attrdomv.sizePolicy().hasHeightForWidth())
        fgdc_attrdomv.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(fgdc_attrdomv)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_codesetd = QtWidgets.QWidget(fgdc_attrdomv)
        self.fgdc_codesetd.setObjectName("fgdc_codesetd")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fgdc_codesetd)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_19.setWordWrap(False)
        self.label_19.setIndent(0)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_36 = QtWidgets.QLabel(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setStyleSheet("font: italic;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_5.addWidget(self.label_36)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fgdc_codesetn = QtWidgets.QComboBox(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_codesetn.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_codesetn.setSizePolicy(sizePolicy)
        self.fgdc_codesetn.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_codesetn.setEditable(True)
        self.fgdc_codesetn.setObjectName("fgdc_codesetn")
        self.fgdc_codesetn.addItem("")
        self.fgdc_codesetn.addItem("")
        self.fgdc_codesetn.addItem("")
        self.fgdc_codesetn.addItem("")
        self.fgdc_codesetn.addItem("")
        self.fgdc_codesetn.addItem("")
        self.horizontalLayout_8.addWidget(self.fgdc_codesetn)
        self.label_20 = QtWidgets.QLabel(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(15, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_20.setIndent(0)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_21 = QtWidgets.QLabel(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_21.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fgdc_codesets = QtWidgets.QLineEdit(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_codesets.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_codesets.setSizePolicy(sizePolicy)
        self.fgdc_codesets.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_codesets.setObjectName("fgdc_codesets")
        self.horizontalLayout_9.addWidget(self.fgdc_codesets)
        self.label_25 = QtWidgets.QLabel(self.fgdc_codesetd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(15, 20))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_25.setIndent(0)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.fgdc_codesetd)
        spacerItem = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(fgdc_attrdomv)
        QtCore.QMetaObject.connectSlotsByName(fgdc_attrdomv)

    def retranslateUi(self, fgdc_attrdomv):
        _translate = QtCore.QCoreApplication.translate
        fgdc_attrdomv.setWindowTitle(_translate("fgdc_attrdomv", "Form"))
        self.label_19.setText(_translate("fgdc_attrdomv", "Codeset Name"))
        self.label_36.setText(
            _translate(
                "fgdc_attrdomv", "Type directly in box below for items not in list."
            )
        )
        self.fgdc_codesetn.setItemText(
            0, _translate("fgdc_attrdomv", "FIPS Code (2-Digit State ID)")
        )
        self.fgdc_codesetn.setItemText(
            1, _translate("fgdc_attrdomv", "FIPS Code (3-Digit County ID)")
        )
        self.fgdc_codesetn.setItemText(
            2, _translate("fgdc_attrdomv", "FIPS Code (5-Digit State & County ID)")
        )
        self.fgdc_codesetn.setItemText(
            3, _translate("fgdc_attrdomv", "US Postal Zip Codes")
        )
        self.fgdc_codesetn.setItemText(
            4, _translate("fgdc_attrdomv", "US Postal 2-Letter State")
        )
        self.fgdc_codesetn.setItemText(
            5, _translate("fgdc_attrdomv", "MAF / TIGER Feature Class Codes (MTFCC)")
        )
        self.label_20.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_20.setText(
            _translate(
                "fgdc_attrdomv",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_21.setText(_translate("fgdc_attrdomv", "Codeset Source"))
        self.label_25.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_25.setText(
            _translate(
                "fgdc_attrdomv",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
