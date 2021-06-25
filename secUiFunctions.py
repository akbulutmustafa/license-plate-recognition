from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QStyleFactory, QTabWidget, QInputDialog, QMessageBox
from secUi import Ui_MainWindow
from editdia import Ui_Dialog
from PyQt5.QtGui import QPixmap, QImage
from detect import platedetect
import cv2
import mysql.connector
from datetime import datetime


class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.allEntries()
        self.ui.btnSubmit.clicked.connect(self.saveCar)
        # self.ui.btnRefresh.clicked.connect(self.loadData)
        self.ui.carList.cellClicked.connect(self.cell_was_clicked)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.timer = QtCore.QTimer()

        self.ui.imchoose.clicked.connect(self.openDialog)
        self.ui.plateFind.clicked.connect(self.plateBox)
        self.ui.readPlate.clicked.connect(self.ocr)

        self.timer.timeout.connect(self.view_cam)
        self.ui.opencam.clicked.connect(self.control_timer)
        self.ui.savecam.clicked.connect(self.save)

        self.ui.slctdDate.clicked.connect(self.getDate)
        self.ui.showAll.clicked.connect(self.allEntries)

    image_path = ''
    crop_path = ''
    plate_num = ''
    selected_date = ''

    # save_img = None

    def openDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(directory='./data/images/',
                                                  filter="All Files (*);;Image Files (*.jpg, *.png)")

        if fileName:
            # fileName = fileName.split('/')[-1]
            # print(fileName)
            # self.photo.setPixmap(QtGui.QPixmap('data/images/'+fileName))
            self.ui.img.setPixmap(QtGui.QPixmap(fileName))
            self.image_path = fileName

    def plateBox(self):
        image, self.plate_num, self.crop_path = platedetect(self.image_path)
        # image = './detections/detection1.png'
        self.ui.img.setPixmap(QtGui.QPixmap(image))

    def ocr(self):
        self.ui.platetxt.setText(self.plate_num)

    def view_cam(self):
        ret, image = self.cap.read()
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite('./data/images/camCapture.png', image)

        height, width, channel = image.shape
        step = channel * width

        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.img.setPixmap(QPixmap.fromImage(qImg))

    def control_timer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            self.ui.opencam.setText("Kamerayı Kapat")
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.opencam.setText("Kamerayı Aç")

    def save(self):
        if self.timer.isActive():
            self.ui.opencam.click()
        image = cv2.imread('./data/images/camCapture.png')

        height, width, channel = image.shape
        step = channel * width
        self.image_path = './data/images/camCapture.png'

        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.img.setPixmap(QPixmap.fromImage(qImg))

    def getDate(self):
        self.selected_date = str(self.ui.dateEdit.date().getDate())
        #print(self.selected_date)
        self.loadData()

    def saveCar(self):
        mdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cars"
        )

        name = self.ui.txtName.text()
        surname = self.ui.txtSurname.text()
        plate = self.plate_num  # self.ui.txtPlate.text()
        now = datetime.now()
        enterTime = now.strftime('%Y-%m-%d %H:%M:%S')
        exitTime = ("1000-01-01 00:00:00")
        self.selected_date = str(self.ui.dateEdit.date().getDate())

        mcursor = mdb.cursor()
        sql = "INSERT INTO newcar (`name`, `surname`, `plate`, `filename`, `enter`, `exit`, `entrydate`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name, surname, plate, self.image_path, enterTime, exitTime, self.selected_date)
        mcursor.execute(sql, val)

        try:
            mdb.commit()
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            mdb.close()

        self.ui.txtName.setText("")
        self.ui.txtSurname.setText("")
        self.loadData()

    def deleteCar(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.carList.indexAt(button.pos())
        if index.isValid():
            mdb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cars"
            )

            mcursor = mdb.cursor()
            if self.selected_date == '':
                mcursor.execute("select * from newcar")
            else:
                mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
            result = mcursor.fetchall()
            id = result[index.row()][0]

        sql = "DELETE FROM newcar WHERE `id`=%s"
        val = (id,)
        mcursor.execute(sql, val)

        try:
            mdb.commit()
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            mdb.close()
        self.selected_date = str(self.ui.dateEdit.date().getDate())
        self.loadData()

    def updateCar(self, name, surname, plate, time, id):
        mdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cars"
        )

        mcursor = mdb.cursor()
        sql = "update newcar set `name`=%s, `surname`=%s, `plate`=%s, `exit`=%s where `id`=%s"
        val = (name, surname, plate, time, id)
        mcursor.execute(sql, val)

        try:
            mdb.commit()
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            mdb.close()

    def cell_was_clicked(self, row, column):
        mdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cars"
        )

        mcursor = mdb.cursor()
        if self.selected_date == '':
            mcursor.execute("select * from newcar")
        else:
            mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
        result = mcursor.fetchall()
        self.ui.img.setPixmap(QtGui.QPixmap(result[row][4]))
        mdb.close()


    def loadData(self):

        mdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cars"
        )

        mcursor = mdb.cursor()
        mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
        result = mcursor.fetchall()
        row = 0
        self.ui.carList.setRowCount(0)
        self.ui.carList.setRowCount(len(result))
        for r in result:
            self.btn_sell = QtWidgets.QPushButton('Çıkış')
            self.btn_sell.clicked.connect(self.handleButtonClicked)
            self.btnEdit = QtWidgets.QPushButton('Düzenle')
            self.btnEdit.clicked.connect(self.show_dialog)
            self.btnDelete = QtWidgets.QPushButton('Sil')
            self.btnDelete.clicked.connect(self.deleteCar)

            self.ui.carList.setItem(row, 0, QtWidgets.QTableWidgetItem(r[1]))
            self.ui.carList.setItem(row, 1, QtWidgets.QTableWidgetItem(r[2]))
            self.ui.carList.setItem(row, 2, QtWidgets.QTableWidgetItem(r[3]))
            self.ui.carList.setItem(row, 3, QtWidgets.QTableWidgetItem(r[5].strftime('%H:%M:%S')))# %Y-%m-%d
            if r[6].strftime('%Y-%m-%d %H:%M:%S') == "1000-01-01 00:00:00":
                self.ui.carList.setCellWidget(row, 4, self.btn_sell)
            else:
                self.ui.carList.setItem(row, 4, QtWidgets.QTableWidgetItem(r[6].strftime('%H:%M:%S')))
            self.ui.carList.setItem(row, 5, QtWidgets.QTableWidgetItem(r[7]))
            self.ui.carList.setCellWidget(row, 6, self.btnEdit)
            self.ui.carList.setCellWidget(row, 7, self.btnDelete)

            row += 1

    def allEntries(self):

        self.selected_date = ''
        mdb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cars"
        )

        mcursor = mdb.cursor()
        mcursor.execute("SELECT * FROM newcar")
        result = mcursor.fetchall()
        row = 0
        self.ui.carList.setRowCount(0)
        self.ui.carList.setRowCount(len(result))
        for r in result:
            self.btn_sell = QtWidgets.QPushButton('Çıkış')
            self.btn_sell.clicked.connect(self.handleButtonClicked)
            self.btnEdit = QtWidgets.QPushButton('Düzenle')
            self.btnEdit.clicked.connect(self.show_dialog)
            self.btnDelete = QtWidgets.QPushButton('Sil')
            self.btnDelete.clicked.connect(self.deleteCar)

            self.ui.carList.setItem(row, 0, QtWidgets.QTableWidgetItem(r[1]))
            self.ui.carList.setItem(row, 1, QtWidgets.QTableWidgetItem(r[2]))
            self.ui.carList.setItem(row, 2, QtWidgets.QTableWidgetItem(r[3]))
            self.ui.carList.setItem(row, 3, QtWidgets.QTableWidgetItem(r[5].strftime('%H:%M:%S')))# %Y-%m-%d
            if r[6].strftime('%Y-%m-%d %H:%M:%S') == "1000-01-01 00:00:00":
                self.ui.carList.setCellWidget(row, 4, self.btn_sell)
            else:
                self.ui.carList.setItem(row, 4, QtWidgets.QTableWidgetItem(r[6].strftime('%H:%M:%S')))
            self.ui.carList.setItem(row, 5, QtWidgets.QTableWidgetItem(r[7]))
            self.ui.carList.setCellWidget(row, 6, self.btnEdit)
            self.ui.carList.setCellWidget(row, 7, self.btnDelete)

            row += 1

    def handleButtonClicked(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.carList.indexAt(button.pos())
        if index.isValid():
            mdb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cars"
            )

            mcursor = mdb.cursor()
            if self.selected_date == '':
                mcursor.execute("select * from newcar")
            else:
                mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
            result = mcursor.fetchall()
            id = result[index.row()][0]
            mdb.close()
            now = datetime.now()
            name = result[index.row()][1]
            surname = result[index.row()][2]
            plate = result[index.row()][3]
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            self.updateCar(name, surname, plate, time, id)
            self.loadData()

    def updateDialog(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.carList.indexAt(button.pos())
        if index.isValid():
            mdb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cars"
            )

            mcursor = mdb.cursor()
            if self.selected_date == '':
                mcursor.execute("select * from newcar")
            else:
                mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
            result = mcursor.fetchall()
            id = result[index.row()][0]
            mdb.close()
            # now = datetime.now()
            name = result[index.row()][1]
            surname = result[index.row()][2]
            plate = result[index.row()][3]
            time = "1000-01-01 00:00:00"  # now.strftime('%Y-%m-%d %H:%M:%S')
            self.updateCar(name, surname, plate, time, id)
            self.loadData()

    def show_dialog(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.carList.indexAt(button.pos())
        if index.isValid():
            mdb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cars"
            )

            mcursor = mdb.cursor()
            if self.selected_date == '':
                mcursor.execute("select * from newcar")
            else:
                mcursor.execute("SELECT * FROM newcar WHERE entrydate=%s", (self.selected_date,))
            result = mcursor.fetchall()
            #mdb.close()
            id = result[index.row()][0]
            name = result[index.row()][1]
            surname = result[index.row()][2]
            plate = result[index.row()][3]

            dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(dialog)
            dialog.show()

            ui.txtad.setText(name)
            ui.txtsoyad.setText(surname)
            ui.txtplk.setText(plate)
            rsp = dialog.exec_()

            if rsp == QtWidgets.QDialog.Accepted:
                name = ui.txtad.text()
                surname = ui.txtsoyad.text()
                plate = ui.txtplk.text()

                sql = "update newcar set `name`=%s, `surname`=%s, `plate`=%s where `id`=%s"
                val = (name, surname, plate, id)
                mcursor.execute(sql, val)

                try:
                    mdb.commit()
                except mysql.connector.Error as err:
                    print("hata: ", err)
                finally:
                    mdb.close()
            if self.selected_date == '':
                self.allEntries()
            else:
                self.loadData()

                
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('GTK+'))
    win = myapp()
    win.show()
    sys.exit(app.exec_())
