"""
Görüntü filtrelerinin doğru çalıştığını test eden birim testleri

Bu dosyada:
- Filtrelerin Image döndürmesi
- Görüntü boyutlarını bozmaması
- Renk modlarının doğru olması
kontrol edilir.
"""

import pytest
from PIL import Image

# Filtre sınıfları import edilir
from filters.blur import BlurFilter
from filters.grayscale import GrayscaleFilter


@pytest.fixture
def sample_image():
    """
    Testlerde kullanılacak örnek görüntü.

    Her test için yeniden oluşturulur.
    """
    return Image.new("RGB", (64, 64), color="red")


def test_blur_filter_keeps_image_size(sample_image):
    """
    Blur filtresi uygulandığında
    görüntü boyutlarının değişmediğini test eder.
    """

    blur_filter = BlurFilter()
    output_image = blur_filter.process(sample_image)

    # Çıktının Image olduğu kontrol edilir
    assert isinstance(output_image, Image.Image)

    # Boyutların korunduğu kontrol edilir
    assert output_image.size == sample_image.size


def test_grayscale_filter_changes_mode(sample_image):
    """
    Grayscale filtresi uygulandığında
    görüntünün gri tonlamaya (L) dönüştüğünü test eder.
    """

    grayscale_filter = GrayscaleFilter()
    output_image = grayscale_filter.process(sample_image)

    # Çıktının Image olduğu kontrol edilir
    assert isinstance(output_image, Image.Image)

    # Gri seviye görüntü modu kontrol edilir
    assert output_image.mode == "L"
