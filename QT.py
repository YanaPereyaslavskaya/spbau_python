import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PIL import Image


class Converter(QWidget):
    def __init__(self):
        super().__init__()

        # инициализация пользовательского интерфейса
        self.initUI()

    def initUI(self):
        # Установка иконки приложения
        self.setWindowIcon(QIcon('icon.png'))

        # Создание и настройка виджетов
        source_label = QLabel('Выберите исходный файл:')
        self.source_file = QLabel('')
        choose_source_file = QPushButton('Обзор...')
        choose_source_file.clicked.connect(self.getSourceFile)

        destination_label = QLabel('Выберите формат конвертации:')
        self.destination_format = QComboBox()
        self.destination_format.addItems(['jpg', 'jpeg'])

        convert_button = QPushButton('Конвертировать')
        convert_button.clicked.connect(self.convertFile)

        # Создание вертикального менеджера компоновки для установки виджетов в столбец
        vbox = QVBoxLayout()

        # Создание сетки для расстановки виджетов
        grid = QGridLayout()
        grid.setSpacing(10)

        # Добавление виджетов в сетку
        grid.addWidget(source_label, 1, 0)
        grid.addWidget(self.source_file, 2, 0)
        grid.addWidget(choose_source_file, 2, 1)
        grid.addWidget(destination_label, 3, 0)
        grid.addWidget(self.destination_format, 4, 0)
        grid.addWidget(convert_button, 5, 0)

        # Добавление сетки в вертикальный менеджер компоновки
        vbox.addLayout(grid)

        # Установка вертикального менеджера компоновки
        self.setLayout(vbox)

        # Установка параметров окна
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Конвертер файлов')
        self.show()

    def getSourceFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Выберите исходный файл', '',
                                                  "Images (*.jpg *.jpeg);;All Files (*)",
                                                  options=options)
        if fileName:
            self.source_file.setText(fileName)

    def convertFile(self):
        # Получение пути к исходному файлу и формат конвертации
        source_file = self.source_file.text()
        destination_format = self.destination_format.currentText()

        # Конвертация файла
        if source_file:
            with Image.open(source_file) as img:
                destination_file = source_file.rsplit('.', 1)[0] + '.' + destination_format
                img_1 = img.copy()
                img_1.save(destination_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = Converter()
    sys.exit(app.exec())
