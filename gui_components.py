# ======================== gui_components.py ========================
"""
GUI component classes

Bu dosya:
- Menü yapısını
- Canvas üzerinde görüntü gösterimini
- Alt durum çubuğunu
yöneten yardımcı sınıfları içerir.
"""

import tkinter as tk
from PIL import Image, ImageTk


class MenuManager:
    """
    Uygulamanın üst menü çubuğunu yöneten sınıf.
    Menü aksiyonları callback_handler üzerinden main_app'e iletilir.
    """

    def __init__(self, root, callback_handler):
        self.root = root
        self.callback = callback_handler
        self.menubar = tk.Menu(self.root)

    def create_menu(self):
        """Ana menü çubuğunu oluşturur"""
        self.root.config(menu=self.menubar)

        self._create_file_menu()
        self._create_filter_menu()
        self._create_adjustment_menu()
        self._create_help_menu()

        return self.menubar

    def _create_file_menu(self):
        file_menu = tk.Menu(self.menubar, tearoff=0)

        file_menu.add_command(
            label="Open Image",
            command=self.callback.browse_image
        )
        file_menu.add_command(
            label="Save",
            command=self.callback.save_image
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.root.quit
        )

        self.menubar.add_cascade(label="File", menu=file_menu)

    def _create_filter_menu(self):
        filter_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Filters", menu=filter_menu)

        # Basic Filters
        basic = tk.Menu(filter_menu, tearoff=0)
        filter_menu.add_cascade(label="Basic Filters", menu=basic)
        basic.add_command(label="Blur", command=lambda: self.callback.apply_filter("blur"))
        basic.add_command(label="Sharpen", command=lambda: self.callback.apply_filter("sharpen"))
        basic.add_command(label="Edge Detect", command=lambda: self.callback.apply_filter("edge_detect"))
        basic.add_command(label="Emboss", command=lambda: self.callback.apply_filter("emboss"))

        # Color Filters
        color = tk.Menu(filter_menu, tearoff=0)
        filter_menu.add_cascade(label="Color Filters", menu=color)
        color.add_command(label="Grayscale", command=lambda: self.callback.apply_filter("grayscale"))
        color.add_command(label="Sepia", command=lambda: self.callback.apply_filter("sepia"))
        color.add_command(label="Invert", command=lambda: self.callback.apply_filter("invert"))
        color.add_command(label="Solarize", command=lambda: self.callback.apply_filter("solarize"))

        # Advanced Filters
        advanced = tk.Menu(filter_menu, tearoff=0)
        filter_menu.add_cascade(label="Advanced Filters", menu=advanced)
        advanced.add_command(label="Gaussian Blur", command=lambda: self.callback.apply_filter("gaussian_blur"))
        advanced.add_command(label="Motion Blur", command=lambda: self.callback.apply_filter("motion_blur"))
        advanced.add_command(label="Canny Edge", command=lambda: self.callback.apply_filter("canny_edge"))
        advanced.add_command(label="Median Filter", command=lambda: self.callback.apply_filter("median_filter"))

    def _create_adjustment_menu(self):
        adjust = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Adjustments", menu=adjust)

        adjust.add_command(
            label="Increase Brightness",
            command=lambda: self.callback.apply_enhancement("brightness_up")
        )
        adjust.add_command(
            label="Decrease Brightness",
            command=lambda: self.callback.apply_enhancement("brightness_down")
        )
        adjust.add_command(
            label="Increase Contrast",
            command=lambda: self.callback.apply_enhancement("contrast_up")
        )
        adjust.add_command(
            label="Decrease Contrast",
            command=lambda: self.callback.apply_enhancement("contrast_down")
        )

    def _create_help_menu(self):
        help_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=help_menu)

        help_menu.add_command(
            label="About",
            command=self.callback.show_about
        )


class ImageDisplay:
    """
    Canvas üzerinde görüntü gösterimini yöneten sınıf.
    Resize ve merkezleme işlemlerini kapsüller.
    """

    def __init__(self, canvas, title="Image"):
        self.canvas = canvas
        self.title = title
        self.photo_image = None  # GC'yi önlemek için referans tutulur

    def display_image(self, image):
        """PIL.Image nesnesini canvas üzerinde gösterir"""
        if image is None:
            return

        canvas_width = max(self.canvas.winfo_width(), 500)
        canvas_height = max(self.canvas.winfo_height(), 400)

        image = self._resize_for_display(
            image,
            canvas_width - 20,
            canvas_height - 20
        )

        self.photo_image = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=self.photo_image,
            anchor=tk.CENTER
        )

    def _resize_for_display(self, image, max_width, max_height):
        """Canvas boyutlarına göre orantılı resize yapar"""
        w, h = image.size
        ratio = min(max_width / w, max_height / h, 1.0)

        if ratio < 1.0:
            return image.resize(
                (int(w * ratio), int(h * ratio)),
                Image.Resampling.LANCZOS
            )
        return image

    def clear_display(self):
        """Canvas içeriğini temizler"""
        self.canvas.delete("all")
        self.photo_image = None


class StatusManager:
    """
    Alt durum çubuğunu yöneten sınıf.
    Kullanıcıya işlem durumunu bildirir.
    """

    def __init__(self, status_var):
        self.status_var = status_var

    def set_status(self, message):
        self.status_var.set(message)

    def set_ready(self):
        self.set_status("Ready - Select an image...")

    def set_processing(self, operation):
        self.set_status(f"Processing: {operation}...")

    def set_error(self, error):
        self.set_status(f"Error: {error}")
