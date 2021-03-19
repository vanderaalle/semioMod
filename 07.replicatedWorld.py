"""
Replica-reduction is thus a framework that takes into account the basic concept of sign, still allowing the implicit encoding of ostension and imprint.
Let us go back to our previous discussion.
"""

import random
import re
import exrex

def makeWorld(chars, dimension, seed = 1932):
    random.seed(seed) # seeding the random generator
    world = []
    for i in range(dimension):
        world.append(random.choice(chars))
    return world

def aggregateWorld(world):
    agg = ""
    for st in world:
        agg = agg+st
    return agg


stk = [chr(i) for i in range(97, 123)]
world = makeWorld(stk, 1000)
aggregateWorld(world)

def calculateSpecificity(type):
    return len(type)-type.count(".")


"""
Here we redefine convertTypes to store interpretation score
"""
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
"""
To read easier a type
"""
def readable(type, stk):
    seq = "["
    for i in stk:
        seq = seq+i
    return type.replace(seq+"]", ".")

code = {
"awa":"bbf",
"z.z":"g.g",
"k.k":"c.c",
"l..":"ooo" # expression form and content form
}
code = convertTypes(code)

"""
The func makeInterpretation is redefined. It keeps track of the number of matches, and calculate an overall score for each E type by the product (number of matches x type specificity).
"""

def makeInterpretation(world, code):
    interpretation = []
    for d in code:
        matched = re.findall(d, aggregateWorld(world))
        interpretation.append([d, code[d], len(matched),len(matched)*code[d][1], matched])
    return interpretation

interpretation = makeInterpretation(world, code)

def calculateInterpretationScore(interpretation):
    return sum([x[3] for x in interpretation ])

calculateInterpretationScore(interpretation)

"""
Can we introduce a positive feedback loop so to generate new rewarding E type?
That is, can we turn sign production from a description into an adaptive system, Holland-style?
At the moment we are not considering the obtained contents.
The idea is that, over four E types, the first three having higher score are kept, and a random one is introduced.
First we have to random generate an E type. Better, we generate a whole random sign function.
"""

def generateSignFunction(stk, eDim = 3, cDim = 3):
    stok = stk.copy()
    items = list(range(len(stok)+1))
    random.shuffle(items)
    stok.append(".")
    eT = [stok[x] for x in items[:eDim]]
    random.shuffle(items)
    cT = [stok[x] for x in items[:cDim]]
    return [eT, cT]

generateSignFunction(stk)

"""
Now we can create a random code.
"""
def assembleTypeFromList(type):
    st = ""
    for x in type:
        st = st+x
    return st

def makeCode(stk, signFuncNum = 4, minEDim = 3, maxEDim = 3, minCDim = 3, maxCDim = 3):
    code  = {}
    for i in range(signFuncNum):
        ec = generateSignFunction(stk, random.randint(minEDim, maxEDim), random.randint(minCDim, maxCDim))
        code[assembleTypeFromList(ec[0])] = assembleTypeFromList(ec[1])
    return code

makeCode(stk)

"""
This is a possible output (effectively generated)
{'...': '...', 'pzv': '.h.', '..j': 'r..'}
Interestingly enough, it opens with the the anythingGoes function. Such a sign function may be generated, but its score being 0, it will be deleted in a dynamic process assigning credits.
"""

code = makeCode(stk)

"""
The following functions select top howMany sign func and return a shortened code
"""
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

rankSignFunctions(interpretation)
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

makeTopCode(interpretation)

"""
cCode is a converted code. Makes an interpretation and return an updated code
"""
def interpretAndUpdate(world, stk, cCode, howMany = 3):
    # iter
    interpretation = makeInterpretation(world, cCode)
    print("score: " + str(calculateInterpretationScore(interpretation)))
    topSignFunc = makeTopCode(interpretation, howMany)
    newSigFunc = convertTypes(makeCode(stk, len(cCode)-howMany)) # a new set of sign funcs
    topSignFunc.update(newSigFunc) # the new set of rule
    return topSignFunc
    # merge the two dicts


# interpretAndUpdate(world, stk, code)

def iterateInterpretation(world, stk, cCode, iterations, howMany = 3):
    for i in range(iterations):
        print("iterations no. "+str(i+1))
        cCode = interpretAndUpdate(world, stk, cCode, howMany)
        #print(len(cCode.keys()))
        for e in cCode:
            #print(e)
            #print(cCode[e])
            print(readable(e, stk)+" : "+readable(cCode[e][0], stk)+" = "+str(cCode[e][1]))
        print("\n")
    return cCode

code = makeCode(stk)
code = convertTypes(code)
iterateInterpretation(world, stk, code, 200)
code = makeCode(stk)
code = convertTypes(code)
iterateInterpretation(world, stk, code, 200)

"""
Variations are of course possbile.
Larger code, replacing 2 sign func at iterations
"""
code = makeCode(stk, 8)
code = convertTypes(code)
iterateInterpretation(world, stk, code, 200, 8-6)

"""
The system looks adaptive, it keeps on generating better scores. We can say that it learns by trials and errors, collecting good results.
Typical beahviour is to start from a variable number of score = 0, then growing almost linearly, then oscillating around various plateaus, eventually raising to a new one.
"""
