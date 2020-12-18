#!/usr/bin/python3
# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3,datetime
from os import path
import sys
import urllib.request
import os 
#import threading
import time
import pafy
import humanize
import posixpath
# import urlparse
# import UI file
from Downlod import Ui_MainWindow
class mainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Button()
        self.DataBase()
########################################################################################################################
################################################### connection db ######################################################
    def DataBase(self):
        self.db = sqlite3.connect('database.db')
        self.db1=self.db.cursor()
        self.db1.execute('CREATE TABLE IF NOT EXISTS TEST(ui TEXT primary key,name TEXT,size INT,ts TEXT,savep ,te TEXT,stat TEXT)')
        self.db1.execute('select name,size,ts,savep,te,stat from TEST')
        p=self.db1.fetchall()
        self.db.commit()
        for row,data in enumerate(p):
            r = self.tableWidget.rowCount()
            if r == row:
                self.tableWidget.insertRow(r)
                for column,item in enumerate(data):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column += 1

        self.db1.close()
        self.db.close()
########################################################################################################################
###################################################### ui change #######################################################
    def Handel_Ui(self):
        self.setWindowIcon(QIcon('brosser.png'))  ##icon program
        self.setWindowTitle("Downloader App")
        self.tabWidget.tabBar().setVisible(False)
        self.setFixedSize(703,483)
        #Animation
        self.Box_1()
        self.Box_2()
        self.Box_3()
        self.Box_4()

########################################################################################################################
####################################################### Button #########################################################
    def Handel_Button(self):
        self.pushButton.clicked.connect(self.Main_App)
        self.pushButton_2.clicked.connect(self.Signle_Download)
        self.pushButton_3.clicked.connect(self.Youtube_Download)
        self.pushButton_6.clicked.connect(self.history_App)
        self.pushButton_4.clicked.connect(self.Settings_App)
        ##############################################################################
        self.pushButton_5.clicked.connect(self.Handel_Browse)
        self.pushButton_16.clicked.connect(self.onstart)
        #####################################################
        self.pushButton_10.clicked.connect(self.On_Start_Get)
        self.pushButton_9.clicked.connect(self.Handel_Browse_youtube_1)
        self.pushButton_8.clicked.connect(self.On_Start_Video)
        ######################################################
        self.pushButton_13.clicked.connect(self.On_Start_Video_playlist)
        self.pushButton_12.clicked.connect(self.Handel_Browse_youtube_2)
        ################################################################################
        self.pushButton_14.clicked.connect(self.Apply_light_blue)
        self.pushButton_15.clicked.connect(self.Apply_dark)
###################################
    def close(self):
        if self.checkBox.isChecked():
            #os.system('shutdown -s')
            os.system('shutdown /p /f')
        if self.checkBox_2.isChecked():
            os._exit(0)
########################################################################################################################
########################################### Handel Button On TabWidget #################################################
    def Main_App(self):
        self.tabWidget.setCurrentIndex(0)
    def Signle_Download(self):
        self.tabWidget.setCurrentIndex(1)
    def Youtube_Download(self):
        self.tabWidget.setCurrentIndex(2)
        self.comboBox_2.addItem('افضل جودة')
        self.comboBox_2.addItem('افضل جودة فديو')
        self.comboBox_2.addItem('افضل جودة صوت')
    def history_App(self):
        self.tabWidget.setCurrentIndex(3)
        self.DataBase()
    def Settings_App(self):
        self.tabWidget.setCurrentIndex(4)
########################################################################################################################
################################################# Apply StyleSheet #####################################################
    def Apply_dark(self):

        self.setStyleSheet("QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon    : url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon    : url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon    : url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}")
    def Apply_light_blue(self):

        self.setStyleSheet(' ')
########################################################################################################################
################################################# App Animation ########################################################
    def Box_1(self):
        box_an1 = QPropertyAnimation(self.groupBox_2,b'geometry')
        box_an1.setDuration(1500)
        box_an1.setStartValue(QRect(500,500,0,0))
        box_an1.setEndValue(QRect(10,10,301,141))
        box_an1.start()
        self.box_an1 = box_an1
    def Box_2(self):
        box_an2 = QPropertyAnimation(self.groupBox_6,b'geometry')
        box_an2.setDuration(1500)
        box_an2.setStartValue(QRect(-500,500,0,0))
        box_an2.setEndValue(QRect(370,10,301,141))
        box_an2.start()
        self.box_an2 = box_an2
    def Box_3(self):
        box_an3 = QPropertyAnimation(self.groupBox_5,b'geometry')
        box_an3.setDuration(1500)
        box_an3.setStartValue(QRect(500,-500,0,0))
        box_an3.setEndValue(QRect(10,190,301,141))
        box_an3.start()
        self.box_an3 = box_an3
    def Box_4(self):
        box_an4 = QPropertyAnimation(self.groupBox_7,b'geometry')
        box_an4.setDuration(1500)
        box_an4.setStartValue(QRect(-500,-500,0,0))
        box_an4.setEndValue(QRect(370,190,301,141))
        box_an4.start()
        self.box_an4 = box_an4
    ########################################################################################################################
    ########################################### This Section For Singl Download ############################################
    def Handel_Browse(self):  # To Save The File With The Orginal
        save_file = QFileDialog.getExistingDirectory(self, "حفظ ك")
        a = self.lineEdit.text()
        path = urllib.parse.urlsplit(a).path
        filename = posixpath.basename(path)
        b = self.lineEdit_8.setText(filename)
        c = self.lineEdit_2.setText(save_file)
        return c
    #######################################################################################
    def onstart(self):  # To Run The Thread And Make Condition For The Line Edit If It Empty
        try:
            self.calc = Thread_run()  # To Take Object And Make Operation On It
            self.calc.count_changed.connect(self.count_change_process)  # To Connect The Signal From Thread To The Funciton In The Main Window
            self.calc.duration.connect(self.count_change_process_Single_label)  # To Connect The Signal From Thread To The Funciton In The Main Window
            self.calc.finsish.connect(self.download_finshed_Single)  # To Connect The Signal From Thread To The Funciton In The Main Window
            self.calc.error.connect(self.Handel_Error_Single)  # To Connect The Signal From Thread To The Funciton In The Main Window
            self.calc.finsh.connect(self.finsh5)
            self.calc.url_d = self.lineEdit.text()
            save = self.lineEdit_2.text()
            self.calc.save_d = self.lineEdit_2.text() + '/' + self.lineEdit_8.text()
            if self.calc.url_d == '':
                return self.label_3.setText("ضع الرابط للتحميل ")
            else:
                self.label_3.setText(" ")
                if save == '':
                    return self.label_4.setText("اختر مكان التحميل ")
                else:
                    self.label_4.setText(" ")
                    self.calc.start()  # To Run The QThread
                    self.lineEdit.setEnabled(False)
                    self.lineEdit_8.setEnabled(False)
                    self.lineEdit_2.setEnabled(False)
                    self.pushButton_5.setEnabled(False)
                    self.pushButton_16.setEnabled(False)
                    #######################################
                    self.ui = self.lineEdit.text()
                    save1 = self.lineEdit_8.text()
                    timep = datetime.datetime.now()
                    time1 = timep.strftime('%Y-%m-%d %H:%M:%S')
                    #######################
                    self.db = sqlite3.connect('database.db')
                    self.db1 = self.db.cursor()
                    self.db.row_factory = sqlite3.Row
                    self.db1.execute('select * from TEST')
                    p = self.db1.fetchall()
                    o = []
                    for i in p:
                        o.append(i[0])
                    if self.ui in o:
                        self.db1.execute('UPDATE TEST SET name=? ,ts=?,savep=?,stat=? WHERE ui=?', (save1,time1,save,'جاري التحميل',self.ui))
                        self.db.commit()
                        print('don')
                        self.db1.close()
                        self.db.close()
                    else:
                        self.db1.execute('INSERT INTO TEST(ui,name,ts,savep,stat ) VALUES(?,?,?,?,?)',(self.ui,save1,time1,save,'جاري التحميل') )
                        self.db.commit()
                        self.db1.close()
                        self.db.close()

        except Exception as a:
            timee = datetime.datetime.now()
            timer2 = timee.strftime('%Y-%m-%d %H:%M:%S')
            self.db = sqlite3.connect('database.db')
            self.db1 = self.db.cursor()
            self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل', timer2, self.ui))
            self.db.commit()
            self.db1.close()
            self.db.close()
    ##################################################################
    def count_change_process_Single_label(self, Saleh):
        self.label_8.setText(Saleh[0])
        siz=Saleh[1]
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET size=? WHERE ui=?', ( siz,self.ui))
        self.db.commit()

        self.db1.close()
        self.db.close()
    ##################################################################
    def Handel_Error_Single(self, error):
        try:
            self.label_8.setText('فشل التحيل تاكد من الرابط او تاكد من الاتصال بالانترنت')
            self.finsh5()
            timef = datetime.datetime.now()
            timeg1 = timef.strftime('%Y-%m-%d %H:%M:%S')
            self.db = sqlite3.connect('database.db')
            self.db1 = self.db.cursor()
            self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل',timeg1,self.ui))
            self.db.commit()

            self.db1.close()
            self.db.close()
        except Exception as a:
            print(a)
    ##################################################################
    def count_change_process(self, saleh):  # To Recived Signal From Thread And Make It In ProgressBar
        self.progressBar.setValue(saleh)
    ##################################################################
    def download_finshed_Single(self):  # To Take Signal From Thread If Download 100% Make That
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_8.setText('')
        self.label_8.setText('')
        self.finsh5()
        QMessageBox.information(self, 'انتهى التحميل', ' انتهى التحميل بنجاح ')  # To Show MessageBox
        timeq = datetime.datetime.now()
        timeq1 = timeq.strftime('%Y-%m-%d %H:%M:%S')
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('تم التحميل بنجاح', timeq1, self.ui))
        self.db.commit()

        self.db1.close()
        self.db.close()

        self.close()
    def finsh5 (self):
        self.lineEdit.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_16.setEnabled(True)
########################################################################################################################
################################## This Section For Get Data From Threading About Quality And Make It In ComboBox ######
    def On_Start_Get(self):  # To Run The Thread And Make Condition For The Line Edit If It Empty
        self.label_2.setText(" ")
        self.get_data = Thread_GetVideo_Data()
        self.get_data.Quality_Combo_Box.connect(self.get_data_combo)
        self.get_data.video_title.connect(self.get_data_title)
        self.get_data.erro.connect(self.erro)
        self.get_data.finsh.connect(self.finsh6)
        self.get_data.url_video1 = self.lineEdit_4.text()
        if self.get_data.url_video1 == '':
            return self.label_2.setText("ضع رابط الفيديو")
        else:
            self.label_2.setText(" ")
            self.get_data.start()  # To Run The QThread
            self.lineEdit_4.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_10.setEnabled(False)
            self.comboBox.setEnabled(False)
    #################################################################
    def get_data_combo(self, combo):  # To Recived Signal From Thread And Make It In ComboBox
        self.comboBox.addItem(combo)
    #################################################################
    def get_data_title(self, title):
        self.lineEdit_7.setText(title)
    ##################################################################
    def erro(self):
        self.label_2.setText("تاكد من الرابط او اتاكد من الانترنت ")
    def finsh6(self):
        self.lineEdit_4.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.pushButton_10.setEnabled(True)

########################################################################################################################
#################### This Section For Download Video From YouTube ######################################################
    def Handel_Browse_youtube_1(self):
        save_file =QFileDialog.getExistingDirectory(self ,"حفظ ك")
        return self.lineEdit_3.setText(save_file)#To save File With It Name 
####################################################################################################
    def On_Start_Video(self):
        try:
            self.video_download = Thread_Download_Video()
            self.video_download.count_change_Prog.connect(self.count_change_process_video_prog)
            self.video_download.count_change_label.connect(self.count_change_process_video_label)
            self.video_download.finsish_video.connect(self.download_finshed_Video)
            self.video_download.erro.connect(self.erorr1)
            self.video_download.video_url = self.lineEdit_4.text()
            self.video_download.save_video = self.lineEdit_3.text()
            self.video_download.indexC = self.comboBox.currentIndex()
            if self.video_download.video_url == '':
                return self.label_2.setText("ضع رابط الفيديو")
            else:
                self.label_2.setText(" ")
                if self.video_download.save_video == '':
                    return self.label.setText("اختر مكان التحميل")
                else:
                    self.label.setText(" ")
                    self.video_download.start() # To Run The QThread
            ################################################
                    self.ul=self.lineEdit_4.text()
                    save1 =self.lineEdit_7.text()
                    save=self.lineEdit_3.text()
                    time = datetime.datetime.now()
                    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
                    self.db = sqlite3.connect('database.db')
                    self.db1 = self.db.cursor()
                    self.db.row_factory = sqlite3.Row
                    self.db1.execute('select * from TEST')
                    p = self.db1.fetchall()
                    o = []
                    for i in p:
                        o.append(i[0])
                    if self.ul in o:
                        print(12)
                        self.db1.execute('UPDATE TEST SET name=? ,ts=?,savep=?,stat=? WHERE ui=?',(save1, time1, save, 'جاري التحميل', self.ul))
                        self.db.commit()
                        self.db1.close()
                        self.db.close()
                    else:
                        self.db1.execute('INSERT INTO TEST(ui,name,ts,savep,stat ) VALUES(?,?,?,?,?)',
                                         (self.ul, save1, time1, save, 'جاري التحميل'))
                        self.db.commit()
                        self.db1.close()
                        self.db.close()
        except Exception as a:
            timee = datetime.datetime.now()
            timer2 = timee.strftime('%Y-%m-%d %H:%M:%S')
            self.db = sqlite3.connect('database.db')
            self.db1 = self.db.cursor()
            self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل', timer2, self.ul))
            self.db.commit()
            self.db1.close()
            self.db.close()
    #####################################################################
    def count_change_process_video_prog(self,value):
        self.progressBar_4.setValue(value)
    #####################################################################
    def count_change_process_video_label(self,Ahmed):
        self.label_7.setText(str('''عدد الدقائق المتبقيه {}
                                          الحجم {}
                                          {}
          السرعة {}                             '''.format(Ahmed[3],Ahmed[0],Ahmed[1],Ahmed[2])))
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET size=? WHERE ui=?', (Ahmed[0], self.ul))
        self.db.commit()
        self.db1.close()
        self.db.close()
    #####################################################################
    def download_finshed_Video(self):
        self.progressBar_4.setValue(0)
        self.lineEdit_4.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.clear()
        self.lineEdit_7.setText('')
        QMessageBox.information(self,'انتهى التحميل',' انتهى التحميل بنجاح ') # To Show MessageBox
        timeq = datetime.datetime.now()
        timeq1 = timeq.strftime('%Y-%m-%d %H:%M:%S')
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('تم التحميل بنجاح', timeq1, self.ul))
        self.db.commit()

        self.db1.close()
        self.db.close()

        self.close()
    #######################################################################
    def erorr1(self):
        self.label_7.setText('فشل التحميل تاكد تاكد من وجود انترنت ')
        timef = datetime.datetime.now()
        timeg1 = timef.strftime('%Y-%m-%d %H:%M:%S')
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل', timeg1, self.ul))
        self.db.commit()
        self.db1.close()
        self.db.close()
########################################################################################################################
########################################################################################################################
######################################### Download Video PlayList ######################################################
    def Handel_Browse_youtube_2(self): # To
        save_file =QFileDialog.getExistingDirectory(self ,"حفظ ك")
        return self.lineEdit_6.setText(save_file)#To save File With It Name 
    ###############################################################################
    def On_Start_Video_playlist(self):
        try:
            self.video_download_playlist = Thread_play_list()
            self.video_download_playlist.count_progress.connect(self.count_Signal_Prog)
            self.video_download_playlist.count_lcd1.connect(self.count_Signal_lcd1)
            self.video_download_playlist.count_lcd2.connect(self.count_Signal_lcd2)
            self.video_download_playlist.count_label.connect(self.count_change_labelplaylist)
            self.video_download_playlist.finshed_playlist.connect(self.Finshed_Signal)
            self.video_download_playlist.erro.connect(self.erro2)
            self.video_download_playlist.playlist_url = self.lineEdit_5.text()
            self.video_download_playlist.playlist_save = self.lineEdit_6.text()
            self.video_download_playlist.indexC1 = self.comboBox_2.currentIndex()
            if self.video_download_playlist.playlist_url == '' :
                return self.label_5.setText("ضع رابط القائمه للتحميل")
            else:
                self.label_5.setText('')
                if self.video_download_playlist.playlist_save == '':
                    return self.label_6.setText("اختر مكان للتحميل ")
                else:
                    self.label_6.setText('')
                    self.video_download_playlist.start() # To Run The QThread
                    self.lineEdit_5.setEnabled(False)
                    self.lineEdit_6.setEnabled(False)
                    self.comboBox_2.setEnabled(False)
                    self.pushButton_13.setEnabled(False)
                    self.pushButton_12.setEnabled(False)
                    ###################################
                    self.uii=self.lineEdit_5.text()
                    save = self.lineEdit_6.text()
                    time = datetime.datetime.now()
                    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
                    self.db = sqlite3.connect('database.db')
                    self.db1 = self.db.cursor()
                    self.db.row_factory = sqlite3.Row
                    self.db1.execute('select * from TEST')
                    p = self.db1.fetchall()
                    o = []
                    for i in p:
                        o.append(i[0])
                    if self.uii in o:
                        self.db1.execute('UPDATE TEST SET ts=?,savep=?,stat=? WHERE ui=?',
                                         (time1, save, 'جاري التحميل', self.uii))
                        self.db.commit()
                        print('don')
                        self.db1.close()
                        self.db.close()
                    else:
                        self.db1.execute('INSERT INTO TEST(ui,ts,savep,stat ) VALUES(?,?,?,?)',
                                         (self.uii, time1, save, 'جاري التحميل'))
                        self.db.commit()
                        self.db1.close()
                        self.db.close()

        except Exception as a:
            timee = datetime.datetime.now()
            timer2 = timee.strftime('%Y-%m-%d %H:%M:%S')
            self.db = sqlite3.connect('database.db')
            self.db1 = self.db.cursor()
            self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل', timer2, self.uii))
            self.db.commit()
            self.db1.close()
            self.db.close()

    ###############################################################################
    def count_Signal_Prog(self,pro):
        self.progressBar_3.setValue(pro)
    ###############################################################################
    def count_Signal_lcd1(self,numb):
        self.lcdNumber_2.display(numb[0])
        n=str(numb[0])+"عدد الفديوهات"
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET size=? ,name=? WHERE ui=?', (n, numb[1],self.uii))
        self.db.commit()
        self.db1.close()
        self.db.close()
    ###############################################################################
    def count_Signal_lcd2(self,numb1):
        self.lcdNumber_3.display(numb1)
    ###############################################################################
    def Finshed_Signal (self):
        QMessageBox.information(self,'انتهى التحميل','انتهي التحميل بنجاح ')
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        time = datetime.datetime.now()
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('تم التحميل بنجاح', time1, self.uii))
        self.db.commit()
        self.db1.close()
        self.db.close()

        self.close()
    ###############################################################################
    def count_change_labelplaylist(self,numb2):

        self.label_21.setText(str('''عدد الدقائق المتبقيه {}
                                          الحجم {}
                                          {}
          السرعة {}                             '''.format(numb2[3],numb2[0],numb2[1],numb2[2])))
    ###############################################################################
    def erro2(self):
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.label_21.setText('فشل التحميل حاول مره اخري')
        time = datetime.datetime.now()
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.db = sqlite3.connect('database.db')
        self.db1 = self.db.cursor()
        self.db1.execute('UPDATE TEST SET stat=? ,te=? WHERE ui=?', ('فشل التحميل', time1, self.uii))
        self.db.commit()
########################################################################################################################
########################################################################################################################
##################### This Threading For ProgressBar SinglDownload File ################################################
class Thread_run(QThread):
    count_changed = pyqtSignal(int) # This Signal For ProgressBar
    finsish = pyqtSignal() # This Signal To Take Signal From Percent To Show QMessageBox To Show The Download Finshed
    duration = pyqtSignal(object)
    error = pyqtSignal(str)
    finsh=pyqtSignal()
    def run (self):
        try:
            d=urllib.request.urlretrieve(self.url_d,self.save_d,self.Handel_ProgressBar)
        except Exception as a :
            print(a)
            self.error.emit(str(a))
    def Handel_ProgressBar(self,block_num,blocksize,totalsize):
        global start_time
        try:
            if totalsize>0:
                start_time = time.time()
                duration = time.time() - start_time
                downloaded = block_num*blocksize
                speed = downloaded/(1024*duration)
                percent=(downloaded*100)/totalsize
                self.count_changed.emit(percent)
                ay=[(" %d%%, %d  MB ,  %s KB/S  , %d  seconds    passed" %(percent, downloaded / (1024 * 1024) , humanize.naturalsize(speed/1024), duration)),totalsize]
                self.duration.emit(ay)
                if percent >= 100 :
                    self.finsish.emit()

        except Exception as a:
            print(a)
        finally:
            self.finsh.emit()
########################################################################################################################
############################################# get quality ##############################################################
class Thread_GetVideo_Data(QThread):
    Quality_Combo_Box = pyqtSignal(str)
    video_title = pyqtSignal(str)
    erro=pyqtSignal()
    finsh=pyqtSignal()
    def run(self):
        try:
            video = pafy.new(self.url_video1)
            video_streams = video.allstreams
            self.video_title.emit(video.title)
            for stream in video_streams:
                size = humanize.naturalsize(stream.get_filesize())
                data = '{} - {} - {} - {}'.format(stream.mediatype, stream.extension, stream.quality, size)
                self.Quality_Combo_Box.emit(data)
        except Exception as a:
            self.erro.emit()
            print(a)
        finally:
            self.finsh.emit()
########################################################################################################################
############################################# Single Video Downoad From Youtube ########################################
class Thread_Download_Video(QThread):
    count_change_Prog = pyqtSignal(int)
    count_change_label = pyqtSignal(object)
    finsish_video = pyqtSignal()
    erro=pyqtSignal()
    def run(self):
        try:
            video = pafy.new(self.video_url)
            video_stream = video.allstreams
            download = video_stream[self.indexC].download(filepath=self.save_video,callback=self.Video_Single_ProgressBar)
        except Exception as a:
            self.erro.emit()
            print(a)
    def Video_Single_ProgressBar(self, total, recived, ratio, rate, time):
        try:
            read_data = recived
            if total > 0:
                pro = ratio * 100
                Sze = humanize.naturalsize(total)
                Recvd = humanize.naturalsize(recived)
                Rate = humanize.naturalsize(rate)
                self.count_change_Prog.emit(pro)
                remeaning =round(time / 60, 2)
                rt = [Sze, Recvd, Rate, remeaning]
                self.count_change_label.emit(rt)
                if pro >= 100:
                    self.finsish_video.emit()
        except Exception as a:
            print(a)
########################################################################################################################
################################################## play list ###########################################################
class Thread_play_list(QThread):
    count_progress = pyqtSignal(int)
    count_lcd1 = pyqtSignal(object)
    count_lcd2 = pyqtSignal(int)
    finshed_playlist = pyqtSignal()
    count_label = pyqtSignal(object)
    erro= pyqtSignal()
    def run(self):
        try:
            playlist = pafy.get_playlist(self.playlist_url)
            playlist_video = playlist['items']
            self.count_lcd1.emit([len(playlist_video),playlist['title']])
            os.chdir(self.playlist_save)
            if os.path.exists(str(playlist['title'])):
                os.chdir(str(playlist['title']))
            else:
                os.mkdir(playlist['title'])
                os.chdir(str(playlist['title']))
            current_video_in_download = 1
            quality = self.indexC1
            print(1)
            if quality ==0:
                for video in playlist_video:
                    current_video_stream = video['pafy'].getbest(preftype='mp4')
                    print(3)
                    self.count_lcd2.emit(current_video_in_download)
                    print(4)
                    current_video_stream.download(callback=self.Playlist_Progress)
                    current_video_in_download += 1
            elif quality ==1:
                for video in playlist_video:
                    current_video_stream = video['pafy'].getbestvideo()
                    self.count_lcd2.emit(current_video_in_download)
                    download = current_video_stream.download(callback=self.Playlist_Progress)
                    current_video_in_download += 1
            else:
                for video in playlist_video:
                    current_video_stream = video['pafy'].getbestaudio()
                    self.count_lcd2.emit(current_video_in_download)
                    download = current_video_stream.download(callback=self.Playlist_Progress)
                    current_video_in_download += 1
            print(2)
        except Exception as a:
            self.erro.emit()
            print(a)
    def Playlist_Progress(self, total, recived, ratio, rate,time):
        try:
            read_data = recived
            if total > 0:
                pro = ratio * 100
                Sze = humanize.naturalsize(total)
                Recvd = humanize.naturalsize(recived)
                Rate = humanize.naturalsize(rate)
                self.count_progress.emit(pro)

                remeaning = [round(time / 60, 2)]
                rt = [Sze, Recvd, Rate,remeaning]
                self.count_label.emit(rt)
        except Exception as a:
            print(a)
########################################################################################################################
####################################### The End Of The Section Of Single Download ######################################
def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
    #https://www.youtube.com/watch?v=sA0-QXbLnaE               https://www.youtube.com/playlist?list=PLY_6uAtgkYXmXFl-zzZ0wQErGi4AbgSkn