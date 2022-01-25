mpdraw = mp.solutions.drawing_utils
mpfacemesh = mp.solutions.face_mesh
facemesh = mpfacemesh.FaceMesh(static_image_mode=True, min_detection_confidence= 0.5, min_tracking_confidence=0.5)
drawing = mpdraw.DrawingSpec(thickness=1, circle_radius=2, color=(0,255, 255))
blank  = np.zeros(img.shape, np.uint8)
with mpfacemesh.FaceMesh(static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    results = facemesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    for face_landmarks in results.multi_face_landmarks:
        print(face_landmarks)
        mpdraw.draw_landmarks(img, face_landmarks, mpfacemesh.FACEMESH_TESSELATION, drawing, drawing)
        mpdraw.draw_landmarks(blank, face_landmarks, mpfacemesh.FACEMESH_TESSELATION, drawing, drawing)
cv2.imshow('face landmarks are:', img)
cv2.imshow('plotting the landmarks', blank)
cv2.waitKey(0)
