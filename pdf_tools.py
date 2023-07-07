import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfReader, PdfWriter
from tkinter import filedialog, simpledialog, messagebox
import os

root = TkinterDnD.Tk()

# Configuración de la ventana principal
root.title("Utilidades PDF")
root.geometry("600x600")

# Función para desbloquear archivos PDF
def unlock_pdf(file_paths):
    password = simpledialog.askstring("Contraseña", "Ingresa la contraseña para desbloquear los archivos PDF:")

    if password:
        for file_path in file_paths:
            input_pdf = PdfReader(file_path)
            output_pdf = PdfWriter()

            if input_pdf.is_encrypted:
                input_pdf.decrypt(password)

            for page in input_pdf.pages:
                output_pdf.add_page(page)

            output_file_path = file_path.replace(".pdf", "_unlocked.pdf")
            with open(output_file_path, "wb") as output_file:
                output_pdf.write(output_file)

        messagebox.showinfo("Completado", "Se han desbloqueado los archivos PDF correctamente.")

# Función para bloquear archivos PDF
def lock_pdf(file_paths):
    password = simpledialog.askstring("Contraseña", "Ingresa la contraseña para bloquear los archivos PDF:")

    if password:
        for file_path in file_paths:
            input_pdf = PdfReader(file_path)
            output_pdf = PdfWriter()

            for page in input_pdf.pages:
                output_pdf.add_page(page)

            output_file_path = file_path.replace(".pdf", "_locked.pdf")
            output_pdf.encrypt(password)
            with open(output_file_path, "wb") as output_file:
                output_pdf.write(output_file)

        messagebox.showinfo("Completado", "Se han bloqueado los archivos PDF correctamente.")

# Función para dividir archivos PDF
def split_pdf(file_paths):
    for file_path in file_paths:
        input_pdf = PdfReader(file_path)

        num_pages = len(input_pdf.pages)
        page_range = simpledialog.askstring("Dividir PDF", f"Ingrese el rango de páginas para dividir el archivo {file_path} (por ejemplo: 1-3,5):")

        if page_range:
            try:
                pages = []
                page_parts = page_range.split(",")
                for part in page_parts:
                    if "-" in part:
                        start, end = part.split("-")
                        start_page = int(start.strip()) - 1
                        end_page = int(end.strip())
                        pages.extend(input_pdf.pages[start_page:end_page])
                    else:
                        page = int(part.strip()) - 1
                        pages.append(input_pdf.pages[page])

                output_pdf = PdfWriter()
                for page in pages:
                    output_pdf.add_page(page)

                output_file_path = file_path.replace(".pdf", "_split.pdf")
                with open(output_file_path, "wb") as output_file:
                    output_pdf.write(output_file)

            except Exception as e:
                messagebox.showerror("Error", f"Error al dividir el archivo {file_path}: {str(e)}")

    messagebox.showinfo("Completado", "Se han dividido los archivos PDF correctamente.")

# Función para unir archivos PDF
def merge_pdf(file_paths):
    output_pdf = PdfWriter()

    for file_path in file_paths:
        input_pdf = PdfReader(file_path)

        for page in input_pdf.pages:
            output_pdf.add_page(page)

    output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

    if output_file_path:
        with open(output_file_path, "wb") as output_file:
            output_pdf.write(output_file)
        messagebox.showinfo("Completado", "Se han unido los archivos PDF correctamente.")
    else:
        messagebox.showwarning("Aviso", "No se ha especificado un archivo de salida.")

# Función para manejar el evento de arrastrar y soltar
def handle_drop(event, func):
    file_paths = event.data

    if isinstance(file_paths, str):
        file_paths = [file_paths]

    func(file_paths)

# Sección para desbloquear PDF
frame_unlock = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_unlock.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_unlock = tk.Label(frame_unlock, text="Desbloquear PDF")
label_unlock.pack()

frame_unlock_drop = tk.Frame(frame_unlock, relief=tk.SUNKEN, bd=2)
frame_unlock_drop.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_unlock_drop = tk.Label(frame_unlock_drop, text="Arrastra y suelta archivos PDF aquí para desbloquearlos")
label_unlock_drop.pack(pady=10)

frame_unlock_buttons = tk.Frame(frame_unlock)
frame_unlock_buttons.pack()

btn_unlock = tk.Button(frame_unlock_buttons, text="Desbloquear", command=lambda: unlock_pdf(filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])) )
btn_unlock.pack(side=tk.LEFT, padx=5)

frame_unlock_drop.drop_target_register(DND_FILES)
frame_unlock_drop.dnd_bind('<<Drop>>', lambda event: handle_drop(event, unlock_pdf))

# Sección para bloquear PDF
frame_lock = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_lock.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_lock = tk.Label(frame_lock, text="Bloquear PDF")
label_lock.pack()

frame_lock_drop = tk.Frame(frame_lock, relief=tk.SUNKEN, bd=2)
frame_lock_drop.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_lock_drop = tk.Label(frame_lock_drop, text="Arrastra y suelta archivos PDF aquí para bloquearlos")
label_lock_drop.pack(pady=10)

frame_lock_buttons = tk.Frame(frame_lock)
frame_lock_buttons.pack()

btn_lock = tk.Button(frame_lock_buttons, text="Bloquear", command=lambda: lock_pdf(filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])) )
btn_lock.pack(side=tk.LEFT, padx=5)

frame_lock_drop.drop_target_register(DND_FILES)
frame_lock_drop.dnd_bind('<<Drop>>', lambda event: handle_drop(event, lock_pdf))

# Sección para dividir PDF
frame_split = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_split.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_split = tk.Label(frame_split, text="Dividir PDF")
label_split.pack()

frame_split_drop = tk.Frame(frame_split, relief=tk.SUNKEN, bd=2)
frame_split_drop.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_split_drop = tk.Label(frame_split_drop, text="Arrastra y suelta archivos PDF aquí para dividirlos")
label_split_drop.pack(pady=10)

frame_split_buttons = tk.Frame(frame_split)
frame_split_buttons.pack()

btn_split = tk.Button(frame_split_buttons, text="Dividir", command=lambda: split_pdf(filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])) )
btn_split.pack(side=tk.LEFT, padx=5)

frame_split_drop.drop_target_register(DND_FILES)
frame_split_drop.dnd_bind('<<Drop>>', lambda event: handle_drop(event, split_pdf))

# Sección para unir PDF
frame_merge = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_merge.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_merge = tk.Label(frame_merge, text="Unir PDF")
label_merge.pack()

frame_merge_drop = tk.Frame(frame_merge, relief=tk.SUNKEN, bd=2)
frame_merge_drop.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label_merge_drop = tk.Label(frame_merge_drop, text="Arrastra y suelta archivos PDF aquí para unirlos")
label_merge_drop.pack(pady=10)

frame_merge_buttons = tk.Frame(frame_merge)
frame_merge_buttons.pack()

btn_merge = tk.Button(frame_merge_buttons, text="Unir", command=lambda: merge_pdf(filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])) )
btn_merge.pack(side=tk.LEFT, padx=5)

frame_merge_drop.drop_target_register(DND_FILES)
frame_merge_drop.dnd_bind('<<Drop>>', lambda event: handle_drop(event, merge_pdf))

root.mainloop()
