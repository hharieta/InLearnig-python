# lambda functions are anonymous functions
def main():
    print((lambda num: num*2)(3,))

    square = lambda n: n*n
    print(square(4))

    is_par: bool = lambda n: n %2 == 0
    print(is_par(5))

    list_numbers = [1,2,3,4,5,6,7,8]
    print(list_numbers)
    
    list_par = list(filter(lambda n : n %2 == 0, list_numbers))
    print(list_par)

    new_list = list(map(lambda n: n*10, list_numbers))
    print(new_list)


if __name__ == '__main__':
    main()