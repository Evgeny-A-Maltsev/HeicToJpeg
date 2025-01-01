from PIL import Image
import pillow_heif
from PIL.ImageFile import ImageFile
import own_file_functions as own_file


def heic_to_jpeg(image_heic_path, destination_directory):
    """The function for converted HEIC to JPEG"""

    status: bool = True

    pillow_heif.register_heif_opener()

    try:
        image: ImageFile = Image.open(image_heic_path)
        image_jpeg_path = f'{destination_directory}{own_file.get_file_stem(image_heic_path)}.jpeg'

        image.save(image_jpeg_path, format='JPEG')
    except:
        status = False

    return status
