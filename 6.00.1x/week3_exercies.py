# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 05:01:45 2020

@author: scker
"""

#odd Tuples
def oddTuples(aTup):
    """
    aTup: a Tuple
    returns: tuple, every other element of aTup.
    """
    odds = ()
    iters = 0
    for t in aTup:
        if iters % 2 == 0:
            odds += (t,)
        iters += 1
    return odds

eval = oddTuples(("I", "am", "a", "test", "tuple"))
print(eval)

#%%odd tuples, less code
def oddTuples(aTup):
    """
    aTup: a Tuple
    returns: tuple, every other element of aTup.
    """
    return aTup[0::2]
eval = oddTuples(("I", "am", "a", "test", "tuple"))