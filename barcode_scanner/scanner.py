
import cv2
from pyzbar.pyzbar import decode
import numpy as np

class BarcodeScanner:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)  # Open camera

    def start_scanning(self):
        """Starts scanning and stops after reading the first barcode"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            barcodes = decode(frame)

            for barcode in barcodes:
                # Draw a rectangle around the barcode
                rect_points = barcode.polygon
                if len(rect_points) == 4:
                    pts = [rect_points[0], rect_points[1], rect_points[2], rect_points[3]]
                    cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 3)
                else:
                    cv2.circle(frame, (barcode.rect.left + barcode.rect.width // 2, barcode.rect.top + barcode.rect.height // 2), 5, (0, 0, 255), 3)

                # Decode and print the barcode data
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type
                print(f"Barcode Data: {barcode_data}, Type: {barcode_type}")

                # Stop scanning after the first barcode is detected
                self.stop_scanning()
                return  # Exit the function

            # Display the frame (optional)
            # cv2.imshow('Barcode Scanner', frame)

            # Exit if 'q' is pressed (optional for manual override)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_scanning()
                break

    def stop_scanning(self):
        """Stops the scanning process"""
        self.cap.release()
        cv2.destroyAllWindows()

    def __del__(self):
        """Ensure resources are released when object is deleted"""
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
