number = input("please enter your id_code:")

con = [len(number)>10, len(number)<10]

if any(con):
    print('your code lenght must be 10')
else:
    num_list = [int(i) for i in number]
    last_num = num_list[9]

    counter = 10
    num = 0
    sum = 0

    for i in num_list:
        if counter>=2:
            num = i* counter
            counter -=1
            sum +=num

    r = sum % 11

    if r < 2:
        if r == last_num:
            print(True)
        else:
            print(False)
    else:
        r = 11-r
        if r == last_num:
            print(True)
        else:
            print(False)

