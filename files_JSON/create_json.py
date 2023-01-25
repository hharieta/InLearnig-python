import json

def main():
    personas = [
        {
            "name": "Ana",
            "lastname": "Pinto",
            "age": 25
        },
        {
            "name": "Paco",
            "lastname": "Piedra",
            "age": 25
        }
    ]

    object_person = json.dumps(personas, indent=2)
    
    # write
    with open("personas.json", "w") as file:
        file.write(object_person)
    
    # read
    with open("file.json", "r") as file:
        data_json = json.load(file)
    
    print(data_json)


if __name__ == '__main__':
    main()
