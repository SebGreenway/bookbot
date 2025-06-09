from stats import word_count, character_count, sort_characters, display_results

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        book_text = get_book_text(book)
        word_count_result = word_count(book_text)
        character_count_result = character_count(book_text)
        sorted_characters = sort_characters(character_count_result)
        display_results(book, word_count_result, sorted_characters)
        #print(f'{word_count_result} words found in the document')
        #print(character_count_result)
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error has occured: {e}')

book = 'books/frankenstein.txt'

main()
