import sys
import json
from enum import Enum
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Direction(Enum):
    UP = 1
    DOWN = 2


class Tasks:
    tasklist = []

    @staticmethod
    def load_tasks():
        Tasks.tasklist = json.load(open('list.json'))

    @staticmethod
    def save_tasks():
        json.dump(Tasks.tasklist, open('list.json', 'w'))

    @staticmethod
    def remove_task_item(parent, index):
        if parent is None:
            del Tasks.tasklist[index]
        else:
            parent_i = parent.index().row()
            del Tasks.tasklist[parent_i]['subtasks'][index]

        Tasks.save_tasks()

    # @staticmethod
    # def remove_subtask(parent_index, index):
    #     del Tasks.tasklist[parent_index]['subtasks'][index]

    @staticmethod
    def set(parent, index, prop_name, value):
        if parent is None:
            Tasks.tasklist[index][prop_name] = value
        else:
            parent_i = parent.index().row()
            Tasks.tasklist[parent_i]['subtasks'][index][prop_name] = value

        Tasks.save_tasks()

    @staticmethod
    def add_task(name):
        dict_ = {
            "name": name,
            "state": False,
            "subtasks": []
        }

        Tasks.tasklist.append(dict_)
        Tasks.save_tasks()

    @staticmethod
    def add_subtask(parent, name):
        dict_ = {
            "name": name,
            "state": False
        }

        Tasks.tasklist[parent.index().row()]['subtasks'].append(dict_)
        Tasks.save_tasks()

    @staticmethod
    def change_subtasks_state(task_item, state):
        index = task_item.index().row()
        for sub in Tasks.tasklist[index]['subtasks']:
            sub['state'] = state

        Tasks.save_tasks()

    @staticmethod
    def all_subtasks_checked(task_item):
        index = task_item.index().row()

        for sub in Tasks.tasklist[index]['subtasks']:
            if sub['state'] == False:
                return False

        return True


class MyWin(QtWidgets.QMainWindow):

    def msg(self, string):
        QtWidgets.QMessageBox.about(self, "Title", str(string))

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # A dictionary with all tasks
        Tasks.load_tasks()

        # TreeView
        self.twmodel = QtGui.QStandardItemModel()
        self.twmodel.itemChanged.connect(self.treeviewitem_changed)
        self.ui.treeView.setModel(self.twmodel)
        self.ui.treeView.selectionModel().selectionChanged.connect(self.treeview_selection_changed)
        self.tw_selected_item = None
        self.ui.treeView.setHeaderHidden(True)
        self.ui.treeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.import_tasks()
        self.ui.treeView.expandAll()

        # Remove button
        self.ui.RemoveButton.clicked.connect(self.remove_task)

        # Add button
        self.ui.AddButton.clicked.connect(self.add_task)

        # Add subtask button
        self.ui.AddSubButton.clicked.connect(self.add_subtask)

        # Move buttons
        self.ui.MoveUpButton.clicked.connect(lambda: self.move_treeviewitem(Direction.UP))
        self.ui.MoveDownButton.clicked.connect(lambda: self.move_treeviewitem(Direction.DOWN))

    def treeviewitem_changed(self, item):
        name = item.text()
        index = item.index().row()
        state = bool(item.checkState())
        parent = item.parent()

        Tasks.set(parent, index, 'name', name)
        Tasks.set(parent, index, 'state', state)

    def treeview_selection_changed(self, selection):
        self.tw_selected_item = self.twmodel.itemFromIndex(selection.indexes()[0])

    def import_tasks(self):
        #root = self.twmodel.invisibleRootItem()
        for i in Tasks.tasklist:
            item = QtGui.QStandardItem(i['name'])
            item.setCheckable(True)
            item.setCheckState(i['state'])
            self.twmodel.appendRow(item)
            for sub in i['subtasks']:
                subitem = QtGui.QStandardItem(sub['name'])
                subitem.setCheckable(True)
                subitem.setCheckState(sub['state'])
                item.appendRow(subitem)

    def remove_task(self, arg):
        if self.ui.treeView.selectedIndexes():
            selected_index = self.ui.treeView.selectedIndexes()[0]
            selected_item = selected_index.model().itemFromIndex(selected_index)
            parent = selected_item.parent()

            Tasks.remove_task_item(parent, selected_index.row())

            root = self.twmodel.invisibleRootItem()
            if parent is None:
                root.removeRow(selected_item.row())
            else:
                parent.removeRow(selected_item.row())

    def add_task(self):
        name = "New Task"
        new_item = QtGui.QStandardItem(name)
        new_item.setCheckable(True)
        self.twmodel.appendRow(new_item)

        Tasks.add_task(name)

    def add_subtask(self):                                          #FIXME: SELECTED ITEM
        if self.ui.treeView.selectedIndexes():
            selected_index = self.ui.treeView.selectedIndexes()[0]
            selected_item = selected_index.model().itemFromIndex(selected_index)
            selected_item_parent = selected_item.parent()

            name = "Subtask"
            new_item = QtGui.QStandardItem(name)
            new_item.setCheckable(True)

            if selected_item_parent is None:
                selected_item.appendRow(new_item)
                Tasks.add_subtask(selected_item, name)
            else:
                selected_item_parent.appendRow(new_item)
                Tasks.add_subtask(selected_item_parent, name)

    def move_treeviewitem(self, direction):
        item = self.tw_selected_item
        parent = item.parent()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
