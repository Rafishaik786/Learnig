#import string

#name1 = input('enter first name=')
#ame2 = input('enter second name=')


def relation():
    name1 = input('enter first name=')
    name2 = input('enter second name=')
    small1 = name1.lower()
    small2 = name2.lower()
    name1_list = list(small1)
    print(name1_list)
    name2_list = list(small2)
    print(name2_list)
    for i in small1:
        print(i)
        for j in small2:
            print(j)
            if i == j:
                del name1_list[name1_list.index(i)]
                del name2_list[name2_list.index(j)]
                break
    print(name1_list)
    print(name2_list)
    flames_count=len(name1_list)+len(name2_list)
    print(flames_count)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    print("FLAMES Array values are = ", flames)
    length1 = len(flames)
    print("FLAMES Array count = ", length1)
    count = 0
    print("Iteration 1 :")
    while len(flames) == 6:
        for x in range(0, flames_count):
            if x == 1:
                if count == len(flames):
                    count = 0
                else:
                    if count == 5:
                        count = 5
                    else:
                        count = count
            else:
                if count == 5:
                    count = 0
                else:
                    count = count + 1
        print("The count for x value ", x, " is = ", count)
        del flames[count]
        print("Iteration 1 Remaining FLAMES List = ", flames)
        print("Last Deleted Array Index = ", count)
        print("Iteration 2 :")
    while len(flames) == 5:
        for x in range(1, flames_count + 1):
            if x == 1:
                if count == len(flames):
                    count = 0
                else:
                    if count == 4:
                        count = 4
                    else:
                        count = count
            else:
                if count == 4:
                    count = 0
                else:
                    count = count + 1
        print("The count for x value ", x, " is = ", count)
        del flames[count]
        print("Iteration 2 Remaining FLAMES List = ", flames)
        print("Last Deleted Array Index = ", count)
        print("Iteration 3 :")
    while len(flames) == 4:
        for x in range(1, flames_count + 1):
            if x == 1:
                if count == len(flames):
                    count = 0
                else:
                    if count == 3:
                        count = 3
                    else:
                        count = count
            else:
                if count == 3:
                    count = 0
                else:
                    count = count + 1
            print("The count for x value ", x, " is = ", count)
        del flames[count]
    print("Iteration 3 Remaining FLAMES List = ", flames)
    print("Last Deleted Array Index = ", count)
    print("Iteration 4 :")
    while len(flames) == 3:
        for x in range(1, flames_count + 1):
            if x == 1:
                if count == len(flames):
                    count = 0
                else:
                    if count == 2:
                        count = 2
                    else:
                        count = count
            else:
                if count == 2:
                    count = 0
                else:
                    count = count + 1
        print("The count for x value ", x, " is = ", count)
        del flames[count]
    print("Iteration 4 Remaining FLAMES List = ", flames)
    print("Last Deleted Array Index = ", count)
    print("Iteration 5 :")
    while len(flames) == 2:
        for x in range(1, flames_count + 1):
            if x == 1:
                if count == len(flames):
                    count = 0
                else:
                    if count == 1:
                        count = 1
                    else:
                        count = count
            else:
                if count == 1:
                    count = 0
                else:
                    count = count + 1
        print("The count for x value ", x, " is = ", count)
        del flames[count]
    print("Iteration 5 Remaining FLAMES List = ", flames)
    print("Last Deleted Array Index = ", count)
    print("The Result of FLAMES is:")
    if flames[0] == 'F':
        print("The relationshiop between ", name1, " and ", name2, " is = Friends")
    elif flames[0] == 'L':
        print("The relationshiop between ", name1, " and ", name2, " is = Love")
    elif flames[0] == 'A':
        print("The relationshiop between ", name1, " and ", name2, " is = Affection")
    elif flames[0] == 'M':
        print("The relationshiop between ", name1, " and ", name2, " is = Marraige")
    elif flames[0] == 'E':
        print("The relationshiop between ", name1, " and ", name2, " is = Enemy")
    else:
        print("The relationshiop between ", name1, " and ", name2, " is = Sacrifice")


relation()