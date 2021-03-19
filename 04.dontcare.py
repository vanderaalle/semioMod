"""
John Holland has worked on adaptive systems.
He has proposed a framework in which the environment or other agents send messages to an agent.
The agent has a set of rules that allows it to extract information from these messages.

Holland's format uses bits: all the world is encoded in terms of {0,1}.

An important element is credit assignment. If the message is matched by a rule (let us call it a sign function) it receives some credit.
This means that the rule is adequate to the message.

if a rule matches a message -> then the associated behaviour is triggered

in our case:

aghsuj -> do something

Two observations:
- In the crypto environment, rule is a fixed set of chars (of 1 char lenght)
- do something (a pragmaticist -maybe- perspective) is undefined, we can say that it simply generate a different arrangement of stk, following the Monist principle (a content)

Holland proposed to add to his bit alphabet ({0,1}) the # sign, so-called "don't care" symbol.
It means that each character can be placed at the # position. As # stands for comments in Python, I will use the dot "." (still an ASCII symbol).

so, a type like

agh.uj

matches all messages having whatsoever char in the . position while having the provided chars in the other positions.
Properly we have a notion of relevance (Prieto) or the selection of distintive features (cf Jakobson with phonology)

In the basic cryptographic example, the World provides expressions to be traced back to expression forms, and expression forms are associated to content forms that lead to contents.

But if we use dontcare symbols we add a certain indeterminacy.
So, in

can.:hund

the : stands for the semiotic function

maybe

can.:h.nd

The latter is not Holland's framework, because in the latter matching rules (with dontcare symbols) are used to trigger specific behaviours.
But the idea can be generalised as a double matching system. It must be observed that such a system still implements total reversibility between E and C. And it still describes a replica labour.

or "insiemi espressivi and nebulose di contenuto"
Can we implement this?
"""
