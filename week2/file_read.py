def print_uppercase_file_contents(file_name):
    try:
        with open(file_name, "r") as file:
            if not file.read(1):
                print("The file is empty.")

            for line in file:
                print(line.strip().upper())
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_name = "file.txt"
    print_uppercase_file_contents(file_name)

if __name__ == "__main__":  
    main()