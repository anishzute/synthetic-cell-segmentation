import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image


def segment_cells_plot(color_image, kernel_size=5, min_distance=20):
    """
    Generates a segmented cells image with a custom color bar.

    :param color_image: Original colored cells image
    :param kernel_size: Size of the Gaussian blur kernel (default is 5)
    :param min_distance: Minimum distance for peak local max (default is 20)
    :return: PIL Image of segmented cells with custom color bar
    """

    # Convert the 16-bit image to 8-bit
    image_uint8 = cv2.convertScaleAbs(color_image, alpha=(1/256.0))

    # Convert the color image to grayscale
    image_gray = cv2.cvtColor(image_uint8, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image_gray, (kernel_size, kernel_size), 0)

    # Thresholding using Otsu's method (without inversion)
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Compute the Euclidean distance from every binary pixel to the nearest zero pixel and find peaks
    distance_map = ndimage.distance_transform_edt(thresholded)
    local_max_coords = peak_local_max(distance_map, min_distance=min_distance, labels=thresholded)

    # Create an image with the same shape as your input, with zeros everywhere except the local maxima
    local_max = np.zeros_like(thresholded)
    local_max[tuple(local_max_coords.T)] = 1

    # Perform a connected component analysis on the local peaks
    markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
    markers = watershed(-distance_map, markers, mask=thresholded)

    # Iterate through unique markers and assign a color to each segment
    segmented_image = np.zeros_like(color_image)
    colors = [(0, 0, 0)]  # Start with black for background
    cell_count = 0
    for marker in np.unique(markers):
        if marker == 0:  # Background
            continue
        mask = np.zeros_like(image_gray, dtype="uint8")
        mask[markers == marker] = 255
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        color = np.array(plt.cm.jet((len(np.unique(markers)) - cell_count - 1) / (len(np.unique(markers)) - 1))[:3])
        colors.append(color)
        color = (color * 255).astype("int")
        color = (int(color[2]), int(color[1]), int(color[0]))  # Convert to BGR
        cv2.drawContours(segmented_image, contours, -1, color, -1)
        cv2.drawContours(segmented_image, contours, -1, (255, 255, 255), 1)  # Draw the edges of the cells
        cell_count += 1

    # Convert the segmented image to RGB
    segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

    # Create a figure and axis with dark background
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')

    # Display the segmented image
    im = ax.imshow(segmented_image_rgb)

    # Create a custom color bar representing the number of cells with matching colors
    cmap = ListedColormap(colors)
    norm = plt.Normalize(vmin=0, vmax=cell_count)
    cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, ticks=range(cell_count + 1), orientation='vertical')

    # Determine step size for labels based on the number of colors
    step_size = max(cell_count // 10, 1)  # Adjust the denominator to control density

    # Modify labels to include only every step_size-th label, but always include the first label
    labels = [str(x) if (x % step_size == 0 or x == cell_count) else '' for x in range(cell_count, -1, -1)[::-1]]
    cbar.ax.set_yticklabels(labels)


    # Save the figure as a PIL Image
    buf = BytesIO()
    plt.savefig(buf, format='png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=.1)
    buf.seek(0)
    pil_image = Image.open(buf)

    return pil_image