import turtle
import colorsys


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length = length / 3
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)


def main():
    print("Turtle Pattern Generator")
    print("1. Koch Snowflake")
    print("2. Colorful Spiral")

    choice = input("Enter your choice (1 or 2): ")

    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("black")
    screen.title("Turtle Pattern Generator")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.hideturtle()

    if choice == "1":
        pen.color("cyan")
        pen.penup()
        pen.goto(-200, 120)
        pen.pendown()

        for _ in range(3):
            koch_curve(pen, 400, 3)
            pen.right(120)

    elif choice == "2":
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()

        for i in range(360):
            color = colorsys.hsv_to_rgb(i / 360, 1, 1)
            pen.pencolor(color)
            pen.forward(i * 0.8)
            pen.right(91)

    else:
        print("Invalid choice. Please enter 1 or 2.")

    screen.mainloop()


if __name__ == "__main__":
    main()