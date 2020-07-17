from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import imutils
import dlib
import cv2
#initialising dlibs face detector
detector = dlib.get_frontal_face_detector()
predictor  = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
fa = FaceAligner(predictor, desiredFaceWidth=256)
image = cv2.imread('images/angelina.jpg')
#to train a smaller image
#image = imutils.resize(image, width=100)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
rects = detector(gray, 2)
for rect in rects:
# extract the ROI of the *original* face, then align the face
# using facial landmarks(right and left eye)
	(x, y, w, h) = rect_to_bb(rect)
	faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
	faceAligned = fa.align(image, gray, rect)

cv2.imshow("Aligned", faceAligned)
cv2.waitKey(0)
cv2.destroyAllWindows()