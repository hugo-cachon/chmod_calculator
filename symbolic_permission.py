from unix_permission_notation import symbolic_notation


def symbolic_user_do():
    read = input("Can the user read the file?(y/n)")
    write = input("Can the user write in the file?(y/n)")
    execute = input("Can the user execute the file?(y/n)")

    if read == "y":
        r = (symbolic_notation.get("read"))
    else:
        r = (symbolic_notation.get("no_permissions"))

    if write == "y":
        w = (symbolic_notation.get("write"))
    else:
        w = (symbolic_notation.get("no_permissions"))

    if execute == "y":
        x = (symbolic_notation.get("execute"))
    else:
        x = (symbolic_notation.get("no_permissions"))

    user = r + w + x

    return user


def symbolic_group_do():
    read = input("Can the group read the file?(y/n)")
    write = input("Can the group write in the file?(y/n)")
    execute = input("Can the group execute the file?(y/n)")

    if read == "y":
        r = (symbolic_notation.get("read"))
    else:
        r = (symbolic_notation.get("no_permissions"))

    if write == "y":
        w = (symbolic_notation.get("write"))
    else:
        w = (symbolic_notation.get("no_permissions"))

    if execute == "y":
        x = (symbolic_notation.get("execute"))
    else:
        x = (symbolic_notation.get("no_permissions"))

    group = r + w + x

    return group


def symbolic_all_do():
    read = input("Can everybody read the file?(y/n)")
    write = input("Can everybody write in the file?(y/n)")
    execute = input("Can everybody execute the file?(y/n)")

    if read == "y":
        r = (symbolic_notation.get("read"))
    else:
        r = (symbolic_notation.get("no_permissions"))

    if write == "y":
        w = (symbolic_notation.get("write"))
    else:
        w = (symbolic_notation.get("no_permissions"))

    if execute == "y":
        x = (symbolic_notation.get("execute"))
    else:
        x = (symbolic_notation.get("no_permissions"))

    all_do = r + w + x

    return all_do


def symbolic_permission_value():

    symbolic_user_value = symbolic_user_do()
    symbolic_group_value = symbolic_group_do()
    symbolic_all_value = symbolic_all_do()

    numeric_value_key = symbolic_user_value + symbolic_group_value + symbolic_all_value

    print("\nYour symbolic permission is:")
    return numeric_value_key
