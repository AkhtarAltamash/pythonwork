"""
Map, Filter & Reduce | Python Tutorials For Absolute Beginners In Hindi #48
map kisi bhi ak function ko list ma convert kar dayta ha

"""

numbers = ["3","23","45"]

numbers = list(map(int,numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
numbers[2]=numbers[2] + 1
print(numbers[2])

