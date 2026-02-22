# ======================== factories.py ========================
"""
Bu dosya, Factory Design Pattern kullanılarak
filtre ve enhancement nesnelerinin oluşturulmasını sağlar.

Amaç:
- Nesne oluşturma mantığını merkezi bir yerde toplamak
- GUI katmanını somut sınıflardan bağımsız hale getirmek
- Yeni filtre / enhancement eklemeyi kolaylaştırmak
"""

from filters import (
    BlurFilter,
    GrayscaleFilter,
    SepiaFilter,
    InvertFilter,
    SharpenFilter,
)

from enhancements import (
    BrightnessEnhancement,
    ContrastEnhancement,
    ColorEnhancement,
    SharpnessEnhancement,
)

from exceptions import FilterError, EnhancementError
from config import AppConfig


class FilterFactory:
    """
    Filtre nesnelerini oluşturan factory sınıfı.
    """

    def __init__(self):
        """
        Filtre isimleri ile filtre sınıfları arasındaki eşleştirme
        dictionary yapısı ile tutulur.

        Bu sayede:
        - if/else karmaşası önlenir
        - Yeni filtre eklemek sadece bu dictionary'e ekleme ile mümkündür
        """
        self.filters = {
            "blur": BlurFilter,
            "grayscale": GrayscaleFilter,
            "sepia": SepiaFilter,
            "invert": InvertFilter,
            "sharpen": SharpenFilter,
        }

    def create_filter(self, filter_name: str):
        """
        Verilen isme göre ilgili filtre nesnesini oluşturur.
        """
        try:
            filter_class = self.filters[filter_name.lower()]
            return filter_class()
        except KeyError:
            raise FilterError(f"Unknown filter: {filter_name}")

    def get_available_filters(self):
        """
        GUI tarafında gösterilmek üzere mevcut filtre isimlerini döner.
        """
        return list(self.filters.keys())


class EnhancementFactory:
    """
    Enhancement nesnelerini oluşturan factory sınıfı.
    """

    def __init__(self):
        """
        Enhancement'lar parametreli olduğu için,
        dictionary içinde lambda fonksiyonları kullanılmıştır.
        """
        self.enhancements = {
            "brightness_up": lambda: BrightnessEnhancement(
                AppConfig.BRIGHTNESS_INCREASE_FACTOR
            ),
            "brightness_down": lambda: BrightnessEnhancement(
                AppConfig.BRIGHTNESS_DECREASE_FACTOR
            ),
            "contrast_up": lambda: ContrastEnhancement(
                AppConfig.CONTRAST_INCREASE_FACTOR
            ),
            "contrast_down": lambda: ContrastEnhancement(
                AppConfig.CONTRAST_DECREASE_FACTOR
            ),
            "color_up": lambda: ColorEnhancement(
                AppConfig.COLOR_INCREASE_FACTOR
            ),
            "color_down": lambda: ColorEnhancement(
                AppConfig.COLOR_DECREASE_FACTOR
            ),
            "sharpness_up": lambda: SharpnessEnhancement(
                AppConfig.SHARPNESS_INCREASE_FACTOR
            ),
            "sharpness_down": lambda: SharpnessEnhancement(
                AppConfig.SHARPNESS_DECREASE_FACTOR
            ),
        }

    def create_enhancement(self, enhancement_name: str):
        """
        Verilen isme göre enhancement nesnesi oluşturur.
        """
        try:
            return self.enhancements[enhancement_name.lower()]()
        except KeyError:
            raise EnhancementError(
                f"Unknown enhancement: {enhancement_name}"
            )

    def get_available_enhancements(self):
        """
        GUI tarafında gösterilmek üzere enhancement isimlerini döner.
        """
        return list(self.enhancements.keys())
