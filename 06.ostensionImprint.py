"""
Recognition is here intended as a meta-labour.
The replica labour is weakened as it can still describe the s-code but that at the same take into account a variable degree of determinism.
What about ostension and imprint?
The two labours can be thought, together wth replica, as a typology of sign functions.
Ostension occurs when a given object [...] is picked up by someone and shown as the expression of the class of which it is member.
A typical aspect of ostension is “homomateriality” between the expression and the possible referent, says Eco.
That is, in ostension the object is “viewed as an expression made with same stuff as its possible referent” (ATS: 224).
How to define ostension in our particular model?
Let us consider this sign function:
"aab":"aac"
E-type and C-type share two chars in the same position. Same position is important because in a small stk set the simple presence, regardless of position, is indeed a poor characterization. The same position means that possibly a whole char block is in both types.
What does the presence of a block both in E and C mean? That the block as an expression stands for the block its content.
Ostension and homomateriality are coupled in Eco's typology, as the only sign functions to feature homomateriality result from ostension labour.
In our model, ostension is again turned into a degree. There is, in fact, a degree of ostension depending on the number of shared chars in the same position. Thus:
"abc":"def" has a degree = 0
"abc":"aef" has a degree = 1
"abc":"abf" has a degree = 2
By the way, by using dontcare symbols a sign function like
"abc":"de."
may have a certain ostension degree or not, depending on the resulting token. A sort of accidental ostension component.
One could say that the ostension degree is 1(dot)/len(stk).
It could be possible to compute the ostension degree from the amount of dontcare symbols. In that case, ostension represents only a feature explicitly provided by a type homology.
The maximal case of ostension happens when the two types coincide, as in:
"abc":"abc"
Is there a viable example of such a situation? The expression is mirrored in the content. While it is not necessary to find a real example for specific case in a simple, abstract model kike ours, still let us consider the case when an object stand exactly for its class.
A sample of an object (e.g. a scarf shown in a shop) represent exactly the scarf.
A code made up of only pure ostensions mirrors exactly that part of the world that it represents. Debate on ostension and its limits seems to be aptly represented by such a paradoxical situation.
But a piece of cloth representing the cloth does not mirror the cloth in itself, so it might be represented by something like this
"abc":"abd"
An explicit notation for ostension coul be provided, like this:

"abc":"O.__"

In the previos, the "O" char is a special char (like "."") that specifies that the following is an ostension. The char O is followed by the description, in which another special symbol, "_", requires to copy the char from E-type into C-type, resulting in

"abc":".bc"

Special notation clearly differentiates ostension from the previous sign function, that can be thought as an implicit form of ostension. We need a special fuction to expand ostension into a standard type, such as:
"""

def expandOstension(eType, cType):
    cType = cType[1:] # skipping O
    ls = [eType[x] if cType[x] == "_" else cType[x] for x in range(len(cType))]
    st = ""
    for x in ls:
        st = st+x
    return st


expandOstension("abc", "O.__")

"""
Such a notation requires to rewrite the function that converts code into a parsable form. More on this later.

Let us consider the remaining labour: invention.
If ostension has a strong theoretical link with homomateriality, imprint is the classic pivotal element in discussing ratio, the type-token relation. Ratio can be facilis or difficilis. As we know, it is facilis if there is no specific relation (recognized) between our two types. On the other side, in case of ratio difficilis, the point is that the expression is motivated by the content.
This has a twofold explanation in Eco:
i) there is a causal link. A fact of the world is recognized as an imprint (E) if it can be traced back to a causal framework. An imprint is the sign of the (past) presence of an "imprinter", so to say with a barbarism.
ii) by considering such a backtracking ("backtracing", so to say) problem, that applies to imprint, Eco proposes a sort of Turing test:
- in the case of ratio facilis, “objects could be produced by a suitably instructed machine which only knows expressions, while another machine could assign to each expression a given content, provided that it was instructed to correlate functives” (ATS:
219);
- on the contrary, in the case of ratio difficilis, “a machine instructed to produce these objects should be considered to have also received semantic instructions. One might say that since it is instructed to produce expressions, it is being fed with schematic semantic representations” (ATS: 219)

In SFL Eco adds that in ratio difficilis “provided that the projection rule is constant, the results obtained by manipulating the expression are diagnostic or prognostic with respect to the content” (SFL: 45, transl. by me, as the section is absent from the English edition).


So, the process of inferring the ratio may works like this:
i) collect the objects as expression-units;
ii) abduct a production rule for expression (the modus operandi for the Expression Generator);
iv) manipulates the abducted Expression Generator;
v) check if there are or have been (prognosis/diagnosis) changes in the content of the resulting sign-function.
vi) In the positive case: it is a machina difficilis, where the Content Generator shares the same type with the Expression Generator; otherwise it is a machina facilis, where Content- and Expression Generators have each their own type.

While imprint is a type of sign function, invention is a labour.
Eco, says:
“If, in Table 39, imprints (even if accidentally replicated rather than recognized) were not been classified as straightforward transformations under the heading of inventions, this was for good reason. In the case of an imprint the content-model already exists. [...] When replicating an imprint one is mapping from something known” (TSG:314).
Long story short:
- inventions and imprint share a feature: content and expression share (part of) the type.
- imprint are conventional, inventions not (yet).

In our model, there is at the moment no place for type creation ex nihilo, that is, for learning, that is, for emergence of new sign functions, that is, for adaptation.
I will thus use imprint as the general term for invention (a too generic term, IMHO).
To describe this type of sign function, I propose as a feature the presence of a procedural mapping between the types on both side.
In short, there is a rule (a generative procedure) that allows to get from E type the C type. The E type becomes "diagnostic" of the C type.

The introduction of such a feature makes the notation much more difficult than ostension.
In fact, any algorithm can connect types. How to notate it?

Let us consider this case:
"abc":"bcd"
Here  the rule connecting the types is evident. Each char in E is replaced by the next alphabetic char in C. A reverse function allows to map C to E.
The following list comprehension gets the desired result and leave unchanged "." symbols.
"""

a = "ab."
[chr(ord(x)+1) if x != "." else x for x in a]

"""
Assuming for convention that each char is represented by c and the type by eType we can write something like:
"ab.":"[chr(ord(c)+1) if c != \".\" else chr(ord(c)) for c in eType]"

The notation is concise but complex. But I have no better idea about how to encode automatically a mapping procedure into a short string.
As in ostension, such a notation requires a replacement procedure to get the actual result. We prepend an I to the rule as we did with O in ostension.
"""

def expandImprint(eType, cType):
    ls =  eval(cType[1:])
    st = ""
    for x in ls:
        st = st+x
    return st

expandImprint("ab.","I[chr(ord(c)+1) if c != \".\" else c for c in eType]")

"""
To sum up, we have three plus one labours:
- recognition as a framing labour, i.e. the labour assigned to the interpreter that properly extract contents from the world
- replica acts as an association between types, with no special relation apart from association.
- ostension include a subset (position matters) of the type in E in the type C
- imprint (or invention, same here) is described by a procedure mapping (partially etc) type E into type C.
An interpreter is described as i) an intepreting procedure plus ii) a code mapping E to C.
In order to have a working procedure we need to convert the code specification into a regex pattern, as we did for the "." symbol.
"""

stk = [chr(i) for i in range(97, 123)]

def convertType(type, stk): # was: convertType
    seq = ""
    for i in stk:
        seq = seq+i
    return type.replace(".", "["+seq+"]")

"""
Note that in the following we have lost specificity, as the function to calculate it should be reimplemented. Not relevant at the moment.
"""
def convertTypes(code, stk):
    cCode= {}
    for r in code:
        if code[r][0] == "I":
            c = expandImprint(r, code[r])
        elif code[r][0] == "O":
            c = expandOstension(r, code[r])
        else:
            c = code[r]
        c = convertType(c, stk)
        e = convertType(r, stk)
        #specificity = calculateSpecificity(r)*calculateSpecificity(code[r])
        cCode[e] = c
    return cCode
code = {
"z.z":"g.g",
"a.c":"O__d",
"m.p":"I[chr(ord(c)+1) if c != \".\" else c for c in eType]",
}
convertTypes(code, stk)
"""
The convertTypes procedure has been initially devised only as a technical procedure, to solve some empirical issues related to regex.
It concerned the implementation, not the formal model.
The expansion of ostensions and imprints shows an interesting feature. At the end, the converted code only shows replicas. And, in our example, they also share exactly the same structure. Of course, the required relations between E and C types are still present, but while in the code they were explicit, in the converted code are implicit, embedded into a standard replica model.
Again, has this difference a theoretical value? It may look like the interpreter is provided with various way to describe type relations, according to Eco's labour. This is significant, because it explicits various, possible relations between E and C to extract information (better and simplier in our context: to produce interpretation). They are part of the competence of the interpreter, rules to create content, and this feature may provide some hints in the context of sign function creation.
On the other side, the converted code shows the basic notion of sign: something stands for something else, aliquid stat pro aliquo. This notion is indeed captured by replica. Not by chance, semiotics as a discipline has extensively worked on such a paradigmatic case. In our model, the dontcare symbol weakens the deterministic strenght of the replica and "opens" the interpretation (as multiple outputs -contents- are possible, while matching multiple inputs, expressions).
"""
