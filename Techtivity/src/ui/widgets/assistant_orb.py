from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt

from src.ui.theme import *


class AssistantOrb(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(260, 260)

        # White Card
        self.setStyleSheet(f"""
        QWidget {{
            background: {CARD};
            border-radius: 130px;
        }}
        """)

        # Shadow
        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(40)

        shadow.setOffset(0, 8)

        shadow.setColor(QColor(0, 0, 0, 40))

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.setContentsMargins(20, 20, 20, 20)

        # Orb
        orb = QLabel("●")

        font = QFont()

        font.setPointSize(90)

        orb.setFont(font)

        orb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        orb.setStyleSheet("""
        color:#3B82F6;
        background:transparent;
        """)

        # Status Text
        status = QLabel("Assistant Ready")

        status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        status.setStyleSheet("""
        color:#64748B;
        font-size:16px;
        background:transparent;
        """)

        layout.addStretch()

        layout.addWidget(orb)

        layout.addWidget(status)

        layout.addStretch()