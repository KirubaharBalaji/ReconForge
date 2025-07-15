import streamlit as st
from generator import generate_wordlist
from combo_generator import generate_combos

st.set_page_config(page_title="PassForge", layout="centered")
st.title("🔐 PassForge - Custom Wordlist Generator")

def multivalue_input(label, help=None):
    raw = st.text_input(label, help=help)
    return [item.strip() for item in raw.split(',')] if raw else []

# Inputs
st.header("🎯 Recon Inputs")
names = multivalue_input("Names (comma-separated)", help="e.g., Aarav, Anika")
nicknames = multivalue_input("Nicknames (comma-separated)", help="e.g., Silenz3, Ray")
pets = multivalue_input("Pets (comma-separated)")
locations = multivalue_input("Locations (comma-separated)")
hobbies = multivalue_input("Hobbies (comma-separated)")
important = multivalue_input("Important People (comma-separated)", help="e.g., Meera, Karthik")
mobiles = multivalue_input("Mobile Numbers (comma-separated)")
dob = st.text_input("Date of Birth (DDMMYYYY)", help="e.g., 01012000")
important_dates = multivalue_input("Important Date(s) (DDMMYYYY, comma-separated)", help="e.g., 14022020, 01012018")

usernames = st.text_input("Usernames for Combo List (comma-separated)", help="Optional for combo list")

depth = st.selectbox("Mutation Depth", [1, 2, 3, 4, 5], index=2)

max_len = st.slider("Max Word Length", 6, 32, 16)
shuffle = st.checkbox("Shuffle Wordlist")
gen_combo = st.checkbox("Generate Combo List")
base_name = names[0].replace(" ", "").lower() if names else "output"
if st.button("🚀 Generate"):
    input_data = list(set(names + nicknames + pets + locations + hobbies + important + mobiles))
    
    # Validate DOB
    if dob and dob.isdigit() and len(dob) == 8:
        input_data.append(dob)

    # Validate important dates
    valid_dates = [d for d in important_dates if d.isdigit() and len(d) == 8]

    # Generate wordlist
    wordlist = generate_wordlist(
        base_words=input_data,
        max_length=max_len,
        shuffle=shuffle,
        depth=depth,
        dob=dob,
        extra_dates=valid_dates
    )
    
    st.success(f"✅ Wordlist Generated: {len(wordlist)} entries")
    wordlist_text = "\n".join(wordlist)
    st.download_button("⬇ Download Wordlist", wordlist_text, file_name=f"{base_name}_wordlist.txt")

    combo_text = ""
    if gen_combo and usernames:
        username_list = [u.strip() for u in usernames.split(',')]
        combos = generate_combos(username_list, wordlist)
        combo_text = "\n".join(combos)
        st.success(f"🔐 Combo List Generated: {len(combos)} entries")
        st.download_button("⬇ Download Combo List", combo_text, file_name=f"{base_name}_combos.txt")

    # Combined download (Wordlist + Combos)
    if wordlist_text:
        combined = f"=== Wordlist ===\n{wordlist_text}"
        if combo_text:
            combined += f"\n\n=== Combo List ===\n{combo_text}"
        st.download_button("📦 Download Both Files Combined", combined, file_name=f"{base_name}_combined.txt")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by PassForge | Streamlit GUI + CLI Ready")
