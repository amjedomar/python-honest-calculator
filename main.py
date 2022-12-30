msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
silly_store_msgs = [msg_10, msg_11, msg_12]

memory = 0.0


def prompt_operation():
    print(msg_0)
    n1_str, oper, n2_str = input().split(' ')

    try:
        n1 = memory if n1_str == 'M' else float(n1_str)
        n2 = memory if n2_str == 'M' else float(n2_str)
    except ValueError:
        print(msg_1)
        return prompt_operation()

    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        return prompt_operation()

    check(n1, oper, n2)

    calc(n1, oper, n2)


def calc(n1, oper, n2):
    result = None

    if oper == '+':
        result = n1 + n2
    elif oper == '-':
        result = n1 - n2
    elif oper == '*':
        result = n1 * n2
    if oper == '/':
        if n2 != 0:
            result = n1 / n2
        else:
            print(msg_3)
            return prompt_operation()

    store_result(result)


def store_result(result):
    global memory

    print(result)

    print(msg_4)
    store_answer = input()
    if store_answer == 'y':
        if is_one_digit(result):
            msg_index = 0

            while msg_index < 3:
                print(silly_store_msgs[msg_index])
                answer = input()
                if answer != 'y':
                    break
                msg_index += 1
            else:
                memory = result
        else:
            memory = result

    print(msg_5)
    continue_answer = input()
    if continue_answer == 'y':
        prompt_operation()


def check(n1, oper, n2):
    msg = ''

    if is_one_digit(n1) and is_one_digit(n2):
        msg += msg_6
    if (n1 == 1 or n2 == 1) and oper == '*':
        msg += msg_7
    if (n1 == 0 or n2 == 0) and oper in ['*', '+', '-']:
        msg += msg_8

    if msg != '':
        print(msg_9 + msg)


def is_one_digit(v):
    return -10 < v < 10 and v - int(v) == 0.0


prompt_operation()

