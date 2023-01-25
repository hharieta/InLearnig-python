
def main():
    names = ["Paco", "Emilio", "Javier"]

    for name in names:
        if name == "Emilio": break 
        print("Name with break: ",name)

    for name in names:
        if name == "Emilio": continue
        print("Name with continue: ",name)

if __name__ == '__main__':
    main()
