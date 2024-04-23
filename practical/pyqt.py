import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

class LampWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lamp Widget")
        self.setGeometry(100, 100, 300, 200)

        self.lamp_status = False

        self.button = QPushButton('Turn On', self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_lamp)
        self.button.setGeometry(100, 50, 100, 50)

    def toggle_lamp(self):
        self.lamp_status = not self.lamp_status
        if self.lamp_status:
            self.button.setText('Turn Off')
        else:
            self.button.setText('Turn On')
        self.send_to_thingspeak()

    def send_to_thingspeak(self):
        # Replace YOUR_API_KEY and YOUR_FIELD_NUMBER with your ThingSpeak API key and field number
        api_key = '35WH7TZRZZWJ87NR'
        field_number = 'field1'
        url = f'https://api.thingspeak.com/update?api_key={api_key}&field{field_number}={int(self.lamp_status)}'
        requests.get(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = LampWidget()
    widget.show()
    sys.exit(app.exec_())
