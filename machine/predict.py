import os
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
from ultralytics import YOLO
import concurrent.futures

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# URL stream camera
url = "http://192.168.1.7/cam-hi.jpg"
model = YOLO("best.pt")

colors = {
    "bening": (0, 255, 0),  # Green for 'bening'
    "keruh": (0, 165, 255),  # Orange for 'keruh' (BGR format)
}


def stream_and_detect():
    cv2.namedWindow("Stream and Detection", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(imgnp, -1)

        results = model(frame)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0]
                label = model.names[int(box.cls[0])]

                # Select color based on class label
                color = colors.get(
                    label, (255, 255, 255)
                )  # Default to white if not found

                # Draw rectangle and put text
                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                frame = cv2.putText(
                    frame,
                    f"{label} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2,
                )

        cv2.imshow("Stream and Detection", frame)

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Program started")
    stream_and_detect()
