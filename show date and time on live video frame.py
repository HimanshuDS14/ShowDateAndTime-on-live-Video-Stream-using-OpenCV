import cv2
import datetime

cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    datet = str(datetime.datetime.now())

    frame = cv2.putText(frame , datet , (10,50) , cv2.FONT_HERSHEY_COMPLEX , 1,(0,0,255) , 2)

    cv2.imshow("live" , frame)

    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()