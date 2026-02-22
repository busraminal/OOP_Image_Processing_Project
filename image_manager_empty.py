# ======================== image_manager.py ========================
"""
Image management and processing operations

Bu sınıf:
- Görüntü yükleme
- Filtre / enhancement uygulama
- Undo (geri alma)
- Kaydetme
işlemlerinden sorumludur.
"""

from PIL import Image
import os


class ImageManager:
    """Manages image loading, processing, and saving"""

    def __init__(self):
        # Orijinal (hiç değişmemiş) görüntü
        self.original_image = None

        # Üzerinde işlem yapılmış güncel görüntü
        self.processed_image = None

        # Yüklenen dosyanın yolu
        self.image_path = None

        # Geri alma (undo) için görüntü geçmişi
        self.image_history = []

    def load_image(self, file_path):
        """Load an image from file"""
        try:
            image = Image.open(file_path)

            self.image_path = file_path
            self.original_image = image.copy()
            self.processed_image = image.copy()

            # Undo mekanizması için ilk state
            self.image_history = [self.processed_image.copy()]

            return True

        except Exception as e:
            raise RuntimeError(f"Image loading failed: {e}")

    def apply_processor(self, processor):
        """Apply an image processor (Filter or Enhancement)"""
        if self.processed_image is None:
            raise RuntimeError("No image loaded")

        try:
            # İşlem her zaman son durum üzerinden uygulanır
            result = processor.process(self.processed_image)

            self.processed_image = result
            self.image_history.append(result.copy())

            return True

        except Exception as e:
            raise RuntimeError(f"Image processing failed: {e}")

    def reset_image(self):
        """Reset image to original state"""
        if self.original_image is None:
            return False

        self.processed_image = self.original_image.copy()
        self.image_history = [self.processed_image.copy()]

        return True

    def save_image(self, file_path):
        """Save the processed image"""
        if self.processed_image is None:
            raise RuntimeError("No processed image to save")

        try:
            self.processed_image.save(file_path)
            return True

        except Exception as e:
            raise RuntimeError(f"Image saving failed: {e}")

    def get_image_info(self):
        """Return basic image metadata"""
        if self.original_image is None:
            return None

        return {
            "filename": os.path.basename(self.image_path),
            "size": self.original_image.size,
            "mode": self.original_image.mode,
            "format": self.original_image.format
        }

    def undo(self):
        """Undo last operation"""
        if len(self.image_history) <= 1:
            return False

        # Son işlemi sil
        self.image_history.pop()

        # Bir önceki duruma dön
        self.processed_image = self.image_history[-1].copy()

        return True
