import cv2
import mediapipe as mp
import serial
import time

# Khởi tạo giao tiếp Serial với Arduino (cổng và baud rate cần tùy chỉnh theo hệ thống của bạn)
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Đợi Arduino khởi động

# Khởi tạo Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Hàm đếm số ngón tay giơ lên
def count_fingers(hand_landmarks):
    # Chỉ số các điểm đầu ngón tay và khớp đầu ngón
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]
    count = 0

    # Kiểm tra từng ngón tay
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:  # Tip cao hơn PIP
            count += 1

    # Kiểm tra ngón cái
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:  # Ngón cái mở rộng
        count += 1

    return count

# Mở camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Lật ảnh để giống với hình ảnh gương
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Xử lý ảnh qua Mediapipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Vẽ các điểm và đường nối trên bàn tay
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Đếm số ngón tay giơ lên
            fingers_up = count_fingers(hand_landmarks)

            # Gửi tín hiệu số ngón tay đến Arduino
            arduino.write(str(fingers_up).encode())
            print(f"Fingers Up: {fingers_up}")

    # Hiển thị khung hình
    cv2.imshow("Hand Detection", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp
cap.release()
cv2.destroyAllWindows()
arduino.close()
