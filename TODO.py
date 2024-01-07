from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    task_list = []
    def add_task(self):
        complete_task = ""
        if self.CompleteradioButton.isChecked():
            complete_task = "Complete"
        else:
            complete_task = "Incomplete"
        task = (self.task_name_entry.text(), complete_task)
        self.task_list.append(task)
        self.task_name_entry.clear()
        self.CompleteradioButton.clearFocus()
        self.IncompleteradioButton.clearFocus()
    def delete_task(self, task_num):
        task_num_int = int(task_num)
        self.task_list[task_num_int - 1] = task_num_int
        self.task_list.remove(task_num_int)
        self.delete_task_entry.clear()
    def display_list(self):
        task_number = 1
        for task in self.task_list:
            task_name = task[0]
            task_status = task[1]
            self.textBrowser.append(f"{task_number} | {task_name} | {task_status}")
            task_number += 1
    def menu_clear(self):
        self.textBrowser.clear()
    def reset(self):
        self.task_name_entry.clear()
        self.delete_task_entry.clear()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 689)
        MainWindow.setMaximumSize(QtCore.QSize(412, 694))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 39, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 32, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 17, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 140, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 39, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 32, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 17, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 140, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 39, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 32, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 17, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 13, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 26, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Python\My Beginner Python\TODO\TODO-App\Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(139, 136, 136);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 98, 77))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\Python\My Beginner Python\TODO\TODO-App\Image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.task_name_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.task_name_entry.setGeometry(QtCore.QRect(140, 120, 161, 41))
        self.task_name_entry.setAutoFillBackground(False)
        self.task_name_entry.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
        self.task_name_entry.setObjectName("task_name_entry")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 176, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.CompleteradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CompleteradioButton.setGeometry(QtCore.QRect(160, 209, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CompleteradioButton.setFont(font)
        self.CompleteradioButton.setObjectName("CompleteradioButton")
        self.IncompleteradioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.IncompleteradioButton.setGeometry(QtCore.QRect(254, 209, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IncompleteradioButton.setFont(font)
        self.IncompleteradioButton.setObjectName("IncompleteradioButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 257, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.delete_task_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.delete_task_entry.setGeometry(QtCore.QRect(143, 278, 131, 41))
        self.delete_task_entry.setAutoFillBackground(False)
        self.delete_task_entry.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
        self.delete_task_entry.setInputMask("")
        self.delete_task_entry.setText("")
        self.delete_task_entry.setObjectName("delete_task_entry")
        self.save_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_task())
        self.save_button.setGeometry(QtCore.QRect(240, 364, 75, 23))
        self.save_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"")
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(True)
        self.save_button.setFlat(True)
        self.save_button.setObjectName("save_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.reset())
        self.reset_button.setGeometry(QtCore.QRect(320, 364, 75, 23))
        self.reset_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.reset_button.setDefault(True)
        self.reset_button.setFlat(True)
        self.reset_button.setObjectName("reset_button")
        self.delete_task_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_task(self.delete_task_entry.text()))
        self.delete_task_button.setGeometry(QtCore.QRect(284, 279, 53, 40))
        self.delete_task_button.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;")
        self.delete_task_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\Python\My Beginner Python\TODO\TODO-App\DeleteIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_task_button.setIcon(icon1)
        self.delete_task_button.setDefault(False)
        self.delete_task_button.setFlat(False)
        self.delete_task_button.setObjectName("delete_task_button")
        self.menu_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.display_list())
        self.menu_button.setGeometry(QtCore.QRect(131, 418, 75, 23))
        self.menu_button.setDefault(True)
        self.menu_button.setFlat(True)
        self.menu_button.setObjectName("menu_button")
        self.clear_menu_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.menu_clear())
        self.clear_menu_button.setGeometry(QtCore.QRect(211, 418, 75, 23))
        self.clear_menu_button.setDefault(True)
        self.clear_menu_button.setFlat(True)
        self.clear_menu_button.setObjectName("clear_menu_button")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-1, 440, 414, 251))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TODO App"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.task_name_entry.setPlaceholderText(_translate("MainWindow", "            Enter task Name"))
        self.label_3.setText(_translate("MainWindow", "Default"))
        self.CompleteradioButton.setText(_translate("MainWindow", "Complete"))
        self.IncompleteradioButton.setText(_translate("MainWindow", "Incomplete"))
        self.label_4.setText(_translate("MainWindow", "Delete"))
        self.delete_task_entry.setPlaceholderText(_translate("MainWindow", "      Enter task Number"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.menu_button.setText(_translate("MainWindow", "Menu"))
        self.clear_menu_button.setText(_translate("MainWindow", "Clear Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
