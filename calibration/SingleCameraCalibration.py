import cv2 as cv
import glob
import numpy as np
 

 
def calibrate_camera(images_folder):
    images_names = sorted(glob.glob(images_folder))
    images = []
    for imname in images_names:
        im = cv.imread(imname, 1)
        images.append(im)
 
    #criteria used by checkerboard pattern detector.
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
 
    rows = 7 
    columns = 10
    world_scaling = 1.
 
    #coordinates of squares in the checkerboard world space
    objp = np.zeros((rows*columns,3), np.float32)
    objp[:,:2] = np.mgrid[0:rows,0:columns].T.reshape(-1,2)
    objp = world_scaling* objp
 
    #frame dimensions.
    width = images[0].shape[1]
    height = images[0].shape[0]
 
    #Pixel coordinates of checkerboards
    imgpoints = [] # 2d points in image plane.
 
    #coordinates of the checkerboard in checkerboard world space.
    objpoints = [] # 3d point in real world space
 
 
    for frame in images:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
        #find the checkerboard
        ret, corners = cv.findChessboardCorners(gray, (rows, columns), None)
 
        if ret == True:
 
            conv_size = (4,4 )
            corners = cv.cornerSubPix(gray, corners, conv_size, (-1, -1), criteria)
            cv.drawChessboardCorners(frame, (rows,columns), corners, ret)

            cv.namedWindow('img', cv.WINDOW_NORMAL)
            cv.resizeWindow('img', 1000, 1000)
            cv.imshow('img', frame)
            k = cv.waitKey(500)
 
            objpoints.append(objp)
            imgpoints.append(corners)
 
 
 
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, (width, height), None, None)
    # print('rmse:', ret)
    # print('camera matrix:\n', mtx)
    # print('distortion coeffs:', dist)
    # print('Rs:\n', rvecs)
    # print('Ts:\n', tvecs)
 
    return mtx, dist

def stereo_calibrate(mtx1, dist1, mtx2, dist2):
    #read the synched frames
    images_namesR = glob.glob("right/*")
    images_namesR = sorted(images_namesR)
    images_namesL = glob.glob("left/*")
    images_namesL = sorted(images_namesL)
    c1_images_names = images_namesL
    c2_images_names = images_namesR
 
    c1_images = []
    c2_images = []
    # loading th eimages from left to c1_images and right to c2_images
    for im1, im2 in zip(c1_images_names, c2_images_names):
        c1_images.append(cv.imread(im1, 1))
        c2_images.append(cv.imread(im2, 1))
        # show the images side by side
        # cv.imshow('left', c1_images[-1])
        # cv.imshow('right', c2_images[-1])
        cv.waitKey(0)
 
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,   0, 0.0001)
 
    rows = 7 
    columns = 10
    world_scaling = 1.
 
    #coordinates of squares in the checkerboard world space
    objp = np.zeros((rows*columns,3), np.float32)
    objp[:,:2] = np.mgrid[0:rows,0:columns].T.reshape(-1,2)
    objp = world_scaling* objp
 
    #frame dimensions. Frames should be the same size.
    width = c1_images[0].shape[1]
    height = c1_images[0].shape[0]
 
    #Pixel coordinates of checkerboards
    imgpoints_left = [] # 2d points in image plane.
    imgpoints_right = []
 
    #coordinates of the checkerboard in checkerboard world space.
    objpoints = [] # 3d point in real world space
 
    for frame1, frame2 in zip(c1_images, c2_images):
        gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
        gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
        c_ret1, corners1 = cv.findChessboardCorners(gray1, (rows, columns), None)
        c_ret2, corners2 = cv.findChessboardCorners(gray2, (rows, columns), None)
 
        if c_ret1 == True and c_ret2 == True:
            corners1 = cv.cornerSubPix(gray1, corners1, (11, 11), (-1, -1), criteria)
            corners2 = cv.cornerSubPix(gray2, corners2, (11, 11), (-1, -1), criteria)
 
            cv.drawChessboardCorners(frame1, (rows, columns), corners1, c_ret1)
            # cv.namedWindow('img1', cv.WINDOW_NORMAL)
            # cv.resizeWindow('img1', 1000, 1000)
            # cv.imshow('img1', frame1) 
            cv.drawChessboardCorners(frame2, (rows, columns), corners2, c_ret2)
            # cv.namedWindow('img2', cv.WINDOW_NORMAL)
            # cv.resizeWindow('img2', 1000, 1000)
            # cv.imshow('img2', frame2)
            k = cv.waitKey(100)
 
            objpoints.append(objp)
            imgpoints_left.append(corners1)
            imgpoints_right.append(corners2)
 
    stereocalibration_flags = cv.CALIB_FIX_INTRINSIC
    ret, CM1, dist1, CM2, dist2, R, T, E, F = cv.stereoCalibrate(objpoints, imgpoints_left, imgpoints_right, mtx1, dist1,
                                                                 mtx2, dist2, (width, height), criteria = criteria, flags = stereocalibration_flags)
 
    print(ret)
    return R, T

 
mtx1, dist1 = calibrate_camera(images_folder = 'D2/*')
mtx2, dist2 = calibrate_camera(images_folder = 'J2/*')