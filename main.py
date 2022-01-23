import services.match
from services.match import *
import itertools
import math
from operator import attrgetter
    
def run(length, compare):
    if not isinstance(length, int):
        raise TypeError("Word length must be an integer.")
    if length < 4 or length > 15:
        raise ValueError("Word length must be between 4-15.")
    if not isinstance(compare, int):
        raise TypeError("No. of words to compare must be an integer.")
    if compare < 2:
        raise ValueError("No. of words to compare must be at least 2.")
    
    with open("./input/dictionary.txt", "rt") as f:
        sol_raw = f.read().splitlines()
    
    sol = []
    for word in sol_raw:
        if len(word) == length:
            sol.append(word)
            
    match_comb = itertools.combinations(sol, compare)
    good_set = []
    threshold = int(math.ceil((2-pow(2,1-compare))*length))
    threshold = 0
    for comb in match_comb:
        comb_match = match(comb)
        if comb_match.cover >= threshold:
            good_set.append(comb_match)
            
    #good_set.sort(key=len)
    max_coverage = max(comb.cover for comb in good_set)
    for x in good_set:
        if x.cover == max_coverage:
            print(x)

if __name__ == "__main__":
    length = 11
    compare = 3
    run(length, compare)
