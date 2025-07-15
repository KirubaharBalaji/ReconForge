def parse_inputs(names, nicknames, pets, locations, hobbies, important, mobiles, dob, extra_dates):
    base_words = list(set(
        names + nicknames + pets + locations + hobbies +
        important + mobiles
    ))
    if dob:
        base_words.append(dob)
    for d in extra_dates:
        if d and len(d) == 8 and d.isdigit():
            base_words.append(d)
    return base_words
