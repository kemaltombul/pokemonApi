import tkinter
window = tkinter.Tk()
import requests as req

window.title("Pokemon")
window.geometry("400x300")
window.resizable(False, False)
###
def getPokemon():
    pokemon = entry.get()
    link='https://pokeapi.co/api/v2/pokemon/'+pokemon+"/"
    res = req.get(link)

    if res.status_code == 200:
        pokemon = res.json()
        weight_label.config(text="Weight: " + str(pokemon.get('weight')))
        height_label.config(text="Height: " + str(pokemon.get('height')))

    else:
        status_label.config(text="Pokemon not found")
###
entry_label = tkinter.Label(window, text="Enter Pokemon Name:")
entry = tkinter.Entry(window)
entry_button = tkinter.Button(window, text="OK", command=getPokemon)
weight_label = tkinter.Label(window,text="")
height_label = tkinter.Label(window,text="")
status_label = tkinter.Label(window, text="")
###
entry_label.pack()
entry.pack()
entry_button.pack()
weight_label.pack()
height_label.pack()
status_label.pack()
###
getPokemon()

window.mainloop()
