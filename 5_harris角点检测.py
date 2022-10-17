import cv2
import numpy as np

def cv_show(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey() #ms 不输入代表任意键销毁窗口
    cv2.destroyAllWindows()

img = cv2.imread(f"01_Picture\\17_Chessboard.jpg")
img_gray = cv2.imread(f"01_Picture\\17_Chessboard.jpg",0)
# cv_show(img_gray)

dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
# print(img_gray.shape, dst.shape, dst)
"""
(512, 512) (512, 512)

[[ 3.6699771e-10  3.6699771e-10  6.2803860e-09 ...  1.3847177e-06
   4.4098829e-07  7.3472353e-07]
 ...
 [ 5.3286503e-06  5.3286503e-06  4.0693500e-05 ...  2.7155602e-05
   4.6793948e-06 -1.9230029e-08]]
"""

max_,min_ = dst.max(), dst.min()
dst_trans = dst * 255 * ((dst-min_) / (max_ - min_))
# 展示角点
cv_show(dst_trans)

img[dst > 0.01 * dst.max() ] = (0,0,255)
cv_show(img)