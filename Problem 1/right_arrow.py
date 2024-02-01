def right_arrow():
    base_char = input()
    head_char = input()

    row0 = "      " + head_char
    row1 = base_char + base_char + base_char + base_char + base_char + base_char + head_char
    row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
    row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char
    ''' Type your code here. '''

    print(row0)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()