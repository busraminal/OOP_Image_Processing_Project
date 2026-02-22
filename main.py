# ======================== main.py ========================
"""
Application entry point

Bu dosya uygulamanın başlangıç (entry point) noktasıdır.
GUI oluşturma ve ana döngüyü başlatma sorumluluğunu taşır.
Filtreleri uygulamak için butonlar eklenmiştir.
"""

import tkinter as tk
from main_app import ImageProcessingApplication
from filters import EdgeDetectionFilter, CannyEdgeFilter, SepiaFilter, InvertFilter
from PIL import Image, ImageTk


def main():
    # Tkinter root nesnesi oluştur
    root = tk.Tk()
    root.title("OOP Image Processing Project")

    # Ana uygulama başlat
    app = ImageProcessingApplication(root)

    # Filtre sınıflarını örnekle
    edge_filter = EdgeDetectionFilter()
    canny_filter = CannyEdgeFilter()
    sepia_filter = SepiaFilter()
    invert_filter = InvertFilter()

    # Filtre callback fonksiyonları
    def apply_edge():
        if hasattr(app, "image") and app.image is not None:
            result = edge_filter.process(app.image)
            result.show()

    def apply_canny():
        if hasattr(app, "image") and app.image is not None:
            result = canny_filter.process(app.image)
            result.show()

    def apply_sepia():
        if hasattr(app, "image") and app.image is not None:
            result = sepia_filter.process(app.image)
            result.show()

    def apply_invert():
        if hasattr(app, "image") and app.image is not None:
            result = invert_filter.process(app.image)
            result.show()

    # Filtre butonlarını GUI'ye ekle

    tk.Button(root, text="Edge Detect", command=apply_edge).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(root, text="Canny Edge", command=apply_canny).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Sepia", command=apply_sepia).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(root, text="Invert", command=apply_invert).grid(row=1, column=1, padx=5, pady=5)


    # Tkinter mainloop
    root.mainloop()


if __name__ == "__main__":
    main()
