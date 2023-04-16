import cv2

# Открываем RTSP-поток
stream_url = "rtsp://atwk:ea33ak@192.168.11.50"
cap = cv2.VideoCapture(stream_url)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Отображаем кадр
    cv2.imshow("Video Stream", frame)

    # Обработка нажатия клавиши "q" для остановки
    if cv2.waitKey(1) == ord("q"):
        break

# Освобождаем ресурсы и закрываем окна
cap.release()
out.release()
cv2.destroyAllWindows()