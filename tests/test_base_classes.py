"""
Base sınıfların doğru çalıştığını test eden birim testleri

Bu dosyada:
- Soyut (base) filtre sınıfının
- process metodunun doğru şekilde çağrılabildiği
kontrol edilir.
"""

import pytest
from PIL import Image

# Projedeki base filtre sınıfı import edilir
from filters.base import BaseFilter


class DummyFilter(BaseFilter):
    """
    Test amaçlı sahte (dummy) filtre sınıfı.

    Gerçek bir filtre gibi davranır fakat
    görüntü üzerinde herhangi bir işlem yapmaz.
    """
    name = "dummy_filter"

    def process(self, image):
        # Gelen görüntüyü aynen geri döndürür
        return image


def test_base_filter_process_returns_image():
    """
    BaseFilter'dan türeyen bir sınıfın
    process metodunun Image döndürdüğünü test eder.
    """

    # 100x100 boyutunda test görüntüsü oluşturulur
    img = Image.new("RGB", (100, 100))

    # Dummy filtre nesnesi oluşturulur
    dummy_filter = DummyFilter()

    # Filtre uygulanır
    result = dummy_filter.process(img)

    # Çıktının Image nesnesi olduğu kontrol edilir
    assert isinstance(result, Image.Image)

    # Görüntünün değişmeden döndüğü kontrol edilir
    assert result == img
