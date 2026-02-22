# ======================== gui_components.py ========================
"""
Bu dosya, GUI tarafında kullanılan yardımcı bileşen sınıflarını içerir.

Amaç:
- main_app.py içindeki kodu sadeleştirmek
- Menü, canvas ve status bar gibi bileşenleri ayrı sorumluluklara ayırmak
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from config import AppConfig


class MenuManager:
    """
    Uygulama menü çubuğunu yöneten sınıf.
    """

    def __init__(self, root, callback_handler):
        self.root = root
        self.callback = callback_handler
        self.menubar = tk.Menu(root)

    def create_menu(self):
        """
        Menü çubuğunu oluşturur ve root pencereye bağlar.
        """
        self._create_file_menu()
        self._create_filter_menu()
        self._create_adjustment_menu()
        self._create_help_menu()

        self.root.config(menu=self.menubar)
        return self.menubar

    def _create_file_menu(self):
        file_menu = tk.Menu(self.menubar, tearoff=0)

        file_menu.add_command(
            label="Open Image",
            command=self.callback.open_image
        )
        file_menu.add_command(
            label="Save Image",
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

        for filter_name in self.callback.get_filters():
            filter_menu.add_command(
                label=filter_name.capitalize(),
                command=lambda f=filter_name: self.callback.apply_filter(f)
            )

        self.menubar.add_cascade(label="Filters", menu=filter_menu)

    def _create_adjustment_menu(self):
        adjustment_menu = tk.Menu(self.menubar, tearoff=0)

        for enh_name in self.callback.get_enhancements():
            adjustment_menu.add_command(
                label=enh_name.replace("_", " ").title(),
                command=lambda e=enh_name: self.callback.apply_enhancement(e)
            )

        self.menubar.add_cascade(label="Adjustments", menu=adjustment_menu)

    def _create_help_menu(self):
        help_menu = tk.Menu(self.menubar, tearoff=0)

        help_menu.add_command(
            label="About",
            command=lambda: tk.messagebox.showinfo(
                "About",
                "OOP Image Processing Application\n"
                "Developed for OOP course"
            )
        )

        self.menubar.add_cascade(label="Help", menu=help_menu)


class ImageDisplay:
    """
    Canvas üzerinde görüntü gösterimini yöneten sınıf.
    """

    def __init__(self, canvas, title="Image"):
        self.canvas = canvas
        self.title = title
        self.photo_image = None

    def display_image(self, image):
        """
        Verilen PIL.Image nesnesini canvas üzerinde gösterir.
        """
        if image is None:
            return

        resized = self._resize_for_display(
            image,
            AppConfig.MAX_DISPLAY_WIDTH,
            AppConfig.MAX_DISPLAY_HEIGHT
        )

        self.photo_image = ImageTk.PhotoImage(resized)

        self.canvas.delete("all")
        self.canvas.create_image(
            AppConfig.CANVAS_WIDTH // 2,
            AppConfig.CANVAS_HEIGHT // 2,
            image=self.photo_image,
            anchor="center"
        )

    def _resize_for_display(self, image, max_width, max_height):
        """
        Görüntüyü canvas boyutlarına sığacak şekilde ölçekler.
        """
        width, height = image.size

        ratio = min(
            max_width / width,
            max_height / height,
            1.0
        )

        if ratio < 1.0:
            new_size = (
                int(width * ratio),
                int(height * ratio)
            )
            return image.resize(
                new_size,
                Image.Resampling.LANCZOS
            )

        return image

    def clear_display(self):
        """
        Canvas içeriğini temizler.
        """
        self.canvas.delete("all")
        self.photo_image = None


class StatusManager:
    """
    Alt durum çubuğunu yöneten sınıf.
    """

    def __init__(self, status_var: tk.StringVar):
        self.status_var = status_var

    def set_status(self, message: str):
        self.status_var.set(message)

    def set_ready(self):
        self.set_status(AppConfig.STATUS_READY)

    def set_processing(self, operation: str):
        self.set_status(
            AppConfig.STATUS_PROCESSING.format(operation)
        )

    def set_error(self, error: str):
        self.set_status(
            AppConfig.STATUS_ERROR.format(error)
        )
