# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fgdc_date.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parent_widget(object):
    def setupUi(self, parent_widget):
        parent_widget.setObjectName("parent_widget")
        parent_widget.resize(210, 47)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(parent_widget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parent_fgdc = QtWidgets.QWidget(parent_widget)
        self.parent_fgdc.setObjectName("parent_fgdc")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.parent_fgdc)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_format = QtWidgets.QWidget(self.parent_fgdc)
        self.widget_format.setObjectName("widget_format")
        self.layout_format = QtWidgets.QHBoxLayout(self.widget_format)
        self.layout_format.setContentsMargins(0, 0, 6, 0)
        self.layout_format.setSpacing(0)
        self.layout_format.setObjectName("layout_format")
        spacerItem = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum
        )
        self.layout_format.addItem(spacerItem)
        self.lbl_format = QtWidgets.QLabel(self.widget_format)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_format.sizePolicy().hasHeightForWidth())
        self.lbl_format.setSizePolicy(sizePolicy)
        self.lbl_format.setStyleSheet("font: italic;")
        self.lbl_format.setObjectName("lbl_format")
        self.layout_format.addWidget(self.lbl_format)
        self.verticalLayout.addWidget(self.widget_format)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.parent_fgdc)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fgdc_caldate = QtWidgets.QLineEdit(self.parent_fgdc)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_caldate.sizePolicy().hasHeightForWidth())
        self.fgdc_caldate.setSizePolicy(sizePolicy)
        self.fgdc_caldate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fgdc_caldate.setObjectName("fgdc_caldate")
        self.horizontalLayout.addWidget(self.fgdc_caldate)
        self.lbl_required = QtWidgets.QLabel(self.parent_fgdc)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_required.sizePolicy().hasHeightForWidth())
        self.lbl_required.setSizePolicy(sizePolicy)
        self.lbl_required.setMinimumSize(QtCore.QSize(15, 0))
        self.lbl_required.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_required.setFont(font)
        self.lbl_required.setScaledContents(True)
        self.lbl_required.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.lbl_required.setIndent(0)
        self.lbl_required.setObjectName("lbl_required")
        self.horizontalLayout.addWidget(self.lbl_required)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.parent_fgdc)

        self.retranslateUi(parent_widget)
        QtCore.QMetaObject.connectSlotsByName(parent_widget)

    def retranslateUi(self, parent_widget):
        _translate = QtCore.QCoreApplication.translate
        parent_widget.setWindowTitle(_translate("parent_widget", "Form"))
        self.lbl_format.setText(_translate("parent_widget", "YYYYMMDD"))
        self.label.setText(_translate("parent_widget", "Date"))
        self.lbl_required.setToolTip(_translate("parent_widget", "Required"))
        self.lbl_required.setText(
            _translate(
                "parent_widget",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
