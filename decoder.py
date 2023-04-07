def convert_encoding(input_file, output_file, input_encoding, output_encoding):
    """Generator function to convert encoding of a file."""
    with open(input_file, "r", encoding=input_encoding) as f:
        lines = f.readlines()
    with open(output_file, "w", encoding=output_encoding) as f:
        f.writelines(lines)


if __name__ == "__main__":
    input_file = input("File to decode: ")
    output_file = f"{input_file.split('.')[0]}_utf8.{input_file.split('.')[-1]}"
    convert_encoding(input_file, output_file, "latin1", "utf-8")
