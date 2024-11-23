# Juniper Vermillo
# CIS 129
# 11/22/2024
# Palindrome_JuniperVermillo_Lab8.py
"""Determines whether or not an inputted word is a palindrome or not"""

def input_word():
    """Prompts the user to input a word"""
    word = input("Input a word to see if it is a palindrome: ")
    while len(word) < 1:
        word = input("Please input a word: ")
    return word

def is_palindrome(word):
    """Creates a reversed version of the inputted word, then compares the two if they are different or the same"""
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[(len(word) - 1) - i]
    if reversed_word.lower() == word.lower():
        return True
    else:
        return False

def palindrome_result(word):
    """Prints the result of the is_palindrome function"""
    result = is_palindrome(word)
    if result == True:
        print(f"{word} - Is a Palindrome")
    else:
        print(f"{word} - Not a Palindrome")

def main():
    word = input_word()
    palindrome_result(word)

main()