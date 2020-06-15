for i in range(1,101):
    if i % 7 == 0:
        continue
    elif (i - 7 ) % 10 == 0:
        continue
    elif 70<= i <= 79:
        continue
    else:
        print(i)
