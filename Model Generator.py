from PyQt5.QtGui import QPixmap, QDrag, QStandardItemModel, QStandardItem, QFont, QIcon, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox, QWidget, QLabel, \
	QTabWidget, QListView, QListWidget, QLineEdit, QListWidgetItem, QAbstractItemView, QTableWidget,QTableWidgetItem, QHeaderView, QComboBox
from PyQt5.QtCore import QDir, QCoreApplication, Qt, QMimeData, QSize, QModelIndex
from MainForm import Ui_MainWindow
import sys
import Layers
import os

TempTarget = []

class TrackableWidgetItem(QLineEdit):
	PropertyFont = QFont('arial')
	PropertyFont.setPointSize(10)

	def __init__(self, Name, Data, ins=None):
		super(TrackableWidgetItem, self).__init__(ins)
		self.setFont(self.PropertyFont)
		self.setText('nA')
		self.textChanged.connect(self.Changed)
		self.Name = Name
		self.Data = Data

	def Changed(self):
		global TempTarget
		if self.Data.attributes[self.Name] == 'INT':
			if not self.text().isnumeric():
				A = QMessageBox.warning(self, 'Warning', 'Int only')
				self.setText('0')
				return
			else:
				self.Data.attributes[self.Name + '_value'] = self.text()
				TempTarget = self.Data
				ChangeUpdate(ui.tabWidget.currentWidget().focusWidget())
		if self.Data.attributes[self.Name] == 'INT1':
			print(self.text())
			if self.text().isnumeric():
				if int(self.text()) >= 100 or int(self.text()) < 1:
					A = QMessageBox.warning(self, 'Warning', 'Int between 0 - 100')
					self.setText('80')
					return
				else:
					self.Data.attributes[self.Name + '_value'] = self.text()
					TempTarget = self.Data
					ChangeUpdate(ui.tabWidget.currentWidget().focusWidget())
			else:
				A = QMessageBox.warning(self, 'Warning', 'Int between 0 - 100')
				self.setText('80')
				return
		if self.Data.attributes[self.Name] == 'NAME':
			self.Data.attributes[self.Name + '_value'] = self.text()
			TempTarget = self.Data
			ChangeUpdate(ui.tabWidget.currentWidget().focusWidget())


		print(self.Data.attributes[self.Name])
		# Item Changed


class NewComboBox(QComboBox):
	PropertyFont = QFont('arial')
	PropertyFont.setPointSize(10)

	def __init__(self, target, each, IndexCounter):
		super(NewComboBox, self).__init__(parent=None)
		targetValue = each + '_value'
		self.addItems(target.attributes[each])
		self.setCurrentIndex(target.attributes[targetValue])
		self.setFont(self.PropertyFont)
		self.data = target
		self.targetValue = targetValue
		self.currentIndexChanged.connect(self.Update)
		self.IndexCounter = IndexCounter

	def Update(self):
		print('pressssss')
		self.data.attributes[self.targetValue] = self.currentIndex()
		global TempTarget
		TempTarget = self.data
		ChangeUpdate(ui.tabWidget.currentWidget().focusWidget())

	def wheelEvent(self, QWheelEvent):
		if self.hasFocus():
			QComboBox.wheelEvent(QWheelEvent)


class NewListWidget(QListWidget):
	item_list = []

	Factory = Layers.LayerFactory()
	PropertyFont = QFont('arial')
	PropertyFont.setPointSize(10)

	def __init__(self, parent=None):
		super(NewListWidget, self).__init__(parent)
		self.setAcceptDrops(True)
		self.setDragDropMode(2)
		print(11)

	def AddNewItem(self, Type):
		index = len(self.item_list)
		self.item_list.append(self.Factory.make(Type, index))

	def dropEvent(self, event):
		if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
			data = event.mimeData()
			source_item = QStandardItemModel()
			source_item.dropMimeData(data, Qt.CopyAction, 0, 0, QModelIndex())
			Instruction = source_item.item(0, 0).text()
			if event.source() != self:
				event.setDropAction(Qt.CopyAction)
				TempItem = QListWidgetItem()
				TempItem.setText(Instruction)
				TempItem.setTextAlignment(Qt.AlignCenter)
				# TempItem.setData()
				self.addItem(TempItem)
				self.AddNewItem(Instruction)
			else:
				event.setDropAction(Qt.MoveAction)
				PrevIndex = self.selectedIndexes()[0].row()
				super(NewListWidget, self).dropEvent(event)
				CurrentIndex = self.selectedIndexes()[0].row()
				self.ItemSwap(PrevIndex, CurrentIndex)
				self.UpdateIndex()
		else:
			event.ignore()

	def ItemSwap(self, Prev, Current):
		traget = self.item_list.pop(Prev)
		self.item_list.insert(Current, traget)

	def UpdateIndex(self):
		for i in range(len(self.item_list)):
			self.item_list[i].attributes['index'] = i

	def mousePressEvent(self, QMouseEvent):
		super().mousePressEvent(QMouseEvent)
		print('pressed')
		current = self.selectedIndexes()[0].row()
		self.ManageProperty(current)

	def ManageProperty(self, index):
		ui.tableWidget.setRowCount(0)

		ui.tableWidget.setFont(self.PropertyFont)
		ui.tableWidget.horizontalHeader().setDefaultSectionSize(120)
		ui.tableWidget.setColumnCount(2)
		ui.tableWidget.setHorizontalHeaderLabels(['Name', 'Value'])
		SkipList = ['type']
		target = self.item_list[index]
		RowCounter = 0
		IndexCounter = 0
		for each in target.attributes:
			if each in SkipList or each[-6:] == '_value':
				IndexCounter += 1
				continue
			if each == 'index':
				target.attributes['index'] = self.currentIndex().row()
				tempItem = QTableWidgetItem('index')
				tempItem.setTextAlignment(Qt.AlignCenter)
				tempItem.setFont(self.PropertyFont)
				tempItem.setFlags(Qt.ItemIsEnabled)
				tempItem.setBackground(Qt.gray)
				ui.tableWidget.insertRow(RowCounter)
				ui.tableWidget.setItem(RowCounter, 0 , tempItem)
				tempItem = QTableWidgetItem(str(self.currentIndex().row() + 1))
				# tempItem.setTextAlignment(Qt.AlignCenter)
				tempItem.setFont(self.PropertyFont)
				tempItem.setFlags(Qt.ItemIsEnabled)
				tempItem.setBackground(Qt.gray)
				ui.tableWidget.setItem(RowCounter, 1 , tempItem)
				RowCounter += 1
				continue
			if target.attributes[each] == 'NA':
				continue
			NameItem = QTableWidgetItem(each)
			NameItem.setTextAlignment(Qt.AlignCenter)
			NameItem.setFont(self.PropertyFont)
			NameItem.setFlags(Qt.ItemIsEnabled)
			NameItem.setBackground(Qt.gray)
			ui.tableWidget.insertRow(RowCounter)
			ui.tableWidget.setItem(RowCounter, 0, NameItem)
			if type(target.attributes[each]) == type([]):
				comboBox = NewComboBox(target, each, IndexCounter)
				comboBox.setFocusPolicy(Qt.StrongFocus)
				ui.tableWidget.setCellWidget(RowCounter, 1, comboBox)
				# comboBox.currentIndexChanged.connect(lambda: self.ChangeUpdate(RowCounter, targetValue))
			else:
				changeableWidget = TrackableWidgetItem(each, target)
				changeableWidget.setText(str(target.attributes[each+'_value']))
				ui.tableWidget.setCellWidget(RowCounter, 1, changeableWidget)

				pass
			RowCounter += 1
			IndexCounter += 1

	def focusWidget(self):
		print(self)

def ChangeUpdate(self):
	print('changed')
	global  TempTarget
	Index = TempTarget.attributes['index']
	self.item_list[Index] = TempTarget








class MainForm(Ui_MainWindow):
	TabList = []
	TabListO = []
	ListWidgetO = []
	ItemFont = QFont('arial')
	ItemFont.setPointSize(20)


	# Form init
	def __init__(self, MainWindow):
		super(MainForm, self).setupUi(MainWindow)
		self.SetTreeWedgit()
		self.SetTabWidegt()
		self.SetListLayer()
		self.pushButton_2.clicked.connect(self.GenerateModel)




	def SetTreeWedgit(self):
		Model =  QFileSystemModel()
		Model.setRootPath(QDir.currentPath())
		self.treeView.setModel(Model)
		self.treeView.setRootIndex(Model.index(QDir.currentPath()))
		self.treeView.setAnimated(False)
		self.treeView.setIndentation(20)
		self.treeView.setSortingEnabled(False)
		self.treeView.hideColumn(1)
		self.treeView.hideColumn(2)
		self.treeView.hideColumn(3)
		self.treeView.doubleClicked.connect(self.TreeViewDoubleClicked)


# get the full path of the double clicked item
	def TreeViewDoubleClicked(self):
		item = self.treeView.selectedIndexes()
		if item:
			item = item[0]
		TreeList = []
		while item.parent().data():
			TreeList.append(item.data())
			item = item.parent()
		BasePath = ''
		TreeList.reverse()
		for element in TreeList:
			BasePath += '/'
			BasePath += element
		_translate = QCoreApplication.translate
		self.AddTab(BasePath, TreeList[len(TreeList)-1])
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget), _translate("MainWindow", TreeList[len(TreeList)-1]))

	def tabWidgetDoubleClicked(self):
		CurrentIndex = self.tabWidget.currentIndex()
		self.tabWidget.removeTab(CurrentIndex)
		self.TabList.pop(CurrentIndex)
		self.TabListO.pop(CurrentIndex)


# check input file type
	def AddTab(self, FilePath, FileName):
		if FileName[-3:] != '.py':
			QMessageBox.warning(self.treeView, 'Warning', 'Cannot open file:\n Wrong extension')
		elif FileName in self.TabList:
			QMessageBox.warning(self.treeView, 'Warning', 'Cannot open file:\n Instance existed')
		else:
			self.LoadFile(FilePath, FileName)

# load new tab
	def LoadFile(self, FilePath, FileName):

		temp = QWidget()
		temp.setAcceptDrops(False)
		self.tabWidget.addTab(temp, FileName)
		self.TabList.append(FileName)
		self.TabListO.append(temp)
		# add widget
		ScrollAreaName = FileName + '_SA'
		ListViewName = FileName + '_LV'
		Index = self.TabList.index(FileName)
		# target item
		self.tabWidget.widget(Index)

		# add scroll area to new tab
		print(temp)
		TempListWidget = NewListWidget(temp)
		# TempScrollArea.setWidgetResizable(True)
		TempListWidget.setMinimumSize(QSize(481, 654))
		TempListWidget.setMaximumSize(QSize(481, 654))
		# TempListView.setGeometry(0,0,200,100)
		TempListWidget.setObjectName(ScrollAreaName)
		TempListWidget.setAutoFillBackground(True)
		self.ListWidgetO.append(TempListWidget)
		TempListWidget.setAcceptDrops(True)
		TempListWidget.setDragDropMode(2)
		TempListWidget.setDefaultDropAction(0)
		TempListWidget.itemDoubleClicked.connect(self.RemoveItem)
		TempListWidget.setFont(self.ItemFont)
		TempListWidget.setItemAlignment(Qt.AlignHCenter)
		print(TempListWidget.acceptDrops())

	def RemoveItem(self, item):
		reply = QMessageBox.question(self.treeView, "Confirmation", "Do you really want to delete this layer?", QMessageBox.Yes | QMessageBox.No)
		if reply == 16384:
			parent = item.listWidget()
			index = parent.row(item)
			parent.takeItem(parent.row(item))
			parent.item_list.pop(index)

	def SetTabWidegt(self):
		self.tabWidget.tabBarDoubleClicked.connect(self.tabWidgetDoubleClicked)

		# # Ready Page
		# ##################################
		# FileName = 'New Model'
		# temp = QWidget()
		# temp.setAcceptDrops(True)
		# self.tabWidget.addTab(temp, FileName)
		# self.TabList.append(FileName)
		# self.TabListO.append(temp)
		# # add widget
		# ScrollAreaName = FileName + '_SA'
		# ListViewName = FileName + '_LV'
		# Index = self.TabList.index(FileName)
		# # target item
		# self.tabWidget.widget(Index)
		#
		# # add scroll area to new tab
		# print(temp)
		# TempScrollArea = QLabel(temp)
		# # TempScrollArea.setWidgetResizable(True)
		# TempScrollArea.setMinimumSize(QSize(200, 50))
		# TempScrollArea.setMaximumSize(QSize(200, 50))
		# TempScrollArea.setGeometry(150, 300, 0, 0)
		# TempScrollArea.setAutoFillBackground(True)
		# TempScrollArea.setAlignment(Qt.AlignCenter)
		# TempScrollArea.setObjectName(ScrollAreaName)
		# TempScrollArea.setAutoFillBackground(True)
		# TempScrollArea.setText('Ready')
		# ####################################
		FileName = 'New Model'

		temp = QWidget()
		temp.setAcceptDrops(False)
		self.tabWidget.addTab(temp, FileName)
		self.TabList.append(FileName)
		self.TabListO.append(temp)
		# add widget
		ScrollAreaName = FileName + '_SA'
		ListViewName = FileName + '_LV'
		Index = self.TabList.index(FileName)
		# target item
		self.tabWidget.widget(Index)

		# add scroll area to new tab
		print(temp)
		TempListWidget = NewListWidget(temp)
		# TempScrollArea.setWidgetResizable(True)
		TempListWidget.setMinimumSize(QSize(481, 654))
		TempListWidget.setMaximumSize(QSize(481, 654))
		# TempListView.setGeometry(0,0,200,100)
		TempListWidget.setObjectName(ScrollAreaName)
		TempListWidget.setAutoFillBackground(True)
		self.ListWidgetO.append(TempListWidget)
		TempListWidget.setAcceptDrops(True)
		TempListWidget.setDragDropMode(3)
		TempListWidget.setDefaultDropAction(0)
		TempListWidget.itemDoubleClicked.connect(self.RemoveItem)
		TempListWidget.setFont(self.ItemFont)
		# TempListWidget.setItemAlignment(Qt.AlignHCenter)

		print(TempListWidget.acceptDrops())

	def SetListLayer(self):
		# Layers = ['Input', 'Conv1D', 'Conv2D', 'Conv3D', 'LSTM', 'Dense', 'RNN','Optimizer', 'Softmax', 'Output']
		Layers = ['Input', 'Conv', 'Pooling', 'Dense', 'Flatten', 'Compile']
		for layer in Layers:
			temp = QListWidgetItem(layer)
			# temp.setIcon(QIcon('File/Image/' + layer + '.jpg'))
			temp.setFont(self.ItemFont)
			temp.setTextAlignment(Qt.AlignHCenter)
			self.listWidget.addItem(temp)
		self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.listWidget.setDragEnabled(True)


	def GenerateModel(self):
		try:
			targets = ui.tabWidget.currentWidget().focusWidget().item_list
		except:
			A = QMessageBox.warning(ui.tabWidget, 'Warning', 'Model not complete')
			return
		if not self.ModelCheck(targets):
			A = QMessageBox.warning(ui.tabWidget, 'Warning', 'Model Invalid')
			return
		FileName = targets[0].attributes['model_name_value']
		if not self.ModelNameCheck(FileName):
			return
		self.GenKerasTF2(targets, FileName)


	def GenKerasTF2(self, targets, FileName):
		File = open(FileName, 'w')
		File.write('# This script is generated by AMLGM2, support TF2.0 only\n')
		File.write('import tensorflow as tf\n')
		File.write('from tensorflow.keras import layers, models\n')
		File.write('import numpy as np\n')
		File.write('# Model starts here\n')
		File.write('model = models.Sequential()\n')
		Generator = Layers.InstructionFactory()
		for index in range(1, len(targets)):
			temp = targets[index]
			statement = Generator.GenerateInstruction(temp, targets[0])
			File.write(statement)



		File.close()



	def ModelNameCheck(self, FileName):
		if FileName in os.listdir():
			A = QMessageBox.warning(ui.tabWidget, 'Warning', 'File Existed, override?', QMessageBox.Yes | QMessageBox.No)
			if A == 16384:
				os.remove(FileName)
				return True
			else:
				return False
		return True





	def ModelCheck(self, targets):
		dangerlist = ['INPUT', 'COMPILE']
		if len(targets) < 2:
			return False
		if targets[0].attributes['type'] != 'INPUT':
			return False
		if targets[len(targets)-1].attributes['type'] != 'COMPILE':
			return False
		for i in range(1, len(targets)-1):
			if targets[i].attributes['type'] in dangerlist:
				return False
		return True







if __name__ == "__main__":
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = MainForm(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
