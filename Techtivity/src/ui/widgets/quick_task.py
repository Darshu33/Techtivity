from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt

from src.ui.theme import *


class QuickTask(QWidget):

    def __init__(self, icon, title):
        super().__init__()

        self.setFixedSize(170, 170)

        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(shadow)

        self.setStyleSheet(f"""
        QWidget {{
            background: {CARD};
            border-radius: 18px;
        }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Icon Circle
        icon_label = QLabel(icon)

        icon_font = QFont()
        icon_font.setPointSize(28)

        icon_label.setFont(icon_font)

        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_label.setFixedSize(70, 70)

        icon_label.setStyleSheet(f"""
        QLabel {{
            background: {PRIMARY_LIGHT};
            color: white;
            border-radius: 35px;
        }}
        """)

        # Title
        title_label = QLabel(title)

        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)

        title_label.setFont(title_font)

        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label.setStyleSheet(f"""
        color: {TEXT};
        background: transparent;
        """)

        layout.addWidget(icon_label)
        layout.addWidget(title_label)