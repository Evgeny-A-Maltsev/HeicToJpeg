from PIL import Image
import pillow_heif
from typing import Union
import pathlib
from file_handler import FileHandler


class ImageConverter:
    SUPPORTED_OUTPUT_FORMATS = {
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png': 'PNG',
        'webp': 'WEBP',
        'bmp': 'BMP',
        'tiff': 'TIFF'
    }

    def __init__(self):
        self._register_heif()

    def _register_heif(self):
        """Register HEIF/HEIC opener if needed"""
        pillow_heif.register_heif_opener()

    def convert_image(self, input_path: Union[str, pathlib.Path], 
                    output_dir: str, output_format: str) -> bool:
        """Convert image to specified format"""
        input_path = pathlib.Path(input_path)
        output_format = output_format.lower()

        if output_format not in self.SUPPORTED_OUTPUT_FORMATS:
            raise ValueError(f"Unsupported output format: {output_format}")

        try:
            with Image.open(input_path) as img:
                output_path = pathlib.Path(output_dir) / \
                            f"{FileHandler.get_file_stem(input_path)}.{output_format}"
                img.save(output_path, format=self.SUPPORTED_OUTPUT_FORMATS[output_format])
                return True
        except Exception as e:
            print(f"Error converting {input_path}: {str(e)}")
            return False