#Equipo: RoboInges

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl

import contextily as cx
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
from cartopy import crs as ccrs
from geodatasets import get_path

import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setCursorPosition(5)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 140, 400, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(275, 250, 50, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 270, 180, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 80, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Downloads/firms.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 410, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 370, 42, 22))
        self.spinBox.setRange(1, 31)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(280, 370, 42, 22))
        self.spinBox_2.setRange(1, 12)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(380, 370, 50, 22))
        self.spinBox_3.setRange(2000, 2023)
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(255, 170, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(215, 210, 170, 30))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 340, 40, 20))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 340, 40, 20))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 340, 40, 20))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 480, 100, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "FIRMS"))
        self.lineEdit_2.setText(_translate("MainWindow", "(Fire Information for Resource Management System)"))
        self.lineEdit_3.setText(_translate("MainWindow", "Country"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select a country"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Aruba"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Afganistan"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Burundi"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Belgium"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Canada"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Chile"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Dominica"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Denmark"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Monaco"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Moldova"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Mexico"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.pushButton_2.setText(_translate("MainWindow", "Visit the website"))
        self.lineEdit_4.setText(_translate("MainWindow", "or search for information locally"))
        self.lineEdit_5.setText(_translate("MainWindow", "Day"))
        self.lineEdit_6.setText(_translate("MainWindow", "Month"))
        self.lineEdit_7.setText(_translate("MainWindow", "Year"))
        self.pushButton_3.setText(_translate("MainWindow", "Send information"))

        #Boton ok
        self.pushButton.clicked.connect(self.datos)
        self.pushButton_2.clicked.connect(self.pagina)

    def pagina(self):
        url = 'https://firms.modaps.eosdis.nasa.gov/map/#d:today;@0.0,0.0,3.0z'
        webbrowser.open(url)

    def datos(self):
        year = self.spinBox_3.text()
        month = self.spinBox_2.text()
        day = self.spinBox.text()

        mx = [-150, 10, -30, 35]
        can = [-150, 40, -49, 79]

        text = self.comboBox.currentText()

        if (text == "Mexico"):
            rangeCountry = mx
            docName = text + ".csv"
        elif (text == "Canada"):
            rangeCountry = can
            docName = text + ".csv"


        # set our fire data
        df = pd.read_csv(docName)
        df_canada = df.copy()
        df_canada['acq_datetime'] = pd.to_datetime((year + str(month).zfill(2) + str(day).zfill(2) + ' ' + df_canada[df_canada['acq_date'] == year + '-' + str(day).zfill(2) + '-' + str(month).zfill(2)]['acq_time'].astype(str).str.zfill(4)), format='%Y%m%d %H%M')
        gdf = geopandas.GeoDataFrame(
            df_canada, geometry=geopandas.points_from_xy(df_canada.longitude, df_canada.latitude), crs="EPSG:4326"
        )
        dt_max = gdf['acq_datetime'].max()
        gdf1 = gdf[gdf['acq_datetime'] >= (dt_max - pd.Timedelta(hours=1))]
        gdf2 = gdf[(gdf['acq_datetime'] >= (dt_max - pd.Timedelta(hours=4))) & (gdf['acq_datetime'] < (dt_max - pd.Timedelta(hours=1)))]
        gdf3 = gdf[(gdf['acq_datetime'] >= (dt_max - pd.Timedelta(hours=12))) & (gdf['acq_datetime'] < (dt_max - pd.Timedelta(hours=4)))]
        gdf4 = gdf[gdf['acq_datetime'] < (dt_max - pd.Timedelta(hours=12))]

        # set out plot

        world = geopandas.read_file(get_path("naturalearth.land"))
        ax = world.plot(figsize=(10, 10), alpha=0)

        ax.set_xlim([rangeCountry[0],  rangeCountry[2]])
        ax.set_ylim([rangeCountry[1],  rangeCountry[3]])

        months = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}

        ax.set(title='Time Since Detection\nCanada wildfires ' + months[str(month)] + ' ' + day + ', ' + year)
        ax.set_axis_off()

        if gdf4.count()[0] > 0 :
            gdf4.plot(ax=ax, color="yellow", markersize=1)
        if gdf3.count()[0] > 0 :
            gdf3.plot(ax=ax, color="orange", markersize=1)
        if gdf2.count()[0] > 0 :
            gdf2.plot(ax=ax, color="red", markersize=1)
        if gdf1.count()[0] > 0 :
            gdf1.plot(ax=ax, color="darkred", markersize=1)

        cx.add_basemap(ax, crs=gdf1.crs)

        plt.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())