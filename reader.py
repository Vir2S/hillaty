from typing import Generator


def read_from_file(filename: str, word: str) -> Generator:
    """A simple generator function to read lines from a file using readline()."""
    with open(filename, "r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if word in line.lower():
                yield line.replace("\n", "")


def write_to_file(filename: str, output_filename: str, word: str):
    """This function reads data from one file and writes to another file using a generator"""
    with open(output_filename, "wb") as output_file:
        for line in read_from_file(filename, word):
            output_file.write(bytes(f"{line}\n", encoding="utf-8"))


def main():
    search_word: str = input("Enter the search word: ")

    filename: str = "example_utf8.txt"
    output_filename: str = "output.txt"

    write_to_file(filename, output_filename, search_word)


if __name__ == "__main__":
    main()
