"""
Moving from cryptography back to some more standard semiotic things.
"""

import random

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

"""
Code is a dictionary coupling fE and fC, i.e. types, into sign functions. It uses the "." char as a dontcare symbol.
Hence on, I will use triplets. This is a design choice that has proven to be apt but of course it can be easily generalized.
"""
code = {
"awa":"bbf",
"z.z":"g.g",
"k.k":"c.c",
"l..":"ooo" # expression form and content form
}

"""
Let us focus for the moment on expression.
Processing is made easy thanks to so-called regular expressions (regexp, regex, re), i.e. a notation for pattern matching in strings.
Here we import two different modules.
The first is the standard regex module that finds regex into a string.
The second reverses the process: from regex creates strings.
"""
import re
import exrex

re.findall("awa", aggregateWorld(world))

"""
Technicalities: the "." symbol in a regex matches all available symbols. More than those allowed by our alphabet stk.
So we convert them.
"""

""" a converter """

def convertType(type, stk):
    seq = ""
    for i in stk:
        seq = seq+i
    return type.replace(".", "["+seq+"]")

newR = convertType("a.a", stk)

""" the interpreter is a dictionary of converted rules """
def convertTypes(code):
    cCode= {}
    for r in code:
        e = convertType(r, stk)
        c = convertType(code[r], stk)
        cCode[e] = c
    return cCode

code = convertTypes(code)

"""
Now we define an interpretation function
"""

def makeInterpretation(world, code):
    interpretation = []
    for d in code:
        matched = re.findall(d, aggregateWorld(world))
        for m in matched:
            cnt = code[d]
            interpretation.append([m, exrex.getone(cnt)])
    return interpretation



interpretation = makeInterpretation(world, code)

"""
Interesting aspects in the model.
i) the presence of dontcare symbols differentiates types. On one side, both ef and cf may contain or not dontcares. On the other side, a sign function may include open and/or closed types.
We could say that a type without dontcares is a closed type. Conversely, a type with dontcare symbols is an open one.
A closed sign function has both closed types. A partially closed sign function has one closed type (on E or C).
The cryptographic interpreter has thus all double closed types, on E and C, i,e. all closed sign functions. It represents the maximally deterministic interepretation, what is generally thought as the model of "code". We can call such a code as "c-code", closed code, vs. "o(pen)-code".
ii) the replica labour is still at work. There is no motivation between E and C apart from their established relation.
Technically speaking with Eco, we do not need semantic instructions to generate expressions (in fact, we can generate expression from expression types using using regex).
iii) an interpreter is a set of sign functions (code) plus an interpretation procedure (algorithm: makeInterpretation). These sign functions can be of various kind.
iv) recognition is the task of the interpreter.
v) closed and open types allows to differentiate the mode of articulation. If we stick to E, a closed type evidently strictly describes exhaustively the expression (cf. allography in Goodman). If the type is open, there is a variable amount of freedom in expression. So, the axis allography vs. autography is a continuum (or a gradatum). Properly, it can even receive a score, as it is enought to count the number of ".". If it is = 0, it is strict allography (closed type), but in our case the degree of freedom can be 1 or even 2, a variable autography.
vi) the last observation has avoided the opposite case. Let us consider a sign function like: "...":"wow".
Now this E-type is fully open. It matches everything. And generate as a content: wow. Stupor mundi. It matches all the expressions. Everything can lead to interpretation, is significant, so to say. This always works, but intuitively it works poorly.
Following a suggestion by Holland, we can consider the specificity of a type as the number of chars vs dots, and we can assing a type score. So, the "..." has specificity = 0. This might be generalised to interpretation. On one side, the same happens on C type. Suppose we have "aaa":"...". A certain expressions leads to whatsoever content. Deconstruction? Overinterpretation? The C type has a specificity = 0. So, inspired by Holland, we can propose an interpretation score resulting from the product E specificity x C specificity. In both our previous case, the total score is, respectively, 0 x n and n x 0 = 0. But in general "catch-all" "..." types (both as E and C) result in an interpretation score = 0. The most bizarre theoretical case is the sign function "anything goes": "...":"...". It matches everything and it means everything. Its score is 0 x 0 = 0.
"""

def calculateSpecificity(type):
    return len(type)-type.count(".")

calculateSpecificity("...")

"""
Here we redefine convertTypes to store interpretation score
"""

def convertTypes(code):
    cCode= {}
    for r in code:
        e = convertType(r, stk)
        c = convertType(code[r], stk)
        specificity = calculateSpecificity(r)*calculateSpecificity(code[r])
        cCode[e] = [c, specificity]
    return cCode

code = {
"awa":"bbf",
"z.z":"g.g",
"k.k":"c.c",
"l..":"ooo" # expression form and content form
}
code = convertTypes(code)

def makeInterpretation(world, code):
    interpretation = []
    for d in code:
        matched = re.findall(d, aggregateWorld(world))
        for m in matched:
            cnt = code[d]
            #print(cnt)
            interpretation.append([m, exrex.getone(cnt[0]), cnt[1]])
    return interpretation


interpretation = makeInterpretation(world, code)

def calculateInterpretationScore(interpretation):
    return sum([x[2] for x in interpretation ])

calculateInterpretationScore(interpretation)
