"""
1. The World and hence the Mind

If the basic point is to to start from a small world, we have to define Eco's stoicheia so to be able to use the same elements to create an interpretation.
The first assumption is that our World is made of characters, combined in a string.
An interpretation is thus something associated to pieces of the World and made up of the same things, i.e. characters.
Hence, the interpreter is something that put together pieces of the World. This is classic in semiotics: the two planes of expression and content. For Eco, the Hjelmslevian purport is, so to say, locally coupled by the semiotic function that associates two blocks, hence defined E and C.
As a side note, the Interpreter should be made up with the same pieces of the World, otherwise it would be literally alien to the world.
As the experiment is performed in the Python language, it could be interesting to use its building blocks. Now, as most programming languages (as far as I know), Python use basically the ASCII character encoding system, that uses a 7 bit encoding, reserving the subset (first 32) to control characters (non printable) while encoding 95 printable characters. For sake of simplicity I will stick to the latter.
we get them in this way:
"""

stk = [] # stoicheia
for c in range(95):
    stk.append(chr(c+32))
"""
Stoicheia are:
' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'

To make things easier (but not different) we skip some special character that disturbs string construction, such as:
", ', \
"""
stk = [ st for st in stk if st not in ["\"", "\'", "\\"]]

"""
A world is a random (as far as we know) sequence of stoicheia. As an example, a small world of 100 elements is
"""
import random # a module with random functions
world = []
for i in range(100):
    world.append(random.choice(stk))


"""
We get e.g. this:

['N', '<', '-', 's', 'C', 'J', 'Y', 'k', '4', ',', '(', 'T', '0', 'L', '6', 'u', '>', '3', 'O', '6', '0', 'h', '9', '1', '#', 'j', '^', 'M', 'A', 'Y', '^', '6', ']', '|', ';', 'w', 'm', 'x', '@', 'o', 'r', 'C', 'C', '-', '!', 'R', ' ', 'a', ';', 'O', '}', '.', 'R', '0', '/', 'c', '<', ';', '`', 'M', 'n', '1', '4', '(', ']', 'd', '{', '%', '(', '7', '-', 'e', '7', '*', ')', 'z', '`', 'f', 'X', '{', ':', '`', 'p', 'i', 's', 'M', '?', '}', 'p', 'm', 'J', 'L', 'v', '^', 'h', 'W', 'r', 'E', 'b', 'w']


Better define an aggregateWorld function that creates a single string, just for visualization
"""

def aggregateWorld(world):
    agg = ""
    for st in world:
        agg = agg+st
    return agg


"""
We get e.g. the following for our world:

N<-sCJYk4,(T0L6u>3O60h91#j^MAY^6]|;wmx@orCC-!R a;O}.R0/c<;`Mn14(]d{%(7-e7*)z`fX{:`pisM?}pmJLv^hWrEbw

Let us make a world creator at this point:
"""

def makeWorld(dimension):
    world = []
    for i in range(dimension):
        world.append(random.choice(stk))
    return world

"""
So we can write:
"""

world = makeWorld(100)
"""
Every time we get a different world, such as

"oLCu{k@u=f5T`%GPZV-70!UCNbB]FC=;sruhsOOw^[&Nps_9,M*y-MXY.s$QrDODay^Z)QCEl]gHVp57knEkVbMv8#18M)7t>bQk"

to be persistent, we can seed the random generator. So we rewrite the makeWorld func
"""


random.seed(1932)
world = makeWorld(100)
print(aggregateWorld(world))
random.seed(1932)
world = makeWorld(100)
print(aggregateWorld(world))


def makeWorld(dimension, seed = 1932):
    random.seed(seed) # seeding the random generator
    world = []
    for i in range(dimension):
        world.append(random.choice(stk))
    return world

print(aggregateWorld(makeWorld(100)))
## same first 100 st
print(aggregateWorld(makeWorld(1000)))
"""
@YtUG`0=<gFJrl{%Cw>Gu5%jJA}+l$[nWfCLIh-3f0AX>AId|NCD^,wQNa6TOqer}v ~bN (;lkR_#-Ug5^(fl{?=qzz%}nie O}

@YtUG`0=<gFJrl{%Cw>Gu5%jJA}+l$[nWfCLIh-3f0AX>AId|NCD^,wQNa6TOqer}v ~bN (;lkR_#-Ug5^(fl{?=qzz%}nie O}6p85bF=IM{KU$(m7XOn}NEYp3qeBKf0(*eCw8)iIu16McEi0%8p=vDtJ]AGR5`7$CIcZr,Y3_$D>L!Gi8h&T5fWmU{3ZZA|~L9,@Z5+G<.eS:@~w]^ q. hL-V7f0K]s^,_UTlfGpN_E##QA&t,^Mlc=tN?L-f5M|aP~yvq}5MM2`@?U9NZ&<W.uz!N;!>0m,OFZ,k/ @+)uAmg*Hv1q+^{&)RZj#RZ/T/PT_/|L0N+ab.w;^75uzmNRl~@[]<y:(+*>]b$ Q$CggmSOdMVxCi_#+]QjvLpVA+<99D=<5$;}+3XOPJCl)@_H!gCvqQ@ra2BlzSCCkwL8!A`J5~eXf*}Yg|DA{I1L?(3o]Jvmn8wB>N0]_h2320}ao}}/8LAA[vdc[D/NN[bi}DcUz2z<&n$uBJ<BgHAC]omSPrMP0G0B? S-2p1xQTPXCbQ#suU6BaEJ{8ats~&7cin*}Eg|?nZj7u7[}UeDesp)1>F)~NpL24Mdd9%P)})@*LLWqmKF0Gf@lV%>v4+v*pwW {aEg:&SOXQ}zdUG;kUACf^|7eart3<<MuV8t#S2W!AK$<MaZ,&`Lm0*S{ajZ4i lO0:z22sXE<XcQ$8pyRw,/+H3(g}+j(VefkEH3];&,ZER?/?PDIYl(N+XQ)#OioIk*yx/;(*dFl@>i7eP&1Vv9u0_[{vobugc-_Iw{5e/?%{%49U!sa8j8]ccrRXD+i~D+j4ZJ&&/>LTf8*)QS1;bS8%W%.~UE7$W(cgZ@[4=6xOK{ML</_6=0p#f#VOVd}/_L!0e7iIEZ8F8`*}ac<R~R@.I[Sa6Yd-RJa7._z8md^98nJ 584t+-:48R%,wW]9 i3Xq2SR=Hm~w*zW@iPl1#/6AX:j_/APtT?~ !}I+/Y!cyV?6IUl

"""

"""
Obvious observation: the World here is made up of the same stuff of the metalanguage we are using to describe it.
The latter is a specific arrangement of the first.
The World here is a sequence, but, of course, this is not an issue. (One may also simply speculate that the World is folded in various ways).
"""

"""
NOTE: simply more functional
"""
import random
def makeWorld(st, dimension, seed = 1932):
    random.seed(seed) # seeding the random generator
    world = []
    for i in range(dimension):
        world.append(random.choice(st))
    return world

def aggregateWorld(world):
    agg = ""
    for st in world:
        agg = agg+st
    return agg

world = makeWorld(stk, 100, 1932)
print(aggregateWorld(world))
