import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# cv2.CascadeClassifier is a class in OpenCV used to load pre-trained models (classifiers) to detect objects like faces, eyes, smiles, cars, etc., in an image or video.
# cv2.data.haarcascades: Path to OpenCV's built-in models
# 'haarcascade_frontalface_default.xml': Model for detecting front-facing faces.
# Instead of training our own model (which is hard), OpenCV gives us a ready-made file to detect faces. It’s based on Haar-like features, trained to find human faces.

cam = cv2.VideoCapture(0)
# Starts accessing your computer’s default webcam (device 0).
# 0 means default webcam
# If you have multiple cameras, use 1, 2, etc.

while True:
    ret ,frame = cam.read()
# cap.read() captures one frame from the webcam.
# ret = Boolean (True if successful)
# frame = Actual image/frame captured

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# It converts the color image captured from the webcam (frame) into a grayscale image and stores it in the variable gray.  
    faces = face.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w , y+ h) ,(0,255,0),1)
# x, y: Top-left corner of face
# w, h: Width and height of the face box
# Draws a green rectangle over each face
# To visually show the user where the face is on screen.
# (0, 255, 0) = green color
# 2 = thickness of the rectangle
    cv2.imshow('Face Detection App', frame)
# Opens a window named "Face Detection App" and displays the frame.
# So the user can see the video feed with rectangles over their face in real-time.
    if cv2.waitKey(1) & 0xFF == ord('c'):
            break
# cv2.waitKey(1) waits 1 ms for a keypress
# If the key pressed is 'q', exit the loop

cam.release()
cv2.destroyAllWindows()
# cam.release() = Stop using the webcam
# cv2.destroyAllWindows() = Close all OpenCV windows

