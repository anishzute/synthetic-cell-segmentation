import customtkinter as ctk
from image_generator import generate_cells_image, generate_cells_plot
from image_segmentation import segment_cells_plot
from PIL import Image

class ImageFrame(ctk.CTkFrame):
	def __init__(self, master, shared_vars, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.shared_vars = shared_vars
		# self.title = "Images"
		# self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
		# self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew",columnspan=3)

		
		self.grid_columnconfigure((0,1), weight = 1)
		self.grid_rowconfigure((0,1,2), weight = 1)

		#Generated Images
		self.generate_label = ctk.CTkLabel(self, text="Generated Image", fg_color="gray30", corner_radius=6)
		self.generate_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

		self.generated_image_label = ctk.CTkLabel(self, text="")  
		self.generated_image_label.grid(row=1, column=0, padx=.5, pady=(10, 0), sticky="news")


		self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generateButton)
		self.generate_button.grid(row=3, column=0, padx=10, pady=10)

		#Segment Images
		self.segment_label = ctk.CTkLabel(self, text="Segmented Image", fg_color="gray30", corner_radius=6)
		self.segment_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="new")

		self.segmented_image_label = ctk.CTkLabel(self, text="")  
		self.segmented_image_label.grid(row=1, column=1, padx=0.5, pady=(10, 0), sticky="news")

		self.generate_button = ctk.CTkButton(self, text="Segment", command=self.segmentButton)
		self.generate_button.grid(row=3, column=1, padx=10, pady=10)
	
	def generateButton(self):
		shared_vars = self.shared_vars
		shared_vars.color_image = generate_cells_image(shared_vars.width.get(), shared_vars.height.get(), shared_vars.num_cells.get(), shared_vars.min_size.get(), shared_vars.max_size.get(), shared_vars.min_intensity.get(), shared_vars.max_intensity.get(), shared_vars.noise_mean.get(), shared_vars.noise_dev.get(), blur_amount=7)
		shared_vars.color_plot = generate_cells_plot(shared_vars.color_image)

		desired_width = 480
		original_width, original_height = shared_vars.color_plot.size
		aspect_ratio = original_height / original_width
		new_height = int(desired_width * aspect_ratio)
		# resized_image = shared_vars.color_plot.image.resize((desired_width, new_height), Image.LANCZOS)

		generated_image = ctk.CTkImage(dark_image=shared_vars.color_plot, size=(desired_width, new_height))
		self.generated_image_label.configure(image=generated_image)
		return generated_image

	def segmentButton(self):
		shared_vars = self.shared_vars
		shared_vars.segmented_plot = segment_cells_plot(shared_vars.color_image, shared_vars.kernel_size.get(), shared_vars.min_distance.get())
		
		desired_width = 480
		original_width, original_height = shared_vars.color_plot.size
		aspect_ratio = original_height / original_width
		new_height = int(desired_width * aspect_ratio)
		# resized_image = shared_vars.color_plot.image.resize((desired_width, new_height), Image.LANCZOS)

		segmented_image = ctk.CTkImage(dark_image=shared_vars.segmented_plot, size=(desired_width, new_height))
		self.segmented_image_label.configure(image=segmented_image)
		return segmented_image