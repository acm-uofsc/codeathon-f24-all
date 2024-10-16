n = int(input())
candy = input().split(" ")
highest = max(candy, key=lambda x: len(set(x)))
print(highest, len(set(highest)))