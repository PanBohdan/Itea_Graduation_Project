from advanced_calculator import calculator_menu
from gcd_and_lcm_calculator import lcm_and_gcd_menu
from area_calculator import area_calculator_menu
from matrix_calculator import matrix_calculator_menu


def shut_down():
    print('Shutting down')


def main_calculator_menu():
    menu_dict = {'1': calculator_menu,
                 '2': lcm_and_gcd_menu,
                 '3': area_calculator_menu.area_calculator_menu,
                 '4': matrix_calculator_menu.matrix_calculator_menu,
                 '5': shut_down}
    print('Select what you want to do\n'
          '1 - open calculator\n'
          '2 - open lcm and gcd calculator\n'
          '3 - open area calculator\n'
          '4 - open matrix calculator\n'
          '5 - shut down')
    inp = input()
    menu_dict.get(inp, main_calculator_menu)()


if __name__ == '__main__':
    main_calculator_menu()
