def calc_square(num: int) -> int:
    return num**2

def main():
    nums = [1,2,3,4,5,6,7,8,9,10]
    square_nums = list(map(calc_square,nums))

    print(square_nums)


if __name__ == '__main__':
    main()
