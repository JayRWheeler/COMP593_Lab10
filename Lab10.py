import os
import poke_doki_api
from tkinter import *
from tkinter import ttk
import ctypes
import image_lib

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the main Window
root = Tk()
root.title("Pokemon Image Viewer")
root.minsize(600, 620)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokemonImageViewer')
icon_path = os.path.join(script_dir, 'Poke-Ball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

img_poke = PhotoImage(file=os.path.join(script_dir, 'PokeLogo.png'))
lbl_poke_image = ttk.Label(frame, image=img_poke)
lbl_poke_image.grid(row=0, column=0)

pokemon_name_list = sorted(poke_doki_api.get_pokemon_names())
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_pokemon_names.set("Select a Pokemon")
cbox_pokemon_names.grid(row=1, column=0, padx=10, pady=10)

def handle_pokemon_sel(event):
    pokemon_name = cbox_pokemon_names.get()
    
    global img_path
    img_path = poke_doki_api.download_pokemon_image(pokemon_name, image_cache_dir)

    if img_path is not None:
        img_poke['file'] = img_path
    btn_set_desktop.state(['!disabled'])
    

def set_desktop_img():
    poke_bg = image_lib.set_desktop_background_image(img_path)

btn_set_desktop = ttk.Button(frame, text='Set as Desktop Image', command=set_desktop_img, state= DISABLED)
btn_set_desktop.grid(row=2, column=0, padx= 10, pady= 10)

cbox_pokemon_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)

root.mainloop()



