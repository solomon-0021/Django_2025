class Teacher:
    def __init__(self):
        pass
    def work(self):
        print("Teacher teach")

class Doctor:
    def __init__(self):
        pass

    def work(self):
        print("Doctor treat patient")


def main():
    objects = [Teacher(), Doctor()]
    for obj in objects:
        obj.work()


if __name__ == "__main__":
    main()