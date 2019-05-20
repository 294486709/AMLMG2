from PyQt5.QtGui import QPixmap, QDrag, QStandardItemModel, QStandardItem, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox, QWidget, QLabel, \
	QTabWidget, QListView, QListWidget, QListWidgetItem, QAbstractItemView, QTableWidget, QHeaderView
from PyQt5.QtCore import QDir, QCoreApplication, Qt, QMimeData, QSize, QModelIndex
from MainForm import Ui_MainWindow
import sys






class NewListWedgit(QListWidget):
	item_list = []
	pass
	def dropEvent(self, event):
		if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
			data = event.mimeData()
			source_item = QStandardItemModel()
			source_item.dropMimeData(data, Qt.CopyAction, 0, 0, QModelIndex())
			Instruction = source_item.item(0, 0).text()
		else:
			event.ignore()
		# if event.mimeData().hasFormat("text/plain"):
		# 	temp = QListWidgetItem()
		# e.accept()
		# print(e.mimeData().text())

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

	def SetListLayer(self):
		Layers = ['Input', 'CNN', 'LSTM', 'NN', 'RNN','Optimizer', 'Softmax', 'Output']
		for layer in Layers:
			temp = QListWidgetItem(layer)
			# temp.setIcon(QIcon('File/Image/' + layer + '.jpg'))
			temp.setFont(self.ItemFont)
			temp.setTextAlignment(Qt.AlignHCenter)
			self.LayerList.addItem(temp)
		self.LayerList.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.LayerList.setDragEnabled(True)

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
		TempListWidget = NewListWedgit(temp)
		# TempScrollArea.setWidgetResizable(True)
		TempListWidget.setMinimumSize(QSize(471, 633))
		TempListWidget.setMaximumSize(QSize(471, 633))
		# TempListView.setGeometry(0,0,200,100)
		TempListWidget.setObjectName(ScrollAreaName)
		TempListWidget.setAutoFillBackground(True)
		self.ListWidgetO.append(TempListWidget)
		TempListWidget.setAcceptDrops(True)
		TempListWidget.setDragDropMode(2)
		TempListWidget.setDefaultDropAction(0)
		TempListWidget.itemDoubleClicked.connect(self.RemoveItem)




		# TempListWidget.selectAll()

	# 	TempListWidget.removeItemWidget()
	#
	def RemoveItem(self, item):
		parent = item.listWidget()
		parent.takeItem(parent.row(item))



		# model = QStandardItemModel()
		# for i in range(100):
		# 	item = QStandardItem(str(i))
		# 	item.setTextAlignment(Qt.AlignHCenter)
		# 	model.appendRow(item)
		# TempListView.setModel(model)
		# TempListView.setFont(self.ItemFont)
		# TempListView.setEditTriggers(QListView.NoEditTriggers)
		# TempListView.dragEnterEvent = DropArea.dragEnterEvent
		# TempListView.mouseMoveEvent = DropArea.mouseMoveEvent
		# TempListView.dropEvent = DropArea.dropEvent
		# TempListView.setAcceptDrops(True)
		# TempListView.layout.setAlignment(Qt.AlignHCenter)
		# TempListView.setAlignment(Qt.AlignHCenter)


		# add list view to scroll area







if __name__ == "__main__":
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = MainForm(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
