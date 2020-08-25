import cv2, time, pandas
from datetime import datetime

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

first_frame = None
status_list = [None, None]
times_list = []
df = pandas.DataFrame(columns = ["Start", "End"])

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur the frame to remove noise and increase accuracy
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    status = 0
    
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #remove the black holes in the white spaces
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    #find the contours; usage of copy method so that the orignal thresh frame doesn't get modified
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #filter the countours
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue

        status = 1
        #define the rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        #draw the rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)
    #save only the last two elements to decrease the memory usage
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times_list.append(datetime.now())
    
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshhold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times_list.append(datetime.now())
        break

df["Start"] = [times_list[i] for i in range(len(times_list)) if i%2 == 0]
df["End"] = [times_list[i] for i in range(len(times_list)) if i%2 ==1]

df.to_csv("Times.csv")


