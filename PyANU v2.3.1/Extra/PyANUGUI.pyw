from PyQt5 import QtCore, QtGui, QtWidgets
from PyANU import *
from CSR import *

class Ui_MainWindow(object):

    def printLabel(self, text, label):
        label.setText(text)

    def setupUi(self, MainWindow):
        c = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.pushButton_1 = QtWidgets.QPushButton(self.tab_1)
        p = lambda: ROV.Power(float(self.lineEdit_1.text()),
                              float(self.lineEdit_2.text()),
                              float(self.lineEdit_3.text()),
                              float(self.lineEdit_4.text()),
                              float(self.lineEdit_5.text()))
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.pushButton_1.clicked.connect(p)
        self.pushButton_1.clicked.connect(lambda: self.printLabel("Power = " + str(ROV.Power(float(self.lineEdit_1.text()),
                              float(self.lineEdit_2.text()),
                              float(self.lineEdit_3.text()),
                              float(self.lineEdit_4.text()),
                              float(self.lineEdit_5.text()))) + " MW", self.label_6))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        v = lambda: ROV.Vertical(float(self.lineEdit_6.text()),
                                float(self.lineEdit_7.text()),
                                float(self.lineEdit_8.text()))
        self.pushButton_2.clicked.connect(v)
        self.pushButton_2.clicked.connect(lambda: self.printLabel("Vertical Distance = " + str(ROV.Vertical(float(self.lineEdit_6.text()),
                                float(self.lineEdit_7.text()),
                                float(self.lineEdit_8.text())) + " Metre(s)"), self.label_7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_4.addWidget(self.lineEdit_9)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.pushButton_3.clicked.connect(lambda: self.printLabel("Unknown Object at a Distance = " + str(ROV.Horizontal(float(self.lineEdit_9.text())))
                                                                  + " Centimeter(s)", self.label_12))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 316))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_5.addWidget(self.lineEdit_10)
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_5.addWidget(self.lineEdit_11)
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_5.addWidget(self.lineEdit_12)
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_5.addWidget(self.lineEdit_13)
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_5.addWidget(self.lineEdit_14)
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_5.addWidget(self.lineEdit_15)
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_5.addWidget(self.lineEdit_16)
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_5.addWidget(self.lineEdit_17)
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_5.addWidget(self.lineEdit_18)
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.clicked.connect(lambda: ROV.Crashmap(self.lineEdit_10.text(),
                                                            float(self.lineEdit_11.text()),
                                                            float(self.lineEdit_12.text()),
                                                            float(self.lineEdit_13.text()),
                                                            float(self.lineEdit_14.text()),
                                                            float(self.lineEdit_15.text()),
                                                            float(self.lineEdit_16.text()),
                                                            float(self.lineEdit_17.text()),
                                                            str(self.lineEdit_18.text())))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_5, "")

        #SEISMO
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 500, 721, 81))
        self.pushButton_4.clicked.connect(lambda: ROV.Seismo(float(self.lineEdit_19.text()),
                                                            float(self.lineEdit_20.text()),
                                                            float(self.lineEdit_21.text()),
                                                            float(self.lineEdit_22.text()),
                                                            float(self.lineEdit_23.text()),
                                                            float(self.lineEdit_24.text()),
                                                            float(self.lineEdit_25.text()),
                                                            float(self.lineEdit_26.text()),
                                                            float(self.lineEdit_27.text()),
                                                            float(self.lineEdit_28.text()),
                                                            float(self.lineEdit_29.text()),
                                                            float(self.lineEdit_30.text()),
                                                            float(self.lineEdit_31.text()),
                                                            float(self.lineEdit_32.text()),
                                                            float(self.lineEdit_33.text()),
                                                            float(self.lineEdit_34.text()),
                                                            float(self.lineEdit_35.text()),
                                                            float(self.lineEdit_36.text()),
                                                            float(self.lineEdit_37.text()),
                                                            float(self.lineEdit_38.text()),
                                                            float(self.lineEdit_39.text()),
                                                            float(self.lineEdit_40.text()),
                                                            float(self.lineEdit_41.text()),
                                                            float(self.lineEdit_42.text()),
                                                            float(self.lineEdit_43.text()),
                                                            float(self.lineEdit_44.text()),
                                                            float(self.lineEdit_45.text()),
                                                            float(self.lineEdit_46.text()),
                                                            float(self.lineEdit_47.text()),
                                                            float(self.lineEdit_48.text()),
                                                            float(self.lineEdit_49.text()),
                                                            float(self.lineEdit_50.text())))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 10, 361, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(380, 10, 351, 22))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 40, 361, 22))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(380, 40, 351, 22))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(10, 70, 361, 22))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(380, 70, 351, 22))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(10, 100, 361, 22))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(380, 100, 351, 22))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_27.setGeometry(QtCore.QRect(10, 130, 361, 22))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_28.setGeometry(QtCore.QRect(380, 130, 351, 22))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_29.setGeometry(QtCore.QRect(10, 160, 361, 22))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_30.setGeometry(QtCore.QRect(380, 160, 351, 22))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_31.setGeometry(QtCore.QRect(10, 190, 361, 22))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_32.setGeometry(QtCore.QRect(380, 190, 351, 22))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_33.setGeometry(QtCore.QRect(10, 220, 361, 22))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_34.setGeometry(QtCore.QRect(380, 220, 351, 22))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_35.setGeometry(QtCore.QRect(10, 250, 361, 22))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_36.setGeometry(QtCore.QRect(380, 250, 351, 22))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_37.setGeometry(QtCore.QRect(10, 280, 361, 22))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_38.setGeometry(QtCore.QRect(380, 280, 351, 22))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_39.setGeometry(QtCore.QRect(10, 310, 361, 22))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_40.setGeometry(QtCore.QRect(380, 310, 351, 22))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_41.setGeometry(QtCore.QRect(10, 340, 361, 22))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_42.setGeometry(QtCore.QRect(380, 340, 351, 22))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_43.setGeometry(QtCore.QRect(10, 370, 361, 22))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_44.setGeometry(QtCore.QRect(380, 370, 351, 22))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_45.setGeometry(QtCore.QRect(10, 400, 361, 22))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_46.setGeometry(QtCore.QRect(380, 400, 351, 22))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_47.setGeometry(QtCore.QRect(10, 430, 361, 22))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_48.setGeometry(QtCore.QRect(380, 430, 351, 22))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_49.setGeometry(QtCore.QRect(10, 460, 361, 22))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_50.setGeometry(QtCore.QRect(380, 460, 351, 22))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.tabWidget.addTab(self.tab_2, "")
        #SEISMO END
        
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_5.clicked.connect(lambda: CSR.RunCSR())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_9.addWidget(self.pushButton_5)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyANU v2.3.0"))
        self.label.setText(_translate("MainWindow", "No. of Turbines"))
        self.label_2.setText(_translate("MainWindow", "Density of the Water in kg/m^3"))
        self.label_3.setText(_translate("MainWindow", "Radius of a Turbine in Metres"))
        self.label_4.setText(_translate("MainWindow", "Tide Strength in Knots"))
        self.label_5.setText(_translate("MainWindow", "Efficiency of the Turbines in %"))
        self.pushButton_1.setText(_translate("MainWindow", "Calculate"))
        self.label_6.setText(_translate("MainWindow", "Power = MW"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Power"))
        self.label_8.setText(_translate("MainWindow", "Density of the Water in kg/m^3"))
        self.label_9.setText(_translate("MainWindow", "Pressure at the Bottom point in Pascal"))
        self.label_10.setText(_translate("MainWindow", "Pressure at the Top point in Pascal"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate"))
        self.label_7.setText(_translate("MainWindow", "Vertical Distance = Metre(s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Veritcal"))
        self.label_11.setText(_translate("MainWindow", "Known Object Width"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate and Graph"))
        self.label_12.setText(_translate("MainWindow", "Unknown Object at a Distance = Centimeter(s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Horizontal"))
        self.label_15.setText(_translate("MainWindow", "Take-off Point"))
        self.label_13.setText(_translate("MainWindow", "Heading Angle"))
        self.label_17.setText(_translate("MainWindow", "Velocity during Ascending in m/sec"))
        self.label_14.setText(_translate("MainWindow", "Rate of Climb (RoC) in m/sec"))
        self.label_16.setText(_translate("MainWindow", "Velocity during Descending in m/sec"))
        self.label_19.setText(_translate("MainWindow", "Rate of Decay (RoD) in m/sec"))
        self.label_18.setText(_translate("MainWindow", "Time of Engine Fail in sec"))
        self.label_20.setText(_translate("MainWindow", "Angle of Wind Movement"))
        self.label_21.setText(_translate("MainWindow", "Equation of Wind"))
        self.pushButton.setText(_translate("MainWindow", "Plot the Crashmap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Crashmap"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate and Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Seismo"))
        self.pushButton_5.setText(_translate("MainWindow", "Scan Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "CSR"))

        self.lineEdit_19.setText(_translate("MainWindow", "1"))
        self.lineEdit_21.setText(_translate("MainWindow", "2"))
        self.lineEdit_23.setText(_translate("MainWindow", "3"))
        self.lineEdit_25.setText(_translate("MainWindow", "4"))
        self.lineEdit_27.setText(_translate("MainWindow", "5"))
        self.lineEdit_29.setText(_translate("MainWindow", "6"))
        self.lineEdit_31.setText(_translate("MainWindow", "7"))
        self.lineEdit_33.setText(_translate("MainWindow", "8"))
        self.lineEdit_35.setText(_translate("MainWindow", "9"))
        self.lineEdit_37.setText(_translate("MainWindow", "10"))
        self.lineEdit_39.setText(_translate("MainWindow", "11"))
        self.lineEdit_41.setText(_translate("MainWindow", "12"))
        self.lineEdit_43.setText(_translate("MainWindow", "13"))
        self.lineEdit_45.setText(_translate("MainWindow", "14"))
        self.lineEdit_47.setText(_translate("MainWindow", "15"))
        self.lineEdit_49.setText(_translate("MainWindow", "16"))

if __name__ == "__main__":
    import sys
    ROV = PyANU()
    CSR = CSR()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())