import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngine import QtWebEngine
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        
        
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        webcog_btn = QAction('Webcog', self)
        webcog_btn.triggered.connect(self.navigate_webcog)
        navbar.addAction(webcog_btn)
        
        self.url_bar = QLineEdit() #address bar
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)
        
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    
    def navigate_webcog(self):
        self.browser.setUrl(QUrl('http://youtube.com/@webcog'))
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    def update_url(self,q):
        self.url_bar.setText(q.toString())
        
        
        

app = QApplication(sys.argv)
QApplication.setApplicationName('Browser | Webcog')
window = MainWindow()
app.exec_()