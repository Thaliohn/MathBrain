from random import randint
import os


try:
    range_mathbrain = int(input("Digite aqui 1 número inteiro: "))
    range_MathBrain = int(input("Digite aqui 1 número inteiro: "))


    def sums():
        first_number = randint(range_mathbrain, range_MathBrain)
        second_number = randint(range_mathbrain, range_MathBrain)
        answer = first_number + second_number
        print(f'Let\'s see if you know how to sum these: {first_number} + {second_number}')
        user_answer = int(input())
        if user_answer == answer:
            print(f'You did it right!')
        else:
            print(f'You could not answer that, the answer was {answer}.')


    def subtraction():
        first_number = randint(range_mathbrain,range_MathBrain)
        second_number = randint(range_mathbrain,range_MathBrain)
        answer = first_number - second_number
        print(f'Let\'s see if you know how to subtract: {first_number} - {second_number}')
        user_answer = int(input())
        if user_answer == answer:
            print(f'You did it right!')
        else:
            print(f'You could not answer that, the answer was {answer}.')


    def division():
        first_number = randint(range_mathbrain,range_MathBrain)
        second_number = randint(range_mathbrain,range_MathBrain)
        answer = round(first_number / second_number, 2)
        print(f'May you know hot to divide right?')
        print(f'Divide this: {first_number} / {second_number}')
        user_answer = float(input())
        if user_answer == answer:
            print(f'You did it right!')
        else:
            print(f'Maybe you have to improve your skills, the answer was {answer}.')


    def multiplication():
        first_number = randint(range_mathbrain,range_MathBrain)
        second_number = randint(range_mathbrain,range_MathBrain)
        answer = first_number * second_number
        print(f'You have to multiply these numbers: {first_number} * {second_number}.')
        user_answer = int(input())
        if user_answer == answer:
            print(f'You did it right!')
        else:
            print(f'You did it wrong, don\'t give up!')


    while True:
        os.system("clear")
        print("To quit, press any keyword different of numbers.")
        sums()
        subtraction()
        division()
        multiplication()



except ZeroDivisionError:
    print("Both values are 0, reset the application and use at least one value different of zero.")
except ValueError:
    print("Please, use only numbers.")


# Enjoy it!