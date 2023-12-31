import numpy as np
import cv2
import insightface
from insightface.app import FaceAnalysis


#buffalo_l model
app_l=FaceAnalysis(name='buffalo_l',root='insightface_model', providers=['CPUExecutionProvider'])
#providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
app_l.prepare(ctx_id=0, det_size=(640,640))


img = cv2.imread('test_image_2.jpg')
result_l = app_l.get(img)


image = img.copy()
gender_encode=['Female', 'Male']
for res in result_l:
    x1, y1, x2, y2 = res['bbox'].astype(int)
    cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 1)

    #key points
    kps = res['kps'].astype(int)

    for k1, k2 in kps:
        cv2.circle(image, (k1,k2), 2, (0,255,255),-1)

    # detection score
    score = 'score: {}%'.format(int(res['det_score']*100))
    cv2.putText(image, score, (x1,y1), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))

    gender = gender_encode[res['gender']]
    age=res['age']
    age_gender = f"{gender}::{age}"
    cv2.putText(image, age_gender, (x1,y2+10), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
    
cv2.imshow('ImageView', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

