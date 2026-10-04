from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)

from src.ui.widgets.assistant_orb import AssistantOrb
from src.ui.theme import *


class HeroSection(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        background:{BACKGROUND};
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            60,
            40,
            60,
            40
        )

        layout.setSpacing(60)

        # ---------------- LEFT ---------------- #

        left = QVBoxLayout()
        left.setSpacing(18)

        hour = datetime.now().hour

        if hour < 12:
            greeting = "🌅 Good Morning!"
        elif hour < 17:
            greeting = "☀️ Good Afternoon!"
        else:
            greeting = "🌙 Good Evening!"

        greet = QLabel(greeting)

        font = QFont()
        font.setPointSize(24)
        font.setBold(True)

        greet.setFont(font)

        greet.setStyleSheet(f"""
        color:{TEXT};
        """)

        welcome = QLabel("Welcome to Techtivity")

        font2 = QFont()
        font2.setPointSize(32)
        font2.setBold(True)

        welcome.setFont(font2)

        welcome.setStyleSheet(f"""
        color:{PRIMARY};
        """)

        description = QLabel(
            "Hi, I'm Tia.\n\n"
            "I'm here to help you use your computer and smartphone\n"
            "with confidence.\n\n"
            "Ask me anything, and I'll guide you step by step."
        )

        description.setWordWrap(True)

        description.setStyleSheet(f"""
        color:{SUBTEXT};
        font-size:17px;
        """)

        start_button = QPushButton("🎤  Start Talking")

        start_button.setFixedSize(230, 55)

        start_button.setStyleSheet(f"""
        QPushButton{{
            background:{PRIMARY};
            color:white;
            border:none;
            border-radius:18px;
            font-size:17px;
            font-weight:bold;
        }}

        QPushButton:hover{{
            background:{PRIMARY_DARK};
        }}
        """)

        left.addWidget(greet)
        left.addWidget(welcome)
        left.addWidget(description)
        left.addSpacing(15)
        left.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignLeft)
        left.addStretch()

        # ---------------- RIGHT ---------------- #

        right = QVBoxLayout()

        right.addStretch()

        right.addWidget(
            AssistantOrb(),
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        right.addStretch()

        layout.addLayout(left, 3)
        layout.addLayout(right, 2)