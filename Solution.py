class Solution(object):

    @staticmethod
    def twoSumNew(nums, target):

        index_list = []
        for i in range(0, len(nums)):
            print("index i =", i, "hold value", nums[i])
            for j in range(i+1, len(nums)):
                print("we look for match with value =", nums[j], "at index:", j)
                two_sum = nums[i] + nums[j]
                print('my sum is: ', two_sum)
                if two_sum == target:
                    index_list.append(i)
                    index_list.append(j)
                    return index_list
            print()


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print("Answer", Solution.twoSumNew(nums, target))

    nums1 = [3,2,4]
    target1 = 6
    print("Answer", Solution.twoSumNew(nums1, target1))

    nums = [3, 3]
    target = 6
    print("Answer", Solution.twoSumNew(nums, target))

main()
