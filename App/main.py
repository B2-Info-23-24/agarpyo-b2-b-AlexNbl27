from my_pygame import MyPygame
from game import Game
from menu import Menu


if __name__ == '__main__':
    mypygame = MyPygame()
    menu = Menu(mypygame)
    menu.run()