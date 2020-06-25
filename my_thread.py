from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import pandas as pd
import pandas_model

def dict_add(dict, key, value):
    dict[key] = value

def add_pandas(df, row):
    df = df.append(row, ignore_index=True)
    df.fillna(0, inplace=True)
    return df

dict1 = {}

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent, video_path,df):
        super().__init__(parent)
        self.df = df
        self.video_path = video_path

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        while True:
            ret, frame = cap.read()

            if ret==False:
                cv2.destroyAllWindows()
                break
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                dict_add(dict1, 'h', h)
                dict_add(dict1, 'w', w)
                dict_add(dict1, 'ch', ch)
                self.df = add_pandas(self.df, dict1)
                # print(self.df)
            
                