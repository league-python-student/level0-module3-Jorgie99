from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    so = simpledialog.askinteger(title=None, prompt='How many shiny objects would you like?')
    str(so)
    for i in range(so):
        playsound('shiny-objects.wav')
    # TODO 2) Ask the user how many shiny objects they want

    # TODO 3) Play the sound that many times

    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
