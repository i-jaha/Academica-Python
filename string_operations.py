def count_vowels(str):
    vowels = "аеиоуыэюяaeiouy"
    count = 0
    for i in str.lower():
        if i in vowels:
            count = count + 1
    return count

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):
    return str == str[::-1]

def capitalize_string(str):
    words = str.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)