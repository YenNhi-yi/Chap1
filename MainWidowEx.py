import random

from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic.properties import QtWidgets

from Chapter_1.Ex24.ui.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.reset_game()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonR.clicked.connect(self.random_numbers)
        self.pushButtonN.clicked.connect(self.reset_game)
        self.pushButtonE.clicked.connect(self.exit_game)

    def reset_game(self):
        self.computer_money = 100
        self.player_money = 100
        self.update_money_display()
        self.label_1.setText("7")
        self.label_2.setText("7")
        self.label_3.setText("7")

    def random_numbers(self):
        if self.player_money < 30:
            QMessageBox.warning(self.MainWindow, "Not Enough Money", "You don't have enough coins to play!")
            return

        # Deduct 30 coins for the spin
        self.player_money -= 30
        self.computer_money += 30

        # Generate random numbers for the 3 boxes
        num1 = random.randint(0, 8)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 10)

        # Update labels with new random numbers
        self.label_1.setText(str(num1))
        self.label_2.setText(str(num2))
        self.label_3.setText(str(num3))

        # Check winnings
        if num1 == 7:
            reward = 100 + 0.5 * self.computer_money
            self.player_money += int(reward)
            self.computer_money -= int(0.5 * self.computer_money)
        if num2 == 7:
            reward = 30 + 0.5 * self.computer_money
            self.player_money += int(reward)
            self.computer_money -= int(0.5 * self.computer_money)
        if num3 == 7:
            reward = 10
            self.player_money += reward

        self.update_money_display()

    def update_money_display(self):
        self.Machine_2.setText(f"{self.player_money}")
        self.Machine.setText(f"{self.computer_money}")

    def exit_game(self):
        """Closes the application."""
        self.MainWindow.close()
