"""
Now, looking for a suitable evolving model.
"""

import random
import re
import exrex


"""
Let us make it simpler. We need a n-ple world. Dimension is number of tuples. N the tuple size.
Here, as usual, we work with triplets.
"""
def makeWorld(chars, dimension, n = 3, seed = 1932):
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
"""
To read easier a type
"""
def readable(type, stk):
    seq = "["
    for i in stk:
        seq = seq+i
    return type.replace(seq+"]", ".")

"""
We add again the generation of content to interpretation (token/substance, not type/form).
"""
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
        #newContents = ""
        print("matched: "+ str(matched))
        interpretation.append([d, code[d], len(matched),len(matched)*code[d][1], matched, newContents])
    return interpretation


def calculateInterpretationScore(interpretation):
    return sum([x[3] for x in interpretation ])

"""
The generator: we keep randomness
"""
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

stk = [chr(i) for i in range(97, 123)]

world = makeWorld(stk, 100)
code = makeCode(stk, 4,10)
code = convertTypes(code)
interpretation = makeInterpretation(world, code)
calculateInterpretationScore(interpretation)


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

"""
We move interpretation outside because we nee to get the content
"""
def updateCode(world, stk, cCode, interpretation, dotNum = 1, howMany = 3):
    # iter
    topSignFunc = makeTopCode(interpretation, howMany)
    newSigFunc = convertTypes(makeCode(stk, len(cCode)-howMany, dotNum)) # a new set of sign funcs
    topSignFunc.update(newSigFunc) # merge the two dicts
    return topSignFunc



def updateWorld(world, interpretation):
    dim = len(world)
    newW = world.copy()
    for c in interpretation:
        if c[2] > 0:
            # adding all contents
            for i in c[5]:
                newW.append([x for x in i])
    newDim = len(newW)
    newW = newW[(newDim-dim):]
    return newW

def iterateInterpretation(world, stk, cCode, iterations, dotNum = 1, howMany = 3):
    for i in range(iterations):
        print("iterations no. "+str(i))
        interpretation = makeInterpretation(world, cCode)
        print("score: " + str(calculateInterpretationScore(interpretation)))
        cCode = updateCode(world, stk, cCode, interpretation, dotNum, howMany)
        for e in cCode:
            print(readable(e, stk)+" : "+readable(cCode[e][0], stk)+" = "+str(cCode[e][1]))
        print("\n")
        #world = updateWorld(world, interpretation)
    return [cCode, world]

code = makeCode(stk, 4,1)
code = convertTypes(code)
interpretation = makeInterpretation(world, code)
updateWorld(world, interpretation)
iterateInterpretation(world, stk, code, 100, 1)

"""
By running the previous example, we assume that the dontcare has the same probability to be picked up as the other chars (1/len(stk) including "."). That is, less than 4%:
"""
1/(len(stk)+1)
"""
Nevertheless, it is statistically overrepresented in the final rules. This means that the credit assignment rewards types having dontcares. By running this:
"""
iterateInterpretation(world, stk, code, 100, 10)

"the replacement probability of dot is much higher, each char has a probability 1/(len(stk)+10)"""

1/((len(stk)+10))

""" So, less than 3%, while the dontcare becomes 10/(len(stk)+10), that is almost 30%. """

10/((len(stk)+10))

"""
It seems, but it should be checked formally, that in the first case dontcare is overrepresented thanks to credit assignment. Second, that the same credit assignment system (unfavoring dontcare) allows (as expected) to increase the score but not linearly. It is not n times bigger if we increase by n dontcare probability.

Now back to content generation. Random generation of content type seems adequate to the notion of arbitrariety as a classic foundation for sign. It could be observed that such a foundation is probably biased by natural language.
But we know from the typology of modes of sign production that actually a vast amount of sign functions are generated by motivation, i.e by ostension and imprint/invention. BTW one might observe that in presence of something not conventionated (expression) the only resource to interpret it is to find something else (content) related in some way to it.
Why abc sould be typically associate to something totally else like def? We know two ways to relate the two planes: by reproducing some of the expression in the content (ostension) and by inferring a rule allowing to map expression to content (imprint/invention).
While in our simple model model it might be difficult to formalize imprint (we need a notation we don't have), ostension is not complicated. If we have as E type abc, then by leaving some chars of E type into C type we have an ostension. As an example:

abc : abd

If we inject abd back into the world we still don't have a match. Looked "externally" the sign function looks like a replica. But dontcare helps a lot. Let us consider:

abc : ab.

Injected content can be abc, and can be matched by the E type. As usual, the more dots the more matching (and the less interpretation score).
This is a sort of intra-connectivity between E and C.
Another form of connectivity can be obtained by associating to an E type (as its C type) an E type from another sign function. We start from:

abc : def

And we can generate:

xyf : abc

Collected in a code, the second sign function injects into the world abc, that is matched by the first.
Can we justify such a connectivity? Actually, it can be thought as a form of analogy.
A slippery notion, still in our context it says that, if there is not a justified E/C association, then better to guess a sort of ressemblance among expressions (assuming injection of course).
Now, in this terms, ostension is just a form of analogy.
In fact, suppose we have a set of E types ET = {et1, et2, et3} and we generare for each a C type. Without constraints, sign functions may include the case et_n : et_n, that is, ostension.
Can we extend analogy on both sides of the sign function?
We start with

abc : def

And we generate:

def : xyz

That is, can we choose a new E type by picking up from C types (cf. connotation). It is evident that the situation at the end is the same, with types that can be totally or partially coincident.
So we have to rewrite the generateSignFunction func. In the previous approach, sign funcs are generated randomly, and they are uncoupled from other sign functions. We can keep this behavior while defining a generation func by analogy. As connectivity is our formal description for analogy, and it is defined over the set of EC types, we need to pass the code to generate a new func.
"""
import itertools

def generateAnalogy(code, stk, dotProb = 30):
    # collecting all types, both E and C
    forms = list(code.keys())
    for i in [x for x in list(code.values())]:
        forms.append(i[0])
    print(forms)
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

code = makeCode(stk, 4,10)
# dotProb = 0, so no added dontcares
generateStrictAnalogy(convertTypes(code), stk, 60)

"""
Now we change the updateCode func, to add new analogies.
"""

def updateCode(world, stk, cCode, interpretation, dotProb = 30, howMany = 3):
    # iter
    topSignFunc = makeTopCode(interpretation, howMany)
    newSigFunc = convertTypes(generateAnalogy(code, stk, dotProb)) # a new set of sign funcs
    topSignFunc.update(newSigFunc) # merge the two dicts
    return topSignFunc

def iterateInterpretation(world, stk, cCode, iterations, dotProb = 20, howMany = 3):
    for i in range(iterations):
        print("iterations no. "+str(i))
        interpretation = makeInterpretation(world, cCode)
        print("score: " + str(calculateInterpretationScore(interpretation)))
        cCode = updateCode(world, stk, cCode, interpretation, dotProb, howMany)
        for e in cCode:
            print(readable(e, stk)+" : "+readable(cCode[e][0], stk)+" = "+str(cCode[e][1]))
        print("\n")
        world = updateWorld(world, interpretation)
        print(world)
    return [cCode, world]

world = makeWorld(stk, 100)
code = makeCode(stk, 4,1)
code = convertTypes(code)
iterateInterpretation(world, stk, code, 100, 5)

"""
It still does not work. But there is a simple reason.
The world changes continuosly. Each time we get better we cut the world.
One could say: if we world changes too fast, no way to interpret it.
"""
