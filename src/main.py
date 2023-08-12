import customtkinter as ctk
from shared_variables import SharedVariables
from slider_frames import GenerateSliderFrame, SegmentSliderFrame
from image_frame import ImageFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Synthetic Cell Image Generation and Segmentation")
        self.geometry('1600x720')

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        shared_vars = SharedVariables()

        self.generate_slider_frame = GenerateSliderFrame(self, shared_vars)
        self.generate_slider_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nesw")

        self.segment_slider_frame = SegmentSliderFrame(self, shared_vars)
        self.segment_slider_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nesw")

        self.image_frame = ImageFrame(self, shared_vars)
        self.image_frame.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="nesw", columnspan=2, rowspan=2)


ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")
app = App()
app.mainloop()
