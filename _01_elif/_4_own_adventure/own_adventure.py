from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
window.withdraw()
name = simpledialog.askstring(title=None, prompt='Enter your name')
messagebox.showinfo(title=None, message='The year is 1835 and the fur tradesman ' + name + ' is preparing to pass the Oregon Trail.')
messagebox.showinfo(title=None, message='' + name + ' heads over to the town store to purchase supplies for the trip.')
money=300
messagebox.showinfo(title=None, message='You have $' + str(money) + '')
messagebox.showinfo(title=None, message='Oxen cost $25 and food costs $0.50 per pound.')
oxen = simpledialog.askinteger(title=None, prompt='How many oxen would you like?')
oxen *= 25
money -= oxen
messagebox.showinfo(title=None, message='You now have $' + str(money) + '')
food = simpledialog.askinteger(title=None, prompt='How many pounds of food would you like?')
food *= 0.5
money -= food
messagebox.showinfo(title=None, message='You now have $' + str(money) + '')
messagebox.showinfo(title=None, message=' ' + name + ' finally sets off on the Oregon Trail.')
miles = 2000