import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

while 1:
    check, frame = vid.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)

    for x, y, p, q in faces:
        frame = cv2.rectangle(frame, (x,y), (x+p,y+q), (0,255,0), 3)

    cv2.imshow("Camera",frame)
    key = cv2.waitKey(1)

    #time.sleep(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
