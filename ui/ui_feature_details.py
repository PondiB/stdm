# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_feature_details.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DetailsDock(object):
    def setupUi(self, DetailsDock):
        DetailsDock.setObjectName(_fromUtf8("DetailsDock"))
        DetailsDock.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.edit_btn = QtGui.QToolButton(self.dockWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)
        self.edit_btn.setIconSize(QtCore.QSize(16, 16))
        self.edit_btn.setObjectName(_fromUtf8("edit_btn"))
        self.horizontalLayout.addWidget(self.edit_btn)
        self.delete_btn = QtGui.QToolButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setIconSize(QtCore.QSize(16, 16))
        self.delete_btn.setObjectName(_fromUtf8("delete_btn"))
        self.horizontalLayout.addWidget(self.delete_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tree_scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.tree_scrollArea.setMinimumSize(QtCore.QSize(70, 70))
        self.tree_scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.tree_scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.tree_scrollArea.setLineWidth(0)
        self.tree_scrollArea.setWidgetResizable(True)
        self.tree_scrollArea.setObjectName(_fromUtf8("tree_scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 221))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tree_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.tree_scrollArea)
        DetailsDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(DetailsDock)
        QtCore.QMetaObject.connectSlotsByName(DetailsDock)

    def retranslateUi(self, DetailsDock):
        DetailsDock.setWindowTitle(_translate("DetailsDock", "Feature Details", None))
        self.edit_btn.setText(_translate("DetailsDock", "...", None))
        self.delete_btn.setText(_translate("DetailsDock", "...", None))

from stdm import resources_rc
