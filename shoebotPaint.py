import shoebot # does not work in hydrogen
import pickle
import re
import math

# if you have pickled a world you can paint it
f = open("world1990-11.pkl", "rb")
world = pickle.Unpickler(f)
world = world.load()
f.close()
f = open("code1990-11.pkl", "rb")
code = pickle.Unpickler(f)
code = code.load()
f.close()



def assembleTypeFromList(type):
    st = ""
    for x in type:
        st = st+x
    return st

def paintWorld(world, code, side = 900, num = False):
    bot = shoebot.create_bot(outputfile="world1990-11.pdf")
    bot.color_mode = "hsb"
    sideStep = int(math.sqrt(len(world)))+1
    step = int(side/sideStep)
    canvas_width = step*sideStep
    canvas_height = step*sideStep
    bot.size(canvas_width+2, canvas_height+2)
    bot.stroke(0)
    bot.fill(1)
    #bot.rect(0, 0, canvas_width, canvas_height)
    x = 0
    y = 0
    print(len(world))
    i = 0
    for triple in world:
        tr = assembleTypeFromList(triple)
        bot.fill(1)
        bot.stroke(0)
        bot.rect(x, y, step, step)
        bot.fill(0)
        if num == True:
            bot.text(str(i), x+5, y+20)
        j = 0
        for sf in code:
            if re.search(sf, tr):
                # painting: e.g. 8 sf, then 8 potential squares
                # inside one other, each with 1 of 8 hues
                #print("matched: "+tr+" by "+sf)
                #col = (float(j)/float(len(code.keys())), 0.9, 0.9)
                #bot.fill(col)
                col = (float(j)/len(code.keys()))
                col = 1-(col*0.7+0.3)
                bot.fill(col)
                bot.stroke(col)
                base = float(len(code.keys()))+3
                mul = step*(base-(j))/base
                bot.oval(x+step*0.5-mul*0.5, y+step*0.5-mul*0.5, mul, mul)
                # does sf e match the triplet i?
                # yes: set color
            j = j+1
        x = x+step
        if x >= (canvas_width):
            x = 0
            y = y+step
        i = i+1
    bot.finish()

paintWorld(world, code, 1100)
