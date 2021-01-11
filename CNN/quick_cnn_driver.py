dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC"

from tensorflow.keras.models import load_model
import cv2

model = load_model(dir_path)
image = cv2.imread(dir_path + "\hand_6.jpg", cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(image, (28, 28)).reshape(-1,28,28,1)
resized_image.shape
resized_image = resized_image / 255.0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
prediction = model.predict_classes(resized_image)
print(prediction[0])