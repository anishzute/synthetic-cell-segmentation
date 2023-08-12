import tkinter as tk
from PIL import Image

class SharedVariables:
    def __init__(self):
        self.width = tk.IntVar()
        self.height = tk.IntVar()
        self.num_cells = tk.IntVar()
        self.min_size = tk.IntVar()
        self.max_size = tk.IntVar()
        self.min_intensity = tk.IntVar()
        self.max_intensity = tk.IntVar()
        self.noise_dev = tk.DoubleVar()
        self.noise_mean = tk.DoubleVar()
        self.kernel_size = tk.IntVar()
        self.min_distance = tk.IntVar()
        self.color_image = Image.new(mode="RGB", size=(256, 256))
        self.color_plot = Image.new(mode="RGB", size=(256, 256))
        self.segmented_plot = Image.new(mode="RGB", size=(256, 256))
