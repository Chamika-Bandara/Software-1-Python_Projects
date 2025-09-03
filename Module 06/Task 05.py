def even_only(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2==0]

arr = [1, 2, 3, 4, 5, 6, 7,]
filtered = even_only(arr)
print("Original:", arr)
print("Evens:", filtered)