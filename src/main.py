import customtkinter as ctk
from shared_variables import SharedVariables
from slider_frames import GenerateSliderFrame, SegmentSliderFrame
from image_frame import ImageFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the title and geometry of the main application window
        self.title("Synthetic Cell Image Generation and Segmentation")
        self.geometry('1600x720')

        # Configure grid layout for the main window
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Create an instance of SharedVariables to hold shared data
        shared_vars = SharedVariables()

        # Create and position the GenerateSliderFrame
        # This frame contains sliders to control cell image generation parameters
        self.generate_slider_frame = GenerateSliderFrame(self, shared_vars)
        self.generate_slider_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nesw")

        # Create and position the SegmentSliderFrame
        # This frame contains sliders to control cell image segmentation parameters
        self.segment_slider_frame = SegmentSliderFrame(self, shared_vars)
        self.segment_slider_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nesw")

        # Create and position the ImageFrame
        # This frame displays the generated and segmented cell images
        self.image_frame = ImageFrame(self, shared_vars)
        self.image_frame.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="nesw", columnspan=2, rowspan=2)

# Set the appearance mode and color theme for customtkinter
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")

# Create an instance of the App class and start the main loop
app = App()
app.mainloop()

