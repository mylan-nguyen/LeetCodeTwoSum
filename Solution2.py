# May 11, 2022
## Mylan Nguyen
# Use a dictionary to solve the 2 sum problem

class Solution2(object):

    @staticmethod
    def twoSum(nums, target):
        my_dict = dict()

        index_list = []
        for i in range(0, len(nums)):
            # key = num in nums, value = index of num
            my_dict[nums[i]] = i
            print(my_dict)
            two_sum = nums[i] + nums[i+1]
            print('my sum is: ', two_sum)
            if two_sum == target:
                return [i, i+1]
            print()

def main():
    nums = [2, 7, 11, 15]
    target = 9
    print("Answer", Solution2.twoSum(nums, target))

    nums1 = [3,2,4]
    target1 = 6
    #print("Answer", Solution2.twoSum(nums1, target1))

    nums = [3, 3]
    target = 6
    #print("Answer", Solution2.twoSum(nums, target))

main()
