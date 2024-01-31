#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    split1 = []
    split2 = []

    for i in list1:
        split1.append(int(i))
    for i in list2:
        split2.append(int(i))

    if len(split1) == len(split2):
        value1 = split1[0] * split2[0]
        value2 = split1[1] * split2[1]
        value3 = split1[2] * split2[2]

        total = value1 + value2 + value3
        print(total)
    else:
        print("Error")

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    a = input()
    b = input()

    sum_of_products(a, b)
