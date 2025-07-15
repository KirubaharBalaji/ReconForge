import random
from mutations import apply_mutations

def generate_wordlist(base_words, max_length=16, shuffle=True, depth=5, dob=None, extra_dates=[]):
    mutated = apply_mutations(base_words, dob=dob, depth=depth, extra_dates=extra_dates)
    filtered = [w for w in mutated if len(w) <= max_length]
    if shuffle:
        random.shuffle(filtered)
    return filtered
