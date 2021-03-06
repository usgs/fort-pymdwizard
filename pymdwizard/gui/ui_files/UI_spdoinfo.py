# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spdoinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_spatial_domain_widget(object):
    def setupUi(self, spatial_domain_widget):
        spatial_domain_widget.setObjectName("spatial_domain_widget")
        spatial_domain_widget.resize(317, 232)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            spatial_domain_widget.sizePolicy().hasHeightForWidth()
        )
        spatial_domain_widget.setSizePolicy(sizePolicy)
        spatial_domain_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        spatial_domain_widget.setAcceptDrops(True)
        spatial_domain_widget.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(spatial_domain_widget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_spdoinfo = QtWidgets.QGroupBox(spatial_domain_widget)
        self.fgdc_spdoinfo.setObjectName("fgdc_spdoinfo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fgdc_spdoinfo)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.fgdc_spdoinfo)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setStyleSheet("font: bold;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.rbtn_yes = QtWidgets.QRadioButton(self.fgdc_spdoinfo)
        self.rbtn_yes.setAutoFillBackground(True)
        self.rbtn_yes.setChecked(True)
        self.rbtn_yes.setObjectName("rbtn_yes")
        self.horizontalLayout.addWidget(self.rbtn_yes)
        self.rbtn_no = QtWidgets.QRadioButton(self.fgdc_spdoinfo)
        self.rbtn_no.setAutoFillBackground(True)
        self.rbtn_no.setChecked(False)
        self.rbtn_no.setObjectName("rbtn_no")
        self.horizontalLayout.addWidget(self.rbtn_no)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.fgdc_spdoinfo)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setStyleSheet("font: italic;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.content_widget = QtWidgets.QWidget(self.fgdc_spdoinfo)
        self.content_widget.setObjectName("content_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_33 = QtWidgets.QLabel(self.content_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QtCore.QSize(0, 0))
        self.label_33.setMaximumSize(QtCore.QSize(1000, 20))
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_33.setObjectName("label_33")
        self.verticalLayout_10.addWidget(self.label_33)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.fgdc_direct = QtWidgets.QComboBox(self.content_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_direct.sizePolicy().hasHeightForWidth())
        self.fgdc_direct.setSizePolicy(sizePolicy)
        self.fgdc_direct.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_direct.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fgdc_direct.setToolTip("")
        self.fgdc_direct.setEditable(True)
        self.fgdc_direct.setObjectName("fgdc_direct")
        self.fgdc_direct.addItem("")
        self.fgdc_direct.addItem("")
        self.fgdc_direct.addItem("")
        self.horizontalLayout_12.addWidget(self.fgdc_direct)
        self.label_34 = QtWidgets.QLabel(self.content_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QtCore.QSize(15, 20))
        self.label_34.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_34.setIndent(0)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_12.addWidget(self.label_34)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addLayout(self.verticalLayout_10)
        self.vector_or_raster = QtWidgets.QStackedWidget(self.content_widget)
        self.vector_or_raster.setObjectName("vector_or_raster")
        self.fgdc_ptvctinf = QtWidgets.QWidget()
        self.fgdc_ptvctinf.setObjectName("fgdc_ptvctinf")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fgdc_ptvctinf)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fgdc_sdtsterm = QtWidgets.QWidget(self.fgdc_ptvctinf)
        self.fgdc_sdtsterm.setObjectName("fgdc_sdtsterm")
        self._2 = QtWidgets.QVBoxLayout(self.fgdc_sdtsterm)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_35 = QtWidgets.QLabel(self.fgdc_sdtsterm)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QtCore.QSize(0, 0))
        self.label_35.setMaximumSize(QtCore.QSize(1000, 20))
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_35.setObjectName("label_35")
        self.verticalLayout_11.addWidget(self.label_35)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.fgdc_sdtstype = QtWidgets.QComboBox(self.fgdc_sdtsterm)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_sdtstype.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_sdtstype.setSizePolicy(sizePolicy)
        self.fgdc_sdtstype.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_sdtstype.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fgdc_sdtstype.setToolTip("")
        self.fgdc_sdtstype.setEditable(True)
        self.fgdc_sdtstype.setObjectName("fgdc_sdtstype")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.fgdc_sdtstype.addItem("")
        self.horizontalLayout_13.addWidget(self.fgdc_sdtstype)
        self.label_36 = QtWidgets.QLabel(self.fgdc_sdtsterm)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QtCore.QSize(15, 20))
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_36.setIndent(0)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_13.addWidget(self.label_36)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self._2.addLayout(self.verticalLayout_11)
        self.label_22 = QtWidgets.QLabel(self.fgdc_sdtsterm)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_22.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_22.setObjectName("label_22")
        self._2.addWidget(self.label_22)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fgdc_ptvctcnt = QtWidgets.QLineEdit(self.fgdc_sdtsterm)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_ptvctcnt.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_ptvctcnt.setSizePolicy(sizePolicy)
        self.fgdc_ptvctcnt.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_ptvctcnt.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_ptvctcnt.setToolTip("")
        self.fgdc_ptvctcnt.setObjectName("fgdc_ptvctcnt")
        self.horizontalLayout_10.addWidget(self.fgdc_ptvctcnt)
        spacerItem1 = QtWidgets.QSpacerItem(
            15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem1)
        self._2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addWidget(self.fgdc_sdtsterm)
        self.vector_or_raster.addWidget(self.fgdc_ptvctinf)
        self.fgdc_rastinfo = QtWidgets.QWidget()
        self.fgdc_rastinfo.setObjectName("fgdc_rastinfo")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fgdc_rastinfo)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_38 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMinimumSize(QtCore.QSize(0, 0))
        self.label_38.setMaximumSize(QtCore.QSize(1000, 20))
        self.label_38.setStyleSheet("")
        self.label_38.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_38.setObjectName("label_38")
        self.verticalLayout_8.addWidget(self.label_38)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.fgdc_rasttype = QtWidgets.QComboBox(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_rasttype.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_rasttype.setSizePolicy(sizePolicy)
        self.fgdc_rasttype.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_rasttype.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fgdc_rasttype.setEditable(True)
        self.fgdc_rasttype.setObjectName("fgdc_rasttype")
        self.fgdc_rasttype.addItem("")
        self.fgdc_rasttype.addItem("")
        self.fgdc_rasttype.addItem("")
        self.fgdc_rasttype.addItem("")
        self.horizontalLayout_14.addWidget(self.fgdc_rasttype)
        self.label_37 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QtCore.QSize(15, 20))
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_37.setIndent(0)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_14.addWidget(self.label_37)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_14)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_30 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setMaximumSize(QtCore.QSize(75, 20))
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_30.setObjectName("label_30")
        self.verticalLayout_5.addWidget(self.label_30)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fgdc_rowcount = QtWidgets.QLineEdit(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_rowcount.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_rowcount.setSizePolicy(sizePolicy)
        self.fgdc_rowcount.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_rowcount.setMaximumSize(QtCore.QSize(75, 20))
        self.fgdc_rowcount.setObjectName("fgdc_rowcount")
        self.horizontalLayout_2.addWidget(self.fgdc_rowcount)
        self.label_29 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QtCore.QSize(15, 0))
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_29.setIndent(0)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_2.addWidget(self.label_29)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_31 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QtCore.QSize(0, 0))
        self.label_31.setMaximumSize(QtCore.QSize(75, 20))
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_31.setObjectName("label_31")
        self.verticalLayout_6.addWidget(self.label_31)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fgdc_colcount = QtWidgets.QLineEdit(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_colcount.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_colcount.setSizePolicy(sizePolicy)
        self.fgdc_colcount.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_colcount.setMaximumSize(QtCore.QSize(75, 20))
        self.fgdc_colcount.setObjectName("fgdc_colcount")
        self.horizontalLayout_3.addWidget(self.fgdc_colcount)
        self.label_32 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(15, 0))
        self.label_32.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_32.setIndent(0)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_3.addWidget(self.label_32)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_39 = QtWidgets.QLabel(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setMinimumSize(QtCore.QSize(0, 0))
        self.label_39.setMaximumSize(QtCore.QSize(75, 20))
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_39.setObjectName("label_39")
        self.verticalLayout_7.addWidget(self.label_39)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fgdc_vrtcount = QtWidgets.QLineEdit(self.fgdc_rastinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_vrtcount.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_vrtcount.setSizePolicy(sizePolicy)
        self.fgdc_vrtcount.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_vrtcount.setMaximumSize(QtCore.QSize(75, 20))
        self.fgdc_vrtcount.setObjectName("fgdc_vrtcount")
        self.horizontalLayout_4.addWidget(self.fgdc_vrtcount)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.vector_or_raster.addWidget(self.fgdc_rastinfo)
        self.verticalLayout_4.addWidget(self.vector_or_raster)
        self.verticalLayout_3.addWidget(self.content_widget)
        self.content_widget.raise_()
        self.label_2.raise_()
        self.verticalLayout_2.addWidget(self.fgdc_spdoinfo)

        self.retranslateUi(spatial_domain_widget)
        self.fgdc_direct.setCurrentIndex(2)
        self.vector_or_raster.setCurrentIndex(0)
        self.fgdc_sdtstype.setCurrentIndex(0)
        self.fgdc_rasttype.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(spatial_domain_widget)

    def retranslateUi(self, spatial_domain_widget):
        _translate = QtCore.QCoreApplication.translate
        spatial_domain_widget.setWindowTitle(
            _translate("spatial_domain_widget", "Form")
        )
        self.fgdc_spdoinfo.setTitle(
            _translate("spatial_domain_widget", "Spatial Data Organization")
        )
        self.label.setText(
            _translate("spatial_domain_widget", "Is this a spatial (GIS) dataset?")
        )
        self.rbtn_yes.setText(_translate("spatial_domain_widget", "Yes"))
        self.rbtn_no.setText(_translate("spatial_domain_widget", "No"))
        self.label_2.setText(
            _translate(
                "spatial_domain_widget",
                "Shapefile, Geotif, Geodatabase feature class, etc",
            )
        )
        self.label_33.setText(
            _translate("spatial_domain_widget", "Spatial Data Category")
        )
        self.fgdc_direct.setItemText(0, _translate("spatial_domain_widget", "Point"))
        self.fgdc_direct.setItemText(1, _translate("spatial_domain_widget", "Vector"))
        self.fgdc_direct.setItemText(2, _translate("spatial_domain_widget", "Raster"))
        self.label_34.setToolTip(_translate("spatial_domain_widget", "Required"))
        self.label_34.setText(
            _translate(
                "spatial_domain_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_35.setText(_translate("spatial_domain_widget", "Vector Object Type"))
        self.fgdc_sdtstype.setItemText(0, _translate("spatial_domain_widget", "Point"))
        self.fgdc_sdtstype.setItemText(
            1, _translate("spatial_domain_widget", "Entity point")
        )
        self.fgdc_sdtstype.setItemText(
            2, _translate("spatial_domain_widget", "Label point")
        )
        self.fgdc_sdtstype.setItemText(
            3, _translate("spatial_domain_widget", "Area point")
        )
        self.fgdc_sdtstype.setItemText(
            4, _translate("spatial_domain_widget", "Node, planar graph")
        )
        self.fgdc_sdtstype.setItemText(
            5, _translate("spatial_domain_widget", "Node, network")
        )
        self.fgdc_sdtstype.setItemText(6, _translate("spatial_domain_widget", "String"))
        self.fgdc_sdtstype.setItemText(7, _translate("spatial_domain_widget", "Link"))
        self.fgdc_sdtstype.setItemText(
            8, _translate("spatial_domain_widget", "Complete chain")
        )
        self.fgdc_sdtstype.setItemText(
            9, _translate("spatial_domain_widget", "Area chain")
        )
        self.fgdc_sdtstype.setItemText(
            10, _translate("spatial_domain_widget", "Network chain, planar graph")
        )
        self.fgdc_sdtstype.setItemText(
            11, _translate("spatial_domain_widget", "Network chain, nonplanar graph")
        )
        self.fgdc_sdtstype.setItemText(
            12, _translate("spatial_domain_widget", "Circular arc, three point center")
        )
        self.fgdc_sdtstype.setItemText(
            13, _translate("spatial_domain_widget", "Elliptical arc")
        )
        self.fgdc_sdtstype.setItemText(
            14, _translate("spatial_domain_widget", "Uniform B-spline")
        )
        self.fgdc_sdtstype.setItemText(
            15, _translate("spatial_domain_widget", "Piecewise Bezier")
        )
        self.fgdc_sdtstype.setItemText(
            16, _translate("spatial_domain_widget", "Ring with mixed composition")
        )
        self.fgdc_sdtstype.setItemText(
            17, _translate("spatial_domain_widget", "Ring composed of strings")
        )
        self.fgdc_sdtstype.setItemText(
            18, _translate("spatial_domain_widget", "Ring composed of chains")
        )
        self.fgdc_sdtstype.setItemText(
            19, _translate("spatial_domain_widget", "Ring composed of arcs")
        )
        self.fgdc_sdtstype.setItemText(
            20, _translate("spatial_domain_widget", "G-polygon")
        )
        self.fgdc_sdtstype.setItemText(
            21, _translate("spatial_domain_widget", "GT-polygon composed of rings")
        )
        self.fgdc_sdtstype.setItemText(
            22, _translate("spatial_domain_widget", "GT-polygon composed of chains")
        )
        self.fgdc_sdtstype.setItemText(
            23,
            _translate("spatial_domain_widget", "Universe polygon composed of rings"),
        )
        self.fgdc_sdtstype.setItemText(
            24,
            _translate("spatial_domain_widget", "Universe polygon composed of chains"),
        )
        self.fgdc_sdtstype.setItemText(
            25, _translate("spatial_domain_widget", "Void polygon composed of rings")
        )
        self.fgdc_sdtstype.setItemText(
            26, _translate("spatial_domain_widget", "Void polygon composed of chains")
        )
        self.label_36.setToolTip(_translate("spatial_domain_widget", "Required"))
        self.label_36.setText(
            _translate(
                "spatial_domain_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_22.setText(
            _translate("spatial_domain_widget", "Point or Vector Object Count")
        )
        self.label_38.setText(_translate("spatial_domain_widget", "Raster Object Type"))
        self.fgdc_rasttype.setToolTip(
            _translate(
                "spatial_domain_widget",
                "Address Type -- the information provided by the address.\n"
                "Type: text\n"
                'Domain: "mailing" "physical" "mailing and physical", free text\n'
                "Short Name: addrtype",
            )
        )
        self.fgdc_rasttype.setItemText(0, _translate("spatial_domain_widget", "Point"))
        self.fgdc_rasttype.setItemText(1, _translate("spatial_domain_widget", "Pixel"))
        self.fgdc_rasttype.setItemText(
            2, _translate("spatial_domain_widget", "Grid Cell")
        )
        self.fgdc_rasttype.setItemText(3, _translate("spatial_domain_widget", "Voxel"))
        self.label_37.setToolTip(_translate("spatial_domain_widget", "Required"))
        self.label_37.setText(
            _translate(
                "spatial_domain_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_30.setText(_translate("spatial_domain_widget", "Row Count"))
        self.fgdc_rowcount.setToolTip(
            _translate(
                "spatial_domain_widget",
                "Postal Code -- the ZIP or other postal code of the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: postal",
            )
        )
        self.label_29.setToolTip(_translate("spatial_domain_widget", "Required"))
        self.label_29.setText(
            _translate(
                "spatial_domain_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_31.setText(_translate("spatial_domain_widget", "Column Count"))
        self.fgdc_colcount.setToolTip(
            _translate(
                "spatial_domain_widget",
                "Postal Code -- the ZIP or other postal code of the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: postal",
            )
        )
        self.label_32.setToolTip(_translate("spatial_domain_widget", "Required"))
        self.label_32.setText(
            _translate(
                "spatial_domain_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_39.setText(_translate("spatial_domain_widget", "Vertical Count"))
        self.fgdc_vrtcount.setToolTip(
            _translate(
                "spatial_domain_widget",
                "Postal Code -- the ZIP or other postal code of the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: postal",
            )
        )
