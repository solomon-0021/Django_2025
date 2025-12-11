def exchange_key_and_value(dict):
    new_dict = {}
    for key, val in dict.items():
        new_dict[val] = key

    return new_dict



def main():
    dict = {
        1: "Abel",
        2: "Beza",
        3: "Chala",
        4: "Emu"
    }

    print("Original dictionary: ", dict)

    result = exchange_key_and_value(dict)
    print("Modified dictionary: ", result)    


if __name__ == "__main__":  
    main()