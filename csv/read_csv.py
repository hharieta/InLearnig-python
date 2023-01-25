import csv, os

def main():
    path_file = os.path.join(os.getcwd(), "new_csv.csv")

    with open(path_file, "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        header = next(reader); i=1
        
        print(" ", header[0], header[1], header[2])
        for row in reader:
            print(i, end=" ")
            for column in row:
                print(column, end=" ")
            i += 1
            print("")


if __name__ == '__main__':
    main()
