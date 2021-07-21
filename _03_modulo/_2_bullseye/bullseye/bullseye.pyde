def setup():
    # Set the size of your sketch

    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass

def setup():
    # Set the size of your sketch
    size(500,500)

    pass

def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    number = 8
    h = 450
    w = 450
    for i in range(8):
        if number % 2 == 0:
            fill('#FF0303')
            ellipse(250, 250, h, w)
        else:
            fill('#000000')
            ellipse(250, 250, h, w)
        number -= 1
        h -= 50
        w -= 50

    # Use an if statement and modulo to alternate the color of your rings


    pass
