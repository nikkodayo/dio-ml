# transforma uma imagem colorida em uma imagem escala de cinza e uma binária preto e branco para uso com redes neurais.
# convert color image in gray scale and binary image for use in neural network.

import cv2

img_color = cv2.imread('path_to_your_image/image.jpg')

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

_, img_binary = cv2.threshold(img_gray ,0.5,1,cv2.THRESH_BINARY)

gray_img = cv2.cvtColor(img_color, 0)

_, img_binary=   cv.threshold(gray ,255/3.5,.9,cv.THRESH_BINARY)

cv.imwrite('path_to_your_directory/grayscaled.png', gray)
