import pandas as panda   
import cv2   
import time  
from datetime import datetime 

initialState = None  
motionTrackList= [ None, None ]   
motionTime = []  
 
dataFrame = panda.DataFrame(columns = ["Initial", "Final"]) 

stream_url = "rtsp://atwk:ea33ak@192.168.11.50"
cap = cv2.VideoCapture(stream_url)

frame_count = 0

while True:  
    #check, cur_frame = video.read()
    check, cur_frame = cap.read()
    if not check:
        break
    var_motion = 0
    gray_image = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)  
    gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)  
    if initialState is None:  
       initialState = gray_frame  
       continue  
    differ_frame = cv2.absdiff(initialState, gray_frame)  
    thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)  
    cont,_ = cv2.findContours(thresh_frame.copy(),   
                      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

    for cur in cont:  
        if cv2.contourArea(cur) < 10000:  
            continue  
        var_motion = 1  
        (cur_x, cur_y,cur_w, cur_h) = cv2.boundingRect(cur)  
        cv2.rectangle(cur_frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 255, 0), 3)  
    motionTrackList.append(var_motion)  
    motionTrackList = motionTrackList[-2:] 

    if motionTrackList[-1] == 1 and motionTrackList[-2] == 0:  
        motionTime.append(datetime.now())  
    if motionTrackList[-1] == 0 and motionTrackList[-2] == 1:  
        motionTime.append(datetime.now())  
    cv2.imshow("The image captured in the Gray Frame is shown below: ", gray_frame)  
    cv2.imshow("Difference between the  inital static frame and the current frame: ", differ_frame)  
    cv2.imshow("Threshold Frame created from the PC or Laptop Webcam is: ", thresh_frame)  
    cv2.imshow("From the PC or Laptop webcam, this is one example of the Colour Frame:", cur_frame)  
    wait_key = cv2.waitKey(1)

    if wait_key == ord('m'):  
        if var_motion == 1:  
            motionTime.append(datetime.now())  
        break  

for a in range(0, len(motionTime), 2): 
    dataFrame = dataFrame.append({"Initial" : time[a], "Final" : motionTime[a + 1]}, ignore_index = True)  
dataFrame.to_csv("EachMovement.csv")    
video.release()  
cv2.destroyAllWindows()
cap.release()
out.release()
cv2.destroyAllWindows()
