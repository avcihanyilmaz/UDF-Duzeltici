import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
def dosya_islem(yol):
    yol = yol.strip('{}')
    if not yol.lower().endswith(".zip"):
        messagebox.showerror("Hata", "Yanlış Dosya! Lütfen bir .zip dosyası seçin.")
        return
    temiz_yol = yol.rsplit('.zip', 1)[0]
    yeni_yol = temiz_yol if temiz_yol.lower().endswith(".udf") else temiz_yol + ".udf"
    try:
        if os.path.exists(yeni_yol):
            if not messagebox.askyesno("Onay", "Bu isimde bir dosya zaten var. Üzerine yazılsın mı?"):
                return
        os.rename(yol, yeni_yol)
        messagebox.showinfo("Başarılı", f"Dosya düzeltildi:\n{os.path.basename(yeni_yol)}")
        placeholder_ekle()
    except Exception as e:
        messagebox.showerror("Hata", f"İşlem başarısız: {e}")
def placeholder_sil(e):
    if yol_girisi.get() == " Dosyayı buraya sürükleyin...":
        yol_girisi.delete(0, tk.END)
        yol_girisi.config(fg="#2d3436")
def placeholder_ekle(e=None):
    if not yol_girisi.get():
        yol_girisi.insert(0, " Dosyayı buraya sürükleyin...")
        yol_girisi.config(fg="#b2bec3")
def surukle_birak(event):
    yol_girisi.delete(0, tk.END)
    yol_girisi.config(fg="#2d3436")
    yol_girisi.insert(0, event.data)
def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(title="Dosya Seç", filetypes=[("ZIP", "*.zip")])
    if dosya_yolu:
        yol_girisi.delete(0, tk.END)
        yol_girisi.config(fg="#2d3436")
        yol_girisi.insert(0, dosya_yolu)
def on_enter_islem(e): islem_btn['background'] = '#485e74'
def on_leave_islem(e): islem_btn['background'] = '#2d3436'

def on_enter_gozat(e): gozat_btn['background'] = '#708090'
def on_leave_gozat(e): gozat_btn['background'] = '#636e72' 
root = TkinterDnD.Tk()
root.title("UDF Düzeltici - Av. Cihan YILMAZ")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="#dfe6e9")
tk.Label(root, text="UDF DOSYA DÜZELTİCİ", bg="#dfe6e9", fg="#2d3436", 
         font=("Segoe UI", 14, "bold")).pack(pady=(25, 15))
entry_frame = tk.Frame(root, bg="#dfe6e9")
entry_frame.pack(pady=10, padx=40, fill='x')
border_frame = tk.Frame(entry_frame, bg="#b2bec3", bd=1)
border_frame.pack(side=tk.LEFT, fill='x', expand=True, padx=(0, 10))
yol_girisi = tk.Entry(border_frame, font=("Segoe UI", 10), relief="flat", 
                      bg="#f1f2f6", fg="#b2bec3", insertbackground="#2d3436")
yol_girisi.pack(fill='x', padx=1, pady=1, ipady=5)
yol_girisi.insert(0, " Dosyayı buraya sürükleyin...")
yol_girisi.drop_target_register(DND_FILES)
yol_girisi.dnd_bind('<<Drop>>', surukle_birak)
yol_girisi.bind("<FocusIn>", placeholder_sil)
yol_girisi.bind("<FocusOut>", placeholder_ekle)
gozat_btn = tk.Button(entry_frame, text="Gözat", command=dosya_sec, relief="flat",
                      bg="#636e72", fg="white", font=("Segoe UI", 9, "bold"), 
                      cursor="hand2", width=10, bd=0, activebackground="#2d3436")
gozat_btn.pack(side=tk.RIGHT)
gozat_btn.bind("<Enter>", on_enter_gozat)
gozat_btn.bind("<Leave>", on_leave_gozat)
islem_btn = tk.Button(root, text="DÜZELT", command=lambda: dosya_islem(yol_girisi.get()), 
                      bg="#2d3436", fg="white", font=("Segoe UI", 12, "bold"), 
                      width=22, bd=0, cursor="hand2", activebackground="#1e272e")
islem_btn.pack(pady=25)
islem_btn.bind("<Enter>", on_enter_islem)
islem_btn.bind("<Leave>", on_leave_islem)
root.mainloop()
