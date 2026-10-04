from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt
from src.ui.theme import *


class FeatureCard(QWidget):

    def __init__(self, icon, title, description, button_text):
        super().__init__()

        self.setFixedSize(300, 320)

        self.setStyleSheet(f"""
        QWidget {{
            background:{CARD};
            border-radius:22px;
        }}
        """)

        # ---------- Shadow ----------

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(30)

        shadow.setOffset(0, 6)

        shadow.setColor(QColor(0, 0, 0, 40))

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(25, 25, 25, 25)

        layout.setSpacing(15)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # ---------- Icon ----------

        icon_label = QLabel(icon)

        icon_font = QFont()

        icon_font.setPointSize(34)

        icon_label.setFont(icon_font)

        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_label.setFixedSize(80, 80)

        icon_label.setStyleSheet(f"""
        QLabel{{
            background:{PRIMARY_LIGHT};
            border-radius:40px;
            color:white;
        }}
        """)

        # ---------- Title ----------

        title_label = QLabel(title)

        title_font = QFont()

        title_font.setPointSize(18)

        title_font.setBold(True)

        title_label.setFont(title_font)

        title_label.setStyleSheet(f"""
        color:{TEXT};
        background:transparent;
        """)

        # ---------- Description ----------

        description_label = QLabel(description)

        description_label.setWordWrap(True)

        description_label.setStyleSheet(f"""
        color:{SUBTEXT};
        background:transparent;
        font-size:14px;
        """)

        # ---------- Button ----------

        button = QPushButton(button_text)

        button.setFixedHeight(45)

        button.setCursor(Qt.CursorShape.PointingHandCursor)

        button.setStyleSheet(f"""
        QPushButton{{
            background:{PRIMARY};
            color:white;
            border:none;
            border-radius:15px;
            font-size:15px;
            font-weight:bold;
        }}

        QPushButton:hover{{
            background:{PRIMARY_DARK};
        }}
        """)

        layout.addWidget(icon_label,
                         alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)

        layout.addWidget(description_label)

        layout.addStretch()

        layout.addWidget(button)