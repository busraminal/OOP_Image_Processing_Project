# ======================== enhancements.py ========================
"""
Bu dosya, görüntü iyileştirme (enhancement) işlemlerini içerir.

Enhancement sınıfları:
- ImageEnhancement soyut sınıfından türetilir
- Ortak process() arayüzünü kullanır
- Factor parametresi ile esnek şekilde ayarlanabilir
"""

from PIL import ImageEnhance
from base_classes import ImageEnhancement


class BrightnessEnhancement(ImageEnhancement):
    """
    Görüntü parlaklığını ayarlayan sınıf.
    """

    def __init__(self, factor: float = 1.3):
        """
        factor:
            1.0  -> Orijinal parlaklık
            >1.0 -> Daha parlak
            <1.0 -> Daha karanlık
        """
        super().__init__("Brightness", factor)

    def process(self, image):
        """
        PIL ImageEnhance.Brightness kullanılarak parlaklık ayarlanır.
        """
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(self.factor)


class ContrastEnhancement(ImageEnhancement):
    """
    Görüntü kontrastını ayarlayan sınıf.
    """

    def __init__(self, factor: float = 1.3):
        super().__init__("Contrast", factor)

    def process(self, image):
        """
        PIL ImageEnhance.Contrast kullanılarak kontrast ayarlanır.
        """
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(self.factor)


class ColorEnhancement(ImageEnhancement):
    """
    Görüntünün renk doygunluğunu (saturation) ayarlayan sınıf.
    """

    def __init__(self, factor: float = 1.3):
        super().__init__("Color", factor)

    def process(self, image):
        """
        PIL ImageEnhance.Color kullanılarak renk doygunluğu ayarlanır.
        """
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(self.factor)


class SharpnessEnhancement(ImageEnhancement):
    """
    Görüntü keskinliğini (sharpness) ayarlayan sınıf.
    """

    def __init__(self, factor: float = 1.3):
        super().__init__("Sharpness", factor)

    def process(self, image):
        """
        PIL ImageEnhance.Sharpness kullanılarak keskinlik ayarlanır.
        """
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(self.factor)
