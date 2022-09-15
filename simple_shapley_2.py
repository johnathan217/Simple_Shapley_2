def main():
    class MemberType:
        def __init__(self, name, value, synergy, amount):
            self.name = name
            self.value = value
            self.synergy = synergy
            self.amount = amount

    while True:
        try:
            n = int(input("How many types of member are in the coalition?:"))
        except ValueError:
            print("Enter an integer")
        else:
            break

    list1 = []
    for i in range(n):
        t = input("Name coalition member type " + str(i + 1) + ": ")
        list1.append(MemberType(str(t), 0, 0, 0, ))

    # for each individual in list access characteristic
    for i in range(len(list1)):
        print(list1[i].name)


main()
