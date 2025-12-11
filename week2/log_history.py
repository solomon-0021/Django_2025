def log_history():
    with open("log.txt", "a") as file:
        file.write("User logged in\n")
    print("Log history updated.")

    print("Content of log.txt:")
    with open("log.txt", 'r') as file:
        print(file.read())


if __name__ == "__main__":
    log_history()