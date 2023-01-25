# *args: a optional tuple with n values
def calc_perimeter(*args: int) -> int:
    perimeter: int = 0

    for n in args:
        perimeter += n
    
    return perimeter


def main():
    print(calc_perimeter(3,5,7,2))


if __name__ == '__main__':
    main()