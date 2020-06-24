import cv2
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from gui_copy import Ui_Dialog
import pandas as pd
import pandas_model

df = pd.DataFrame()


if __name__ == '__main__':
    app = QApplication([])
    gui = Ui_Dialog()

    gui.setupUi(df)
    # model = pandas_model.PandasModel(df)
    # gui.frame_value.setModel(model)
    gui.show()
    app.exec_() # For Signal and Slot actions catch
