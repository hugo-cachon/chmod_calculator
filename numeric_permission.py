from unix_permission_notation import numeric_notation


def numeric_user_do():
    read = input("Can the user read the file?(y/n)")
    write = input("Can the user write in the file?(y/n)")
    execute = input("Can the user execute the file?(y/n)")

    if read == "y":
        r = (numeric_notation.get("read"))
    else:
        r = (numeric_notation.get("no_permissions"))
    if write == "y":
        w = (numeric_notation.get("write"))
    else:
        w = (numeric_notation.get("no_permissions"))
    if execute == "y":
        x = (numeric_notation.get("execute"))
    else:
        x = (numeric_notation.get("no_permissions"))

    user = r + w + x

    return str(user)


def numeric_group_do():
    read = input("Can the group read the file?(y/n)")
    write = input("Can the group write in the file?(y/n)")
    execute = input("Can the group execute the file?(y/n)")

    if read == "y":
        r = (numeric_notation.get("read"))
    else:
        r = (numeric_notation.get("no_permissions"))

    if write == "y":
        w = (numeric_notation.get("write"))
    else:
        w = (numeric_notation.get("no_permissions"))

    if execute == "y":
        x = (numeric_notation.get("execute"))
    else:
        x = (numeric_notation.get("no_permissions"))

    group = r + w + x

    return str(group)


def numeric_all_do():
    read = input("Can everybody read the file?(y/n)")
    write = input("Can everybody write in the file?(y/n)")
    execute = input("Can everybody execute the file?(y/n)")

    if read == "y":
        r = (numeric_notation.get("read"))
    else:
        r = (numeric_notation.get("no_permissions"))

    if write == "y":
        w = (numeric_notation.get("write"))
    else:
        w = (numeric_notation.get("no_permissions"))

    if execute == "y":
        x = (numeric_notation.get("execute"))
    else:
        x = (numeric_notation.get("no_permissions"))

    all_do = r + w + x

    return str(all_do)


def numeric_permission_value():

    numeric_user_value = numeric_user_do()
    numeric_group_value = numeric_group_do()
    numeric_all_value = numeric_all_do()

    numeric_value_key = numeric_user_value + numeric_group_value + numeric_all_value
    
    print("\nYour numeric permission value is: ")
    return numeric_value_key
