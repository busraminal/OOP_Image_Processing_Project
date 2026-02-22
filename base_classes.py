# ======================== base_classes.py ========================
"""
Bu dosya, projede kullanılan tüm görüntü işleme operasyonları için
temel soyut sınıfları içerir.

Amaç:
- Ortak bir arayüz (interface) tanımlamak
- Polimorfizmi mümkün kılmak
- Filtre ve iyileştirme sınıflarını standartlaştırmak
"""

from abc import ABC, abstractmethod


class ImageProcessor(ABC):
    """
    Tüm görüntü işleme sınıflarının türediği soyut sınıf.

    Bu sınıf sayesinde:
    - Her işlemci aynı process() metoduna sahip olur
    - GUI ve ImageManager, hangi sınıfla çalıştığını bilmeden işlem yapabilir
    """

    @abstractmethod
    def process(self, image):
        """
        Alt sınıflar tarafından implemente edilmesi zorunlu olan metot.

        Parametre:
            image (PIL.Image): İşlenecek görüntü

        Dönüş:
            PIL.Image: İşlenmiş görüntü
        """
        pass


class Filter(ImageProcessor):
    """
    Tüm filtre sınıfları için temel sınıf.

    Blur, Sharpen, Grayscale gibi filtreler bu sınıftan türetilir.
    """

    def __init__(self, name: str):
        """
        Filtrenin adını tutar.

        name parametresi, GUI tarafında filtre ismini göstermek
        ve loglama yapmak için kullanılır.
        """
        self.name = name

    def __str__(self):
        """
        Filtrenin okunabilir string temsili.

        Örnek çıktı:
            'Blur Filter'
        """
        return f"{self.name} Filter"


class ImageEnhancement(ImageProcessor):
    """
    Parlaklık, kontrast gibi görüntü iyileştirme işlemleri için
    temel sınıf.
    """

    def __init__(self, name: str, factor: float):
        """
        Parametreler:
            name (str): İyileştirmenin adı
            factor (float): İyileştirme katsayısı
                            (örn: 0.5 düşük, 1.0 normal, 1.5 yüksek)
        """
        self.name = name
        self.factor = factor

    def __str__(self):
        """
        İyileştirmenin string temsili.

        Örnek çıktı:
            'Brightness Enhancement (factor=1.2)'
        """
        return f"{self.name} Enhancement (factor={self.factor})"
