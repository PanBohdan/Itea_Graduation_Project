# Itea_Graduation_Project# Itea_Graduation_Project
Опис пакетів, модулів і функцій

1(M)advanced_calculator_main_menu.py - основний модуль програми який залежно від вводу
1.1)main_calculator_menu() - залежно від вводу переносить користувача до підмодулів програми
1.2)shut_down() - виключає програму

2(M)advanced_calculator.py - підмодуль який обчислює введену функцію за допомогою eval
2.2)calculator_menu() - меню підмодуля яке виводить результат введеної формули
2.3)is_evaluation_right(inp_str) - приймає формулу в виді str і перевіряє її правильність
2.4)calculator(inp_str) - приймає формулу в виді str і повертає її результат

3(M)gcd_and_lcm_calculator.py - підмодуль який визначає і принтить НСК і НСД
lcm_and_gcd_menu - меню підмодуля яке викликає print_gcd, або print lcm
3.1)print_gcd() - принтить gcd чисел які були введені через пробіл за допомогою наступних функцій
	-find_gcd_of_multiple_nums(inp_list) знаходить gcd чисел в списку який приймає і повертає gcd
	-find_gcd_of_two_nums(x, y) знаходить gcd двох чисел і повертає їх gcd
3.2)print_lcm - принтить lcd чисел які були введені через пробіл за домопогою наступної функції
	-find_lcm(inp_list) знаходить lcm чисел списку і повертає lcm

4(M)area_calculator - модуль з калькулятором площ різних фігур
area_calculator_menu.py - підмодуль з меню функцій
area_calculator_menu() - функція яка викликає підменю
4.1)area_of_quadrilateral_calculator_menu() - підменю знаходження площі чотирикутників за домопогою функцій з файлу area_of_quadrilateral_calculator.py
4.1.1)calculate_and_print_area_of_quad_by_half_perimeter_and_r_of_incircle() - принтить площу чотирикутника за допомогою нищенаведеної функції
	-calculate_area_of_quad_by_half_perimeter_and_r_of_incircle(p, r) - приймає p(півпериметр) і r(радіус) (int/float) і повертає площу
4.1.2)calculate_and_print_area_of_quad_by_diagonals_and_degree_between() - принтить площу чотирикутника за домопогою нищенаведеної функції
	-calculate_area_of_quad_by_diagonals_and_degree_between(d1, d2, degree) приймає d1, d2 діагоналі, а degree кут між ними (int/float) і повертає площу 
4.2)area_of_triangle_calculator_menu() - підменю знаходження площі трикутників за допомогою функцій з файлу area_of_triangle_calculator.py
4.2.1)calculate_and_print_area_of_triangle_by_side_and_altitude() - принтить площу трикутника за допомогою нищенаведеної функції
	 -calculate_area_of_triangle_by_side_and_altitude(a, s) a(висота), s(сторона) (int/float) і повертає площу
4.2.2)calculate_and_print_area_of_triangle_by_two_sides_and_degree() - принтить площу трикутника за допомогою нищенаведеної функції
	 -calculate_area_of_triangle_by_two_sides_and_degree(a, b, d) a(перша сторона), b(друга сторона), d(кут між ними) (int/float) і повертає площу
4.2.3)calculate_and_print_area_of_triangle_by_three_sides() - принтить площу трикутника за допомогою нищенаведеної функції
	 -calculate_area_of_triangle_by_three_sides(a, b, c) a, b, c(сторони int/float) повертає площу
4.3)-area_of_disk_calculator.py - підмодуль знаходження площі диска
4.3.1)calculate_and_print_area_of_disk() - перевіряє введений радіус на правильність і принтить площу диск за домопогою нищенаведеної функції
	-calculate_area_of_disk(r) - приймає r (радіус) int, або float і повертає площу диска
4.4)-area_of_square_or_rectangle.py - підмодуль знаходження площі квадрата або прямокутника
4.4.1)calculate_and_print_area_of_square_or_rectangle() - принтить площу введеного прямокутника або квадрата за допомогою нищенаведених функцій
	-calculate_area_of_square(s) - приймає s(side) сторону квадрату (int/float) і повертає його площу
	-calculate_area_of_rectangle(a, b) - приймає a, b (сторони прямокутника int/float) і повертає його площу

5)matrix_calculator - модуль з калькулятором матриць
matrix_calculator_menu.py - підмодуль з меню функцій
5.1)matrix_calculator_menu() функція яка викликає нищенаведені функції з нищенаведених файлів калькулятора
5.2)matrix_calculator.py
Всі нищенаведені функції приймають матриці за допомогою функції matrix_from_input()
5.2.1)print_matrix_to_the_power_of_number() принтить матрицю піднесену до степені за допомогою нищенаведеної функції
	-matrix_to_the_power_of_number(matrix, number) matrix(матриця(list)) number(int) повертає нову матрицю де всі елементи піднесені до степені
5.2.2)multiply_and_print_matrix_by_number() принтить матрицю помножену на число за допомогою нищенаведеної функції
	-multiply_matrix_by_number(matrix, number) matrix(матриця(list)) number(int) повертає нову матрицю де всі елементи помножені на число
5.2.3)multiply_and_print_two_matrix() принтить матрицю помножену на матрицю за допомогою нищенаведеної функції
	-multiply_two_matrix(matrix1, matrix2) matrix1, matrix2 (матриця(list)) повертає нову матрицю яка складається з результату множення елементів матриць
5.2.4)sum_and_print_matrix() принтить суму двох матриць за домопогою нищенаведених функцій 
	-sum_matrix(matrix1, matrix2) matrix1, matrix2 (матриця(list)) повертає нову матрицю яка складається з сум елементів матриць
5.3)matrix_transposer.py
5.3.1)print_and_transpose_matrix() принтить транспоновану матрицю за допомогою нищенаведеної функції
	-matrix_transpose(matrix) matrix(матриця(list)) повертає транспоновану матрицю
utils.py - файл з утилітами які часто використовуються
