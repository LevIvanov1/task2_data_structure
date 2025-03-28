def main(list1, list2):
    spisok1 = list1.split()
    spisok2 = list2.split()
    intersection = []
    for num1 in spisok1:
        for num2 in spisok2:
            if num1 == num2 and num1 not in intersection:
                intersection.append(num1)
    return " ".join(intersection)
list1 = input("список 1:  ")
list2 = input("список 2:  ")
result = main(list1, list2)
print("Общие элементы: ", result)