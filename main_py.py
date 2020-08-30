from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pafy
import  time
#this to treat witn file and open main.ui
import os
from os import path
#this to start the app
import sys
#this to turn byt to Mb
import humanize
#to use main.ui without turn it to main.py
from main import Ui_MainWindow

class mainapp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Button()
        self.UI()


####this is change will happen when app startz
    def UI(self):
        #titel of MainWindow and size
        self.setWindowTitle("Downloader videos from youtube")
        self.setFixedSize(807,354)
    # control with button
    def Button(self):
        self.pushButton_2.clicked.connect(self.Download)
        self.pushButton.clicked.connect(self.Save_Browse)
        self.pushButton_3.clicked.connect(self.Get_quailty)
#######to select place of save
    def Save_Browse(self):
        place = QFileDialog.getExistingDirectory(self, " please select download directory ")
        self.lineEdit_2.setText(place)
######to resever information about downloding
    def Progress(self,list):
        pro=list[0]
        Sze =list[1]
        Recvd=list[2]
        Rate=list[3]
        name=list[4]
        long=list[5]
        self.setFixedSize(832, 650)
        self.progressBar.setValue(int(pro))
        self.label_3.setText("Name video : {}\n\nLength video : {}\n\nSize video : {}\n\nRate : {} \n\nRecvd : {}".format(name,long,Sze,Rate,Recvd))

#####to get quality of video
    def Get_quailty(self):
        self.Vido_Dl = self.lineEdit.text()# lenk of video
        if self.Vido_Dl =="":
            self.label_4.setText("please enter link of video")
        else:
            try:
                self.label_4.setText(" ")
                self.work = WorkerThread(self.Vido_Dl)
                self.work.quality.connect(self.showquality)
                self.work.error.connect(self.erro1)
                self.work.finsh.connect(self.finsh1)
                self.work.start()
                self.lineEdit.setEnabled(False)
                self.pushButton_3.setEnabled(False)
            except Exception as p:
                pass
                '''print(p)
            self.label_4.setText("the link isn't correct or ckeck the internet ")
        except Exception as p:
            print(p)'''
    def showquality(self,text):
        self.comboBox.addItem(text)
    def erro1(self):
        self.label_4.setText("the link isn't correct or ckeck the internet ")

    def finsh1(self):
        self.lineEdit.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        #print (self.work.isFinished())
        self.work.exit()
#####download video
    def Download(self):
        self.label_6.setText("")  ##to story link and place save and quaity video
        Vido_Dl = self.lineEdit.text()
        Save_location = self.lineEdit_2.text()
        qualit = self.comboBox.currentIndex()
        if Vido_Dl == "":
            self.label_4.setText("please enter link of video")
        else:
            self.label_4.setText("")
            if Save_location == "":
                self.label_5.setText("please enter save location of video")
            else:
                self.label_5.setText("")
                try:
                    self.worker=WorkerThreadDown(Vido_Dl,Save_location,qualit)
                    self.worker.All.connect(self.Progress)
                    self.worker.finsh.connect(self.finsh)
                    self.worker.error.connect(self.erro)
                    self.worker.start()
                    self.lineEdit.setEnabled(False)
                    self.pushButton_3.setEnabled(False)
                    self.pushButton_2.setEnabled(False)
                    self.pushButton.setEnabled(False)
                    self.comboBox.setEnabled(False)
                except:
                    self.label_6.setText("The Downlaod has faild  please tye agan ")
                    self.setFixedSize(807, 354)
                    self.label_3.setText("  ")
    def erro(self):
        self.i()
        self.label_6.setText("             The Downlaod has faild  please tye agan ")
        self.setFixedSize(807, 354)
        self.label_3.setText("  ")

    def i(self):
        self.lineEdit.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.comboBox.setEnabled(True)

    def finsh(self):
        ########to clean all after download
        QMessageBox.information(self, " Information", "The Downlaod has done \n thank you  ")
        self.i()
        #self.worker.stop
        self.lineEdit.setText("")
        self.progressBar.setValue(0)
        self.comboBox.clear()
        self.setFixedSize(807, 354)
        self.label_3.setText(" ")
################# threading ###################to search quality and set it to showquality############################
class WorkerThread(QThread):
    quality=pyqtSignal(str)
    error = pyqtSignal()
    finsh=pyqtSignal()
    def __init__(self,link,parent=None):
        super(WorkerThread, self).__init__(parent)
        self.link=link #lenk of video
    def run(self):
        try:
            vido = pafy.new(self.link)  # to connect with internet
            qualiy = vido.videostreams  # to all video quality
            for q in qualiy:  # to show all quality in combox
                size = humanize.naturalsize(q.get_filesize())  # to turn size from byte
                Qualiy = ' {}   {}   {}   {}  '.format(q.mediatype, q.extension, q.quality, size)
                self.quality.emit(Qualiy)
        except:
            self.error.emit()

        finally:
            self.finsh.emit()

################# threading ###################to downlaod vidio ###############
class WorkerThreadDown(QThread):
    All=pyqtSignal(object)
    finsh=pyqtSignal()
    error=pyqtSignal()
    def __init__(self,link,saveplace,quality,parent=None):
        super(WorkerThreadDown, self).__init__(parent)
        self.link=link #lenk of video
        self.saveplace=saveplace
        self.quality=quality
    def run(self):
        try:
            time.sleep(3)
            vido = pafy.new(self.link)
            self.name = vido.title
            self.long = vido.duration
            v = vido.videostreams
            ##to start downlaod
            down = v[self.quality].download(filepath=self.saveplace, quiet=True, callback=self.Progress)
        #self.quality.emit(Qualiy)
        except Exception as a:
            #print (a)
            self.error.emit()
    def Progress(self, total, recvd, ratio, rate, eta):
        try:
            pro =ratio * 100
            Sze = humanize.naturalsize(total)
            Recvd = humanize.naturalsize(recvd)
            Rate = humanize.naturalsize(rate)
            rt=[pro, Sze, Recvd, Rate,self.name,self.long]
            self.All.emit(rt)
            if pro >=100:
                self.finsh.emit()

        except Exception as a:
            print (a)





#https://www.youtube.com/watch?v=il444OsH4E4