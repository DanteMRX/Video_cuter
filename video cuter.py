      
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import tkinter as tk

def seleccionar_video():
    archivo_video = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4")])
    entry_video.delete(0, tk.END)
    entry_video.insert(0, archivo_video)

def recortar_video():
    nombre_video = entry_video.get()
    duracion_clip = int(entry_duracion.get())

    video = VideoFileClip(nombre_video)
    duracion_total = video.duration

    # Calcula la cantidad de clips que se pueden obtener
    cantidad_clips = int(duracion_total / duracion_clip)

    lbl_resultado.config(text=f"Se generarán {cantidad_clips} clips de {duracion_clip} segundos cada uno")

    for i in range(cantidad_clips):
        tiempo_inicio = i * duracion_clip
        tiempo_fin = (i + 1) * duracion_clip
        nombre_salida = f"(11) Guardianes de la Galaxia (2014) Parte_{i+1}.mp4"

        clip_recortado = video.subclip(tiempo_inicio, tiempo_fin)
        clip_recortado.write_videofile(nombre_salida, codec="libx264", threads=4, preset="ultrafast")

    video.close()
    lbl_resultado.config(text="Recorte completado")

# Crear ventana
ventana = tk.Tk()
ventana.title("Video Cutter")

# Etiqueta y campo de entrada para el video
lbl_video = tk.Label(ventana, text="Video:")
lbl_video.grid(row=0, column=0, padx=10, pady=10)
entry_video = tk.Entry(ventana)
entry_video.grid(row=0, column=1, padx=10, pady=10)
btn_seleccionar = tk.Button(ventana, text="Seleccionar", command=seleccionar_video)
btn_seleccionar.grid(row=0, column=2, padx=10, pady=10)

# Etiqueta y campo de entrada para la duración de cada clip
lbl_duracion = tk.Label(ventana, text="Duración de cada clip (segundos):")
lbl_duracion.grid(row=1, column=0, padx=10, pady=10)
entry_duracion = tk.Entry(ventana)
entry_duracion.grid(row=1, column=1, padx=10, pady=10)

# Botón de recorte
btn_recortar = tk.Button(ventana, text="Recortar", command=recortar_video)
btn_recortar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
lbl_resultado = tk.Label(ventana, text="")
lbl_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz
ventana.mainloop()

      
    