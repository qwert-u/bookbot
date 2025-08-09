
def get_num_words(text):
   num_words = len(text.split())
   return num_words

def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars