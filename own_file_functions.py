import pathlib
from typing import Any


def image_search(source_directory, recursive, image_format):
    """The function for file search"""

    if recursive:
        images: list[Any] = list(pathlib.Path(source_directory).rglob(image_format, case_sensitive=False))
    else:
        images: list[Any] = list(pathlib.Path(source_directory).glob(image_format, case_sensitive=False))

    return list(images)


def get_file_name(file):
    """The function for getting the file name"""

    return pathlib.PurePosixPath(file).name


def get_file_stem(file):
    """The function for getting the file name without its suffix"""

    return pathlib.PurePosixPath(file).stem


def delete_file(file):
    """The function for delete file"""

    status: bool = True

    try:
        file.unlink()
    except:
        status = False

    return status


def checking_path(path):
    """The function for checking the path"""

    if pathlib.Path(path).is_dir():
        status: bool = True
    else:
        status: bool = False

    return status
