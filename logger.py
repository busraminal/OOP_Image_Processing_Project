# ======================== logger.py ========================
"""
Logging functionality

Uygulama genelinde:
- bilgi
- hata
- uyarı
- debug
loglarını merkezi olarak yönetir.
"""

import logging
import os


class AppLogger:
    """Application logger"""

    def __init__(self, log_file: str = "image_processing.log"):
        self.log_file = log_file
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Setup logger configuration"""
        logger = logging.getLogger("ImageProcessingApp")
        logger.setLevel(logging.DEBUG)

        # Aynı logger tekrar oluşturulmasın diye kontrol
        if logger.handlers:
            return logger

        # Log klasörü yoksa oluştur
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Dosya handler
        file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # Konsol handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Ortak format
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)

    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)

    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(message)

    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(message)
