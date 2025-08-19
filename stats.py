
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

def sort_on(chars):
    return chars["num"]

def get_sorted_list(char_dict):
    list_of_dicts = []
    for c in char_dict:
        list_of_dicts.append({"char": c, "num": char_dict[c]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

