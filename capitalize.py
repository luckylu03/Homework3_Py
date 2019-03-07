#Write a function taking in a string like WOW this is REALLY amazing 
# and returning Wow this is really amazing.

def filter_words(st):
    st = st.capitalize()
    while "  " in st:
        st = st.replace("  ", " ")
    return st.strip()