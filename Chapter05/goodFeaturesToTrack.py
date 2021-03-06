import cv2
import numpy as np

img = cv2.imread('./image/box.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 7, 0.05, 25)
# params
#	gray: image to detect corners
#	7: the number of corners to detect
#	0.05: threshold for detecting corners
#	25: the minimum distance between corners

corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    cv2.circle(img, (x,y), 5, 255, -1)

cv2.imshow("Top 'k' features", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
