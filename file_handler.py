import pathlib
from typing import List, Union


class FileHandler:
    @staticmethod
    def image_search(source_directory: str, recursive: bool, image_format: str) -> List[pathlib.Path]:
        """Search for image files in a directory"""
        if recursive:
            images = list(pathlib.Path(source_directory).rglob(image_format, case_sensitive=False))
        else:
            images = list(pathlib.Path(source_directory).glob(image_format, case_sensitive=False))
        return images

    @staticmethod
    def get_file_name(file: Union[str, pathlib.Path]) -> str:
        """Get the file name with extension"""
        return pathlib.PurePosixPath(file).name

    @staticmethod
    def get_file_stem(file: Union[str, pathlib.Path]) -> str:
        """Get the file name without extension"""
        return pathlib.PurePosixPath(file).stem

    @staticmethod
    def delete_file(file: pathlib.Path) -> bool:
        """Delete a file"""
        try:
            file.unlink()
            return True
        except Exception:
            return False

    @staticmethod
    def check_path(path: str) -> bool:
        """Check if path exists and is a directory"""
        return pathlib.Path(path).is_dir()