# find_ft_type.py


def all_thing_is_obj(obj: any) -> int:
    obj_type = type(obj)

    type_dict = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String",
    }

    if obj_type in type_dict:
        if obj_type == str:
            print(f"{obj} is in the kitchen : {obj_type}")
        else:
            print(f"{type_dict[obj_type]} : {obj_type}")
    else:
        print("Type not found")

    return 42


if __name__ == "__main__":

    pass
