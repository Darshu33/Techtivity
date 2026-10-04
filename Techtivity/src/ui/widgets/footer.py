from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)

from PySide6.QtGui import QFont

from src.ui.theme import *


class Footer(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(80)

        self.setStyleSheet(f"""
        background:transparent;
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(40,20,40,20)

        left = QLabel("🟢  Tia is Ready")

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        left.setFont(font)

        left.setStyleSheet(f"""
        color:{SUCCESS};
        background:transparent;
        """)

        right = QLabel(
            "Your privacy is protected • Version 1.0"
        )

        right.setStyleSheet(f"""
        color:{SUBTEXT};
        background:transparent;
        font-size:13px;
        """)

        layout.addWidget(left)

        layout.addStretch()

        layout.addWidget(right)