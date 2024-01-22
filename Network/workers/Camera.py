import threading

import numpy as np
from PyQt5.QtCore import pyqtSignal as Signal, QObject
from threading import Lock
import cv2

class Video_Thread(QObject):
    send_vid = Signal(np.ndarray)

    last_frame = None
    last_ready = None
    lock = Lock()

    def __init__(self, rtsp_link):
        super().__init__()
        self.capture = None
        thread = threading.Thread(target=self.rtsp_cam_buffer, args=(self.capture, rtsp_link), name="rtsp_read_thread")
        thread.daemon = True
        thread.start()

    def rtsp_cam_buffer(self, capture, rtsp_link):

        if capture is None:
            capture = cv2.VideoCapture(rtsp_link)
        if not capture.isOpened():
            capture = cv2.VideoCapture(rtsp_link)
        while True:
            with self.lock:
                if capture is None:
                    capture = cv2.VideoCapture(rtsp_link)
                if not capture.isOpened():
                    capture = cv2.VideoCapture(rtsp_link)
                self.last_ready, self.last_frame = capture.read()

                self.last_frame = cv2.cvtColor(self.last_frame, cv2.COLOR_RGB2BGR)
                self.send_vid.emit(self.last_frame)

    def read(self):
        if (self.last_ready is not None) and (self.last_frame is not None):
            return True, self.last_frame.copy()
        else:
            return False, None
