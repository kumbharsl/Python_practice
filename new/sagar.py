from PyQt5 import QtCore, QtGui, QtWidgets

class RegistrationPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Window settings
        self.setWindowTitle("Register Account")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #E3F3FD;")  # Light gradient-like background

        # Main frame settings
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setGeometry(QtCore.QRect(150, 50, 500, 500))
        self.main_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 2px solid #D3D3D3;
            }
        """)

        # Layout for the form
        layout = QtWidgets.QVBoxLayout(self.main_frame)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        # Add camera icon (You can add an actual icon here)
        camera_label = QtWidgets.QLabel(self.main_frame)
        camera_label.setPixmap(QtGui.QPixmap("camera_icon.png").scaled(80, 80, QtCore.Qt.KeepAspectRatio))
        camera_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(camera_label)

        # Title label
        title_label = QtWidgets.QLabel("Register Account")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #555;")
        layout.addWidget(title_label)

        # Input fields with placeholder icons
        self.add_input_field(layout, "Your Name", "user_icon.png")
        self.add_input_field(layout, "Username", "username_icon.png")
        self.add_input_field(layout, "Your Email", "email_icon.png")
        self.add_input_field(layout, "Password", "password_icon.png", password=True)
        self.add_input_field(layout, "Confirm Password", "password_icon.png", password=True)

        # Terms and privacy text
        terms_label = QtWidgets.QLabel("Don't worry, you can change your username later\nI agree to Terms of Service & Privacy Policy")
        terms_label.setAlignment(QtCore.Qt.AlignCenter)
        terms_label.setStyleSheet("font-size: 10px; color: #888;")
        layout.addWidget(terms_label)

        # Register button
        register_button = QtWidgets.QPushButton("Register")
        register_button.setStyleSheet("""
            QPushButton {
                background-color: #00C897;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #00B386;
            }
        """)
        layout.addWidget(register_button)
        
        # Center align the button
        register_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

    def add_input_field(self, layout, placeholder_text, icon_path, password=False):
        """Helper method to add input fields with icons."""
        input_frame = QtWidgets.QFrame()
        input_layout = QtWidgets.QHBoxLayout(input_frame)

        # Icon
        icon_label = QtWidgets.QLabel()
        icon_label.setPixmap(QtGui.QPixmap(icon_path).scaled(20, 20, QtCore.Qt.KeepAspectRatio))
        input_layout.addWidget(icon_label)

        # Text input
        line_edit = QtWidgets.QLineEdit()
        line_edit.setPlaceholderText(placeholder_text)
        if password:
            line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        line_edit.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid #D3D3D3;
                padding: 5px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-bottom: 2px solid #00C897;
            }
        """)
        input_layout.addWidget(line_edit)

        layout.addWidget(input_frame)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration_page = RegistrationPage()
    registration_page.show()
    sys.exit(app.exec_())
