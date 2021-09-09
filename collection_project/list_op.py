import random
colours = ['red', 'purple', 'more purple', 'even more purple']
print (colours)
print (colours[0])
for colour in colours:
    colours.remove(random.choice(colours))
    print (colour)
