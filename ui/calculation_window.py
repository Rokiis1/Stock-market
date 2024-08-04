from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from .widgets import  BackButtonWidget, SubmitButtonWidget, ResultWidget, ClearButtonWidget, StockMetricsWidget, StockBasicInfoWidget, SectorSelectionWidget

class CalculationWindow(QWidget):
    back_to_main_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Stonks")
        
        self.showMaximized()
        
        layout = QVBoxLayout()
        
        self.back_button_widget = BackButtonWidget()
        self.back_button_widget.back_to_main_signal.connect(self.on_close)
        layout.addWidget(self.back_button_widget)
        
        self.stock_info_widget = StockBasicInfoWidget()
        layout.addWidget(self.stock_info_widget)
        
        self.sector_selection_widget = SectorSelectionWidget()
        layout.addWidget(self.sector_selection_widget)
        
        self.stock_metrics_widget = StockMetricsWidget()
        layout.addWidget(self.stock_metrics_widget)
        
        self.result_widget = ResultWidget()
        layout.addWidget(self.result_widget)
        
        self.submit_button_widget = SubmitButtonWidget()
        self.submit_button_widget.set_submit_action(self.on_submit)
        layout.addWidget(self.submit_button_widget)
        
        self.clear_button_widget = ClearButtonWidget(self.result_widget)
        self.clear_button_widget.setVisible(False)  # Initially hidden
        self.clear_button_widget.clear_signal.connect(self.on_clear)
        layout.addWidget(self.clear_button_widget)
        
        self.setLayout(layout)
        
        # Set initial geometry to avoid warnings
        self.resize(800, 600)
        
    def on_submit(self):
        total_sum = 0

        for row in range(2):  # Iterate over both rows
            for col in range(15):
                input_field = self.stock_metrics_widget.table.cellWidget(row, col)
                if input_field:
                    try:
                        value = float(input_field.text())
                        total_sum += value
                    except ValueError:
                        pass
        
        result = total_sum
        
        # For demonstration, let's just concatenate the values
        self.result_widget.set_result(str(result))

        # Make the clear button visible
        self.clear_button_widget.setVisible(True)
    
    def on_clear(self):
        # Hide the clear button when the result is cleared
        self.clear_button_widget.setVisible(False)
        
    def on_close(self):
        # I need to emit the signal to open the main window because otherwise the main window will not open and will be stacked behind the calculation window
        self.back_to_main_signal.emit()
        self.close()