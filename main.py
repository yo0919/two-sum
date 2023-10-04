from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], idx]
        num_dict[num] = idx
    return []

if __name__ == "__main__":
    data_str = input("Enter nums and target in format 'nums = [x,y,z], target = w': ")

    nums_str = data_str.split("nums = ")[1].split(", target")[0].strip("[]")
    target_str = data_str.split("target = ")[1].strip()

    nums = list(map(int, nums_str.split(",")))
    target = int(target_str)

    result = twoSum(nums, target)
    print("Indices:", result)
