"""
Now, we expand the world.
"""

import random
import re
import exrex
import itertools
from tkinter import *
import colorsys
import math


"""
Standard stuff
"""
def makeWorld(chars, dimension, n = 3, seedOn = True, seed = 1932):
    if seedOn:
        random.seed(seed) # seeding the random generator
    world = []
    for i in range(dimension):
        t = [random.choice(chars) for x in range(n)]
        world.append(t)
    return world

def calculateSpecificity(type):
    return len(type)-type.count(".")

def convertType(type, stk):
    seq = ""
    for i in stk:
        seq = seq+i
    return type.replace(".", "["+seq+"]")

def convertTypes(code):
    cCode= {}
    for r in code:
        e = convertType(r, stk)
        c = convertType(code[r], stk)
        specificity = calculateSpecificity(r)*calculateSpecificity(code[r])
        cCode[e] = [c, specificity]
    return cCode

def readable(type, stk):
    seq = "["
    for i in stk:
        seq = seq+i
    return type.replace(seq+"]", ".")

def makeInterpretation(world, code):
    interpretation = []
    for d in code:
        matched = []
        for tuple in world:
            match = re.findall(d, assembleTypeFromList(tuple))
            if match != []:
                for m in match:
                    matched.append(m)
        newContents = [exrex.getone(code[d][0]) for x in matched]
        print("matched: "+ str(matched))
        print("how many matched: "+str(len(matched)))
        print("score for: "+str(len(matched)*code[d][1]))
        print("generated contents is: "+str(newContents))
        interpretation.append([d, code[d], len(matched),len(matched)*code[d][1], matched, newContents])
    return interpretation


def calculateInterpretationScore(interpretation):
    return sum([x[3] for x in interpretation ])

def generateSignFunction(stk, dotNum = 1, eDim = 3, cDim = 3):
    stok = stk.copy()
    items = list(range(len(stok)+dotNum))
    random.shuffle(items)
    for i in range(dotNum):
        stok.append(".")
    eT = [stok[x] for x in items[:eDim]]
    random.shuffle(items)
    cT = [stok[x] for x in items[:cDim]]
    return [eT, cT]

def assembleTypeFromList(type):
    st = ""
    for x in type:
        st = st+x
    return st

def makeCode(stk, signFuncNum = 4, dotNum = 1, minEDim = 3, maxEDim = 3, minCDim = 3, maxCDim = 3):
    code  = {}
    for i in range(signFuncNum):
        ec = generateSignFunction(stk, dotNum, random.randint(minEDim, maxEDim), random.randint(minCDim, maxCDim))
        code[assembleTypeFromList(ec[0])] = assembleTypeFromList(ec[1])
    return code


def rankSignFunctions(interpretation):
    creditDict = {}
    scores = set([x[3] for x in interpretation])
    scores = list(scores)
    scores.sort()
    scores.reverse()
    minVal = scores[-1]
    for i in scores:
        creditDict[i] = []
    for i in interpretation:
        if i[3] >= minVal:
            eT = assembleTypeFromList(i[0])
            cT = assembleTypeFromList(i[1][0])
            score =  i[1][1]
            creditDict[i[3]].append([eT, [cT,score]])
    return creditDict

def makeTopCode(interpretation, howMany = 3):
    top = rankSignFunctions(interpretation)
    code = {}
    ranked = list(top.keys())
    ranked.sort()
    ranked.reverse()
    cnt = 0
    for i in ranked:
        for j in top[i]:
            code[j[0]] = j[1]
            cnt = cnt+1
            if(cnt >= howMany):
                break
        if(cnt >= howMany):
            break
    return code


def generateAnalogy(code, stk, dotProb = 30):
    # collecting all types, both E and C
    forms = list(code.keys())
    for i in [x for x in list(code.values())]:
        forms.append(i[0])
    #print(forms)
    random.shuffle(forms)
    # we need the dot format
    eT = readable(forms[0], stk)
    newEt = []
    for i in eT:
        newEt.append(random.choices([i, "."], [100-dotProb, dotProb]))
    newEt  = list(itertools.chain(*newEt))
    #print(newEt)
    newEt = assembleTypeFromList(newEt)
    cT = readable(forms[1], stk)
    newCt = []
    for i in cT:
        newCt.append(random.choices([i, "."], [100-dotProb, dotProb]))
    newCt  = list(itertools.chain(*newCt))
    newCt = assembleTypeFromList(newCt)
    return {newEt: newCt}

def generateStrictAnalogy(code, stk, dotProb = 30):
    # collecting all types, both E and C, separately
    eforms = list(code.keys())
    cforms = [x[0] for x in list(code.values())]
    #print(eforms)
    #print(cforms)
    random.shuffle(eforms)
    random.shuffle(cforms)
    # we need the dot format
    eT = readable(cforms[0], stk)
    newEt = []
    for i in eT:
        newEt.append(random.choices([i, "."], [100-dotProb, dotProb]))
    newEt  = list(itertools.chain(*newEt))
    #print(newEt)
    newEt = assembleTypeFromList(newEt)
    cT = readable(eforms[0], stk)
    newCt = []
    for i in cT:
        newCt.append(random.choices([i, "."], [100-dotProb, dotProb]))
    newCt  = list(itertools.chain(*newCt))
    newCt = assembleTypeFromList(newCt)
    return {newEt: newCt}

def updateCode(world, stk, cCode, interpretation, dotProb = 30, howMany = 3):
    # iter
    topSignFunc = makeTopCode(interpretation, howMany)
    newSigFunc = convertTypes(generateAnalogy(code, stk, dotProb)) # a new set of sign funcs
    while list(newSigFunc.keys())[0] in list(topSignFunc.keys()):
        #print("again")
        # we can use both cases of analogy
        newSigFunc = convertTypes(generateStrictAnalogy(code, stk, dotProb)) # a new set of sign funcs
    topSignFunc.update(newSigFunc) # merge the two dicts
    return topSignFunc

"""
Now we add to the world, rather than taking it as a stack
"""

def updateWorld(world, interpretation):
    dim = len(world)
    newW = world.copy()
    for c in interpretation:
        if c[2] > 0:
            # adding all contents
            for i in c[5]:
                newW.append([x for x in i])
    return newW

def iterateInterpretation(world, stk, cCode, iterations, dotProb = 20, howMany = 3, worldLimit = 100000):
    for i in range(iterations):
        print("iterations no. "+str(i+1))
        print("world size: "+str(len(world)))
        worldSet = set([assembleTypeFromList(x) for x in world])
        print("world set size: "+str(len(worldSet)))
        print("worldSet/world: "+str(len(worldSet)/len(world)))
        print("code: ")
        for e in cCode:
            print(readable(e, stk)+" : "+readable(cCode[e][0], stk)+" = "+str(cCode[e][1]))
        interpretation = makeInterpretation(world, cCode)
        matchNum = sum([x[2] for x in interpretation])
        print("total matches: "+str(matchNum))
        print("matches/world ratio: "+str(matchNum/len(world)))
        print("total score: " + str(calculateInterpretationScore(interpretation)))
        cCode = updateCode(world, stk, cCode, interpretation, dotProb, howMany)
        world = updateWorld(world, interpretation)
        print("\n")
        if len(world) > worldLimit:
            break
    #return [cCode, world]
    return [cCode, world]

def hsvToHex(h,s,v):
    # input: tuple
    rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = list(map(lambda x: int(x*255), rgb))
    rgb = (rgb[0], rgb[1], rgb[2])
    return "#%02x%02x%02x" % rgb

def paintWorld(world, code, side = 900):
    master = Tk()
    sideStep = int(math.sqrt(len(world)))+1
    step = int(side/sideStep)
    canvas_width = step*sideStep
    canvas_height = step*sideStep
    w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
    x = 0
    y = 0
    for triple in world:
        j = 0
        tr = assembleTypeFromList(triple)
        w.create_rectangle(x, y, x+step, y+step, fill="white")
        for sf in code:
            if re.search(sf, tr):
                #print("matched: "+tr+" by "+sf)
                col = hsvToHex(j/4, 0.8, 0.8)
                mul = step*(len(code.keys())-(j))/len(code.keys())
                w.create_rectangle(x, y, x+mul, y+mul, fill=col)
                # does sf e match the triplet i?
                # yes: set color
            j = j+1
            #print(str(j))
        x = x+step
        if x >= (canvas_width):
            x = 0
            y = y+step
    w.pack()
    mainloop()

def makeCodeGraph(code, stk, path = ""):
    eT = []
    cT = []
    for i in list(code.keys()):
        eT.append(readable(i, stk))
        cT.append(readable(code[i][0], stk))
    file = open("graphGrammar.dot", "w")
    header = """
digraph \"code graph\" {
    graph [
        //label=\"Code Graph\",
        fontname = \"Avenir Next LT Pro\",
        fontsize = 18
    ]
    node [
        shape = plaintext,
        width = 1,
        color = red,
        style = filled,
        fontcolor = white,
        fontname = \"DejaVu Sans Mono\"
    ]
        """
    nodes = ""
    links = ""
    i = 0
    for e in eT:
        node = "\""+e+":"+cT[i]+"\""
        nodes = nodes + "\t"+node+";\n"
        i = i+1
        j = 0
        for c in cT:
            n = 0
            newC = ""
            for x in c:
                if x == ".":
                    newC = newC + e[n]
                else:
                    newC = newC + x
                n = n+1
            #print([e,c, newC])
            if re.search(e, newC):
                # relation: isMatched
                target = "\""+eT[j]+":"+cT[j]+"\""
                # create link
                links = links+"\t"+target+"->"+node+";\n"
            j = j+1
    file.write(header+nodes+links+"}\n")
    file.close()


stk = [chr(i) for i in range(97, 123)]
world = makeWorld(stk, 100, seedOn = False)
code = makeCode(stk, 4,1)
code = convertTypes(code)
makeCodeGraph(code, stk, "")

code, world = iterateInterpretation(world, stk, code, 100, 10, worldLimit = 4000)

"""
Observations
- we might have many starting iterations with score = 0. A real beginning (positive score) is just a lucky match
- if we have a positive score, then it grows. Crucial point: partial analogy
- it is important to have a certain percentage of dontcares to ensure flexibility. Less score, but more matching

"""

#code = {'nuq':['vel', 9], 'vel':['nu.', 9]}
makeCodeGraph(code, stk, "")

paintWorld(world, code)
