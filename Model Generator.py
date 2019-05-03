from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox, QWidget, QLabel, QTabWidget, QListView
from PyQt5.QtCore import QDir, QCoreApplication, Qt, QMimeData, QSize
from MainForm import Ui_MainWindow
import sys


class DropArea(QTabWidget):
	# def __init__(self):
	# 	super(self).__init__()

	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.LeftButton:
			return

		mimeData = QMimeData()

		drag = QDrag(self)
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.pos() - self.rect().topLeft())
		drag.exec_(Qt.CopyAction)


	# def mousePressEvent(self, e):
	#
	# 	super().mousePressEvent(e)
	#
	# 	if e.button() == Qt.LeftButton:
	# 		print('press')


	def dragEnterEvent(self, e):
		e.accept()


	def dropEvent(self, e):
		# position = e.pos()
		# self.move(position)
		# We specify the type of the drop action with setDropAction().
		# In our case it is a move action.
		e.setDropAction(Qt.CopyAction)
		e.accept()


class DraggableLabel(QLabel):
	def __init__(self, title):
		super().__init__(title)

	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.LeftButton:
			return

		mimeData = QMimeData()

		drag = QDrag(self)
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.pos() - self.rect().topLeft())
		drag.exec_(Qt.CopyAction)


	# def mousePressEvent(self, e):
	#
	# 	super().mousePressEvent(e)
	#
	# 	if e.button() == Qt.LeftButton:
	# 		print('press')


	def dragEnterEvent(self, e):
		e.accept()


	def dropEvent(self, e):
		position = e.pos()
		# self.move(position)
		# We specify the type of the drop action with setDropAction().
		# In our case it is a move action.
		e.setDropAction(Qt.CopyAction)
		e.accept()


class MainForm(Ui_MainWindow):
	TabList = []
	TabListO = []
	ScrollArea = []

	# Form init
	def __init__(self, MainWindow):
		super(MainForm, self).setupUi(MainWindow)

		# self.tabWidget.mouseMoveEvent = DropArea.mouseMoveEvent
		# self.tabWidget.dragEnterEvent = DropArea.dragEnterEvent
		# self.tabWidget.dropEvent = DropArea.dropEvent
		# self.tabWidget = DropArea(self.tabWidget)

		self.SetTreeWedgit()
		self.SetLayerBackground()
		self.SetTabWidegt()

		self.NNLayer1 = DraggableLabel(QLabel(self.scrollAreaWidgetContents_4))
		self.NNLayer1.setMinimumSize(QSize(200, 50))
		self.NNLayer1.setMaximumSize(QSize(200, 50))
		self.NNLayer1.setAutoFillBackground(True)
		self.NNLayer1.setAlignment(Qt.AlignCenter)
		self.NNLayer1.setObjectName("NNLayer1")
		self.verticalLayout_2.addWidget(self.NNLayer1)
		self.NNLayer1.setAcceptDrops(True)
		self.scrollAreaWidgetContents_4.setAcceptDrops(True)
		self.scrollArea_2.setAcceptDrops(True)
		self.groupBox_4.setAcceptDrops(True)
		self.groupBox_3.setAcceptDrops(True)
		self.centralWidget.setAcceptDrops(True)
		self.tabWidget.setAcceptDrops(True)
		self.NNLayer1.setPixmap(QPixmap('File/Image/Optimizer.jpg'))






	# init
	def SetTreeWedgit(self):
		# treeview init
		Model = QFileSystemModel()
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


	def SetLayerBackground(self):
		# Layer Background
		ImgCNN = QPixmap('File/Image/CNN.jpg')
		if ImgCNN.isNull():
			raise FileNotFoundError
		ImgNN = QPixmap('File/Image/NN.jpg')
		if ImgNN.isNull():
			raise FileNotFoundError
		ImgRNN = QPixmap('File/Image/RNN.jpg')
		if ImgRNN.isNull():
			raise FileNotFoundError
		ImgLSTM = QPixmap('File/Image/LSTM.jpg')
		if ImgLSTM.isNull():
			raise FileNotFoundError
		ImgInput = QPixmap('File/Image/Input.jpg')
		if ImgInput.isNull():
			raise FileNotFoundError
		ImgOutput = QPixmap('File/Image/Output.jpg')
		if ImgOutput.isNull():
			raise FileNotFoundError
		ImgOptimizer = QPixmap('File/Image/Optimizer.jpg')
		if ImgOptimizer.isNull():
			raise FileNotFoundError
		ImgSoftmax = QPixmap('File/Image/Softmax.jpg')
		if ImgSoftmax.isNull():
			raise FileNotFoundError
		self.InputLayer.setPixmap(ImgInput)
		self.CNNLayer.setPixmap(ImgCNN)
		self.NNLayer.setPixmap(ImgNN)
		self.RNNLayer.setPixmap(ImgRNN)
		self.LSTMLayer.setPixmap(ImgLSTM)
		self.Optimizer.setPixmap(ImgOptimizer)
		self.OutputLayer.setPixmap(ImgOutput)
		self.SoftmaxLayer.setPixmap(ImgSoftmax)

	# tab double click binding
	def tabWidgetDoubleClicked(self):
		CurrentIndex = self.tabWidget.currentIndex()
		self.tabWidget.removeTab(CurrentIndex)
		self.TabList.pop(CurrentIndex)
		self.TabListO.pop(CurrentIndex)



	# set tab widget
	def SetTabWidegt(self):

		self.tabWidget.removeTab(0)
		self.tabWidget.tabBarDoubleClicked.connect(self.tabWidgetDoubleClicked)

		# Ready Page
		##################################
		FileName = 'New Model'
		temp = QWidget()
		temp.setAcceptDrops(True)
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
		TempScrollArea = QLabel(temp)
		# TempScrollArea.setWidgetResizable(True)
		TempScrollArea.setMinimumSize(QSize(200, 50))
		TempScrollArea.setMaximumSize(QSize(200, 50))
		TempScrollArea.setGeometry(150,300,0,0)
		TempScrollArea.setAutoFillBackground(True)
		TempScrollArea.setAlignment(Qt.AlignCenter)
		TempScrollArea.setObjectName(ScrollAreaName)
		TempScrollArea.setAutoFillBackground(True)
		TempScrollArea.setText('Ready')
		####################################






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
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", TreeList[len(TreeList)-1]))

	# check extension
	def CheckType(self, FileName):
		return FileName[-3:] == '.py'

	# add tab
	def AddTab(self, BasePath, FileName):
		# if name existed in Tablist skip
		if not self.CheckType(FileName):
			QMessageBox.warning(self.CNNLayer, "Warning", "Cannot open File:\n Wrong extension")
		elif FileName in self.TabList:
			QMessageBox.warning(self.CNNLayer, "Warning", "Cannot open File:\n Instance existed")
		else:
			self.LoadFile(BasePath, FileName)

	# load file
	def LoadFile(self, FilePath, FileName):
		# add new tab
		temp = QWidget()
		temp.setAcceptDrops(True)
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
		TempListView = QListView(temp)
		# TempScrollArea.setWidgetResizable(True)
		TempListView.setMinimumSize(QSize(471, 633))
		TempListView.setMaximumSize(QSize(471, 633))
		# TempListView.setGeometry(0,0,200,100)
		TempListView.setObjectName(ScrollAreaName)
		TempListView.setAutoFillBackground(True)
		self.TabListO.append(TempListView)


		# add list view to scroll area







if __name__ == "__main__":
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = MainForm(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())