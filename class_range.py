# range(init, end, step). end is not inclusive

def main():
    serie1 = range(5)
    serie2 = range(5, 10)
    serie3 = range(5, 10, 2)

    print(list(serie1))
    print(list(serie2))
    print(list(serie3))


if __name__ == '__main__':
    main()