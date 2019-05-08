# coding=utf-8


def list_basics():
    L1 = []  # An empty list
    print(f"List 1:{L1}")

    L2 = [123, 'abc', 1.23, {}]
    print(f"List 2:{L2}")

    L3 = ['Bob', 40.0, ['dev', 'mgr']]
    print(f"List 3:{L3}")

    L4 = list('spam')
    print(f"List 4:{L4}")  # This will create a list of 4 items.

    L5 = list(range(-4, 4))  # Starting from -4, upto but not including 4
    print(f"List 5:{L5}")


if __name__ == '__main__':
    list_basics()

    first_name = list('winter')
    print(first_name)

    print(f"The list has a length of :{len(first_name)}")

    start_position = 3
    end_position = 4  # upto but not including
    print(f"{first_name[start_position:end_position]}")

    second_name = list('padding')
    print(second_name)

    full_name = first_name + second_name
    print(full_name)



