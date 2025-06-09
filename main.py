def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    return(len(book_text.split()))

def main():
    try:
        book_text = get_book_text('books/frankenstein.txt')
        result = word_count(book_text)
        print(f'{result} words found in the document')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error has occured: {e}')

main()
