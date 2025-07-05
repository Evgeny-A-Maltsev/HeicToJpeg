import click
from typing import List, Any
from file_handler import FileHandler
from image_handler import ImageConverter


class CLIApp:
    PROGRAM_DESCRIPTION = "Image Converter by Evgeny A. Maltsev (yevmal@gmail.com)"
    PROGRAM_VERSION = "0.1.0"

    def __init__(self):
        self.file_handler = FileHandler()
        self.image_converter = ImageConverter()

    def run(self, source_dir: str, dest_dir: str, 
           recursive: bool, delete: bool, 
           input_format: str, output_format: str) -> None:
        """Main conversion logic"""
        if not (self.file_handler.check_path(source_dir) and 
               self.file_handler.check_path(dest_dir)):
            print("Error: SOURCE_DIRECTORY or DESTINATION_DIRECTORY does not exist")
            return

        images = self.file_handler.image_search(
            source_dir, recursive, f"*.{input_format.lower()}"
        )

        counts = {'ok': 0, 'fail': 0, 'deleted': 0}

        for img in images:
            if self.image_converter.convert_image(img, dest_dir, output_format):
                counts['ok'] += 1
                print(f"Converted: {self.file_handler.get_file_name(img)}")

                if delete and self.file_handler.delete_file(img):
                    counts['deleted'] += 1
                    print(f"Deleted: {self.file_handler.get_file_name(img)}")
            else:
                counts['fail'] += 1
                print(f"Failed: {self.file_handler.get_file_name(img)}")

        self._print_summary(len(images), counts)

    def _print_summary(self, total: int, counts: dict) -> None:
        """Print conversion summary"""
        print(f"\nSummary:")
        print(f"Total images: {total}")
        print(f"Converted: {counts['ok']}")
        print(f"Deleted: {counts['deleted']}")
        print(f"Failed: {counts['fail']}")


@click.command()
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, 
              help='Recursively search for images')
@click.option('-d', '--delete', is_flag=True, default=False, 
              help='Delete original image after conversion')
@click.option('-if', '--input-format', default='heic', 
              help='Input image format (e.g. heic, png, jpg, webp, bmp, tiff)')
@click.option('-of', '--output-format', default='jpeg', 
              help='Output image format (e.g. heic, png, jpg, webp, bmp, tiff)')
def cli(source_directory, destination_directory, recursive, 
       delete, input_format, output_format):
    print(f"{CLIApp.PROGRAM_DESCRIPTION}\nversion {CLIApp.PROGRAM_VERSION}\n")
    app = CLIApp()
    app.run(source_directory, destination_directory, 
           recursive, delete, input_format, output_format)


if __name__ == '__main__':
    cli()