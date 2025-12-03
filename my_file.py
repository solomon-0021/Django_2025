def read_from_file(file_name):
    """Reading content from a file."""
    try:
        with open(file_name) as file:
            content = file.read()
            if content == "":
                return "The file is empty."
        return content.strip()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def write_to_file(file_name, content):
    """Writing content to a file."""
    with open(file_name, "a") as file:
        file.write(content)

    print("Content written to file successfully.")


def main():
    FILE_NAME = "solution.txt"

    content = read_from_file(FILE_NAME)

    print("File Content:")
    print(content)

    new_content = input("Enter content to append to the file: ")
    write_to_file(FILE_NAME, new_content + "\n")

if __name__ == "__main__":
    main()



# def my_file(file_name):
#     try:
#         with open(file_name, "r") as file:
#             data = file.read()
#             print(f"Wolcome {data}")
#     except FileNotFoundError:    
#         with open(file_name, "w") as file: 
#             file.write("Guest\n")  

# my_file("guests.txt")




