def sum_list(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    return total

arr = [1, 5, 7, -2, 10]
print("List:", arr)
print("Sum:", sum_list(arr))