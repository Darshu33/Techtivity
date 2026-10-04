from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor, QFont

from src.ui.theme import *


class TipCard(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(180)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 40))

        self.setGraphicsEffect(shadow)

        self.setStyleSheet(f"""
        QWidget{{
            background:{CARD};
            border-radius:22px;
        }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(25,30,30,25)

        title = QLabel("💡 Tip of the Day")

        font = QFont()
        font.setPointSize(22)
        font.setBold(True)

        title.setFont(font)

        title.setStyleSheet(f"""
        color:{PRIMARY};
        background:transparent;
        """)

        tip = QLabel(
            "Did you know?\n\n"
            "You can simply say:\n"
            "\"Tia, help me connect to Wi-Fi\"\n\n"
            "and I'll guide you step by step."
        )

        tip.setWordWrap(True)

        tip.setStyleSheet(f"""
        color:{SUBTEXT};
        background:transparent;
        font-size:16px;
        """)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(tip)