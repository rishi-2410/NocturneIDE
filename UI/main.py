import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence

from eric7.UI.ai_core import ask_ai


class AIAssistantPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("AI Assistant", parent)
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("Ask AI something...")

        self.sendButton = QPushButton("Send to AI")
        self.sendButton.clicked.connect(self.send_to_ai)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.sendButton)

        container = QWidget()
        container.setLayout(layout)
        self.setWidget(container)

    def send_to_ai(self):
        prompt = self.textEdit.toPlainText()
        self.textEdit.append("\nAI is thinking...")

        try:
            response = ask_ai(prompt)
            self.textEdit.append(f"\nAI: {response}")
        except Exception as e:
            self.textEdit.append(f"\nError: {str(e)}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eric IDE with AI Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Додаємо панель AI
        self.ai_panel = AIAssistantPanel(self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.ai_panel)

        # Add keyboard shortcut to toggle AI panel
        self.toggle_ai_shortcut = QShortcut(QKeySequence("Ctrl+Shift+A"), self)
        self.toggle_ai_shortcut.activated.connect(self.toggle_ai_panel)

    def toggle_ai_panel(self):
        is_visible = self.ai_panel.isVisible()
        self.ai_panel.setVisible(not is_visible)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
