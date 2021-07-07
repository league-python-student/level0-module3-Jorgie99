from tkinter import simpledialog, messagebox, Tk
import random

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title=None, prompt='Enter your name.')
    messagebox.showinfo(title=None, message='The year is 1835')
    messagebox.showinfo(title=None, message ='The fur tradesman ' + name + ' is preparing to pass the Oregon Trail.')
    messagebox.showinfo(title=None, message='' + name + ' heads over to the town store to purchase supplies for the trip.')
    money = 300
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
    messagebox.showinfo(title=None, message='Fort Kearny is four days away.')
    food *= 4
    food -= food
    messagebox.showinfo(title=None, message='' + name + ' arrives at Fort Kearny.')
    FK = simpledialog.askstring(title=None, prompt='You have ' + str(food) + ' pounds of food left. Would you like to purchase more?')
    if FK == 'Yes':
        food = simpledialog.askinteger(title=None, prompt='How many pounds of food would you like?')
        food *= 0.5
        money -= food
        messagebox.showinfo(title=None, message='You now have $' + str(money) + '')
        messagebox.showinfo(title=None, message='' + str(name) + ' leaves for Independence Rock.')
    if FK == 'No':
        messagebox.showinfo(title=None, message='' + str(name) + ' leaves for Independence Rock.')
    rand_num = random.randint(1, 4)
    if rand_num == 1:
        messagebox.showinfo(title=None, message='' + str(name) + ' has dysentery. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num == 2:
        messagebox.showinfo(title=None, message='' + str(name) + ' has cholera. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num == 3:
        messagebox.showinfo(title=None, message='A thief has come in the night and stole 50 pounds of food.')
        messagebox.showinfo(title=None, message='' + str(name) + ' has arrived at Independence Rock.')
    if rand_num == 4:
        messagebox.showinfo(title=None, message='' + str(name) + ' has arrived at Independence Rock.')
    IR = simpledialog.askstring(title=None, prompt='Do you want to carve your name in the rock?')
    if IR == 'Yes':
        messagebox.showinfo(title=None, message='Congrats! Your name will now be there forever.')
        messagebox.showinfo(title=None, message='' + str(name) + ' continues along the trail to Fort Boise.')
    if IR == 'No':
        messagebox.showinfo(title=None, message='' + str(name) + ' continues along the trail to Fort Boise.')
    rand_num1 = random.randint(1, 4)
    if rand_num1 == 1:
        messagebox.showinfo(title=None, message='' + str(name) + ' has dysentery. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num1 == 2:
        messagebox.showinfo(title=None, message='' + str(name) + ' has cholera. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num1 == 3:
        messagebox.showinfo(title=None, message='A thief has come in the night and stole 50 pounds of food.')
        messagebox.showinfo(title=None, message='' + str(name) + ' has arrived at Fort Boise, the last stop.')
    if rand_num1 == 4:
        messagebox.showinfo(title=None, message='' + str(name) + ' has arrived at Fort Boise, the last stop.')
    FB = simpledialog.askstring(title=None, prompt='You have ' + str(
        food) + ' pounds of food left. Would you like to purchase more?')
    if FB == 'Yes':
        food = simpledialog.askinteger(title=None, prompt='How many pounds of food would you like?')
        food *= 0.5
        money -= food
        messagebox.showinfo(title=None, message='You now have $' + str(money) + '')
    if FB == 'No':
        messagebox.showinfo(title=None, message='You have ' + str(
            food) + ' pounds of food left.')
    River = simpledialog.askstring(title=None, prompt='You now must cross a river. Do you choose to caulk or ford it?')
    if River == 'Caulk':
        rand_num2 = random.randint(1, 10)
        if ((rand_num2 == 1) and (rand_num2 == 3) and (rand_num2 == 5) and (rand_num2 == 7) and (rand_num2 == 9)):
            messagebox.showinfo(title=None, message='You have succesfully crossed the river.')
        if ((rand_num2 == 2) and (rand_num2 == 4) and (rand_num2 == 6) and (rand_num2 == 8) and (rand_num2 == 10)):
            messagebox.showinfo(title=None, message='You failed to cross the river.')
            messagebox.showinfo(title=None, message='Game over.')
            exit()
    if River == 'Ford':
        rand_num2 = random.randint(1, 10)
        if ((rand_num2 == 1) and (rand_num2 == 3) and (rand_num2 == 5) and (rand_num2 == 7) and (rand_num2 == 9)):
            messagebox.showinfo(title=None, message='You have successfully crossed the river.')
        if ((rand_num2 == 2) and (rand_num2 == 4) and (rand_num2 == 6) and (rand_num2 == 8) and (rand_num2 == 10)):
            messagebox.showinfo(title=None, message='You failed to cross the river.')
            messagebox.showinfo(title=None, message='Game over.')
            exit()
    rand_num3 = random.randint(1, 4)
    if rand_num3 == 1:
        messagebox.showinfo(title=None, message='' + str(name) + ' has dysentery. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num3 == 2:
        messagebox.showinfo(title=None, message='' + str(name) + ' has cholera. You die.')
        messagebox.showinfo(title=None, message='Game Over')
        exit()
    if rand_num3 == 3:
        messagebox.showinfo(title=None, message='You have broken your arm. Three drays are added to your travel.')
        messagebox.showinfo(title=None, message='' + str(name) + ' has arrived in Oregon.')
        messagebox.showinfo(title=None, message='Congrats! You have survived the Oregon Trail. Thanks for playing!')
        exit()
    if rand_num3 == 4:
        messagebox.showinfo(title=None, message='Congrats! You have survived the Oregon Trail. Thanks for playing!')
        exit()