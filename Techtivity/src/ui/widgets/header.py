from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from src.ui.theme import PRIMARY


class Header(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(120)

        # Root Layout
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # Blue Top Bar
        top_bar = QFrame()
        top_bar.setObjectName("TopBar")
        top_bar.setFixedHeight(120)

        top_bar.setStyleSheet(f"""
        QFrame#TopBar {{
            background-color: {PRIMARY};
        }}
        """)

        layout = QHBoxLayout(top_bar)
        layout.setContentsMargins(35, 20, 35, 20)

        # ---------------- Left ---------------- #

        left = QVBoxLayout()

        title = QLabel("TECHTIVITY")
        title_font = QFont()
        title_font.setPointSize(28)
        title_font.setBold(True)
        title.setFont(title_font)

        subtitle = QLabel("Helping You Every Step of the Way")

        title.setStyleSheet("""
            color:white;
            background:transparent;
        """)

        subtitle.setStyleSheet("""
            color:#E6F0FF;
            background:transparent;
            font-size:15px;
        """)

        left.addWidget(title)
        left.addWidget(subtitle)

        # ---------------- Right ---------------- #

        language = QPushButton("🌍 English")
        settings = QPushButton("⚙ Settings")

        button_style = """
        QPushButton{

            background:rgba(255,255,255,35);

            color:white;

            border:none;

            border-radius:18px;

            padding:10px 18px;

            font-size:14px;

            min-width:140px;

        }

        QPushButton:hover{

            background:rgba(255,255,255,60);

        }
        """

        language.setStyleSheet(button_style)
        settings.setStyleSheet(button_style)

        layout.addLayout(left)
        layout.addStretch()
        layout.addWidget(language)
        layout.addSpacing(15)
        layout.addWidget(settings)

        root_layout.addWidget(top_bar)