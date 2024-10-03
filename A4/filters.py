from abc import ABC, abstractmethod
import cv2

class Filter(ABC):
    @abstractmethod
    def apply(frame):
        pass

class BlackAndWhiteFilter(Filter):
    def apply(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

class FlipFilter(Filter):
    def apply(self, frame):
        return cv2.flip(frame, 0)

class CropFilter(Filter):
    def apply(self, frame):
        return frame[:, 200:654]

class ResizeFilter(Filter):
    def apply(self, frame):
        return cv2.resize(frame, (480, 854))