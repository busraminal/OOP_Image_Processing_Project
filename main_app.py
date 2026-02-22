"""
Main application class

Uygulamanın:
- GUI akışını
- kullanıcı etkileşimlerini
- ImageManager + Factory entegrasyonunu
yöneten ana sınıf.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

from image_manager import ImageManager
from factories import FilterFactory, EnhancementFactory
from gui_components import MenuManager, ImageDisplay, StatusManager


class ImageProcessingApplication:
    """Main application class"""

    def __init__(self, root):
        self.root = root
        self._configure_root()

        # Core logic
        self.image_manager = ImageManager()
        self.filter_factory = FilterFactory()
        self.enhancement_factory = EnhancementFactory()

        # GUI helpers
        self.original_display = None
        self.processed_display = None
        self.status_manager = None

        self._setup_styles()
        self._setup_gui()
        self._setup_menu()
        self._setup_keyboard_shortcuts()

    # ------------------------------------------------------------------
    # Root & Style
    # ------------------------------------------------------------------
    def _configure_root(self):
        self.root.title("OOP Image Processing Application")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")

    def _setup_styles(self):
        """Setup ttk styles"""
        style = ttk.Style()
        style.theme_use("clam")

    # ------------------------------------------------------------------
    # GUI Layout
    # ------------------------------------------------------------------
    def _setup_gui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        self._setup_title(main_frame)
        self._setup_image_panels(main_frame)
        self._setup_control_panel(main_frame)
        self._setup_status_bar(main_frame)

    def _setup_title(self, parent):
        title = ttk.Label(
            parent,
            text="OOP Image Processing Application",
            font=("Helvetica", 16, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    def _setup_image_panels(self, parent):
        left_panel = ttk.LabelFrame(parent, text="Original Image", padding="10")
        left_panel.grid(row=1, column=0, padx=(0, 10), sticky="nsew")

        right_panel = ttk.LabelFrame(parent, text="Processed Image", padding="10")
        right_panel.grid(row=1, column=1, sticky="nsew")

        self._setup_file_controls(left_panel)
        self._setup_canvases(left_panel, right_panel)

    def _setup_file_controls(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(frame, text="Select Image", command=self.browse_image).pack(side=tk.LEFT)

        self.file_path_var = tk.StringVar(value="No file selected")
        ttk.Label(frame, textvariable=self.file_path_var, font=("Helvetica", 9)).pack(
            side=tk.LEFT, padx=(10, 0)
        )

    def _setup_canvases(self, left, right):
        original_canvas = tk.Canvas(left, width=500, height=400, bg="white", relief=tk.SUNKEN, borderwidth=2)
        original_canvas.pack(expand=True, fill=tk.BOTH)
        self.original_display = ImageDisplay(original_canvas, "Original")

        processed_canvas = tk.Canvas(right, width=500, height=400, bg="white", relief=tk.SUNKEN, borderwidth=2)
        processed_canvas.pack(expand=True, fill=tk.BOTH)
        self.processed_display = ImageDisplay(processed_canvas, "Processed")

    # ------------------------------------------------------------------
    # Controls
    # ------------------------------------------------------------------
    def _setup_control_panel(self, parent):
        panel = ttk.Frame(parent)
        panel.grid(row=2, column=0, columnspan=2, pady=(20, 0), sticky="ew")

        quick_filters = ttk.LabelFrame(panel, text="Quick Filters", padding="10")
        quick_filters.pack(fill=tk.X, pady=(0, 10))

        filters = [
            ("Blur", "blur"),
            ("Sharpen", "sharpen"),
            ("Grayscale", "grayscale"),
            ("Edge Detect", "edge_detect"),
            ("Sepia", "sepia"),
            ("Invert", "invert"),
        ]

        for i, (label, name) in enumerate(filters):
            ttk.Button(
                quick_filters,
                text=label,
                width=12,
                command=lambda f=name: self.apply_filter(f)
            ).grid(row=i // 3, column=i % 3, padx=5, pady=5)

        actions = ttk.Frame(panel)
        actions.pack(fill=tk.X)

        ttk.Button(actions, text="Reset", command=self.reset_image).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(actions, text="Save", command=self.save_image).pack(side=tk.LEFT)

    def _setup_status_bar(self, parent):
        self.status_var = tk.StringVar(value="Ready - Select an image...")
        ttk.Label(
            parent,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        self.status_manager = StatusManager(self.status_var)

    # ------------------------------------------------------------------
    # Menu & Shortcuts
    # ------------------------------------------------------------------
    def _setup_menu(self):
        MenuManager(self.root, self).create_menu()

    def _setup_keyboard_shortcuts(self):
        self.root.bind("<Control-o>", lambda _: self.browse_image())
        self.root.bind("<Control-s>", lambda _: self.save_image())
        self.root.bind("<Control-q>", lambda _: self.root.quit())

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("All Image Formats", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
            ],
        )

        if not file_path:
            return

        try:
            self.image_manager.load_image(file_path)

            self.file_path_var.set(f"Selected: {os.path.basename(file_path)}")
            self.original_display.display_image(self.image_manager.original_image)
            self.processed_display.display_image(self.image_manager.processed_image)

            info = self.image_manager.get_image_info()
            self.status_manager.set_status(
                f"Image loaded: {info['filename']} ({info['size'][0]}x{info['size'][1]})"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_manager.set_error(e)

    def apply_filter(self, filter_name):
        try:
            processor = self.filter_factory.create_filter(filter_name)
            self.status_manager.set_processing(processor.name)

            self.image_manager.apply_processor(processor)
            self.processed_display.display_image(self.image_manager.processed_image)

            self.status_manager.set_status(f"{processor.name} filter applied")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_manager.set_error(e)

    def apply_enhancement(self, enhancement_name):
        try:
            processor = self.enhancement_factory.create_enhancement(enhancement_name)
            self.status_manager.set_processing(processor.name)

            self.image_manager.apply_processor(processor)
            self.processed_display.display_image(self.image_manager.processed_image)

            self.status_manager.set_status(f"{processor.name} adjustment applied")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_manager.set_error(e)

    def reset_image(self):
        if self.image_manager.reset_image():
            self.processed_display.display_image(self.image_manager.processed_image)
            self.status_manager.set_status("Image reset")

    def save_image(self):
        if self.image_manager.processed_image is None:
            messagebox.showwarning("Warning", "No image to save!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"), ("TIFF", "*.tiff")],
        )

        if not file_path:
            return

        try:
            self.image_manager.save_image(file_path)
            messagebox.showinfo("Success", "Image saved successfully")
            self.status_manager.set_status(f"Image saved: {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_about(self):
        messagebox.showinfo(
            "About",
            "OOP Image Processing Application\n\n"
            "• Modular OOP architecture\n"
            "• Factory pattern\n"
            "• PIL & OpenCV based filters\n"
            "• Extensible design"
        )
