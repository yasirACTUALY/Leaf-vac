
import cv2 as cv
import numpy as np
import glob
blockSize=25
#Load in the camera
#0 is the default camera, usually the webcam and 1 is the external camera we wre using
i = 0
cap = cv.VideoCapture(0)
while True:
    # Capture a frame
    ret, frame = cap.read()
    # print(frame.shape)
    # split the frame into two halves one for each of the stereo cameras
    imgL  = frame[:, :frame.shape[1]//2, :]
    imgR  = frame[:, frame.shape[1]//2:, :]
    # showcase the two halves seperately
    cv.imshow('Left Half', imgL )
    cv.imshow('Right Half', imgR )
    #


    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv.waitKey(1) & 0xFF == ord('s'):
        # take two images
        i += 1
        cv.imwrite(f'left_image_{i}.png', imgL )
        cv.imwrite(f'right_image_{i}.png', imgR )
    elif cv.waitKey(1) & 0xFF == ord('c'):
        
        # Creating an object of StereoSGBM algorithm
        stereo = cv.StereoSGBM_create(
            minDisparity=0,
            numDisparities=16,
            blockSize=blockSize,
            disp12MaxDiff=1,
            uniquenessRatio=10,
            speckleWindowSize=100,
            speckleRange=32
        )
        # Calculating disparith using the StereoSGBM algorithm
        disp = stereo.compute(imgL, imgR).astype(np.float32)
        disp = cv.normalize(disp,0,255,cv.NORM_MINMAX)
        
        # Displaying the disparity map
        cv.imshow("disparity",disp)
        cv.waitKey(0)
        

# Release the capture and destroy windows
cap.release()
cv.destroyAllWindows()

