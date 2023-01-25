def main():
    names = ["Paco", "Emilio", "Javier", "Ana"]
    e_names = enumerate(names, start=1)
    print(list(e_names))

    for i, v in enumerate(names, start=1):
        print(i, v)


if __name__ == '__main__':
    main()
