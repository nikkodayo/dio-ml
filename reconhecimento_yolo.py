#pip install opencv-python tensorflow keras

#git clone https://github.com/AlexeyAB/darknet.git
#cd darknet
#make

#pesos pré treinados YOLOv4
#wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4.weights

import cv2
import numpy as np

# Carregar a rede YOLOv4
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

# Carregar a imagem
image = cv2.imread("image.jpg")
height, width = image.shape[:2]

# Pré-processar a imagem para a YOLO
blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
net.setInput(blob)
outputs = net.forward(output_layers)

# Processar as detecções
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Ajuste o limiar conforme necessário
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Coordenadas da caixa delimitadora
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # Recorte do rosto detectado
            face = image[y:y+h, x:x+w]

            # Exibir a caixa delimitadora
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#model.h5 para classificação
from tensorflow.keras.models import load_model

# Carregar o classificador
classifier = load_model("model.h5")

# Pré-processar o rosto detectado
face_resized = cv2.resize(face, (160, 160))  # Ajuste para o tamanho de entrada do seu classificador
face_normalized = face_resized / 255.0
face_input = np.expand_dims(face_normalized, axis=0)

# Fazer a previsão
prediction = classifier.predict(face_input)
predicted_label = np.argmax(prediction)
print(f"Classe prevista: {predicted_label}")
