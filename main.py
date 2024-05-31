def main():
    path = 'books/frankenstein.txt'
    file = read_text(path)
    num_words = count_words(file)
    chars_dict = char_count(file)
    chars_list = convert_dict(chars_dict)
    sorted_list = sort_list(chars_list)

    print(f'--- Begin report of {path} ---')
    print(f'{num_words} words found in the document')
    print()
    for dict in sorted_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print('--- End report ---')

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    chars = {}
    for char in file_contents.lower():
        if char.isalpha():
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return chars

def convert_dict(chars_dict):
    list = []
    for chars in chars_dict:
        list.append({'name': chars, 'num': chars_dict[chars]})
    return list

def sort_on(dict):
    return dict['num']

def sort_list(chars_list):
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def read_text(path):
    with open(path) as f:
        file = f.read()
    return file

main()

