def main():
    list_nums = [1,2,3,4,5,6,7,8,9,10]

    set_pairs = {num for num in list_nums if num % 2 == 0}
    print(set_pairs)

    vowels = "aeiou"
    dictionary = {vowel.lower(): vowel.upper() for vowel in vowels}
    print(dictionary)

if __name__ == '__main__':
    main()
