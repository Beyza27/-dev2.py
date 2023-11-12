import cv2
import numpy as np

# Kamerayı başlatma
cap = cv2.VideoCapture(0)

while True:
    # Kamera görüntüsü okuma
    ret, frame = cap.read()

    # Renk uzayını değiştir (BGR -> HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığı tanımlama
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renkli nesneleri maskeleme
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Kırmızı nesneleri orijinal görüntüde gösterme
    result = cv2.bitwise_and(frame, frame, mask=mask_red)

    # Görüntüleri gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Red Objects', result)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# kamerayı kapatma
cap.release()
cv2.destroyAllWindows()
