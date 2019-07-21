from utils import is_matched


def calculator(inp_str):
    result = eval(inp_str)
    return str(result)


def is_evaluation_right(inp_str):
    is_ev_right = False
    index = 0
    for i in inp_str:
        if i == '+' or i == '-' or i == '(' or i == ')' or \
                i == '/'or i == '*':
            if index+1 == len(inp_str) and not inp_str[index].isdigit() \
                    and i != ')':
                is_ev_right = False
                return is_ev_right
            if i == '*' or i == '/':
                if inp_str[index-1] == i and inp_str[index+1] == i:
                    is_ev_right = False
                    return is_ev_right
                if index == 0:
                    is_ev_right = False
                    return is_ev_right
            is_ev_right = True
            index += 1

        elif i.isdecimal():
            is_ev_right = True
            index += 1

        elif i == '.':
            index += 1
            if inp_str[index] != '.':
                is_ev_right = True
            else:
                is_ev_right = False
                return is_ev_right
        if i.isalpha() or i == ',' or i == ' ':
            is_ev_right = False
            return is_ev_right
    if is_matched(inp_str):
        return is_ev_right
    else:
        is_ev_right = False
        return is_ev_right


def calculator_menu():
    print('Input evaluation that you want to calculate')
    inp_str = input()
    if is_evaluation_right(inp_str):
        print(inp_str + ' = ' + calculator(inp_str))
    else:
        print('Evaluation cannot contain symbols '
              'that not numbers or * / - + .')
        calculator_menu()


if __name__ == '__main__':
    calculator_menu()
