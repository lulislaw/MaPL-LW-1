mas = ["a", "e","i","o","u"]
y = "y"
p = 0
chars = str(input())
if (len(chars) == 1):
    if(chars == y):
        print("Может и гласная, и согласная")
        p = 1
    else:
        for i in range(5):
            if(chars == mas[i]):
                print("Гласная")
                p = 1
                break
    if(p == 0):
        print("Согласная")
else:
    print("str")

#Бред, бесмысленные if