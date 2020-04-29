#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @file gui.py
# @brief GUI for ivs-calc calculator.
# @author Denis Kramár <xkrama06@vutbr.cz>
# @date April 2019
#

from PyQt5.QtWidgets import QLayout, QApplication, QToolButton, QLineEdit, QSizePolicy, QGridLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from decimal import Decimal
import sys
import main

# define button shape and font
class Button(QToolButton):
     def __init__(self, text):
          super().__init__()

          self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
          self.setText(text)
          font = self.font()
          font.setPointSize(font.pointSize() + 5)
          self.setFont(font)

     def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 23)
        size.setWidth(max(size.width(), size.height()))
        return size

# main window
class CalculatorWindow(QWidget):
     def __init__(self):
          super().__init__()

          # expression shown on display
          self.displayExpression = ""

          # expression for calculation
          self.calculateExpression = ""

          # define window title, position and size
          self.setWindowTitle('Calculator')
          self.setGeometry(200, 200, 300, 500)

          # define display and font size
          self.display = QLineEdit('0')
          self.display.setFixedHeight(70)
          self.display.setReadOnly(True)
          self.display.setAlignment(Qt.AlignRight)
          self.display.setMaxLength(20)

          font = self.display.font()
          font.setPointSize(font.pointSize() + 7)
          self.display.setFont(font)

          # define clear all button and backspace button
          self.clearAllButton = self.createButton("CE", self.clearAllClicked)
          self.backspaceButton = self.createButton("<=", self.backspaceClicked)

          # define buttons for math operations
          self.operantsButton = []
          self.operants = ["x^n", "n√x", "log", "x!", "+", "-", "×", "÷"]

          for i in range(len(self.operants)):
               self.operantsButton.append(self.createButton(str(self.operants[i]), self.buttonClicked))

          # define number buttons
          self.numbersButton = []
          for i in range(9,0,-1):
               self.numbersButton.append(self.createButton(str(i), self.buttonClicked))

          # define button for 0 number and decimal point
          self.number0Button = self.createButton("0", self.buttonClicked)
          self.decimalButton = self.createButton(".", self.buttonClicked)
          
          # define button for open and closed parentheses
          self.openParenthesisButton = self.createButton("(", self.buttonClicked)
          self.closedParenthesisButton = self.createButton(")", self.buttonClicked)

          # define equal sign button
          self.equalsButton = self.createButton("=", self.equalsClicked)

          # create grid layout
          gridLayout = QGridLayout()
          gridLayout.setSizeConstraint(QLayout.SetFixedSize)

          # assign display to position
          gridLayout.addWidget(self.display, 0, 0, 1, 4)

          # assign clear all and backspace buttons to position
          gridLayout.addWidget(self.clearAllButton, 1, 0, 1, 2)
          gridLayout.addWidget(self.backspaceButton, 1, 2, 1, 2)

          # assign operants to position
          for i in range(2):
               for j in range(4):
                    gridLayout.addWidget(self.operantsButton[i*4+j], i+2, j)

          # assign numbers to position
          for i in range(3):
               for j in range(3):
                    gridLayout.addWidget(self.numbersButton[i*3+j], i+4, 2-j)

          # assign number 0 and decimal point to position
          gridLayout.addWidget(self.number0Button, 7, 0, 1, 2)
          gridLayout.addWidget(self.decimalButton, 7, 2)
          
          # assign open and closed parentheses, and equals sign button to position
          gridLayout.addWidget(self.openParenthesisButton, 4, 3,)
          gridLayout.addWidget(self.closedParenthesisButton, 5, 3)
          gridLayout.addWidget(self.equalsButton, 6, 3, 2, 1)

          self.setLayout(gridLayout)

     # creates custom buttom 
     """
     @brief creates custom button
     """
     def createButton(self, text, member):

        button = Button(text)
        button.clicked.connect(member)
        return button

     # recognises if clearall button was clicked, clears expressions and shows empty display
     def clearAllClicked(self):
          self.displayExpression = ""
          self.calculateExpression = ""

          self.display.setText(self.displayExpression)
          print(self.calculateExpression)

     # recognises if backspace button was clicked, removes last char or "log" from expressions
     def backspaceClicked(self):
          if (len(self.displayExpression) == 0):
               return
          elif self.displayExpression[-3:] == "log":
               self.displayExpression = ''.join(self.displayExpression[:-3])
               self.calculateExpression = ''.join(self.calculateExpression[:-3])
          else:
               self.displayExpression = ''.join(self.displayExpression[:-1])
               self.calculateExpression = ''.join(self.calculateExpression[:-1])

          self.display.setText(self.displayExpression)
          print(self.calculateExpression)

     # recognises other buttons clicks and adds signs to expressions
     def buttonClicked(self):
          clickedButton = self.sender()
          textOfButtonDisplay = clickedButton.text()
          if len(self.displayExpression) >= 20:
               self.displayExpression = "%20s" % "Expression too long"
          else:
               if textOfButtonDisplay == "x^n":
                    textOfButtonDisplay = "^"
               elif textOfButtonDisplay == "n√x":
                    textOfButtonDisplay = "√"
               elif textOfButtonDisplay == "x!":
                    textOfButtonDisplay = "!"

               self.displayExpression += textOfButtonDisplay

               if textOfButtonDisplay == "√":
                    textOfButtonCalculation = "r"
               elif textOfButtonDisplay == "×":
                    textOfButtonCalculation = "*"
               elif textOfButtonDisplay == "÷":
                    textOfButtonCalculation = "/"
               else:
                    textOfButtonCalculation = textOfButtonDisplay
               
               self.calculateExpression += textOfButtonCalculation
          
          self.display.setText(self.displayExpression)
          print(self.calculateExpression)

     # recognises if equals was clicked, tries to get result or pops out error to screen
     def equalsClicked(self):
          try:
               result = str(main.calculation(self.calculateExpression))
               self.calculateExpression = result
               if "e" in result:
                    result_split = result.split("e")
                    if (len(result_split[0]) + len(result_split[1])) > 20:
                         roundNumber = 17 - len(result_split[1])
                         firstNumber = round(float(result_split[0]), roundNumber)
                         secondNumber = result_split[1]
                         self.displayExpression = str(firstNumber) + "e" + secondNumber
               elif len(result) > 20:
                    self.displayExpression = "%.12E" % Decimal(int(result))
               else:
                    self.displayExpression = result

               self.display.setText(self.displayExpression)
          except:
               self.display.setText("MathError")
               pass

if __name__ == '__main__':
     app = QApplication(sys.argv)
     calculator = CalculatorWindow()
     calculator.show()
     sys.exit(app.exec())