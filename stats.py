def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    char_counts = {}
    for character in text:
        character = character.lower()
        if character not in char_counts:
            char_counts[character] = 1
        else:
            char_counts[character] += 1
    return char_counts

def sort_on(dict_item):
    return dict_item["count"]

def get_character_report(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
