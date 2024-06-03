from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo")
        self.setFixedSize(QSize(400,400))
        #main
        main_layout = QVBoxLayout()
        #input
        hbox = QHBoxLayout()
        #create data 
        try:
            open("data_todo.txt", "x")
        except:
            f = open("data_todo.txt","r")
        self.todo = [] #ALL Todo array
        
        
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        add_btn = QPushButton("add")
        add_btn.clicked.connect(self.add_todo)
        
        self.Todo_in = QLineEdit()
        hbox.addWidget(self.Todo_in)
        hbox.addWidget(add_btn)
        main_layout.addLayout(hbox)
        #all todo
        self.todo_list = QListWidget()
        main_layout.addWidget(self.todo_list)
        #load file data todo
        try:
            open("data_todo.txt", "x")
        except:
            f = open("data_todo.txt","r")
            self.todo = f.read().splitlines()
        ## set todo defined
        for i in self.todo:
            self.todo_list.addItem(i)
        #del
        dell = QHBoxLayout()
        
        clear_btn = QPushButton("clear")
        clear_btn.clicked.connect(self.remove_todo)
        
        clear_all_btu = QPushButton("clear all")
        clear_all_btu.clicked.connect(self.clearAll_todo)
        
        dell.addWidget(clear_btn)
        dell.addWidget(clear_all_btu)
        main_layout.addLayout(dell)
        #setlayout
        self.setLayout(main_layout)
        
    #/add todo to array
    def add_todo(self):
        text = self.Todo_in.text()
        self.todo.append(text)
        self.todo_list.addItem(text)
        self.Todo_in.clear()
    
    def remove_todo(self):
        selected_items = self.todo_list.selectedItems()
        for i in selected_items:
            self.todo.remove(i.text())
            self.todo_list.takeItem(self.todo_list.row(i))

    def clearAll_todo(self):
        self.todo_list.clear()
        self.todo = []
    
    def save_file(self):
        w = open("data_todo.txt" , "w")
        for i in self.todo:
            w.write(f'{i}\n')

app=QCoreApplication.instance()
if app is None:
    app=QApplication([])
window = MainWindow()
app.aboutToQuit.connect(window.save_file)
window.show()
app.exec()