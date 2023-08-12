import numpy as np
import cv2
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

def add_noise(image, mean = 0, std_dev = .5):
	"""
	Adds Gaussian noise to the given image.

	:param image: Image to add noise to
	:return: Noisy image
	"""
	# Generate Noise
	noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint16)

	# Scale the noise to match the image's data type, avoiding division by zero
	noise = (noise * (65535 / (noise.max() + 1e-5))).astype(np.uint16)

	# Add the noise to the image
	image_noisy = np.clip(image + noise, 0, 65535).astype(np.uint16)

	return image_noisy

def black_to_yellow_colormap():
    """
    Defines a custom color map that transitions from black to yellow.

    :return: LinearSegmentedColormap object
    """
    cdict = {
        'red': [(0, 0, 0), (1, 1, 1)],
        'green': [(0, 0, 0), (1, 1, 1)],
        'blue': [(0, 0, 0), (1, 0, 0)]
    }
    return LinearSegmentedColormap('BlackYellow', cdict, N=256)

def generate_cells_image(width, height, num_cells, min_size, max_size, min_intensity, max_intensity, noise_mean, noise_dev, blur_amount):
    """
    Generates a colored image of yellow flourescing cells on a black background

    :param width: Width of the image
    :param height: Height of the image
    :param num_cells: Number of cells to be generated
    :param min_size: Minimum size of cells
    :param max_size: Maximum size of cells
    :param min_intensity: Minimum intensity value of cells
    :param max_intensity: Maximum intensity value of cells
    :param blur_amount: Amount of Gaussian blur to apply (default is 7)
    :return: Colored image of cells
    """

    # Create an empty image with uint16 data type
    image = np.zeros((height, width), np.uint16)

    # Generate the cells
    for _ in range(num_cells):
        # Randomly generate the cell's features
        center = np.random.randint(0, width), np.random.randint(0, height)
        axes = np.random.randint(min_size, max_size, size=2)
        angle = np.random.randint(0, 360)
        intensity = np.random.randint(min_intensity, max_intensity)  # Adjust range as needed for uint16

        # Generate the cell
        cv2.ellipse(image, tuple(center), tuple(axes), angle, 0, 360, intensity, -1)

    # Apply a Gaussian blur to mimic cell edges
    grayscale_image = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)

    # Add noise to the image (ensure add_noise function handles uint16)
    noisy_image = add_noise(grayscale_image, noise_mean, noise_dev)

    # Create an empty blue channel and set it to 0, then stack into 3 channel image
    blue_channel = np.zeros((height, width), np.uint16)
    color_image = np.dstack((blue_channel, noisy_image, noisy_image))

    # Normalize the image to the uint16 range
    # cv2.normalize(color_image, color_image, 0, 65535, cv2.NORM_MINMAX)
    # cv2.normalize(color_image, None, 0, 65535, cv2.NORM_MINMAX)

    return color_image


    # return image



# New function to generate color cells image with legend
def generate_cells_plot(color_image):
	"""
	Generates a colored cells image with a dark mode theme.

	:param color_image: Original colored cells image
	:return: PIL Image with dark mode theme
	"""
	height, width, channel = color_image.shape

	# Extract the green channel, as it represents the intensity in the monochromatic yellow image
	intensity_image = color_image[:, :, 1]

	# Create a figure and axis with dark background
	plt.style.use('dark_background')
	fig, ax = plt.subplots(figsize=(8, 6))
	fig.patch.set_facecolor('#1e1e1e')
	ax.set_facecolor('#1e1e1e')

	# Use the custom black to yellow colormap
	colormap = black_to_yellow_colormap()

	# Display the image
	im = ax.imshow(intensity_image, cmap=colormap)

	# Add tick marks with white color
	ax.set_xticks(np.arange(0, width, width // 10))
	ax.set_yticks(np.arange(0, height, height // 10))
	ax.set_xticklabels(np.arange(0, width, width // 10), color='white')
	ax.set_yticklabels(np.arange(0, height, height // 10), color='white')

	# Create a color bar without label
	cbar = fig.colorbar(im, ax=ax)
	cbar.ax.yaxis.set_tick_params(color='white')
	plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

	# Save the figure as a PIL Image
	buf = BytesIO()
	plt.savefig(buf, format='png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=.1)
	buf.seek(0)
	pil_image = Image.open(buf)

	return pil_image