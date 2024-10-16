import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'A simple implementation of the Unix cut command.')
    parser.add_argument('-f', '--fields', required = True, help = 'Field number to extract(e.g., 2 for the second field).')
    parser.add_argument('filename', help = 'Input file to process.')
    return parser.parse_args()
## Initializes argument parser and adds a few arguments: a required field, and filename. Parses command-line arguments and returns them as an object to be used elsewhere in the program.

def extract_field(filename, field_number, delimiter = '\t'):
    try:
        with open (filename, 'r') as file:
            for line in file:
                parts = line.rstrip('\n').split(delimiter)
                if field_number <= len(parts):
                    print(parts[field_number - 1])
                else:
                    print('')
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found', file = sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'An error occurred: {e}', file = sys.stderr)
        sys.exit(1)
## Method takes a name and path of a file to process, the specific field number to extract from each line, and a character used to separate fields. Defaults to a tab (\t).
## Opens the file in read mode, iterates over each line in the file, removes any trailing newline characters from the line and splits the line into a list of fields based on the specified delimiter. Come back to this later - can likely be optimized. For now it is ok.
## Checks if the specified field number exists in the current line (fields are 1 indexed, pythonic lists are 0 indexed hence field_number -1). Prints desired field to the standard output. If specified field number doesn't exist, prints an empty string.

def main():
    args = parse_arguments()
    try:
        field_number = int(args.fields)
        if field_number < 1:
            raise ValueError
    except ValueError:
        print('Error: Field number must be a positive integer.', file = sys.stderr)
        sys.exit(1)
        
    extract_field(args.filename, field_number)
## Assigns parsed command-line arugments returned by parse_arguments to the variable args.
## Converts the fields argument from a string to an integer. If this winds up being an invalid integer, a ValueError is raised.
## Invokes the extract_field function with the provided filename and validated field_number.
if __name__ == '__main__':
    main()