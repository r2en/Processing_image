import cv2
def cv_fourcc(c1,c2,c3,c4):
    return (ord(c1)&255) + \
    ((ord(c2)&255)<<8) + \
    ((ord(c3) & 255) << 16) + \
    ((ord(c4) & 255) << 24)

if __name__ == '__main__':
    ESC_KEY = 27
    INTERVAL = 33
    FRAME_RATE = 30

    ORG_WINDOW_NAME = 'org'
    GAUSSIAN_WINDOW_NAME = 'gaussian'
    GAUSSIAN_FILE_NAME = 'gaussian.mov'

    DEVICE_ID = 0

    cap = cv2.VideoCapture(DEVICE_ID)

    end_flag,c_frame = cap.read()
    height,width,channels = c_frame.shape
    rec = cv2.VideoWriter(GAUSSIAN_FILE_NAME,\
    cv_fourcc('X','V','I','D'),\
    FRAME_RATE,(width,height),\
    True)

    cv2.namedWindow(ORG_WINDOW_NAME)
    cv2.namedWindow(GAUSSIAN_WINDOW_NAME)

    while end_flag == True:
        g_frame = cv2.GaussianBlur(c_frame,(15,15),10)

        cv2.imshow(ORG_WINDOW_NAME,c_frame)
        cv2.imshow(GAUSSIAN_WINDOW_NAME,g_frame)

        rec.write(g_frame)

        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break
        
        end_flag,c_frame = cap.read()
    cv2.destroyAllWindows()
    cap.release()
    rec.release()
