from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextBrowser,
    QSizePolicy,
    QScrollArea,
    QPushButton,
    QLineEdit,
)

from PyQt6.QtGui import QTextOption

import requests
import sys


def get_definition():
    word = user_input.text()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    definition = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    user_input.setText("")
    definition_area.setPlainText(f"{word}: {definition}")


app = QApplication([])
window = QWidget()
window.setWindowTitle("Dictionary GUI")
main_layout = QVBoxLayout()

instructions = QLabel("Enter the word you need the definition of: ")
main_layout.addWidget(instructions)

user_input = QLineEdit()
main_layout.addWidget(user_input)

scroll_area = QScrollArea()  # Create a scroll area
scroll_area.setWidgetResizable(True)

definition_area = QTextBrowser()
definition_area.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
definition_area.setSizePolicy(
    QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
)

scroll_area.setWidget(definition_area)
scroll_area.setFixedHeight(100)

main_layout.addWidget(scroll_area)

submit_btn = QPushButton("Search Definition")
main_layout.addWidget(submit_btn)
submit_btn.clicked.connect(get_definition)

window.setMaximumHeight(250)
window.setLayout(main_layout)
window.show()
sys.exit(app.exec())
