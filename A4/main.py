import cv2
from filters import *

class Pipeline:
    
    def __init__ (self):
        self.filters = []
    
    def add_filter(self, *filters):
        for filter in filters:
            if isinstance(filter, Filter):
                self.filters.append(filter)
            else:
                raise ValueError(f"Expected {Filter} found - {filter}")
    
    def run(self, frame):
        for f in self.filters:
            frame = f.apply(frame)
        
        return frame

if __name__ == "__main__":
    pipeline = Pipeline()

    pipeline.add_filter(BlackAndWhiteFilter(), FlipFilter(), CropFilter(), ResizeFilter())

    cap = cv2.VideoCapture("minecraft_parkour.mp4")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        filtered_frame = pipeline.run(frame)

        cv2.imshow("Original frame", frame)
        cv2.imshow("Filtered frame", filtered_frame)

        # 27 is ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()