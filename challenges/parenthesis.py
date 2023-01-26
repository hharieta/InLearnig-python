import re

# def balancer(sentence: str) -> bool:
#     open = sentence.count("(",0, len(sentence))
#     close = sentence.count(")",0, len(sentence))
#     return open == close

def balancer(sentence: str) -> bool:
    open = 0
    for i in sentence:
        if i == "(":
            open += 1
        elif i == ")":
            open -= 1
            if open < 0: return False
    
    return open == 0


def main():
    r = balancer(") (())())")
    print(r)


if __name__ == '__main__':
    main()
