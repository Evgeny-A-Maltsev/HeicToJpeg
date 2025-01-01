import click
import own_file_functions as own_file
import own_image_functions as own_image
from typing import Any

program_description: str = "HeicToJpeg by Evgeny A. Maltsev (yevmal@gmail.com)"
program_version: str = "0.1.0"


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.argument('destination_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively image search')
@click.option('-d', '--delete', is_flag=True, default=False, help='Delete original image')
def image_converter(source_directory, destination_directory, recursive, delete):
    if (own_file.checking_path(source_directory) and own_file.checking_path(destination_directory)):
        images: list[Any] = own_file.image_search(source_directory, recursive, "*.heic")

        count_ok: int = 0
        count_fail: int = 0
        count_deleted: int = 0

        for heic_image in images:
            if own_image.heic_to_jpeg(heic_image, destination_directory):
                count_ok += 1
                print(f"The file {own_file.get_file_name(heic_image)} has been converted")

                if delete:
                    if own_file.delete_file(heic_image):
                        count_deleted += 1
                        print(f"The file {own_file.get_file_name(heic_image)} has been deleted")
                    else:
                        print(f"The file {own_file.get_file_name(heic_image)} has not deleted")
            else:
                count_fail += 1
                print(f"The file {own_file.get_file_name(heic_image)} was not converted")

        print(f"Out of {len(images)} images, {count_ok} were converted, {count_deleted} were deleted and {count_fail} were skipped.")
    else:
        print("Error: SOURCE_DIRECTORY or DESTINATION_DIRECTORY does not exist")


if __name__ == '__main__':
    print(f'{program_description}\nversion {program_version}\n')

    image_converter()
