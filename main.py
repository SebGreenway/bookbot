import sys
from stats import word_count, character_count, sort_characters, display_results

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        book_text = get_book_text(sys.argv[1])
        word_count_result = word_count(book_text)
        character_count_result = character_count(book_text)
        sorted_characters = sort_characters(character_count_result)
        display_results(sys.argv[1], word_count_result, sorted_characters)
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error has occured: {e}')

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)


main()
