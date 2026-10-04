from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):

    def __init__(self, text):

        super().__init__(text)

        self.setMinimumHeight(60)

        self.setStyleSheet("""

        QPushButton{

            background:#5AA9F8;

            color:white;

            font-size:18px;

            border:none;

            border-radius:18px;

        }

        QPushButton:hover{

            background:#3B82D6;

        }

        QPushButton:pressed{

            background:#2E6FB6;

        }

        """)