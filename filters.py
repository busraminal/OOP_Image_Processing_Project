# ======================== filters.py ========================
"""
Bu dosya, projede kullanılan somut (concrete) filtre implementasyonlarını içerir.

Her filtre:
- Filter soyut sınıfından türetilir
- process(image) metodunu implemente eder
- GUI ve ImageManager tarafından polimorfik olarak kullanılır
"""

from PIL import Image, ImageFilter, ImageOps
import cv2
import numpy as np

from base_classes import Filter
from config import AppConfig
from exceptions import FilterError


class BlurFilter(Filter):
    """Basit bulanıklaştırma filtresi"""

    def __init__(self):
        super().__init__("Blur")

    def process(self, image):
        return image.filter(ImageFilter.BLUR)


class SharpenFilter(Filter):
    """Görüntü keskinleştirme filtresi"""

    def __init__(self):
        super().__init__("Sharpen")

    def process(self, image):
        return image.filter(ImageFilter.SHARPEN)


class EdgeDetectionFilter(Filter):
    """Kenar tespiti filtresi"""

    def __init__(self):
        super().__init__("Edge Detection")

    def process(self, image):
        return image.filter(ImageFilter.FIND_EDGES)


class EmbossFilter(Filter):
    """Kabartma (emboss) efekti"""

    def __init__(self):
        super().__init__("Emboss")

    def process(self, image):
        return image.filter(ImageFilter.EMBOSS)


class GrayscaleFilter(Filter):
    """Görüntüyü gri tonlamaya çevirir"""

    def __init__(self):
        super().__init__("Grayscale")

    def process(self, image):
        # PIL ImageOps.grayscale L moduna çevirir,
        # GUI uyumu için tekrar RGB'ye dönülür
        gray = ImageOps.grayscale(image)
        return gray.convert("RGB")


class SepiaFilter(Filter):
    """Sepya (eski fotoğraf) efekti"""

    def __init__(self):
        super().__init__("Sepia")

    def process(self, image):
        try:
            pixels = np.array(image)

            sepia_matrix = np.array([
                [0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131],
            ])

            sepia_img = pixels.dot(sepia_matrix.T)
            sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

            return Image.fromarray(sepia_img)
        except Exception as e:
            raise FilterError(f"Sepia filter failed: {e}")


class InvertFilter(Filter):
    """Renkleri tersine çevirir"""

    def __init__(self):
        super().__init__("Invert")

    def process(self, image):
        return ImageOps.invert(image)


class SolarizeFilter(Filter):
    """Solarizasyon efekti"""

    def __init__(self):
        super().__init__("Solarize")

    def process(self, image):
        return ImageOps.solarize(
            image, threshold=AppConfig.SOLARIZE_THRESHOLD
        )


class GaussianBlurFilter(Filter):
    """Gaussian blur filtresi"""

    def __init__(self, radius=AppConfig.GAUSSIAN_BLUR_RADIUS):
        super().__init__("Gaussian Blur")
        self.radius = radius

    def process(self, image):
        return image.filter(ImageFilter.GaussianBlur(self.radius))


class CannyEdgeFilter(Filter):
    """OpenCV kullanarak Canny kenar algılama"""

    def __init__(self):
        super().__init__("Canny Edge")

    def process(self, image):
        # PIL → NumPy
        img_np = np.array(image)

        # RGB → Grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        # Canny edge detection
        edges = cv2.Canny(gray, 100, 200)

        # Tek kanallı görüntüyü RGB'ye çevir
        edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

        return Image.fromarray(edges_rgb)


class MedianFilter(Filter):
    """Gürültü azaltmak için median filtre"""

    def __init__(self, kernel_size=AppConfig.MEDIAN_FILTER_KERNEL):
        super().__init__("Median Filter")
        self.kernel_size = kernel_size

    def process(self, image):
        img_np = np.array(image)
        filtered = cv2.medianBlur(img_np, self.kernel_size)
        return Image.fromarray(filtered)


class MotionBlurFilter(Filter):
    """Hareket bulanıklığı efekti"""

    def __init__(self):
        super().__init__("Motion Blur")

    def process(self, image):
        # 9x9 hareket bulanıklığı çekirdeği
        kernel_size = 9
        kernel = np.zeros((kernel_size, kernel_size))
        kernel[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        kernel = kernel / kernel_size

        return image.filter(
            ImageFilter.Kernel(
                size=(kernel_size, kernel_size),
                kernel=kernel.flatten(),
                scale=1
            )
        )
