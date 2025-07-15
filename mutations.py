import re

# Depth 1 – Casing Variants
def casing_mutations(words):
    result = set()
    for word in words:
        result.add(word.lower())
        result.add(word.upper())
        result.add(word.title())
        result.add(to_camel_case(word))
        result.add(to_pascal_case(word))
        result.add(to_snake_case(word))
        result.add(to_kebab_case(word))
    return result

# Depth 2 – Symbol Variants
def symbol_combinations(words):
    symbols = ['@', '.', '-', '_']
    result = set()
    for word in words:
        for symbol in symbols:
            result.add(symbol + word)
            result.add(word + symbol)
            result.add(symbol + word + symbol)
    return result

# Depth 3 – Leetspeak and Reversals
def leetspeak_mutations(words):
    result = set()
    translations = str.maketrans('aAeEiIoOsS', '@433!10o$5')
    for word in words:
        result.add(word.translate(translations))
    return result

def reversed_mutations(words):
    return {word[::-1] for word in words}

# Depth 4 – Typos and Suffix/Prefix
def typo_mutations(words):
    result = set()
    for word in words:
        for i in range(len(word)):
            result.add(word[:i] + word[i+1:])  # remove one char
    return result

def suffix_prefix_mutations(words):
    extras = ['123', '!', '2023', 'pwd']
    result = set()
    for word in words:
        for extra in extras:
            result.add(word + extra)
            result.add(extra + word)
    return result

# Depth 5 – Advanced Mutations
def symbol_casing_combos(words):
    result = set()
    for word in words:
        result.add(word.upper() + "@")
        result.add(word.lower() + "#")
        result.add(word.title() + "!")
    return result

def recursive_date_fusion(words, dob, extra_dates):
    result = set()
    all_dates = []
    if dob:
        all_dates.append(dob)
    if extra_dates:
        all_dates += extra_dates

    for date in all_dates:
        if len(date) == 8:
            day = date[:2]
            month = date[2:4]
            year = date[4:]
            year2 = year[-2:]
            combos = [day, month, year, day + month, month + year2, day + year2, day + month + year2]
            for word in words:
                for c in combos:
                    result.add(word + c)
                    result.add(c + word)
                    result.add(word + "_" + c)
                    result.add(c + "_" + word)
    return result

def advanced_fusion_mutations(words):
    result = set()
    for word in words:
        result.add(word[::-1] + "!@#")
        result.add("$$" + word.upper())
        result.add("0_" + word + "_0")
    return result

# Common across depth 2 & 5
def date_variations(words, dob=None, extra_dates=None):
    result = set()
    dates = []
    if dob:
        dates.append(dob)
    if extra_dates:
        dates += extra_dates

    for date in dates:
        if len(date) == 8:
            day = date[:2]
            month = date[2:4]
            year = date[4:]
            short_year = year[-2:]
            combos = [
                day, month, year, short_year,
                day+month, month+short_year,
                day+short_year, day+month+short_year
            ]
            for word in words:
                for c in combos:
                    result.add(word + c)
                    result.add(c + word)
                    result.add(word + "_" + c)
                    result.add(c + "_" + word)
    return result

# Utility Functions
def to_camel_case(word):
    parts = re.split(r'\s|_|-', word)
    return parts[0].lower() + ''.join(w.title() for w in parts[1:])

def to_pascal_case(word):
    parts = re.split(r'\s|_|-', word)
    return ''.join(w.title() for w in parts)

def to_snake_case(word):
    return re.sub(r'\s+', '_', word.lower())

def to_kebab_case(word):
    return re.sub(r'\s+', '-', word.lower())

# 🔁 Apply All Mutations
def apply_mutations(words, depth=3, dob=None, extra_dates=None):
    mutated = set(words)

    if depth >= 1:
        mutated |= casing_mutations(words)

    if depth >= 2:
        mutated |= date_variations(words, dob, extra_dates)
        mutated |= symbol_combinations(words)

    if depth >= 3:
        mutated |= leetspeak_mutations(words)
        mutated |= reversed_mutations(words)

    if depth >= 4:
        mutated |= typo_mutations(words)
        mutated |= suffix_prefix_mutations(words)

    if depth >= 5:
        mutated |= symbol_casing_combos(words)
        mutated |= recursive_date_fusion(words, dob, extra_dates)
        mutated |= advanced_fusion_mutations(words)

    return list(mutated)
