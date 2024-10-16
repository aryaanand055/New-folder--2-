from pyzbar.pyzbar import decode
from PIL import Image

image_path = r'C:\Users\Hxtreme\Pictures\Image1.jpg' 
image = Image.open(image_path)

decoded_objects = decode(image)

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))
    print("Bounding box:", obj.rect)
import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert OpenCV frame to PIL Image
    img = Image.fromarray(frame)

    # Decode barcodes from the frame
    barcodes = decode(img)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Draw a rectangle around the barcode and display the data
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'{barcode_type}: {barcode_data}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print("Type:", barcode_type)
        print("Data:", barcode_data)

    # Show the frame
    cv2.imshow('Barcode Scanner', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()