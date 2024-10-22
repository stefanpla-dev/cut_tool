import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'A simple implementation of the Unix cut command.')
    parser.add_argument('-f', '--fields', required = True, help = 'Comma or space separated list of field numbers to extract (e.g., "1,2" or "1 2").')
    parser.add_argument('-d', '--delimiter', default = '\t', help = 'Delimiter to use between fields (default is tab).')
    parser.add_argument('filename', help = 'Input file to process.')
    return parser.parse_args()
## Initializes argument parser and adds a few arguments: a required field (can be multiple fields), and filename. Parses command-line arguments and returns them as an object to be used elsewhere in the program.

def extract_field(filename, field_numbers, delimiter = '\t'):
    try:
        with open (filename, 'r') as file:
            for line in file:
                parts = line.rstrip('\n').split(delimiter)

                selected_fields = [parts[field_number - 1] if field_number <= len(parts) else '' for field_number in field_numbers]

                print(delimiter.join(selected_fields))

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found', file = sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'An error occurred: {e}', file = sys.stderr)
        sys.exit(1)
## Method takes a name and path of a file to process, the specific field number(s) to extract from each line, and a character used to separate fields. Defaults to a tab (\t).
## Opens the file in read mode, iterates over each line in the file, removes any trailing newline characters from the line and splits the line into a list of fields based on the specified delimiter.
## Checks if the specified field number exists in the current line (fields are 1 indexed, pythonic lists are 0 indexed hence field_number -1). Prints desired field(s) to the standard output. If specified field number(s) doesn't(don't) exist, prints an empty string.

def main():
    args = parse_arguments()
    try:
        field_numbers = [int(f) for f in args.fields.replace(',', ' ').split() if int(f) > 0]
    except ValueError:
        print('Error: Fields must be a positive integer or a list of positive integers.', file = sys.stderr)
        sys.exit(1)
        
    extract_field(args.filename, field_numbers, args.delimiter)
## Assigns parsed command-line arugments returned by parse_arguments to the variable args.
## Converts the fields argument from a string to an integer. If this winds up being an invalid integer, a ValueError is raised.
## Invokes the extract_field function with the provided filename, validated field_number, and delimiter if one is provided (default is tab).
if __name__ == '__main__':
    main()