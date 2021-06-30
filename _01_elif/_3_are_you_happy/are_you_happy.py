from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    q1 = simpledialog.askstring(title=None, prompt='Are you happy, yes or no?')
    if q1 == 'yes':
        messagebox.showinfo(title=None, message='Keep doing whatever you are doing')
    if q1 == 'no':
        q2 = simpledialog.askstring(title=None, prompt='Do you want to be happy?')
    if q2 == 'no':
        messagebox.showinfo(title=None, message='Keep doing whatever you are doing')
    if q2 == 'yes':
        messagebox.showinfo(title=None, message='Change something')
pass
