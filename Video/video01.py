import cv2
ESC_KEY = 27
INTERVAL = 33
FRAME_RATE = 30

ORG_WINDOW_NAME = 'org'
GRAY_WINDOW_NAME = 'gray'
ORG_FILE_NAME = 'slow.mov'
GRAY_FILE_NAME = 'gray_slow.mov'

org = cv2.VideoCapture(ORG_FILE_NAME)

end_flag,c_frame = org.read()
height,width,channels = c_frame.shape
rec = cv2.VideoWriter(GRAY_FILE_NAME,cv2.VideoWriter_fourcc(*'XVID'),FRAME_RATE,(width,height),False)

cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)

while end_flag == True:
    g_frame = cv2.cvtColor(c_frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow(ORG_WINDOW_NAME,c_frame)
    cv2.imshow(GRAY_WINDOW_NAME,g_frame)

    rec.write(g_frame)

    key = cv2.waitKey(INTERVAL)
    if  key == ESC_KEY:
        break
    end_flag,c_frame = org.read()
cv2.destroyAllWindows()
org.release()
rec.release()

