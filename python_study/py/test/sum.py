#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 18:47
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : sum.py
# @Software: PyCharm


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for tmp in range(len(nums)):
            mid = target - nums[tmp]
            for index in range(tmp + 1, len(nums)):
                if nums[index] == mid:
                    print([tmp, index])
                    return [tmp, index]

    def twoSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for tmp in range(len(nums)):
            for index in range(tmp + 1, len(nums)):
                if nums[tmp] + nums[index] == target:
                    print([tmp, index])
                    return [tmp, index]


if __name__ == "__main__":
    # str_line = input()
    # target = int(input())
    # line = str_line.replace("[", "").replace("]", "").split(",")
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    solution.twoSums(nums, target)
