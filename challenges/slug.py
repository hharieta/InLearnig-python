import re


def slug(url: str) -> str:
    slug = url.replace(" ","-").strip().lower()
    patern = '[^\w\-]'
    return re.sub(patern,"", slug )


def main():
    r = slug("yg-g%s!f 1#iYy* io")
    print(r)


if __name__ == '__main__':
    main()
