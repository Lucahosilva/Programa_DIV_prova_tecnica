def is_less_than_ten(number):
    if number < 10:
        print('O numero é menor do que 10.')


def is_even(number):
    if number % 2 == 0:
        print('O numero é par.')


def between_eight_and_sixteen(number):
    if number >= 8 and number <= 16:
        print('O numero está entre 8 e 16.')


def is_51_or_80(number):
    if number == 51 or number == 80:
        print('O número é 51 ou 80.')


if __name__ == '__main__':

    number = float(input('Digite o numero desejado'))

    is_less_than_ten(number)
    is_even(number)
    between_eight_and_sixteen(number)
    is_51_or_80(number)
