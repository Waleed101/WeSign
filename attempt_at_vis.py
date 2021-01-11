dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC"

from tensorflow.keras.models import load_model
from ann_visualizer.visualize import ann_viz;

model = load_model(dir_path)
ann_viz(model, title="My first neural network")