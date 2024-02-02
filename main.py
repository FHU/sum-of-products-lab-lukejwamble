#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    split1 = []
    split2 = []

    for i in list1:
        split1.append(int(i))
    for i in list2:
        split2.append(int(i))

    if len(split1) == len(split2):
        total = 0
        for i in range(len(split1)):
            total = total + (split1[i] * split2[i])
            i += 1
        print(total)

    else:
        print("error")

if __name__ == '__main__':
    a = input()
    b = input()

    newlist1 = a.split(" ")
    newlist2 = b.split(" ")

    sum_of_products(newlist1, newlist2)
