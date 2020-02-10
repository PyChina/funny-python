from turtle import Turtle

t = Turtle()


def spiral(n):
    if n < 300:
        t.forward(n)
        t.right(89)
        spiral(n + 1)


spiral(30)
input('Press any key to continue...')
