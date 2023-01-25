
def repeat_letter(word:str) -> str | None:
    c = 0
    for i in word:
        letter = i
        for j in word[c+1:]:
            # print(j)
            if j == letter: return j
        
        c += 1
    
    return None


def main():
    r = repeat_letter("hola mundo")
    print(r)

if __name__ == '__main__':
    main()
