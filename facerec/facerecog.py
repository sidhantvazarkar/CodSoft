import threading
import cv2
from deepface import DeepFace
from deepface.detectors import FaceDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

# Load the reference image
reference_img = cv2.imread("abd.jpg")
reference_img = cv2.resize(reference_img, (224, 224))
reference_img = reference_img.astype('float32') / 255.0

def check_face(frame):
    global face_match
    try:
        # Detect faces in the frame
        detector_backend = "opencv"  # Try other backends like 'mtcnn', 'ssd', 'dlib' if needed
        faces = FaceDetector.detect_faces(detector_backend, frame)
        
        for face in faces:
            x, y, w, h = face['region']
            detected_face = frame[y:y+h, x:x+w]
            detected_face = cv2.resize(detected_face, (224, 224))
            detected_face = detected_face.astype('float32') / 255.0

            # Verify the detected face against the reference image
            result = DeepFace.verify(detected_face, reference_img.copy(), model_name='Facenet', distance_metric='euclidean_l2')
            
            print(f"Distance: {result['distance']}, Verified: {result['verified']}")
            if result['distance'] < 0.6:  # Adjust this threshold if needed
                face_match = True
            else:
                face_match = False
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 10 == 8:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
