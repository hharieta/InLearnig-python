def anagram(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())


def main():
    r = anagram("ane", "Ena")
    print(r)


if __name__ == '__main__':
    main()
