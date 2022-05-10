class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        # your code goes here
        indexes = []
        for num in nums:
            print("i am here at this num", num)
            for num2 in nums:
                #if num == num2:

                print("num2: ", num2)
                check = nums.index(num)
                print('the num is: ', num, "and it's index is: ", check)
                check2 = nums.index(num2)
                print('the num2 is: ', num2, "and it's index is: ", check2)
                if check != check2:
                    two_sum = num + num2
                    print("the sum of ", num, " and ", num2, " is ", two_sum)
                    print("The target is ", target)
                    if num + num2 == target:
                        print("FOUND A PAIR: ", num, " and ", num2)
                        num_index = nums.index(num)
                        num2_index = nums.index(num2)
                        print(num_index)
                        print(num2_index)
                        indexes.append(num_index)
                        indexes.append(num2_index)
                        print(indexes)
                print()

        print('My current index list looks: ', indexes)
        unique_list = []
        [unique_list.append(n) for n in indexes if n not in unique_list]
        return unique_list

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

    # nums = [3, 3, 2, 4]
    nums = [3, 3]
    target = 6
    print("Answer", Solution.twoSumNew(nums, target))








main()
