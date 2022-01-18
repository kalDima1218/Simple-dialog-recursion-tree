def dialog(outprint, commands, lambdas):
    s = input(outprint)
    while s not in commands and s != "exit":
        s = input("Неверный формат ввода\n\nВвод: ")
    if s == "exit":
        return
    lambdas[commands.index(s)]()

while True:
    dialog("Команды:\nhelp\nping\ndo\n\nВвод: ", ["help", "ping", "do"], [
        lambda:print("хелпую"),
        lambda:dialog("Куда пингуем:\nнаискосок вправо вверх\nнаискосок влево вниз\n\nВвод: ", ["наискосок вправо вверх", "наискосок влево вниз"], [
            lambda:print("Пинг наискосок вправо вверх"),
            lambda:print("Пинг наискосок влево вниз")
        ]),
        lambda:dialog("Ходы Королевы:\nвверх\nвниз\n\nВвод: ", ["up", "down"], [
            lambda:print("Движение вверх"),
            lambda:print("Движение вниз")
        ])
    ])
    print()