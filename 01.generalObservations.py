"""
GENERAL OBSERVATIONS

1. What is this
The following research has an ambiguous status
- it is intended as a reflection on some semiotic concepts/constructs, in particular in relation to Eco's theories
- it is a sort of (tentative) demonstration of the semiotic richness of programming languages and of their usefulness as tools for semiotic research
- it is thought as an application in computational semiotics, or a possible way to think about a computational approach to semiotics
- it is a Gedakenexperiment, simply trying to define a very simple model and to study, empirically and partially, issues that result from it

2. Sources
Sources for the following observations are:

- U. Eco, Theory of modes of sign production (Trattato di semiotica generale). The second part of Eco's treatise is entirely devoted to a theory of sign production. The perspective is related to semiotic dynamics. The theory defines the way in which expressions are generated and related to contents. Eco describes four parameters: i) the physical labour to produce expression (various ways); ii) the type-token ratio (be it facilis or difficilis); iii) the continuum to be formed if it is shared or not between expression and referent; iv) mode and complexity in articulation. Interesting elements for our discussion:
-- signs are intended as sign functions, that is something the relates two planes
-- the parameters provide a compact organization for a sign function typology, that can be further explored
-- the focus is not on generic cognitive operations or on the description of contents (cf. Greimas), but specifically in how to produce expressions
-- recognition is a semiotic labour. This is interesting but paradoxical: in recognizing an imprint, the recognizer has not produced it. On the other side, when speaking of ostension, replica, invention, the theory assumes the perspective of the producer. This requires to explicitly double the perspective.

- U. Eco, Sulla generazione di messaggi estetici in lingua edenica. A neglected essay by Eco, originally in Le forme del contenuto, reprinted in the actual edition of Opera aperta (English version in The Role of The Reader). Here Eco starts (and departs) from the Grammarama project by Miller (1967).
The author's main interest is in a basic language made up of two symbols (A, B) and a grammar in the form (X, nY, X) that allows to generate well-formed strings (e.g. ABBBBBA, BAB, etc). Eco takes into account various states of the world denoted by a list of expressions in order to discuss how typical aspects of aesthetic (one could say: everyday too) usage of language can emerge even in such a simplified model. Particularly interesting points are:
-- the use of simple strings and a formally defined grammar to define a languages
-- the idea of a model in vitro to feed a Gedakenexperiment
(Note: in the preface, Eco still considers this essay as a major work)

- U. Eco, Sull'essere. Eco's most relevant late contribution to semiotics (Kant e l'ornitorinco) opens with a reflections on being (nothing less!). But also in this place, Eco propose a simplified model of the world that is thought as a set of "stoicheia" to be represented by a set of symbols in a Mind (interpreter). Eco takes into account various (quantitative) relations between these two sets: their cardinality and the ratios between cardinalities of the two sets.
Some interesting suggestions:
-- again, this is a Gedakenexperiment and it is performed by using discrete units
-- Eco considers the dualism implicit in the model just as a simplification. The Mind can be thought as made up of the same stoicheia of the World. Hence: the World represents itself (Eco adds: in animals, vegetables, and maybe also in minerals, i.e. in the "epifania silicea dei calcolatori"). This is a sort of Peircean Monism, and assumes dualism not ontologically but functionally, where function here, one could say, properly refers to sign function
-- Eco is still allergic to the problem of the origin of sign. Yet, it touches such a delicate point in various essays. Here too, this Mind/World model seems to open the issue. Not in historical or neuroscientific terms, rather in posing the issue of semiotic dynamics

- J. Holland, Hidden order. In his Ulam lectures, Holland (the father of genetic algorithms) describes various models, starting from communication between agents to reach a simplified but, on the other side, accurate model of ecological (multiagents, adaptive) environment. While this final model (called Echo) is far beyond the topics of my discussion (and beyond my competences), Holland first discusses models for communication and exchange of information with the environment and other agents. Interestingly:
-- again, the model can be thought as a way to perform Gedakenexperiment
-- Holland works exclusively with strings of symbols, to gain control over operations
-- it provides various way to deal with interpreting rules, meant as matching patterns between a certain state of the world and a state of symbols. An interesting case is the "don't care" symbol, that means that a certain pattern may have various symbols in a certain position so to match more than one string


3. Strategy
The research strategy includes:
- define simplified models using strings, still capable of capturing aspects of semiotic theory
- write everything in Python. Comments, as "semiotic insertions", allow to include text in the code (at least, in English). This can be seen, by the way, as a form of the so-called "Literate programming" (Knuth)
- use interactively programming as a way to experiment, by trials and errors. Also, to demonstrate the relevance of programming in semiotic research
"""
