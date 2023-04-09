from pympler import asizeof
from typing import Generator


def read_from_file(filename: str, word: str) -> Generator:
    """A simple generator function to read lines from a file using readline()."""
    with open(filename, "r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if word.lower() in line.lower():
                yield line.replace("\n", "")


def write_to_file_and_count(filename: str, output_filename: str, word: str) -> tuple:
    """This function reads data from one file and writes to another file using a generator"""
    lines_counter: int = 0
    output_file = open(output_filename, "wb")
    for line in read_from_file(filename, word):
        output_file.write(bytes(f"{line}\n", encoding="utf-8"))
        lines_counter += 1
    filesize = asizeof.asizeof(open(output_file.name).read())
    output_file.close()
    return lines_counter, filesize


def main():
    search_word: str = input("Enter the search word: ")

    filename: str = "rockyou_utf8.txt"
    output_filename: str = "results.txt"

    lines, filesize = write_to_file_and_count(filename, output_filename, search_word)
    print(f"Total lines in output file: {lines}\nTotal output file size: {filesize} bytes")


if __name__ == "__main__":
    main()
