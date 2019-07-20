def is_matched(evaluation):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in evaluation:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue


def is_number_int_or_float(inp):
    is_ev_right = False
    is_dot_passed = False
    index = 0
    for i in inp:
        if i == '':
            is_ev_right = False
            return is_ev_right
        elif i.isdigit():
            is_ev_right = True
        elif i == '-':
            if index != 0:
                is_ev_right = False
                return is_ev_right
            is_ev_right = True
        elif i == '.' and len(inp) > 1 and index != len(inp)-1 and index != 0:
            if is_dot_passed:
                is_ev_right = False
                return is_ev_right
            is_ev_right = True
            is_dot_passed = True
        else:
            is_ev_right = False
            return is_ev_right
        index += 1
    return is_ev_right


def is_number_float(inp):
    is_num_float = False
    for i in inp:
        if i == '.':
            is_num_float = True
    return is_num_float


def str_to_float_or_int_converter(inp):
    if is_number_int_or_float(inp):
        if is_number_float(inp):
            inp = float(inp)
        else:
            inp = int(inp)
    else:
        return False
    return inp


if __name__ == '__main__':
    print(is_matched('1+2+(-2)'), 'for 1+2+(-2)')
    print(is_matched('1+2+(-2'), 'for 1+2+(-2')
    print(is_number_int_or_float('1.5'), 'for 1.5')
    print(is_number_int_or_float('.'), ' for .')
    print(str_to_float_or_int_converter('1.5')+2)
    print(str_to_float_or_int_converter('.15'))
    print(is_number_float('1.5'), 'for 1.5')
    print(is_number_float('1'), 'for 1')
