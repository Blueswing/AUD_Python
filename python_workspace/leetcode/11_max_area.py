"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

解题思路：双指针
"""
from typing import List


def max_area(height: List[int]) -> int:
    start = 0
    end = len(height) - 1
    max_a = 0
    while start < end:
        area = min(height[start], height[end]) * (end - start)
        max_a = max(area, max_a)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return max_a


print(max_area([1, 2, 3, 4, 5, 6, 7, 8, 9]))
