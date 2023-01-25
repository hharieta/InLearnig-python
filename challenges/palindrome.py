
def palindrome(word: str) -> bool:
    w = ""
    for i in range(len(word)-1, -1, -1):
        w += word[i]
    
    return w == word

def main():
    r = palindrome("hola")
    print(r)


if __name__ == '__main__':
    main()
