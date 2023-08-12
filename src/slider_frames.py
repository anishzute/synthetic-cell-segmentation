import customtkinter as ctk

# SegmentSliderFrame class for segmenting image parameters
class SegmentSliderFrame(ctk.CTkFrame):
    def __init__(self, master, shared_vars, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Segment Image Parameters"
        self.shared_vars = shared_vars

        # Create and grid title label
        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=3)

        # Create sliders for kernel size and minimum distance
        self.kernel_size_slider, self.kernel_size_label, self.kernel_size_val = self.create_slider("Kernel Size", self.shared_vars.kernel_size, 1, 55, 15, 1, step_=2)
        self.min_distance_slider, self.min_distance_label, self.min_distance_val = self.create_slider("Min Distance", self.shared_vars.min_distance, 2, 20, 6, 2)

    # Method to create a slider with a label and value display
    def create_slider(self, label, variable, from_, to_, default, row_, step_=1):
        # Code for creating and gridding and returning the slider, label, and value display
        slider = ctk.CTkSlider(self, variable=variable, from_=from_, to=to_, orientation="horizontal")
        slider.set(default)
        slider.grid(row=row_,column=1, padx=10, pady=(10,0), sticky = 'ew')
        slider_label = ctk.CTkLabel(self, text=label)
        slider_label.grid(row=row_, column=0, padx=10, pady=(10,0), sticky = 'w')
        slider_val = ctk.CTkLabel(self, textvariable=variable)
        slider_val.grid(row=row_, column=2, padx=10, pady=(10,0), sticky = 'w')
        return slider, slider_label, slider_val

# GenerateSliderFrame class for generating cell image parameters
class GenerateSliderFrame(ctk.CTkFrame):
    def __init__(self, master, shared_vars, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.shared_vars = shared_vars
        self.title = "Generate Cell Image Parameters"

        # Create and grid title label
        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=3)

        # Create sliders for various image generation parameters
        # Width, height, number of cells, sizes, intensity, noise, etc.
        self.width_slider, self.width_label, self.width_val = self.create_slider("Width", self.shared_vars.width, 64, 2048, 1024,1)

        self.height_slider, self.height_label, self.height_val = self.create_slider("Height", self.shared_vars.height, 64, 2048, 1024,2)

        self.num_cells_slider, self.num_cells_label, self.num_cells_val = self.create_slider("Number of Cells", self.shared_vars.num_cells, 1, 255, 50,3)

        self.min_size_slider, self.min_size_label, self.min_size_val = self.create_slider("Min Size", self.shared_vars.min_size, 1, 250, 25,4)

        self.max_size_slider, self.max_size_label, self.max_size_val = self.create_slider("Max Size", self.shared_vars.max_size, 5, 250, 50,5)

        self.min_intensity_slider, self.min_intensity_label, self.min_intensity_val = self.create_slider("Min Intensity", self.shared_vars.min_intensity, 0, 65535, 250,6 )

        self.max_intensity_slider, self.max_intensity_label, self.max_intensity_val = self.create_slider("Max Intensity", self.shared_vars.max_intensity, 0, 65535, 65535,7)

        self.noise_dev_slider, self.noise_dev_label, self.noise_dev_val = self.create_slider("Noise Std. Dev", self.shared_vars.noise_dev, 0, 1, .75,8)

        self.noise_mean_slider, self.noise_mean_label, self.noise_mean_val = self.create_slider("Noise Mean", self.shared_vars.noise_mean, 0, 1, 0,9)

        # Warning text with some limitations and guidelines
        warning_text = "Note: There are some limitations in the interest of time.\n - Error handling has not been fully implemented. \n - Make sure to set the min_size and min_intensity to < the respective maximum values.\n - GUI scaling can have some issues if the aspect ratio is too far from square.\n - Kernel size must be set to an odd integer\n - Image segmentation may take a while for large images or many cells"
        self.warning = ctk.CTkLabel(self, text=warning_text, fg_color="gray30", corner_radius=6, justify="left", pady=10)
        self.warning.grid(row=10, column=0, padx=10, pady=(10, 0), sticky="w", columnspan=3)

 # Method to create a slider with a label and value display, similar to the SegmentSliderFrame class
    def create_slider(self, label, variable, from_, to_, default, row_, step_=1):
        # Code for creating and gridding the slider, label, and value display
        # Return the created elements
        slider = ctk.CTkSlider(self, variable=variable, from_=from_, to=to_, orientation="horizontal")
        slider.set(default)
        slider.grid(row=row_,column=1, padx=10, pady=(10,0), sticky = 'ew')
        slider_label = ctk.CTkLabel(self, text=label)
        slider_label.grid(row=row_, column=0, padx=10, pady=(10,0), sticky = 'w')
        slider_val = ctk.CTkLabel(self, textvariable=variable)
        slider_val.grid(row=row_, column=2, padx=10, pady=(10,0), sticky = 'w')
        return slider, slider_label, slider_val

