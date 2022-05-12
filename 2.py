old = float(input())
if(old < 0):
    print("Ошибка слишком молодой")
else:
    if(old >= 2):
        olddog = (old - 2) * 4 + 10.5 * 2
    else:
        olddog = old * 10.5
    print(olddog)
