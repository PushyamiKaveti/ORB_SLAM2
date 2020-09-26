import os
import numpy as np
import cv2 

s_ref = set(os.listdir("/home/auv/software/ORB_SLAM2/window_refocused/rgb"))
s_mono = set(os.listdir("/home/auv/software/ORB_SLAM2/window_mono/rgb"))
s_dyn = set(os.listdir("/home/auv/software/ORB_SLAM2/window_dynaslam/rgb"))

final_s = s_ref.union(s_mono)
final_s = final_s.intersection(s_dyn)
final_s = sorted(final_s)
print(len(final_s))
with open('video_sequence.txt', 'w') as f:
    for item in final_s:
        print >> f, item

#make the video frame
frame = np.zeros((1080,1920, 3))

#read the list of images from the three paths and fill the frame
for item in final_s:
    # mono
    pang_mono =  cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_mono/rgb", item),cv2.IMREAD_COLOR)
    fr_mono  = cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_mono", item[:-4]), cv2.IMREAD_UNCHANGED)
    
    pang_dyn =  cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_dynaslam/rgb", item), cv2.IMREAD_COLOR)
    fr_dyn  = cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_dynaslam", item[:-4]) , cv2.IMREAD_UNCHANGED)
    
    pang_ref =  cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_refocused/rgb", item) , cv2.IMREAD_COLOR)
    fr_ref  = cv2.imread(os.path.join("/home/auv/software/ORB_SLAM2/window_refocused", item[:-4]) , cv2.IMREAD_UNCHANGED)
    
    if pang_mono is not None:
        pang_mono = cv2.resize(pang_mono, (640, 540))
        fr_mono = cv2.resize(fr_mono, (640, 540))
        frame[ 0:540, 0:640, :] = fr_mono
        frame[540:1080,0:640, :] = pang_mono
    if pang_dyn is not None:
        pang_dyn = cv2.resize(pang_dyn, (640, 540))
        fr_dyn = cv2.resize(fr_dyn, (640, 540))
        frame[0:540, 640:1280,  :] = fr_dyn
        frame[540:1080,640:1280,  :] = pang_dyn
    if pang_ref is not None:
        pang_ref = cv2.resize(pang_ref, (640, 540))
        fr_ref = cv2.resize(fr_ref, (640, 540))
        frame[0:540,1280:1920,  :] = fr_ref
        frame[540:1080,1280:1920,  :] = pang_ref
       
    cv2.imwrite("video"+item[:-4], frame)
