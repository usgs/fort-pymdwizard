# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taxoncl.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_taxoncl(object):
    def setupUi(self, fgdc_taxoncl):
        fgdc_taxoncl.setObjectName("fgdc_taxoncl")
        fgdc_taxoncl.resize(201, 158)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_taxoncl)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taxoncl_groupbox = QtWidgets.QGroupBox(fgdc_taxoncl)
        self.taxoncl_groupbox.setObjectName("taxoncl_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.taxoncl_groupbox)
        self.verticalLayout_3.setContentsMargins(20, 5, 0, 6)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_taxonrn = QtWidgets.QLabel(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_taxonrn.sizePolicy().hasHeightForWidth())
        self.lbl_taxonrn.setSizePolicy(sizePolicy)
        self.lbl_taxonrn.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_taxonrn.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_taxonrn.setFont(font)
        self.lbl_taxonrn.setStyleSheet("")
        self.lbl_taxonrn.setScaledContents(False)
        self.lbl_taxonrn.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_taxonrn.setWordWrap(False)
        self.lbl_taxonrn.setIndent(0)
        self.lbl_taxonrn.setObjectName("lbl_taxonrn")
        self.verticalLayout_3.addWidget(self.lbl_taxonrn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_taxonrn = QtWidgets.QLineEdit(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_taxonrn.sizePolicy().hasHeightForWidth())
        self.fgdc_taxonrn.setSizePolicy(sizePolicy)
        self.fgdc_taxonrn.setMinimumSize(QtCore.QSize(150, 0))
        self.fgdc_taxonrn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_taxonrn.setText("")
        self.fgdc_taxonrn.setPlaceholderText("")
        self.fgdc_taxonrn.setObjectName("fgdc_taxonrn")
        self.horizontalLayout.addWidget(self.fgdc_taxonrn)
        self.required = QtWidgets.QLabel(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.required.sizePolicy().hasHeightForWidth())
        self.required.setSizePolicy(sizePolicy)
        self.required.setMinimumSize(QtCore.QSize(15, 0))
        self.required.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.required.setFont(font)
        self.required.setScaledContents(True)
        self.required.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.required.setIndent(0)
        self.required.setObjectName("required")
        self.horizontalLayout.addWidget(self.required)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lbl_taxonrv = QtWidgets.QLabel(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_taxonrv.sizePolicy().hasHeightForWidth())
        self.lbl_taxonrv.setSizePolicy(sizePolicy)
        self.lbl_taxonrv.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_taxonrv.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_taxonrv.setFont(font)
        self.lbl_taxonrv.setStyleSheet("")
        self.lbl_taxonrv.setScaledContents(False)
        self.lbl_taxonrv.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_taxonrv.setWordWrap(False)
        self.lbl_taxonrv.setIndent(0)
        self.lbl_taxonrv.setObjectName("lbl_taxonrv")
        self.verticalLayout_3.addWidget(self.lbl_taxonrv)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fgdc_taxonrv = QtWidgets.QLineEdit(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_taxonrv.sizePolicy().hasHeightForWidth())
        self.fgdc_taxonrv.setSizePolicy(sizePolicy)
        self.fgdc_taxonrv.setMinimumSize(QtCore.QSize(150, 0))
        self.fgdc_taxonrv.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_taxonrv.setText("")
        self.fgdc_taxonrv.setPlaceholderText("")
        self.fgdc_taxonrv.setObjectName("fgdc_taxonrv")
        self.horizontalLayout_2.addWidget(self.fgdc_taxonrv)
        self.required_2 = QtWidgets.QLabel(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.required_2.sizePolicy().hasHeightForWidth())
        self.required_2.setSizePolicy(sizePolicy)
        self.required_2.setMinimumSize(QtCore.QSize(15, 0))
        self.required_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.required_2.setFont(font)
        self.required_2.setScaledContents(True)
        self.required_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.required_2.setIndent(0)
        self.required_2.setObjectName("required_2")
        self.horizontalLayout_2.addWidget(self.required_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lbl_common = QtWidgets.QLabel(self.taxoncl_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_common.sizePolicy().hasHeightForWidth())
        self.lbl_common.setSizePolicy(sizePolicy)
        self.lbl_common.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_common.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_common.setFont(font)
        self.lbl_common.setStyleSheet("")
        self.lbl_common.setScaledContents(False)
        self.lbl_common.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_common.setWordWrap(False)
        self.lbl_common.setIndent(0)
        self.lbl_common.setObjectName("lbl_common")
        self.verticalLayout_3.addWidget(self.lbl_common)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.child_taxoncl = QtWidgets.QWidget(self.taxoncl_groupbox)
        self.child_taxoncl.setObjectName("child_taxoncl")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.child_taxoncl)
        self.verticalLayout.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addWidget(self.child_taxoncl)
        self.verticalLayout_2.addWidget(self.taxoncl_groupbox)

        self.retranslateUi(fgdc_taxoncl)
        QtCore.QMetaObject.connectSlotsByName(fgdc_taxoncl)

    def retranslateUi(self, fgdc_taxoncl):
        _translate = QtCore.QCoreApplication.translate
        fgdc_taxoncl.setWindowTitle(_translate("fgdc_taxoncl", "Form"))
        self.taxoncl_groupbox.setTitle(
            _translate("fgdc_taxoncl", "Taxonomic Classification")
        )
        self.lbl_taxonrn.setToolTip(
            _translate("fgdc_taxoncl", "The name of the person to contact")
        )
        self.lbl_taxonrn.setText(_translate("fgdc_taxoncl", "Taxon Rank Name"))
        self.fgdc_taxonrn.setToolTip(
            _translate(
                "fgdc_taxoncl",
                "Contact Person -- the name of the individual to which the contact type applies.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: cntper",
            )
        )
        self.required.setToolTip(_translate("fgdc_taxoncl", "Required"))
        self.required.setText(
            _translate(
                "fgdc_taxoncl",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.lbl_taxonrv.setToolTip(
            _translate("fgdc_taxoncl", "The name of the person to contact")
        )
        self.lbl_taxonrv.setText(_translate("fgdc_taxoncl", "Taxon Rank Value"))
        self.fgdc_taxonrv.setToolTip(
            _translate(
                "fgdc_taxoncl",
                "Contact Person -- the name of the individual to which the contact type applies.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: cntper",
            )
        )
        self.required_2.setToolTip(_translate("fgdc_taxoncl", "Required"))
        self.required_2.setText(
            _translate(
                "fgdc_taxoncl",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.lbl_common.setToolTip(
            _translate("fgdc_taxoncl", "The name of the person to contact")
        )
        self.lbl_common.setText(_translate("fgdc_taxoncl", "Common Name"))
