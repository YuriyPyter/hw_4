def salary(hours, bet, prize):
    """
    Функция расчёта заработной платы, где:
    :param hours: выроботка в часах
    :param bet:  ставка в час
    :param prize: премия
    """
    return hours * bet + prize


print(salary(22.5, 1000, 1000))