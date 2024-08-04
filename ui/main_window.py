from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
from .widgets import StockInfoTableWidget, StockCalculationButton

# MainWndow purpose is to create a window with a layout
class MainWindow(QMainWindow):
    open_calculation_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stonks")

        layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)
        
        self.stock_calc_button = StockCalculationButton()
        layout.addWidget(self.stock_calc_button)
        
        self.stock_table = StockInfoTableWidget()
        layout.addWidget(self.stock_table)
        
        self.stock_calc_button.clicked.connect(self.open_calculation_window)
        
        self.showMaximized()
        
    def open_calculation_window(self):
        # I need to emit the signal to open the calculation window because otherwise the calculation window will not open and will be stacked behind the main window
        self.open_calculation_signal.emit()
        self.hide() 