def array_of_names(names_dict):
    full_names = []
    for first_name, last_name in names_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

if __name__ == "__main__":
    names = {
        "cat": "dog",
        "snake": "fish",
        "kangaroo": "whale"
    }
    
    print(array_of_names(names))