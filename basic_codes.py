import cv2 as cv 
#read and show image as well as video
img=cv.imread("G:\learn opencv/dollar.tif")
cv.imshow("original image", img)
capture=cv.VideoCapture("G:\learn opencv/LEARN_OPENCV_in_3_HOURS_with_Python_Including_3xProject_WQeoO7MI0Bs_247.mkv")

#resclae video 
def rescale_frame(frame,scale=0.5):
    width,height=frame.shape[:2]
    dimension=(int(width),int(height))
    return cv.resize(frame,dimension,interpolation=cv.INTER_LINEAR)

while True:
    isTrue,frame=capture.read() #read each frame in capture and if it reads successfuly, isTrue will be True
    resized_frame=rescale_frame(frame,scale=0.5)
    cv.imshow("original video",frame)
    cv.imshow("resized video",resized_frame)
    if cv.waitKey(25) & 0xFF == ord("q"): #after 25ms if user presses the letter q, the movie will finish 
        break
    
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)