# ======================== utils.py ========================
"""
Utility functions and helper classes

Bu dosya:
- dosya ve görüntü doğrulama
- yeniden boyutlandırma
- dosya sistemi yardımcıları
için ortak araçları içerir.
"""

import os
from PIL import Image


class ImageValidator:
    """Validates image files and operations"""

    SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'}
    MAX_FILE_SIZE_MB = 50

    @staticmethod
    def is_valid_image_file(file_path: str) -> bool:
        """Check if file is a valid image"""
        try:
            # Dosya var mı?
            if not os.path.isfile(file_path):
                return False

            # Uzantı kontrolü
            ext = os.path.splitext(file_path)[1].lower()
            if ext not in ImageValidator.SUPPORTED_EXTENSIONS:
                return False

            # Dosya boyutu kontrolü
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if size_mb > ImageValidator.MAX_FILE_SIZE_MB:
                return False

            # PIL ile doğrulama (dosya bozuk mu?)
            with Image.open(file_path) as img:
                img.verify()

            return True

        except Exception:
            return False

    @staticmethod
    def validate_dimensions(
        image: Image.Image,
        max_width: int = 10000,
        max_height: int = 10000
    ) -> bool:
        """Validate image dimensions"""
        width, height = image.size
        return width <= max_width and height <= max_height


class ImageResizer:
    """Handles image resizing operations"""

    @staticmethod
    def resize_to_fit(
        image: Image.Image,
        max_width: int,
        max_height: int
    ) -> Image.Image:
        """Resize image to fit within max dimensions"""
        width, height = image.size

        width_ratio = max_width / width
        height_ratio = max_height / height
        ratio = min(width_ratio, height_ratio, 1.0)

        if ratio < 1.0:
            new_size = (int(width * ratio), int(height * ratio))
            return image.resize(new_size, Image.Resampling.LANCZOS)

        return image

    @staticmethod
    def calculate_aspect_ratio(width: int, height: int) -> float:
        """Calculate aspect ratio (width / height)"""
        if height == 0:
            return 0.0
        return width / height


class FileManager:
    """Handles file operations"""

    @staticmethod
    def get_file_info(file_path: str) -> dict | None:
        """Get file information"""
        if not os.path.isfile(file_path):
            return None

        stats = os.stat(file_path)

        return {
            "filename": os.path.basename(file_path),
            "path": os.path.abspath(file_path),
            "size_bytes": stats.st_size,
            "size_mb": round(stats.st_size / (1024 * 1024), 2),
            "extension": os.path.splitext(file_path)[1].lower()
        }

    @staticmethod
    def ensure_directory_exists(file_path: str) -> bool:
        """Ensure directory exists for file path"""
        try:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            return True
        except Exception:
            return False
