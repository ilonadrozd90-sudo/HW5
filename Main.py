from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QLabel, QPushButton, QSlider
from Body import Body
from About import About
from Graphs import Graph

class HeatTransfer(QWidget):
    def __init__(self):
        super().__init__()

        self.b1 = Body(mass=10, heat_capacity=0.40, temp=0)
        self.b2 = Body(mass=10, heat_capacity=0.40, temp=0)
        self.sigma = 1
        self.dt = 0.01

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)

        self.setup()

    def setup(self):
        self.setWindowTitle("Heat Transfer")
        self.setFixedSize(700, 420)

        self.left_slider = QSlider(Qt.Orientation.Vertical, self)
        self.left_slider.setRange(0, 200)
        self.left_slider.setValue(int(self.b1.temp))
        self.left_slider.move(35, 45)
        self.left_slider.resize(25, 160)
        self.left_slider.valueChanged.connect(self.left_slider_changed)

        self.left_visual = QLabel(self)
        self.left_visual.move(75, 50)
        self.left_visual.resize(90, 150)
        self.left_visual.setStyleSheet(self.temp_to_color(self.b1.temp))

        self.left_temp_label = QLabel("Temp.", self)
        self.left_temp_label.move(40, 230)
        self.left_temp_display = QDoubleSpinBox(self)
        self.left_temp_display.setRange(0.0, 200.0)
        self.left_temp_display.setDecimals(1)
        self.left_temp_display.setSuffix(" °C")
        self.left_temp_display.setReadOnly(True)
        self.left_temp_display.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.left_temp_display.setValue(self.b1.temp)
        self.left_temp_display.move(85, 225)
        self.left_temp_display.resize(110, 25)

        self.left_mass_label = QLabel("Mass", self)
        self.left_mass_label.move(40, 265)
        self.left_mass_input = QDoubleSpinBox(self)
        self.left_mass_input.setRange(0.01, 10000.0)
        self.left_mass_input.setDecimals(2)
        self.left_mass_input.setSuffix(" kg")
        self.left_mass_input.setValue(self.b1.mass)
        self.left_mass_input.move(85, 260)
        self.left_mass_input.resize(110, 25)

        self.left_h_cap_label = QLabel("H. Cap.", self)
        self.left_h_cap_label.move(40, 300)
        self.left_h_cap_input = QDoubleSpinBox(self)
        self.left_h_cap_input.setRange(0.01, 10000.0)
        self.left_h_cap_input.setDecimals(2)
        self.left_h_cap_input.setSuffix(" J/kg°C")
        self.left_h_cap_input.setValue(self.b1.heat_capacity)
        self.left_h_cap_input.move(85, 295)
        self.left_h_cap_input.resize(110, 25)

        
        self.conductivity_label = QLabel("Conductivity", self)
        self.conductivity_label.move(315, 50)
        self.conductivity_input = QDoubleSpinBox(self)
        self.conductivity_input.setRange(0.0, 1000.0)
        self.conductivity_input.setDecimals(2)
        self.conductivity_input.setSuffix(" J/s°C")
        self.conductivity_input.setValue(self.sigma)
        self.conductivity_input.move(295, 75)
        self.conductivity_input.resize(110, 25)

        self.bridge = QLabel(self)
        self.bridge.move(165, 110)
        self.bridge.resize(370, 25)
        self.bridge.setStyleSheet("background-color: gray; border: 1px solid black;")

        self.start_button = QPushButton("Start", self)
        self.start_button.setCheckable(True)
        self.start_button.move(300, 225)
        self.start_button.resize(100, 35)
        self.start_button.clicked.connect(self.start_stop_button_method)

        self.graphs_button = QPushButton("Graphs", self)
        self.graphs_button.move(300, 270)
        self.graphs_button.resize(100, 35)
        self.graphs_button.clicked.connect(self.open_graphs_window)

        self.about_button = QPushButton("About", self)
        self.about_button.move(300, 315)
        self.about_button.resize(100, 35)
        self.about_button.clicked.connect(self.show_about)

        
        self.right_visual = QLabel(self)
        self.right_visual.move(535, 50)
        self.right_visual.resize(90, 150)
        self.right_visual.setStyleSheet(self.temp_to_color(self.b2.temp))

        self.right_slider = QSlider(Qt.Orientation.Vertical, self)
        self.right_slider.setRange(0, 200)
        self.right_slider.setValue(int(self.b2.temp))
        self.right_slider.move(640, 45)
        self.right_slider.resize(25, 160)
        self.right_slider.valueChanged.connect(self.right_slider_changed)

        self.right_temp_display = QDoubleSpinBox(self)
        self.right_temp_display.setRange(0.0, 200.0)
        self.right_temp_display.setDecimals(1)
        self.right_temp_display.setSuffix(" °C")
        self.right_temp_display.setReadOnly(True)
        self.right_temp_display.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.right_temp_display.setValue(self.b2.temp)
        self.right_temp_display.move(505, 225)
        self.right_temp_display.resize(110, 25)
        self.right_temp_label = QLabel("Temp.", self)
        self.right_temp_label.move(625, 230)

        self.right_mass_input = QDoubleSpinBox(self)
        self.right_mass_input.setRange(0.01, 10000.0)
        self.right_mass_input.setDecimals(2)
        self.right_mass_input.setSuffix(" kg")
        self.right_mass_input.setValue(self.b2.mass)
        self.right_mass_input.move(505, 260)
        self.right_mass_input.resize(110, 25)
        self.right_mass_label = QLabel("Mass", self)
        self.right_mass_label.move(625, 265)

        self.right_h_cap_input = QDoubleSpinBox(self)
        self.right_h_cap_input.setRange(0.01, 10000.0)
        self.right_h_cap_input.setDecimals(2)
        self.right_h_cap_input.setSuffix(" J/kg°C")
        self.right_h_cap_input.setValue(self.b2.heat_capacity)
        self.right_h_cap_input.move(505, 295)
        self.right_h_cap_input.resize(110, 25)
        self.right_h_cap_label = QLabel("H. Cap.", self)
        self.right_h_cap_label.move(625, 300)

    def temp_to_color(self, temp_val):
        borders = max(0, min(200, temp_val))
        ratio = borders / 200.0
        red = int(ratio * 255)
        blue = int((1.0 - ratio) * 255)
        return f"background-color: rgb({red}, 0, {blue}); border: 1px solid black;"

    def left_slider_changed(self, value):
        self.b1.temp = value
        self.left_temp_display.setValue(self.b1.temp)
        self.left_visual.setStyleSheet(self.temp_to_color(self.b1.temp))

    def right_slider_changed(self, value):
        self.b2.temp = value
        self.right_temp_display.setValue(self.b2.temp)
        self.right_visual.setStyleSheet(self.temp_to_color(self.b2.temp))

    def open_graphs_window(self):
        self.graph_window = Graph()
        self.graph_window.show()

    def show_about(self):
        self.about_window = About()
        self.about_window.show()

    def start_stop_button_method(self):
        if self.start_button.isChecked():
            self.b1 = Body(mass=self.left_mass_input.value(), heat_capacity=self.left_h_cap_input.value(),temp=self.left_slider.value())
            self.b2 = Body(mass=self.right_mass_input.value(), heat_capacity=self.right_h_cap_input.value(), temp=self.right_slider.value())
            self.start_button.setText("Stop")
            self.timer.start(self.dt*1000)
        else:
            self.start_button.setText("Start")
            self.timer.stop()

    def timer_method(self):
        sigma = self.conductivity_input.value()
        T1 = self.b1.temp
        T2 = self.b2.temp

        I1 = sigma * (T2 - T1)
        I2 = sigma * (T1 - T2)

        Q1 = I1 * self.dt
        Q2 = I2 * self.dt

        new_T1 = self.b1.add_heat(Q1)
        new_T2 = self.b2.add_heat(Q2)

        self.left_temp_display.setValue(new_T1)
        self.left_visual.setStyleSheet(self.temp_to_color(new_T1))
        self.right_temp_display.setValue(new_T2)
        self.right_visual.setStyleSheet(self.temp_to_color(new_T2))

        self.left_slider.blockSignals(True)
        self.left_slider.setValue(round(new_T1))
        self.left_slider.blockSignals(False)
        self.right_slider.blockSignals(True)
        self.right_slider.setValue(round(new_T2))
        self.right_slider.blockSignals(False)

if __name__ == "__main__":
    app = QApplication()
    window = HeatTransfer()
    window.show()
    app.exec()