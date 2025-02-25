"""def find_min_unrepresentable(nums):
    nums.sort()
    target = 1
    for num in nums:
        if num <= target:
            target += num
        else:
            break
    return target
N = int(input())
numbers = [int(input()) for _ in range(N)]
result = find_min_unrepresentable(numbers)
print(result)"""
def find(nums):
    nums.sort()
    target = 1
    for n in nums:
        if n <= target:
            target += n
        else:
            break
    return target
i = open("input.txt","r")
n = int(i.readline())
num = [int(i.readline()) for _ in range(n)]
result = find(num)
o = open("output.txt", 'w')
o.write(str(result))



