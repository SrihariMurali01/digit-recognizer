from PIL import Image
import numpy as np


class ImageProcessor:

    def __init__(self, path):
        self.path = path

    def process(self):
        # Open the image file
        image = Image.open(self.path)

        # Convert the image to grayscale if it's not already
        image = image.convert('L')

        # Convert the image to a NumPy array
        image_array = np.array(image)

        pixel_data = image_array.flatten().tolist()

        # Now, 'pixel_data' contains the pixel values as a list
        return np.array(pixel_data)/255


# # Example usage
# processor = ImageProcessor('images/01.png')
# pixel_data_list = processor.process()
