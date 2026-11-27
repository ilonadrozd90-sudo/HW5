from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

class About(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setGeometry(400,400,600,150)
        self.setStyleSheet('font-family: "Lucida Sans Unicode"; font-size: 18px;')

        self.name = QLabel("Name: Ilona Drozd", self)
        self.name.setGeometry(180,20,300,30)

        self.email = QLabel("Email: IlonaDrozd@s.afeka.co.il", self)
        self.email.setGeometry(180,50,300,30)

        github_url = "https://github.com/ilonadrozd90-sudo/HW5"
        self.github = QLabel(f'<a href="{github_url}">GitHub Repository</a>', self)
        self.github.setGeometry(180,80,600,30)
        self.github.setOpenExternalLinks(True)

        image = QPixmap("picture.jpg")
        image = image.scaled(100,100)

        self.picture = QLabel(self)
    
        self.picture.setGeometry(40,20,100,100)
        self.picture.setPixmap(image)




if __name__ == '__main__':
    app = QApplication()
    window = About()
    window.show()
    app.exec()