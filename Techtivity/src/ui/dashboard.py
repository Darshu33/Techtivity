from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from PySide6.QtGui import QFont

from src.ui.theme import *

from src.ui.widgets.hero_section import HeroSection
from src.ui.widgets.feature_card import FeatureCard
from src.ui.widgets.quick_task import QuickTask
from src.ui.widgets.tip_card import TipCard
from src.ui.widgets.footer import Footer


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        background:{BACKGROUND};
        """)

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(35, 35, 35, 35)

        main_layout.setSpacing(35)

        # ====================================================
        # Hero Section
        # ====================================================

        main_layout.addWidget(HeroSection())

        # ====================================================
        # Section Title
        # ====================================================

        title = QLabel("What would you like help with today?")

        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)

        title.setFont(title_font)

        title.setStyleSheet(f"""
        color:{TEXT};
        """)

        subtitle = QLabel(
            "Choose one of the options below to get started."
        )

        subtitle.setStyleSheet(f"""
        color:{SUBTEXT};
        font-size:15px;
        """)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ====================================================
        # Feature Cards
        # ====================================================

        feature_grid = QGridLayout()

        feature_grid.setHorizontalSpacing(25)
        feature_grid.setVerticalSpacing(25)

        feature_grid.addWidget(
            FeatureCard(
                "💻",
                "Computer Help",
                "Learn to use your computer step by step.",
                "Open"
            ),
            0,0
        )

        feature_grid.addWidget(
            FeatureCard(
                "📱",
                "Phone Help",
                "Guided assistance for Android and iPhone.",
                "Open"
            ),
            0,1
        )

        feature_grid.addWidget(
            FeatureCard(
                "📚",
                "Tutorials",
                "Beginner friendly lessons for everyday tasks.",
                "Explore"
            ),
            1,0
        )

        feature_grid.addWidget(
            FeatureCard(
                "💬",
                "Talk to Tia",
                "Ask anything naturally using your voice.",
                "Start"
            ),
            1,1
        )

        main_layout.addLayout(feature_grid)

        # ====================================================
        # Everyday Tasks
        # ====================================================

        task_title = QLabel("Everyday Tasks")

        task_font = QFont()
        task_font.setPointSize(22)
        task_font.setBold(True)

        task_title.setFont(task_font)

        task_title.setStyleSheet(f"""
        color:{TEXT};
        """)

        main_layout.addWidget(task_title)

        task_grid = QGridLayout()

        task_grid.setHorizontalSpacing(20)
        task_grid.setVerticalSpacing(20)

        task_grid.addWidget(
            QuickTask("📶","Wi-Fi"),0,0)

        task_grid.addWidget(
            QuickTask("📧","Email"),0,1)

        task_grid.addWidget(
            QuickTask("🌐","Internet"),0,2)

        task_grid.addWidget(
            QuickTask("📷","Photos"),0,3)

        task_grid.addWidget(
            QuickTask("🖨","Printer"),1,0)

        task_grid.addWidget(
            QuickTask("🎥","Video Call"),1,1)

        task_grid.addWidget(
            QuickTask("🔊","Volume"),1,2)

        task_grid.addWidget(
            QuickTask("💾","USB Drive"),1,3)

        main_layout.addLayout(task_grid)

        # ====================================================
        # Tip Card
        # ====================================================

        main_layout.addWidget(TipCard())

        # ====================================================
        # Footer
        # ====================================================

        main_layout.addWidget(Footer())

        main_layout.addStretch()