# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MetadataDate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 201)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_timeperd = QtWidgets.QGroupBox(Form)
        self.fgdc_timeperd.setObjectName("fgdc_timeperd")
        self.label_2 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fgdc_timeinfo = QtWidgets.QTabWidget(self.fgdc_timeperd)
        self.fgdc_timeinfo.setGeometry(QtCore.QRect(10, 50, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_timeinfo.setFont(font)
        self.fgdc_timeinfo.setObjectName("fgdc_timeinfo")
        self.fgdc_sngdate = QtWidgets.QWidget()
        self.fgdc_sngdate.setObjectName("fgdc_sngdate")
        self.label_4 = QtWidgets.QLabel(self.fgdc_sngdate)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 101, 16))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.fgdc_sngdate)
        self.dateEdit.setGeometry(QtCore.QRect(120, 30, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 30))
        self.dateEdit.setObjectName("dateEdit")
        self.fgdc_timeinfo.addTab(self.fgdc_sngdate, "")
        self.fgdc_rngdates = QtWidgets.QWidget()
        self.fgdc_rngdates.setObjectName("fgdc_rngdates")
        self.label_5 = QtWidgets.QLabel(self.fgdc_rngdates)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.fgdc_rngdates)
        self.label_6.setGeometry(QtCore.QRect(190, 20, 131, 20))
        self.label_6.setObjectName("label_6")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.fgdc_rngdates)
        self.dateEdit_2.setGeometry(QtCore.QRect(30, 40, 110, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2000, 1, 30))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.fgdc_rngdates)
        self.dateEdit_3.setGeometry(QtCore.QRect(200, 40, 110, 22))
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setDate(QtCore.QDate(2000, 1, 30))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.fgdc_timeinfo.addTab(self.fgdc_rngdates, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.addDate = QtWidgets.QDateEdit(self.tab_3)
        self.addDate.setGeometry(QtCore.QRect(30, 20, 110, 22))
        self.addDate.setCalendarPopup(True)
        self.addDate.setDate(QtCore.QDate(2000, 1, 30))
        self.addDate.setObjectName("addDate")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 111, 31))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 191, 20))
        self.label_7.setObjectName("label_7")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(220, 10, 111, 71))
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 50, 61, 31))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.fgdc_timeinfo.addTab(self.tab_3, "")
        self.label_3 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_3.setGeometry(QtCore.QRect(380, 100, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.fgdc_current = QtWidgets.QComboBox(self.fgdc_timeperd)
        self.fgdc_current.setGeometry(QtCore.QRect(410, 50, 131, 21))
        self.fgdc_current.setEditable(True)
        self.fgdc_current.setObjectName("fgdc_current")
        self.fgdc_current.addItem("")
        self.fgdc_current.setItemText(0, "")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.label_8 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_8.setGeometry(QtCore.QRect(410, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.fgdc_timeperd)

        self.retranslateUi(Form)
        self.fgdc_timeinfo.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_timeperd.setTitle(_translate("Form", "Time Period Information"))
        self.label_2.setText(_translate("Form", "What is the time period of the information represented in the data set?"))
        self.label_4.setText(_translate("Form", "Date (YYYYMMDD)"))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.fgdc_timeinfo.setTabText(self.fgdc_timeinfo.indexOf(self.fgdc_sngdate), _translate("Form", "Single Date"))
        self.label_5.setText(_translate("Form", "BeginningDate (YYYYMMDD)"))
        self.label_6.setText(_translate("Form", "End Date (YYYYMMDD)"))
        self.dateEdit_2.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.dateEdit_3.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.fgdc_timeinfo.setTabText(self.fgdc_timeinfo.indexOf(self.fgdc_rngdates), _translate("Form", "Date Range"))
        self.addDate.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.pushButton.setText(_translate("Form", "Add Date"))
        self.label_7.setText(_translate("Form", "Add Series of Dates (YYYYMMDD)"))
        self.pushButton_2.setText(_translate("Form", "Delete"))
        self.fgdc_timeinfo.setTabText(self.fgdc_timeinfo.indexOf(self.tab_3), _translate("Form", "Multiple Dates"))
        self.label_3.setText(_translate("Form", "Enter information for only one option, either \'Single Date\', \'Date Range\', or \'Multiple Dates\'."))
        self.fgdc_current.setItemText(1, _translate("Form", "ground condition"))
        self.fgdc_current.setItemText(2, _translate("Form", "observed"))
        self.fgdc_current.setItemText(3, _translate("Form", "publication date"))
        self.fgdc_current.setItemText(4, _translate("Form", "See Supplemental Info"))
        self.label_8.setText(_translate("Form", "Currentness Reference"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

