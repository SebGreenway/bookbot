def word_count(book_text):
    return(len(book_text.split()))

def character_count(book_text):
    lower_text = book_text.lower()
    character_dic = {}
    for character in lower_text:
        if character in character_dic:
            character_dic[character] += 1
        else:
            character_dic[character] = 1
    return character_dic

def sort_characters(character_count_result):
    alpha_characters = {} 
    for character in character_count_result:
        if character.isalpha():
            alpha_characters[character] = character_count_result[character]
    return sorted(alpha_characters.items(), key=lambda item: item[1], reverse = True)

def display_results(book, word_count_result, character_count_result):
    output = (
        '============ BOOKBOT ============\n'
        f'Analyzing book found at {book}\n'
        '----------- Word Count -----------\n'
        f'Found {word_count_result} total words\n'
        '--------- Character Count ---------\n'
        +'\n'.join(f'{character}: {count}' for character, count in character_count_result) 
        +'\n------------- END -------------\n'
    )
    print(output)