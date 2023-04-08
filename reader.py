from pympler import asizeof
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


def write_to_file_and_count_lines(filename: str, output_filename: str, word: str) -> int:
    """This function reads data from one file and writes to another file using a generator"""
    lines_counter: int = 0
    with open(output_filename, "wb") as output_file:
        for line in read_from_file(filename, word):
            output_file.write(bytes(f"{line}\n", encoding="utf-8"))
            lines_counter += 1
    return lines_counter


def get_file_size(file_path: str) -> int:
    """This function reads file and returns filesize in bytes"""
    with open(file_path, "rb") as file:
        file_obj = file.read()
    return asizeof.asizeof(file_obj)


def main():
    search_word: str = input("Enter the search word: ")

    filename: str = "rockyou_utf8.txt"
    output_filename: str = "results.txt"

    lines: int = write_to_file_and_count_lines(filename, output_filename, search_word)

    total_size: int = get_file_size(output_filename)

    print(f"Total lines in output file: {lines}\nTotal output file size: {total_size} bytes")


if __name__ == "__main__":
    main()
