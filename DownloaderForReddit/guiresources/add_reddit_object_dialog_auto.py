# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\add_reddit_object_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddRedditObjectDialog(object):
    def setupUi(self, AddRedditObjectDialog):
        AddRedditObjectDialog.setObjectName("AddRedditObjectDialog")
        AddRedditObjectDialog.resize(603, 328)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources\\ui_files\\../images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddRedditObjectDialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(10)
        AddRedditObjectDialog.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(AddRedditObjectDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab_widget = QtWidgets.QTabWidget(AddRedditObjectDialog)
        self.tab_widget.setAutoFillBackground(False)
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setObjectName("tab_widget")
        self.single_add_tab = QtWidgets.QWidget()
        self.single_add_tab.setObjectName("single_add_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.single_add_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.single_add_label = QtWidgets.QLabel(self.single_add_tab)
        self.single_add_label.setObjectName("single_add_label")
        self.verticalLayout.addWidget(self.single_add_label)
        self.single_object_line_edit = QtWidgets.QLineEdit(self.single_add_tab)
        self.single_object_line_edit.setObjectName("single_object_line_edit")
        self.verticalLayout.addWidget(self.single_object_line_edit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tab_widget.addTab(self.single_add_tab, "")
        self.multi_add_tab = QtWidgets.QWidget()
        self.multi_add_tab.setObjectName("multi_add_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.multi_add_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.multi_add_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.name_count_label = QtWidgets.QLabel(self.multi_add_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_count_label.sizePolicy().hasHeightForWidth())
        self.name_count_label.setSizePolicy(sizePolicy)
        self.name_count_label.setObjectName("name_count_label")
        self.horizontalLayout_3.addWidget(self.name_count_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.multi_object_list_widget = QtWidgets.QListWidget(self.multi_add_tab)
        self.multi_object_list_widget.setObjectName("multi_object_list_widget")
        self.verticalLayout_4.addWidget(self.multi_object_list_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.multi_object_line_edit = QtWidgets.QLineEdit(self.multi_add_tab)
        self.multi_object_line_edit.setObjectName("multi_object_line_edit")
        self.horizontalLayout_2.addWidget(self.multi_object_line_edit)
        self.add_button = QtWidgets.QToolButton(self.multi_add_tab)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_2.addWidget(self.add_button)
        self.remove_button = QtWidgets.QToolButton(self.multi_add_tab)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_2.addWidget(self.remove_button)
        self.import_button = QtWidgets.QPushButton(self.multi_add_tab)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_2.addWidget(self.import_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tab_widget.addTab(self.multi_add_tab, "")
        self.verticalLayout_3.addWidget(self.tab_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.download_on_add_checkbox = QtWidgets.QCheckBox(AddRedditObjectDialog)
        self.download_on_add_checkbox.setObjectName("download_on_add_checkbox")
        self.horizontalLayout.addWidget(self.download_on_add_checkbox)
        self.dialog_button_box = QtWidgets.QDialogButtonBox(AddRedditObjectDialog)
        self.dialog_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_button_box.setObjectName("dialog_button_box")
        self.horizontalLayout.addWidget(self.dialog_button_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(AddRedditObjectDialog)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddRedditObjectDialog)

    def retranslateUi(self, AddRedditObjectDialog):
        _translate = QtCore.QCoreApplication.translate
        AddRedditObjectDialog.setWindowTitle(_translate("AddRedditObjectDialog", "Add"))
        self.single_add_label.setText(_translate("AddRedditObjectDialog", "Enter new user:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.single_add_tab), _translate("AddRedditObjectDialog", "Single Add"))
        self.label_2.setText(_translate("AddRedditObjectDialog", "Names in list:"))
        self.name_count_label.setText(_translate("AddRedditObjectDialog", "0"))
        self.add_button.setText(_translate("AddRedditObjectDialog", "+"))
        self.remove_button.setText(_translate("AddRedditObjectDialog", "-"))
        self.import_button.setText(_translate("AddRedditObjectDialog", "Import"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.multi_add_tab), _translate("AddRedditObjectDialog", "Multi-Add"))
        self.download_on_add_checkbox.setText(_translate("AddRedditObjectDialog", "Download on add"))
