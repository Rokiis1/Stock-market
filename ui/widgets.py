from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QComboBox, QLabel, QHBoxLayout, QPushButton, QLineEdit, QFormLayout, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIntValidator

# SectorSelectionWidget purpose is to create a sector selection dropdown
class SectorSelectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout(self)
        
        self.sector_label = QLabel("Select Sector:")
        self.sector_combo = QComboBox()
        self.sector_combo.addItems(["Technology"])
        
        self.layout.addWidget(self.sector_label)
        self.layout.addWidget(self.sector_combo)
        
        self.setLayout(self.layout)

# StockCalculationButton purpose is to create a button for stock calculation
class StockCalculationButton(QWidget):
    clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout(self)
        
        self.calc_button = QPushButton("Stock Calculation")
        self.calc_button.clicked.connect(self.clicked)
        
        self.layout.addWidget(self.calc_button)
        
        self.setLayout(self.layout)

# StockTableWidget purpose is to create a table widget
class StockInfoTableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Ticker", "Sector", "Price", "Value", "Volatility", "Beta", "RSI"])
        
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

class StockBasicInfoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QFormLayout()
        
        self.ticker_input = QLineEdit()
        self.sector_input = QLineEdit()
        
        ticker_label = QLabel("Ticker:")
        
        label_width = 100
        ticker_label.setFixedWidth(label_width)
        
        layout.addRow(ticker_label, self.ticker_input)
        
        self.setLayout(layout)

class StockMetricsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(15)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels([
            "Year", "Revenue (Net Sales)", "Income", "P/E", "Forward P/E", "P/B", "Debt/Eq", 
            "PEG", "P/FCF", "Gross Margin", "Operating Profit Margin", "Net Profit Margin", 
            "ROA", "ROE", "ROI", "EPS next 5Y", "EPS next Y"
        ])
        
        # Set year labels in the first column
        self.table.setItem(0, 0, QTableWidgetItem("Year 1"))
        self.table.setItem(1, 0, QTableWidgetItem("Year 2"))
        
        int_validator = QIntValidator()
        
        for row in range(2):
            for col in range(1, 15):
                input_field = QLineEdit()
                input_field.setValidator(int_validator)
                self.table.setCellWidget(row, col, input_field)
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.table)
        self.setLayout(layout)
        
class BackButtonWidget(QWidget):
    back_to_main_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        self.back_button = QPushButton("Back to Main Window")
        self.back_button.clicked.connect(self.on_close)
        layout.addWidget(self.back_button)
        
        self.setLayout(layout)
        
    def on_close(self):
        # emit the signal to go back to the main window
        self.back_to_main_signal.emit()

class SubmitButtonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        self.submit_button = QPushButton("Submit")
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
    def set_submit_action(self, action):
        self.submit_button.clicked.connect(action)
        
class ResultWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        # Create a horizontal layout for the label and result input
        row_layout = QHBoxLayout()
        
        self.label = QLabel("Result:")
        row_layout.addWidget(self.label)
        
        self.result_input = QLineEdit()
        self.result_input.setReadOnly(True)
        row_layout.addWidget(self.result_input)
        
        # Add the horizontal layout to the main layout
        layout.addLayout(row_layout)
        
        self.setLayout(layout)
        
    def set_result(self, result):
        self.result_input.setText(result)
    
    def clear_result(self):
        self.result_input.clear()
        
class ClearButtonWidget(QWidget):
    clear_signal = pyqtSignal()
    
    def __init__(self, result_widget, parent=None):
        super().__init__(parent)
        
        self.result_widget = result_widget
        
        layout = QVBoxLayout()
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_result)
        layout.addWidget(self.clear_button)
        
        self.setLayout(layout)
        
    def clear_result(self):
        self.result_widget.clear_result()
        self.clear_signal.emit()

