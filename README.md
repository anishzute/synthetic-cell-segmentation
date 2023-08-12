# Synthetic Cell Image Generation and Segmentation

This project provides a graphical user interface (GUI) to generate and segment images of cells. It uses custom sliders to control various parameters of the generated images and applies segmentation techniques to identify individual cells.

![Sample Image](images/sample.png) <!-- You can include an image if available -->

## Features

- Generate cell images with adjustable parameters like size, intensity, and noise.
- Apply segmentation to recognize individual cells.
- Customize appearance through sliders and controls.
- Dark mode theme for GUI.

## Installation

### Option 1: Download the Executable (Windows)

1. Download the latest executable from the [Releases](https://github.com/anishzute/synthetic_cell_segmentation/releases) page.
2. Unzip the downloaded file.
3. Run `synthetic_cell_segmentation.exe` to launch the application.

### Option 2: Build from Python Source

#### Prerequisites

- Python 3.x
- PIL (Pillow)
- NumPy
- OpenCV
- scikit-image
- matplotlib
- customtkinter
- tkinter

#### Install Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/synthetic_cell_segmentation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd synthetic_cell_segmentation
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Simply double-click on `synthetic_cell_segmentation.exe` to launch the application. You may need to click

Run the main script to launch the GUI:

```bash
python src/main.py
```

Use the sliders and buttons in the GUI to generate and segment cell images according to your preferences.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was created as a test for the St-Pierre Lab at the Baylor College of Medicine
