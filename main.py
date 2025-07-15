import argparse
from generator import generate_wordlist
from combo_generator import generate_combos
from exporter import export_to_file
from input_parser import parse_inputs

def parse_args():
    parser = argparse.ArgumentParser(description="🎯 PassForge - Custom Wordlist Generator")
    parser.add_argument("--names", nargs='*', default=[], help="Target names")
    parser.add_argument("--nicknames", nargs='*', default=[], help="Nicknames")
    parser.add_argument("--pets", nargs='*', default=[], help="Pet names")
    parser.add_argument("--locations", nargs='*', default=[], help="Locations")
    parser.add_argument("--hobbies", nargs='*', default=[], help="Hobbies")
    parser.add_argument("--important", nargs='*', default=[], help="Important people")
    parser.add_argument("--mobiles", nargs='*', default=[], help="Mobile numbers")
    parser.add_argument("--dob", help="Date of Birth (DDMMYYYY)")
    parser.add_argument("--extra_dates", nargs='*', default=[], help="Important Dates (DDMMYYYY)")
    parser.add_argument("--usernames", nargs='*', default=[], help="Usernames for combo list")
    parser.add_argument("--depth", type=int, default=3, choices=[1, 2, 3, 4, 5], help="Mutation depth (1-5)")

    parser.add_argument("--maxlen", type=int, default=16, help="Max password length")
    parser.add_argument("--combo", action='store_true', help="Generate combo list")
    parser.add_argument("--shuffle", action='store_true', help="Shuffle wordlist")
    return parser.parse_args()

def main():
    
    args = parse_args()
    base_words = parse_inputs(
        args.names, args.nicknames, args.pets, args.locations,
        args.hobbies, args.important, args.mobiles, args.dob, args.extra_dates
    )
    output_name = args.names[0].replace(" ", "").lower() if args.names else "output"
    wordlist = generate_wordlist(base_words, max_length=args.maxlen, shuffle=args.shuffle, depth=args.depth, dob=args.dob, extra_dates=args.extra_dates)
    export_to_file(f"{output_name}_wordlist.txt", wordlist)
    print(f"✅ Wordlist saved with {len(wordlist)} entries.")

    if args.combo and args.usernames:
        combos = generate_combos(args.usernames, wordlist)
        export_to_file(f"{output_name}_combos.txt", combos)
        print(f"🔐 Combo list saved with {len(combos)} entries.")

if __name__ == '__main__':
    main()
