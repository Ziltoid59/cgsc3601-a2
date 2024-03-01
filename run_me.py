from a2 import TextAnalyer


def main():
    path = input("Please enter the full path of your review directory: ")

    nlp = TextAnalyer(path)
    nlp.analyze()


if __name__ == "__main__":
    main()