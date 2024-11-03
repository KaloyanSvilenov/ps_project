class Logic:
    def __init__(self, start, length):
        self.start = start
        self.length = length

        self.str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


    def printTable(self):

        substr = self.str[self.start:self.start + self.length]
        print("\n" + substr.encode('utf-8').hex(sep=" ", bytes_per_sep=8) + "\n")

st = int(input("Enter start id: "))
ln = int(input("Enter length: "))
obj = Logic(st, ln)
obj.printTable()


# def string_to_hex_table(input_string, start, length):
#     # Extract the specified part of the string
#     substring = input_string[start:start + length]
#
#     # Convert the substring to bytes
#     byte_data = substring.encode('utf-8')
#
#     # Prepare to format the output
#     hex_lines = []
#     for i in range(0, len(byte_data), 64):
#         # Get the next 64 bytes
#         chunk = byte_data[i:i + 64]
#         # Convert to hex and format
#         hex_chunk = ' '.join(f'{byte:02x}' for byte in chunk)
#         hex_lines.append(hex_chunk)
#
#     # Print the formatted hex output
#     for line in hex_lines:
#         print(line)
#
#
# # Example usage
# if __name__ == "__main__":
#     # Hardcoded string
#     example_string = "This is an example of a long string that we will use to demonstrate the conversion to hex format. " \
#                      "It contains multiple characters and will be used to test the functionality of the program."
#
#     # Input parameters
#     start = int(input("Enter the start position: "))
#     length = int(input("Enter the length in bytes: "))
#
#     # Call the function
#     string_to_hex_table(example_string, start, length)
