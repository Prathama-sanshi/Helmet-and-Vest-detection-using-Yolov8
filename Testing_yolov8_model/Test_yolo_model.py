 # import the opencv library
import cv2
from send_notification import send_notif
from ultralytics import YOLO


 
data_check = ['NO-Safety Vest','NO-Hardhat']
model = YOLO('weights/best.pt')
def checkfun(img):
    pred = model.predict(img)[0]
    for c in pred.boxes.cls:
        print(model.names[int(c)])
        if str(model.names[int(c)]) in data_check:
            cv2.imwrite('out.jpg', img)
            send_notif()
    pred_plotted = pred.plot()
    return pred_plotted
    # if not results or len(results) == 0:
    #     continue


# define a video capture object
vid = cv2.VideoCapture(0)
#0 means it uses default camera , if 1 then it checks for external webcam.
#or Provide a location of an image or a video.

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    frame = checkfun(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
