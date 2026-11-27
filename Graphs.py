from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Graph(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.graph_setup()

    def graph_setup(self):
        self.setWindowTitle("Graph Window")
        self.resize(700, 500)

        self.body_selector = QComboBox(self)
        self.body_selector.addItems(["Body 1", "Body 2", "Both"])

        self.draw_btn = QPushButton("Draw", self)
        self.draw_btn.clicked.connect(self.draw_graph)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.clicked.connect(self.clear_graph)

        self.export_btn = QPushButton("Export to CSV", self)
        self.export_btn.clicked.connect(self.export_to_csv)

        controls = QHBoxLayout()
        controls.addWidget(self.body_selector)
        controls.addWidget(self.draw_btn)
        controls.addWidget(self.clear_btn)
        controls.addWidget(self.export_btn)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlabel("Time (s)")
        self.axes.set_ylabel("Temperature (°C)")
        self.canvas = FigureCanvasQTAgg(self.figure)

        layout = QVBoxLayout(self)
        layout.addLayout(controls)
        layout.addWidget(self.canvas)

    def draw_graph(self):
        pass

    def clear_graph(self):
        pass

    def export_to_csv(self):
        pass