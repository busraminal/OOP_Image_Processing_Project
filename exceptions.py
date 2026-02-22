# ======================== exceptions.py ========================
"""
Bu dosya, uygulama genelinde kullanılan özel (custom) exception sınıflarını içerir.

Amaç:
- Hataları anlamlı şekilde ayırmak
- try-except bloklarında spesifik hata yakalayabilmek
- GUI katmanında kullanıcıya daha açıklayıcı mesajlar göstermek
"""


class ImageProcessingError(Exception):
    """
    Görüntü işleme sırasında oluşabilecek tüm hatalar için
    temel (base) exception sınıfı.

    Diğer tüm özel hatalar bu sınıftan türetilir.
    """
    pass


class ImageLoadError(ImageProcessingError):
    """
    Görüntü dosyası yüklenemediğinde fırlatılır.

    Örnek nedenler:
    - Dosya bulunamadı
    - Desteklenmeyen format
    - Bozuk dosya
    """
    pass


class ImageSaveError(ImageProcessingError):
    """
    Görüntü kaydedilirken hata oluştuğunda fırlatılır.
    """
    pass


class FilterError(ImageProcessingError):
    """
    Bir filtre uygulanırken hata oluştuğunda fırlatılır.

    Örnek:
    - Filtre parametresi hatalı
    - process() sırasında beklenmeyen durum
    """
    pass


class EnhancementError(ImageProcessingError):
    """
    Enhancement (parlaklık, kontrast vb.) işlemleri sırasında
    oluşan hatalar için kullanılır.
    """
    pass


class InvalidImageError(ImageProcessingError):
    """
    Geçersiz veya None olan görüntü üzerinde işlem
    yapılmaya çalışıldığında fırlatılır.
    """
    pass


class UnsupportedFormatError(ImageProcessingError):
    """
    Desteklenmeyen bir görüntü formatı seçildiğinde fırlatılır.
    """
    pass
