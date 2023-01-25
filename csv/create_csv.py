import csv, os

def main():

    columns = ["nombre", "apellido", "edad"]
    data = ["Paco", "Botero", 26]

    data_list = [
        ["Paco", "Botero", 26],
        ["Javier", "Quiñonez", 24],
        ["Emilio", "Tafur", 25]
    ]
    data_dict = [
        {"nombre": "Paco", "apellido": "Botero", "edad": 26},
        {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
        {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
    ]

    path_file = os.path.join(os.getcwd(), "new_csv.csv")
    # file = open(path_file, "w")
    # writer = csv.writer(file, delimiter=",")
    # file.close()

    # with open(path_file, "w", newline="") as file:
    #     writer = csv.writer(file, delimiter=",")
    #     writer.writerow(columns)
    #     writer.writerows(data_list)

    with open(path_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data_dict)


if __name__ == '__main__':
    main()
