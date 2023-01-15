# /Users/Wolfram_3387/Downloads/WelcomeWindow.ui
# /Users/Wolfram_3387/PycharmProjects/LenaApp/design/WelcomeWindow.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/WelcomeWindow.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/WelcomeWindow.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/MainWindow.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/MainWindow.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/InformationalWindows1.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/InformationWindow1.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/InformationalWindows2.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/InformationWindow2.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/InformationalWindows3.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/InformationWindow3.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/InformationalWindows4.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/InformationWindow4.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/InformationalWindows5.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/InformationWindow5.py
# pyuic5 /Users/Wolfram_3387/Downloads/lena_ui/Calculator.ui -o /Users/Wolfram_3387/PycharmProjects/LenaApp/design/Calculator.py

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from design import WelcomeWindow, MainWindow, InformationWindow1, \
    InformationWindow2, InformationWindow4, InformationWindow3, \
    InformationWindow5, Calculator  # Это наш конвертированный файл дизайна


class HelloWindow(QtWidgets.QMainWindow, WelcomeWindow.Ui_WelcomeWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле WelcomeWindow.py
        super().__init__()
        self.setFixedSize(509, 507)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_2.clicked.connect(self.button_no)
        self.pushButton.clicked.connect(self.button_yes)

    def button_no(self):
        self.window().close()

    def button_yes(self):
        self.close()
        self.general_window = GeneralWindow()
        self.general_window.show()


class GeneralWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле HelloWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setFixedSize(509, 507)
        # self.pushButton.clicked.connect(self.open_1_window)
        # self.pushButton_2.clicked.connect(self.open_2_window)
        self.pushButton.clicked.connect(self.open_1_window)
        self.pushButton_2.clicked.connect(self.open_2_window)
        self.pushButton_3.clicked.connect(self.open_3_window)
        self.pushButton_4.clicked.connect(self.open_4_window)
        self.pushButton_5.clicked.connect(self.open_5_window)
        self.pushButton_6.clicked.connect(self.open_welcome_window)

    def open_1_window(self):
        self.close()  # закрыть текущее окно
        self.one_window = OneWindow()  # Подготовить следующее окно
        self.one_window.show()  # Показать следующее окно

    def open_2_window(self):
        self.close()
        self.two_window = TwoWindow()
        self.two_window.show()

    def open_3_window(self):
        self.close()
        self.three_window = ThreeWindow()
        self.three_window.show()

    def open_4_window(self):
        self.close()
        self.four_window = FourWindow()
        self.four_window.show()

    def open_5_window(self):
        self.close()
        self.five_window = FiveWindow()
        self.five_window.show()

    def open_welcome_window(self):
        self.close()
        self.hello_window = HelloWindow()
        self.hello_window.show()


class OneWindow(QtWidgets.QMainWindow, InformationWindow1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(509, 507)
        self.pushButton.clicked.connect(self.open_main_window)

    def open_main_window(self):
        self.close()
        self.main_window = GeneralWindow()
        self.main_window.show()


class TwoWindow(QtWidgets.QMainWindow, InformationWindow2.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 507)
        self.pushButton.clicked.connect(self.open_main_window)

    def open_main_window(self):
        self.close()
        self.main_window = GeneralWindow()
        self.main_window.show()


class ThreeWindow(QtWidgets.QMainWindow, InformationWindow3.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 507)
        self.pushButton.clicked.connect(self.open_main_window)

    def open_main_window(self):
        self.close()
        self.main_window = GeneralWindow()
        self.main_window.show()


class FourWindow(QtWidgets.QMainWindow, InformationWindow4.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 507)
        self.pushButton.clicked.connect(self.open_main_window)
        self.pushButton_2.clicked.connect(self.open_calculator)

    def open_main_window(self):
        self.close()
        self.main_window = GeneralWindow()
        self.main_window.show()

    def open_calculator(self):
        self.calculator = CalculatorWindow()
        self.calculator.show()


class FiveWindow(QtWidgets.QMainWindow, InformationWindow5.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(509, 507)
        self.pushButton_6.clicked.connect(self.open_main_window)

    def open_main_window(self):
        self.close()
        self.main_window = GeneralWindow()
        self.main_window.show()


class CalculatorWindow(QtWidgets.QMainWindow, Calculator.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(241, 182)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        try:
            user_number = float(self.textEdit.toPlainText().replace(',', '.'))
            if user_number == 0:
                answer = 'Окружность'
            elif 0 < user_number < 1:
                answer = 'Эллипс'
            elif user_number == 1:
                answer = 'Парабола'
            elif user_number > 1:
                answer = 'Гипербола'
            else:
                answer = 'Некорректное число'
        except ValueError:
            answer = 'Введено не число'
        self.textEdit_2.setText(answer)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HelloWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

# pyuic5 path/to/OneWindow.ui -o path/to/OneWindow.py
