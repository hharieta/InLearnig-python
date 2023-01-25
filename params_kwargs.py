# kwargs: a optional dict win k,v items
def func_kwargs(**kwargs: dict [str | int]) -> None:
    for k,v in kwargs.items():
        print(f"Key: {k}, Value: {v}")
    
    print(kwargs.keys(), kwargs.values())
    

def main():
    func_kwargs(manzanas=4, peras=3, uvas=5, piña=2)


if __name__ == '__main__':
    main()
