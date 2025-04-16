def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = list(text.lower())
    char_counts = {}

    for char in characters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts


def sort_dictionary(dictionary):
    output_list = []
    for k in dictionary:
        output_list.append({ "char": k, "count": dictionary[k] })

    def sort_by_count(item):
        return item["count"]

    output_list.sort(reverse=True, key=sort_by_count)

    return output_list