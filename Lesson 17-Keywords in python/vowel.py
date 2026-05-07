word=input("Enter a word:")
def check_vowel(word):
    vowels="aeiouAEIOU"
    for var in word:
        if var in vowels:
            print(f"{var} is a vowel")
        else:
            print(f"{var} is not a vowel")
check_vowel(word)
            