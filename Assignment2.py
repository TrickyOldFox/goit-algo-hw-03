import turtle
import argparse


argparse = argparse.ArgumentParser()

argparse.add_argument(
    "--recursion-level",
    dest="recursion_level",
    default=3,
    type=int,
    help="Recursion level"
)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 4)
    t.pendown()

    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)

    window.mainloop()


if __name__ == '__main__':
    args = argparse.parse_args()
    draw_koch_snowflake(args.recursion_level)
