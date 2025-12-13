class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = self.height * self.width


def main():
    height, width = 5, 8

    rectangle = Rectangle(width=width, height=height)
    print(f"Area of rectangle {height}x{width} is: {rectangle.area}")


if __name__ == "__main__":
    main()