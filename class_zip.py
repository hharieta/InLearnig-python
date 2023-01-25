def main():
    names = ["Paco", "Emilio", "Olafur"]
    last_names = ["Botero", "Tafur", "Arnals"]

    full_name = list(zip(names, last_names))
    print(full_name)

    names_unzip, last_names_unzip = zip(*full_name)
    print(names_unzip, "\n", last_names_unzip )

    for name, last_name in zip(names, last_names):
        print(name, last_name)


if __name__ == '__main__':
    main()
