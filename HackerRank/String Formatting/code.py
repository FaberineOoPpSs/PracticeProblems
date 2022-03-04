def print_formatted(number):
    space = ' ' * 8
    for i in range(1, number + 1):
        print(end = ' ' * (len(str(bin(number).replace('0b', ''))) - len(str(i))))
        print(str(i), end = ' ' * (len(str(bin(number).replace('0b', ''))) - len(str(oct(i).replace('0o', ''))) + 1))
        #print(str(i), end = space)
        print(str(oct(i).replace('0o', '')), end = ' ' * (len(str(bin(number).replace('0b', ''))) - len(str(hex(i).replace('0x', ''))) + 1))
        print(str(hex(i).replace('0x', '').upper()), end = ' ' * (len(str(bin(number).replace('0b', ''))) - len(str(bin(i).replace('0b', ''))) + 1))
        print(str(bin(i)).replace('0b', ''))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n
