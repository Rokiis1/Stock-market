import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.calculation_window import CalculationWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    calculation_window = CalculationWindow()
    
    # Connect signals to handle window transitions
    main_window.open_calculation_signal.connect(calculation_window.show)
    calculation_window.back_to_main_signal.connect(main_window.show)
    
    # Hide the calculation window initially
    calculation_window.hide()
    
    main_window.show()
    sys.exit(app.exec_())