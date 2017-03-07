#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Citation <citation> section


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.

Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.

Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""

from lxml import etree

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView, QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit, QRadioButton, QFrame
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle, QScrollArea, QGroupBox
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint



from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_Citation
from pymdwizard.gui.single_date import SingleDate
from pymdwizard.gui.repeating_element import RepeatingElement

class Citation(WizardWidget): #

    drag_label = "Citation <citation>"

    def __init__(self, parent=None, include_lwork=True):
        self.include_lwork = include_lwork
        WizardWidget.__init__(self, parent=parent)

    def build_ui(self, ):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_Citation.Ui_Form()
        self.ui.setupUi(self)

        if self.include_lwork:
            self.lworkcit_widget = Citation(parent=self, include_lwork=False)
            self.lworkcit_widget.ui.fgdc_lworkcit.deleteLater()
            self.ui.lworkcite_ext.layout().addWidget(self.lworkcit_widget)
        else:
            self.lworkcit_widget = None
        self.ui.lworkcite_ext.hide()

        self.ui.series_ext.hide()
        self.ui.pub_ext.hide()
        self.single_date = SingleDate(label='', show_format=False)
        self.ui.pubdate_layout.addWidget(self.single_date)

        #Multi_Inst onlink
        olParams = {'Add text':'add another url',
                  'Remove text': 'remove last url',
                  'widget_kwargs': {'label': 'Link'}}
        self.onlink_list = RepeatingElement(params=olParams)
        self.onlink_list.add_another()
        self.ui.onlink_layout.addWidget(self.onlink_list)

        #Multi_Inst originator
        ogParams = {'Add text':'add another originator',
                  'Remove text': 'remove last originator',
                  'widget_kwargs': {'label': 'Originator'}}
        self.fgdc_origin = RepeatingElement(params=ogParams, which='vertical')
        self.fgdc_origin.add_another()
        self.ui.originator_layout.addWidget(self.fgdc_origin)

        self.setup_dragdrop(self)

    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.radio_lworkyes.toggled.connect(self.include_lworkext_change)
        self.ui.radioButton_3.toggled.connect(self.include_seriesext_change)
        self.ui.radioButton_5.toggled.connect(self.include_pubext_change)



    def include_seriesext_change(self, b):
        """
        Extended citation to support series information of the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.series_ext.show()
        else:
            self.ui.series_ext.hide()

    def include_pubext_change(self, b):
        """
        Extended citation to support publication information of the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.pub_ext.show()
        else:
            self.ui.pub_ext.hide()

    def include_lworkext_change(self, b):
        """
        Extended citation to support a larger body of information for the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.lworkcite_ext.show()
        else:
            self.ui.lworkcite_ext.hide()


    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'citation'

        Parameters
        ----------
        e : qt event

        Returns
        -------
        None

        """
        print("pc drag enter")
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element.tag == 'citation':
                e.accept()
        else:
            e.ignore()


         
                
    def _to_xml(self):
        """
        encapsulates the QLineEdit text in an element tag

        Returns
        -------
        citation element tag in xml tree
        """
        citation = etree.Element('citation')
        citeinfo = etree.Element('citeinfo')

        pubdate = etree.Element("pubdate")
        # edition = etree.Element("edition")
        geoform = etree.Element("geoform")
        title = etree.Element("title")
        onlink = etree.Element("onlink")
        cnt = 0
        list_orig = self.fgdc_origin.widgets
        len_listorig = len(self.fgdc_origin.widgets)
        while cnt < len_listorig:
            linEdit = self.fgdc_origin.widgets[cnt].findChildren(QLineEdit)
            og_text = linEdit[0].text()
            str_og = str(og_text)
            origin = etree.Element("origin")
            origin.text = str_og
            cnt +=1
            citeinfo.append(origin)

        temp_var = self.single_date.findChild(QLineEdit, "lineEdit").text()
        pubdate.text = temp_var

        title.text = self.findChild(QLineEdit, "fgdc_title").text()
        # edition.text = self.findChild(QLineEdit, "fgdc_edition").text()
        # geoform.text = self.findChild(QComboBox, "fgdc_geoform").currentText()

        citeinfo.append(pubdate)
        citeinfo.append(title)
        # citeinfo.append(edition)
        # citeinfo.append(geoform)

        if self.ui.radioButton_3.isChecked():
            serinfo = etree.Element("serinfo")
            sername = etree.Element("sername")
            sername.text = self.findChild(QLineEdit, "fgdc_sername").text()
            issue = etree.Element("issue")
            issue.text = self.findChild(QLineEdit, "fgdc_issue").text()
            serinfo.append(sername)
            serinfo.append(issue)
            citeinfo.append(serinfo)

        else:
            pass

        if self.ui.radioButton_5.isChecked():
            pubinfo = etree.Element("pubinfo")
            pubplace = etree.Element("pubplace")
            pubplace.text = self.findChild(QLineEdit, "fgdc_pubplace").text()
            publish = etree.Element("publish")
            publish.text = self.findChild(QLineEdit, "fgdc_publish").text()
            pubinfo.append(pubplace)
            pubinfo.append(publish)
            citeinfo.append(pubinfo)

        else:
            pass

        if self.include_lwork and self.ui.radio_lworkyes.isChecked():
            lworkcit = self.lworkcit_widget._to_xml()
            citeinfo.append(lworkcit)

        for widget in self.onlink_list.get_widgets():
            onlink = xml_utils.xml_node('onlink', text=widget.added_line.text(),
                                        parent_node=citation)

        citation.append(citeinfo)
        return citation

    def _from_xml(self, citation):
        """
        parses the xml code into the relevant citation elements

        Parameters
        ----------
        citation - the xml element status and its contents

        Returns
        -------
        None
        """
        try:
            if citation.tag == "citation":
                if citation.findall("citeinfo/origin"):
                    origin_text = citation.findtext("citeinfo/origin")

                    origin_box = self.findChild(QLineEdit, 'fgdc_origin')
                    origin_box.setText(origin_text)
                else:
                    print ("No origin tag")

                if citation.findall("citeinfo/pubdate"):
                    pubdate_text = citation.findtext("citeinfo/pubdate")

                    pubdate_box = self.findChild(QLineEdit, 'fgdc_pubdate')
                    pubdate_box.setText(pubdate_text)
                else:
                    print ("No pubdate tag")

                if citation.findall("citeinfo/title"):
                    title_text = citation.findtext("citeinfo/title")

                    title_box = self.findChild(QLineEdit, 'fgdc_title')
                    title_box.setText(title_text)
                else:
                    print ("No title tag")

                if citation.findall("citeinfo/edition"):
                    edition_text = citation.findtext("citeinfo/edition")

                    edition_box = self.findChild(QLineEdit, 'fgdc_edition')
                    edition_box.setText(edition_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/geoform"):
                    geoform_text = citation.findtext("citeinfo/geoform")

                    geoform_box = self.findChild(QComboBox, 'fgdc_geoform')
                    geoform_box.setCurrentText(geoform_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/onlink"):
                    onlink_text = citation.findtext("citeinfo/onlink")

                    onlink_box = self.findChild(QLineEdit, 'fgdc_onlink')
                    onlink_box.setText(onlink_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/serinfo"):
                    self.ui.radioButton_3.setChecked(True)
                    sername_text = citation.findtext("citeinfo/serinfo/sername")

                    sername_box = self.findChild(QLineEdit, 'fgdc_sername')
                    sername_box.setText(sername_text)

                    issue_text = citation.findtext("citeinfo/serinfo/issue")

                    issue_box = self.findChild(QLineEdit, 'fgdc_issue')
                    issue_box.setText(issue_text)

                else:
                    print ("No series name tag")

                if citation.findall("citeinfo/pubinfo"):
                    self.ui.radioButton_5.setChecked(True)
                    pubplace_text = citation.findtext("citeinfo/pubinfo/pubplace")

                    pub_box = self.findChild(QLineEdit, 'fgdc_pubplace')
                    pub_box.setText(pubplace_text)

                    publish_text = citation.findtext("citeinfo/pubinfo/publish")

                    publish_box = self.findChild(QLineEdit, 'fgdc_publish')
                    publish_box.setText(publish_text)

                else:
                    print ("No pub tag")

                    ##############################################################################################################

                if citation.findall("citeinfo/lworkcit"):
                    self.ui.radioButton.setChecked(True)
                    if citation.findall("citeinfo/lworkcit/citeinfo/origin"):
                        origin_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/origin")

                        origin_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_origin')
                        origin_box1.setText(origin_text1)
                    else:
                        print ("No origin tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/origin"):
                        pubdate_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubdate")

                        pubdate_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_pubdate')
                        pubdate_box1.setText(pubdate_text1)
                    else:
                        print ("No pubdate tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/title"):
                        title_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/title")

                        title_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_title')
                        title_box1.setText(title_text1)
                    else:
                        print ("No title tag")

                    if citation.findall("lworkcit/citeinfo/edition"):
                        edition_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/edition")

                        edition_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_edition')
                        edition_box1.setText(edition_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/geoform"):
                        geoform_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/geoform")

                        geoform_box1 = self.lworkcit.findChild(QComboBox, 'fgdc_geoform')
                        geoform_box1.setCurrentText(geoform_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/onlink"):
                        onlink_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/onlink")

                        onlink_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_onlink')
                        onlink_box1.setText(onlink_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/serinfo"):
                        self.lworkcit.ui.radioButton_3.setChecked(True)
                        sername_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/serinfo/sername")

                        sername_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_sername')
                        sername_box1.setText(sername_text1)

                        issue_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/serinfo/issue")

                        issue_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_issue')
                        issue_box1.setText(issue_text1)

                    else:
                        print ("No series name tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/pubinfo"):
                        self.lworkcit.ui.radioButton_5.setChecked(True)
                        pubplace_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubinfo/pubplace")

                        pub_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_pubplace')
                        pub_box1.setText(pubplace_text1)

                        publish_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubinfo/publish")

                        publish_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_publish')
                        publish_box1.setText(publish_text1)

                    else:
                        print ("No series issue tag")

                        ###########################################################################################


            else:
                print ("The tag is not citation")



        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(Citation,
                        "Citation testing")

