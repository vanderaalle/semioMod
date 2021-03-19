"""
The previous model is inspired by genetic algorithms. It is also possible that it may be directly represented in GA terms.
But it is not the formalism per se that is interesting.
Rather, starting from semiotic theory, it looks potentially significant to describe a barebone mechanism in which sign functions are contructed by summing random guesses and storing inductively good results.
The code in use in the previous example is constrained to four sign functions. This limit is used to trim at each iteration a sign function in order to leave space for a new one. This leads to a statiscal increase in the interpretation score, with a general steep curve and various oscillation around an empirical maxima.
Such a simple interpreter is thus provided with an interpretation algorithm plus a small memory. Something not far from the characterization of many living beings. Still, the interpreter learns by storing good matches, introducing new sign functions, discarding less perfoming ones. Loosing sign function is also something that sounds appropriate both in cognitive terms and in cultural ones. The renewal of culture,  in the single interpreter exactly as in a society, implies (if not requires) an exercise in oblivion.
Variations on the model can be easily added. As an example, rather than discarding a rule for each iteration, one can think of discarding a sf only if its score = 0. So each iteration add a new rule, which is discarded in the following iteration if its score = 0. This would lead to a progressive increase in the dimension of the code. Which is btw a good characterization of what typically happens in cultures. Colin Renfrew has discussed about the increase in cognitive/cultural richness caused by the Neolithic revolution. More material richness has implied more symbolic richness. Of course, the increase in code dimension seems to model the increase in complexity, on the other side is fairly evident that a constrain on dimension is also required. One could say: ecologically.
Of course, the main point at stake here is that the model provides a characterization in terms of E/C, however it does not say anything about content. It just deals with expression matching. To speak with Hjelmslev, it is monoplanar, content simply being a sort of appendage, so to say, to expression.
The Monistic principle has lead to a definition of expression and content as made literally of the same stuff.
So, there is no difference properly between E and C. Content can be considered as a mental/cognitive representation (as mostly happens in linguistic studies). There is no space in our poor model for such a conceptual form. On the other side, content being the reply to an expression, is more related to a fact in the world. Content in biosemiotics (and not only, one can just thing about Peirce) can be a response to something, the expression in our structuralistic parliance. Talking with a friend, I hear her/him speaking and I reply by speaking. Behaviour is significant. On the other side, expression are material, but they can be literally made of the stuff that dreams are made of. While dreaming, expressions and contents are evidently present in a semiotic context that btw requires a complex interpretative work. Properly there is no difference, in semiotic terms, i.e. in terms of semiotic labors, between reading, dreaming, following a trail, talking.
But, again, what to do with content in our model?
Eco comes again to help with a very famous suggestion, dealing with semiotics as a discipline. As an interpretive practice, the latter is not to be thought as the exploration of the sea, “where a ship’s wake disappears as soon as it has passed,” but, rather, as the exploration of a forest: this means that, technically speaking, the interpretation leaves “footprints” and “cart-trails” that “modify the explored landscape.” (ATS:29). This does not apply only to the epistemological level. The Model Q as the regulative model of the Encyclopedia is intended as complex graph connecting with multiple inputs and outputs cultural entries in which the difference between E and C is simply positional, that is, in graph parliance, between the starting vertex and the ending vertex in a direct graph.
Rhyzomatic topology apart, Eco strongly suggests that every interpretation modifies the graph. How this formally happens is not specified but the suggestion is relevant.
It is also evident:
- we live in a symbolic world, where objects and their interpretations are intertwined
- semiotic behaviour has evidently material effects. One may think today to Anthropocene. But the human imprint is far more distant in the past, at least since the discovery of fire. And btw living behaviour shapes the world constantly (from algae to engineering anaimals, like elephants, cf. Chelazzi)
To sum up:
- there is no difference between E and C
- each interpretation (E->C) is an act or a fact in the world
Is it possible to implement the latter feature in our model?
A possible solution is to exploit the first point, so to plunge back content (actual of course, not type) into the world.
Let us consider a rule like:
"ahb":"qux"
When E type matches, C type is available as a generating rule. It is the response of the interpreter to E, and a new string is generated, that does not need to be identical to the type, as it may include dontcares.
So, in our case, every matched E generates a new C that can be added (in various way, to be studied) to the world.
Interpretation modifies the world. The world is not static but it interacts with the interpreter.
Properly, the world is recreated (partially) by the interpreter, in the same way in which the interpreter has to adequate to the world.
Some interesting consequences:
- in a general model by addition, the world gets larger at each interpretation. This makes sense: the more interpretations, the richer the world. Again, the constraint issue emerge: is this growing infinite? Large yes, infinite not likely
- the world does not necessary change only because of the interpreter. If it is no more intended as a constant, then it can change because of extra-interpretative facts (5 great mass extinctions are enough to calm down the most Idealistic supporter). As an example, it is possible to add a random perturbation factor, that adds/delete/modifies the world independently from the interpreter. But random perturbations may affect the interepreter too (i.e. modifying the code). Such a behaviour would perform a role analogous to mutation in genetics, and in particular in this context, in genetic programming.
- if contents are plunged into the world, then sign functions to match them need to result in the code following our standard mechanism to increase the interpretation score. This leads theoretically to have in both side of the code the same types. Here, sign functions seem so to adhere more strictly to recursive production rules typical of formal grammars. To reach a content from an expression, then to move on to another content, as (technically) expressed by the first, and so on, is evidently a very well know cognitive and cultural procedure, and has been the model of various semiotic constructions (from connotation chains to unlimited semiosis, from semiosphere to encyclopedia).
"""

import random
import re
import exrex

"""
We finally understood that world can be a pure string
"""
def makeWorld(chars, dimension, seed = 1932):
    random.seed(seed) # seeding the random generator
    world = ""
    for i in range(dimension):
        world = world + random.choice(chars)
    return world

stk = [chr(i) for i in range(97, 123)]
world = makeWorld(stk, 1000)

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
        matched = re.findall(d, world)
        newContents = [exrex.getone(code[d][0]) for x in matched]
        print("matched: "+ str(matched))
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

"""
We move interpretation outside because we nee to get the content
"""
def updateCode(world, stk, cCode, interpretation, dotNum = 1, howMany = 3):
    # iter
    topSignFunc = makeTopCode(interpretation, howMany)
    newSigFunc = convertTypes(makeCode(stk, len(cCode)-howMany, dotNum)) # a new set of sign funcs
    topSignFunc.update(newSigFunc) # merge the two dicts
    return topSignFunc


"""
In this first version every sign function having a score > 1 pushes its content in the world
"""

def updateWorld(world, interpretation):
    dim = len(world)
    for c in interpretation:
        if c[2] > 0:
            # adding all contents
            for i in c[5]:
                world = world+i
    newDim = len(world)
    world = world[(newDim-dim):]
    return world

def iterateInterpretation(world, stk, cCode, iterations, dotNum = 1, howMany = 3):
    for i in range(iterations):
        print("iterations no. "+str(i))
        interpretation = makeInterpretation(world, cCode)
        print("score: " + str(calculateInterpretationScore(interpretation)))
        cCode = updateCode(world, stk, cCode, interpretation, dotNum, howMany)
        for e in cCode:
            print(readable(e, stk)+" : "+readable(cCode[e][0], stk)+" = "+str(cCode[e][1]))
        print("\n")
        world = updateWorld(world, interpretation)
    return [cCode, world]

code = makeCode(stk, 4,10)
code = convertTypes(code)
interpretation = makeInterpretation(world, code)
iterateInterpretation(world, stk, code, 100, 10, 3)

"""
It does not work. We may get high scores or at the same time 0 score. So there is no learning, just contingency.
a) if we delimit the world by cutting out the string head we favour the string tail. Now, the latter is made up of contents, that are not matched yet. Actually, we are polluting the environment by adding unmatched string. The production of content (i.e. its injection in the world) worsen the situation (i.e. decrease intepretation score). This is not so unsounding (cf. Tin Machine, I can't read shit anymore) but does not favour adaptation
b) code is limited. Maybe too much.
c) matching does not happen on generated content. Actually it works on a single string, so there are no n-tuple boundaries. Maybe we have to think about the world as made up by n-tuples, and have rules trying to match those.
d) a possibility is to intrinsically generate matching. Example: content is not random, but it's generated following an expression type. This is not totally absurd. At the end, content is arbitrary, why not try to describe it with known things? So, code would be made up by generating content type from expression type. This ensures matching. But the degree of connectivity of the code graph would no more be emerging, rather constructed ad hoc. I.e.: ad hoc solution. On the other side, the basic idea is analogy. Properly, to generate content that is adequate to expression means to find relation among things and to exploit these relations.
"""
