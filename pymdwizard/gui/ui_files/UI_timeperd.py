# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeperd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 226)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fgdc_timeperd = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_timeperd.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_timeperd.setSizePolicy(sizePolicy)
        self.fgdc_timeperd.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_timeperd.setObjectName("fgdc_timeperd")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fgdc_timeperd)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: bold;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_36 = QtWidgets.QLabel(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setStyleSheet("font: italic;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout.addWidget(self.label_36)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_current = QtWidgets.QComboBox(self.fgdc_timeperd)
        self.fgdc_current.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fgdc_current.setEditable(True)
        self.fgdc_current.setObjectName("fgdc_current")
        self.fgdc_current.addItem("")
        self.fgdc_current.setItemText(0, "")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.horizontalLayout.addWidget(self.fgdc_current)
        self.label_9 = QtWidgets.QLabel(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(15, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_11.addWidget(self.fgdc_timeperd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_timeperd.setWhatsThis(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">Time Period Information</span></p><p>&lt;FGDC shortname: <span style=" font-style:italic;">timeperd</span>&gt;</p><p><br/></p><p>Time period(s) for which the dataset corresponds to the currentness reference.</p><p><br/></p><p>Specify only one of:</p><p><span style=" font-size:11pt;">    single date if the dataset ... </span></p><p><span style=" font-size:11pt;">     a Date range if it ...</span></p><p><span style=" font-size:11pt;">    or multiple dates if ...</span></p><p><br/></p><p>Choose only one.</p></body></html>',
            )
        )
        self.fgdc_timeperd.setTitle(_translate("Form", "Time Period Information"))
        self.label_8.setWhatsThis(
            _translate(
                "Form",
                "<html><head/><body><p>currentness what's this....</p><p>fakls;dfhjl;sakdjfl</p></body></html>",
            )
        )
        self.label_8.setText(_translate("Form", "Currentness Reference"))
        self.label_36.setText(
            _translate("Form", "Type directly in box below for items not in list.")
        )
        self.fgdc_current.setItemText(1, _translate("Form", "ground condition"))
        self.fgdc_current.setItemText(2, _translate("Form", "observed"))
        self.fgdc_current.setItemText(3, _translate("Form", "publication date"))
        self.fgdc_current.setItemText(4, _translate("Form", "See Supplemental Info"))
        self.label_9.setToolTip(_translate("Form", "Required"))
        self.label_9.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
