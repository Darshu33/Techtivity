from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QScrollArea,
)

from PySide6.QtCore import Qt

from src.ui.theme import *
from src.ui.widgets.header import Header
from src.ui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Techtivity")

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setMinimumSize(
            WINDOW_MIN_WIDTH,
            WINDOW_MIN_HEIGHT
        )

        # ==========================
        # Central Widget
        # ==========================

        central = QWidget()

        central.setStyleSheet(f"""
        background:{BACKGROUND};
        """)

        self.setCentralWidget(central)

        # ==========================
        # Main Layout
        # ==========================

        main_layout = QVBoxLayout(central)

        main_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.setSpacing(0)

        # ==========================
        # Header
        # ==========================

        header = Header()

        main_layout.addWidget(header)

        # ==========================
        # Scroll Area
        # ==========================

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setFrameShape(QScrollArea.Shape.NoFrame)

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # ==========================
        # Dashboard
        # ==========================

        dashboard = Dashboard()

        scroll.setWidget(dashboard)

        # ==========================
        # Modern Scrollbar
        # ==========================

        scroll.setStyleSheet(f"""
        QScrollArea {{
            border: none;
            background: {BACKGROUND};
        }}

        QScrollBar:vertical {{
            background: transparent;
            width: 10px;
            margin: 0px;
        }}

        QScrollBar::handle:vertical {{
            background: {PRIMARY_LIGHT};
            border-radius: 5px;
            min-height: 50px;
        }}

        QScrollBar::handle:vertical:hover {{
            background: {PRIMARY};
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0px;
        }}

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {{
            background: transparent;
        }}
        """)

        main_layout.addWidget(scroll)