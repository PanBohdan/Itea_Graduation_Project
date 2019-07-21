from math import gcd


def find_lcm(inp_list):
    lcm = inp_list[0]
    for i in inp_list[1:]:
        lcm = round(lcm * i / gcd(lcm, i))
    return lcm


def find_gcd_of_two_nums(x, y):
    while y:
        x, y = y, x % y
    return x


def find_gcd_of_multiple_nums(inp_list):
    num_x = inp_list[0]
    num_y = inp_list[1]
    gcd1 = find_gcd_of_two_nums(num_x, num_y)
    for i in range(2, len(inp_list)):
        gcd1 = find_gcd_of_two_nums(gcd1, inp_list[i])
    return gcd1


def print_lcm():
    inp = input('Enter numbers that you want to find'
                ' lcm from splitting them with spaces ')
    index = 0
    for i in inp:
        if i == ' ':
            inp_list = inp.split(' ')
            for j in range(len(inp_list)):
                if inp_list[j].isdigit():
                    inp_list[j] = int(inp_list[j])
                else:
                    print('Can not find lcm of non integers')
                    lcm_and_gcd_menu()
            print(find_lcm(inp_list))
            break
        elif index + 1 == len(inp):
            print('Numbers must be divided by spaces')
            lcm_and_gcd_menu()
        index += 1


def print_gcd():
    inp = input('Enter numbers that you want to find '
                'gcd from splitting them with spaces ')
    index = 0
    for i in inp:
        if i == ' ':
            inp_list = inp.split(' ')
            for j in range(len(inp_list)):
                if inp_list[j].isdigit():
                    inp_list[j] = int(inp_list[j])
                else:
                    print('Can not find gcd of non integers')
                    lcm_and_gcd_menu()
            if len(inp_list) > 2:
                print(find_gcd_of_multiple_nums(inp_list))
            elif len(inp_list) == 2:
                print(find_gcd_of_two_nums(inp_list[0], inp_list[1]))
            break
        elif index + 1 == len(inp):
            print('Numbers must be divided by spaces')
            lcm_and_gcd_menu()
        index += 1


def lcm_and_gcd_menu():
    lcm_and_gcd_menu_dict = {
        '1': print_lcm,
        '2': print_gcd
    }
    print('Select what you want to do\n'
          '1 - find lcm\n'
          '2 - find gcd')
    inp = input()
    lcm_and_gcd_menu_dict.get(inp, lcm_and_gcd_menu)()


if __name__ == '__main__':
    lcm_and_gcd_menu()
