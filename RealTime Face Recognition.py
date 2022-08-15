import cv2
from os.path import dirname
def main():
    cascPath=f'{dirname(__file__)}\haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
    
        ret, frames = video_capture.read()
        
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            if(len(faces)-1): cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
            else: cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    video_capture.release()
    cv2.destroyAllWindows()

if(__name__=='__main__'):
    main()




