"""
Once we have the World, it is possible to thing about its representation.
The assumption has been that a part of the world is used as expression for another part fo the world.
Classic cryptography provides a starting example.
A substitution cipher (dates back to Julius Caesar, cf. Poe's The Gold-Bug) is a basic cryptographic technique that associated a letter to another letter.
Typically, there is shift rule that compactly describe the operation, based on alphabetical order.
So, in a shift by 3, an A becomes a C.
But let us suppose a substitution in which each character another is associated to another character.
To make it easy, let us create a random sequence of character.
"""
import random

def makeWorld(stk, dimension, seed = 1932):
    random.seed(seed) # seeding the random generator
    world = []
    for i in range(dimension):
        world.append(random.choice(stk))
    return world

def aggregateWorld(world):
    agg = ""
    for st in world:
        agg = agg+st
    return agg

"""
The following create an expression form: a random sequence of chars
"""
def makeEF(seed = 1932):
    random.seed(seed)
    ef = [chr(i) for i in range(97, 123)]
    return random.sample(ef, len(ef))

"""
The following, instead, given a world, its set of stoicheia, and an expression form, creates an expression
"""
def makeExpression(world, stk, ef):
    return [ef[stk.index(x)] for x in world]

stk = [chr(i) for i in range(97, 123)] # stoicheia
world = makeWorld(stk, 100)

ef = makeEF()
print(ef)
rep = makeExpression(world, stk, ef)

print(aggregateWorld(world))
print(aggregateWorld(rep))

"""
This cryptographic example is oversimple, nevertheless it has some interesting feature:
- it is a typical example of code (Eco's s-code) as an association between two list
- it is a typical example of a specif labour: replica. Each character is a perfect replication
- it is a typical case of ratio facilis. As Eco says, a machine working by ratio facilis can produce expression even without having any information concerning its content. It could properly work by itself, generating expression that do not match any state of the world. A random string from ef is a possible expression. Better, it is an expression of a possible content.

As Eco says, in the case of ratio facilis, “objects could be produced by a suitably instructed machine which only knows expressions, while another machine could assign to each expression a given content, provided that it was instructed to correlate functives” (ATS:219);

- there is a perfect isomorphism between representation and world (cf. Eco's total reversibility). In fact, it is possible to define a reverse function that returns the world from its representation:
"""

def getWorld(representation, stk, ef):
    return [stk[ef.index(x)] for x in representation]

print(aggregateWorld(getWorld(rep, stk, ef)))

"""
In our case, stk represents content types and ef expression types. They in fact can have various occurrences in the representation and the world.
An evidently open issue is that we are mixing referent and content. Or, better, properly at the moment there is no difference.
But one could also say that there is no difference between expressions and referents.
On one side, expressions, like contents, are parts of the world. If not, the Monism principle would not have been respected.
On the other side, expressions and contents both have a form that specifies some relevant features with respect to the world, so that they can be distinguished.
"""

"""
First of all, let us break the symmetry.
Let us suppose that we encode couples: we have 26 x 26 = 676 possible couples.
The following is a clumping function
"""
def clump(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]
clump(world, 2)
"""
A new expression system, created from previous one (in order not to motivate the expression via content)
"""
newEf = []
for s in ef:
    for c in ef:
        newEf.append([s,c])
"""
newEf contains 676 couples. Now we redefine makeExpression
"""
def makeExpression(world, stk, ef):
    newWorld = clump(world, 2)
    return [ef[ef.index(x)][0] for x in newWorld]

representation = makeExpression(world, stk, newEf)
len(representation)
"""
If we find [a,b] in the World, we represent it (only) with a. The same would happen for all couples starting with a.
The new representation has a lenght of 50. But it does not represent THE World. Rather, it represent 50 x 26 worlds.
E.g. we find in expression a, it could be [a, a], [a, b] and so on.
This is idea is worth a further exploration.
"""
