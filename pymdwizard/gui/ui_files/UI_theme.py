# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theme.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Taxonomy(object):
    def setupUi(self, Taxonomy):
        Taxonomy.setObjectName("Taxonomy")
        Taxonomy.resize(523, 280)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Taxonomy.sizePolicy().hasHeightForWidth())
        Taxonomy.setSizePolicy(sizePolicy)
        Taxonomy.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Taxonomy)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_taxonomy = QtWidgets.QGroupBox(Taxonomy)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_taxonomy.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_taxonomy.setSizePolicy(sizePolicy)
        self.fgdc_taxonomy.setObjectName("fgdc_taxonomy")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_taxonomy)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.widget_contents = QtWidgets.QWidget(self.fgdc_taxonomy)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_contents.sizePolicy().hasHeightForWidth()
        )
        self.widget_contents.setSizePolicy(sizePolicy)
        self.widget_contents.setObjectName("widget_contents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_contents)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.theme_groupbox = QtWidgets.QGroupBox(self.widget_contents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.theme_groupbox.sizePolicy().hasHeightForWidth()
        )
        self.theme_groupbox.setSizePolicy(sizePolicy)
        self.theme_groupbox.setObjectName("theme_groupbox")
        self.theme_kws_layout = QtWidgets.QVBoxLayout(self.theme_groupbox)
        self.theme_kws_layout.setObjectName("theme_kws_layout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(9, -1, 9, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_add_iso_2 = QtWidgets.QPushButton(self.theme_groupbox)
        self.btn_add_iso_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add_iso_2.setFont(font)
        self.btn_add_iso_2.setStyleSheet("")
        self.btn_add_iso_2.setObjectName("btn_add_iso_2")
        self.horizontalLayout_4.addWidget(self.btn_add_iso_2)
        spacerItem = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_add_iso = QtWidgets.QPushButton(self.theme_groupbox)
        self.btn_add_iso.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add_iso.setFont(font)
        self.btn_add_iso.setStyleSheet("")
        self.btn_add_iso.setObjectName("btn_add_iso")
        self.horizontalLayout_4.addWidget(self.btn_add_iso)
        self.theme_kws_layout.addLayout(self.horizontalLayout_4)
        self.widget = QtWidgets.QWidget(self.theme_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.theme_kws_layout.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.theme_groupbox)
        self.main_layout.addWidget(self.widget_contents)
        self.verticalLayout.addLayout(self.main_layout)
        self.verticalLayout_2.addWidget(self.fgdc_taxonomy)

        self.retranslateUi(Taxonomy)
        QtCore.QMetaObject.connectSlotsByName(Taxonomy)

    def retranslateUi(self, Taxonomy):
        _translate = QtCore.QCoreApplication.translate
        Taxonomy.setWindowTitle(_translate("Taxonomy", "Form"))
        Taxonomy.setToolTip(_translate("Taxonomy", "test docstring"))
        self.fgdc_taxonomy.setTitle(_translate("Taxonomy", "Taxonomy"))
        self.theme_groupbox.setTitle(_translate("Taxonomy", "Theme Keywords"))
        self.btn_add_iso_2.setText(
            _translate("Taxonomy", "Search Controlled Vocabularies")
        )
        self.btn_add_iso.setText(_translate("Taxonomy", "Add ISO 19115"))
