def generate_combos(usernames, passwords):
    return [f"{u}:{p}" for u in usernames for p in passwords]
