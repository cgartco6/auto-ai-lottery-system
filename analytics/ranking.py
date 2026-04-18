from collections import Counter

def rank_combinations(combos):

    counter = Counter(combos)

    ranked = counter.most_common()

    return ranked
