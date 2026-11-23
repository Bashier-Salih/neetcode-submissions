class Solution:
    """
    Understand:
    Input: a num array and a target value
    Output: an array with index1 and index2 of the values that sum up to the target value
    Edge Cases: none

    Plan:
    initialize a current sum to 0
    two pointers first and second
    loop while second does not equal array length - 1
        add index first and index second
        check if they are equal to the target: if they are we return [first + 1, second + 2]
        else if the target - current > second:
            second += 1
        else:
            first += 1
         

    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, second = 0, 1
        current = 0
        while current != target:
            current = numbers[first] + numbers[second]
            print(first, second)
            if current == target: 
                return [first + 1, second + 1]
            elif (target - current) < numbers[second]:
                second += 1
            else:
                first += 1
        return [first, second]