import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore


class MyDialog(QtWidgets.QWidget):
    def __init__(self, title):
        super(MyDialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.first_name = QtWidgets.QLineEdit('First Name')
        self.first_name.setMaximumWidth(120)
        self.last_name = QtWidgets.QLineEdit('Last Name')
        self.last_name.setMaximumWidth(120)
        self.email = QtWidgets.QLineEdit('Email')
        self.email.setMaximumWidth(120)
        self.male_rad = QtWidgets.QRadioButton('Male')
        self.male_rad.setMaximumWidth(100)
        self.female_rad = QtWidgets.QRadioButton('Female')
        self.female_rad.setMaximumWidth(100)
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.cancel_button = QtWidgets.QPushButton('Cancel')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        hbox_1 = QtWidgets.QHBoxLayout()
        hbox_1.setAlignment(QtCore.Qt.AlignLeft)
        hbox_2 = QtWidgets.QHBoxLayout()
        hbox_2.setAlignment(QtCore.Qt.AlignLeft)
        hbox_3 = QtWidgets.QHBoxLayout()
        hbox_3.setAlignment(QtCore.Qt.AlignLeft)

        hbox_1.addWidget(self.first_name)
        hbox_1.addWidget(self.last_name)
        main_layout.addLayout(hbox_1)

        hbox_2.addWidget(self.email)
        hbox_2.addWidget(self.male_rad)
        hbox_2.addWidget(self.female_rad)
        main_layout.addLayout(hbox_2)

        hbox_3.addWidget(self.submit_button)
        hbox_3.addWidget(self.cancel_button)
        main_layout.addLayout(hbox_3)

        # connections
        self.submit_button.clicked.connect(self.submit)
        self.male_rad.clicked.connect(self.gendercheck)
        self.female_rad.clicked.connect(self.gendercheck)
        self.first_name.textChanged.connect(self.name)

    def submit(self):
        print("Submit Clicked!!")

    def gendercheck(self):
        if self.male_rad.isChecked():
            print("Male selected")
        elif self.female_rad.isChecked():
            print("Female selected")

    def name(self):
        print(self.first_name.text())


app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog('My Dialog')
dialog.show()
sys.exit(app.exec_())



# Datta's code
import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore

class My_Main_Dialog(QtWidgets.QWidget):
    def __init__(self,title):
        super(My_Main_Dialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.submit_button.setMaximumWidth(100)
        self.submit_button.setMaximumHeight(30)
        self.cancel_button = QtWidgets.QPushButton('Cancel')
        self.cancel_button.setMaximumWidth(100)
        self.cancel_button.setMaximumHeight(30)


    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignBottom)

        hbox_1 = QtWidgets.QHBoxLayout()
        hbox_1.addWidget(self.submit_button)
        hbox_1.addWidget(self.cancel_button)
        main_layout.addLayout(hbox_1)

        # Connections
        self.submit_button.clicked.connect(self.Submit_fun)

    def Submit_fun(self):
        sms_dialogue =  My_sms_Dialog()
        sms_dialogue.show()
        sys.exit(sms_dialogue.exec_())


'''Here is the second sms class declaration'''
class My_sms_Dialog(QtWidgets.QWidget):
    def __init__(self):
        super(My_sms_Dialog, self).__init__()
        #self.setWindowTitle(title)
        self.setMinimumWidth(500)
        self.setMaximumHeight(200)
        self.sms_create_widgets()
        self.sms_create_layout()


    def sms_create_widgets(self):
        self.sms_text = QtWidgets.QLabel("Hello, You have just pressed SUBMIT button")
        self.sms_submit_button = QtWidgets.QPushButton("OK")
        self.sms_submit_button.setMaximumWidth(100)
        self.sms_submit_button.setMaximumHeight(30)


    def sms_create_layout(self):
        sms_main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(sms_main_layout)
        sms_main_layout.setAlignment(QtCore.Qt.AlignCenter)

        sms_hbox_1 = QtWidgets.QHBoxLayout()
        sms_hbox_1.addWidget(self.sms_text)
        sms_main_layout.addLayout(sms_hbox_1)

        sms_hbox_2 = QtWidgets.QHBoxLayout()
        sms_hbox_2.addWidget(self.sms_submit_button)
        sms_main_layout.addLayout(sms_hbox_2)






app = QtWidgets.QApplication(sys.argv)
dialog = My_Main_Dialog('DATTA')
dialog.show()
sys.exit(app.exec_())

