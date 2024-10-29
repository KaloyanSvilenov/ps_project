# class Logic:
#     def __init__(self, start, length):
#         self.start = start
#         self.length = length

        # # Example string
        # example_string = "This is an example string that is exactly sixty-four bytes long!"
        #
        # # Convert to bytes and then to hexadecimal
        # hexadecimal_representation = example_string.encode('utf-8').hex()
        #
        # print(hexadecimal_representation)

        # # Define an array (list) of numbers
        # arr = [10, 20, 30, 40, 50]
        #
        # # Use a for loop with enumerate to get index and value
        # for index, value in enumerate(arr):
        #     print(f"Index: {index}, Value: {value}")

st = int(input("Enter start id: "))
ln = int(input("Enter length: "))

str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

substr = str[st:st+ln]
print(substr + "\n")
print(substr.encode('utf-8').hex() + "\n")
