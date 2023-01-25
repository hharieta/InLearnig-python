def calc_square(num: int) -> int:
    return num**2


def main():
    list_nums = [1,2,3,4,5,6,7,8,9,10]
    # square_nums = [num**2 for num in list_nums]
    square_nums = [calc_square(num) for num in list_nums]
    print(square_nums)

    pair_square_nums = [calc_square(num) for num in list_nums if num % 2 == 0]
    print(pair_square_nums)

    pair_square_nums2 = [calc_square(num) if num % 2 == 0 else 0 for num in list_nums]
    print(pair_square_nums2)

if __name__ == '__main__':
    main()
