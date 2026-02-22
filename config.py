# ======================== config.py ========================
"""
Uygulama genelinde kullanılan tüm sabit (configuration) değerleri içerir.

Bu dosyanın ayrı tutulma amacı:
- Magic number kullanımını önlemek
- GUI, filtre ve enhancement ayarlarını merkezi bir noktadan yönetmek
- Uygulamanın kolayca yapılandırılabilir olmasını sağlamak
"""


class AppConfig:
    """
    Uygulama yapılandırma sınıfı.

    Tüm değerler class-level tanımlanmıştır çünkü:
    - Değişmez (immutable) olmaları beklenir
    - Nesne oluşturmaya gerek yoktur
    """

    # ===================== Window / GUI Ayarları =====================
    WINDOW_TITLE = "OOP Image Processing Application"
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    WINDOW_BG = "#f0f0f0"

    # ===================== Canvas Ayarları =====================
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 400
    CANVAS_BG = "white"
    CANVAS_BORDER = 2

    # ===================== Görüntü Gösterim Ayarları =====================
    # Büyük resimlerin GUI dışına taşmaması için maksimum boyutlar
    MAX_DISPLAY_WIDTH = 480
    MAX_DISPLAY_HEIGHT = 380
    DEFAULT_IMAGE_FORMAT = "PNG"

    # ===================== Filtre Parametreleri =====================
    # Bu değerler filtre sınıfları tarafından kullanılır
    GAUSSIAN_BLUR_RADIUS = 2
    MEDIAN_FILTER_KERNEL = 5
    SOLARIZE_THRESHOLD = 128

    # ===================== Enhancement Parametreleri =====================
    # Factor değerleri ImageEnhancement sınıflarında kullanılır
    BRIGHTNESS_INCREASE_FACTOR = 1.3
    BRIGHTNESS_DECREASE_FACTOR = 0.7

    CONTRAST_INCREASE_FACTOR = 1.3
    CONTRAST_DECREASE_FACTOR = 0.7

    COLOR_INCREASE_FACTOR = 1.3
    COLOR_DECREASE_FACTOR = 0.7

    SHARPNESS_INCREASE_FACTOR = 1.5
    SHARPNESS_DECREASE_FACTOR = 0.5

    # ===================== Dosya Diyalog Ayarları =====================
    SUPPORTED_FORMATS = [
        ("All Image Formats", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
        ("JPEG", "*.jpg *.jpeg"),
        ("PNG", "*.png"),
        ("BMP", "*.bmp"),
        ("TIFF", "*.tiff"),
        ("GIF", "*.gif"),
    ]

    SAVE_FORMATS = [
        ("PNG", "*.png"),
        ("JPEG", "*.jpg"),
        ("BMP", "*.bmp"),
        ("TIFF", "*.tiff"),
    ]

    # ===================== UI Metinleri =====================
    TITLE_TEXT = "OOP Image Processing Application"
    ORIGINAL_LABEL = "Original Image"
    PROCESSED_LABEL = "Processed Image"
    QUICK_FILTERS_LABEL = "Quick Filters"

    # ===================== Durum / Bilgi Mesajları =====================
    STATUS_READY = "Ready - Select an image..."
    STATUS_NO_FILE = "No file selected"
    STATUS_PROCESSING = "Processing: {}..."
    STATUS_IMAGE_LOADED = "Image loaded: {} ({}x{})"
    STATUS_FILTER_APPLIED = "{} filter applied"
    STATUS_IMAGE_SAVED = "Image saved: {}"
    STATUS_IMAGE_RESET = "Image reset"
    STATUS_ERROR = "Error: {}"
