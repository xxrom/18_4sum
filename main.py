from typing import List


class Solution:

  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    size = len(nums)

    ans = {}

    for i in range(size):
      for j in range(i + 1, size):
        for k in range(j + 1, size):
          for e in range(k + 1, size):
            if i != j and i != k and i != e and j != k and j != e and k != e:
              if (nums[i] + nums[j] + nums[k] + nums[e]) == target:
                print(i, j, k, e)
                values = [nums[i], nums[j], nums[k], nums[e]]
                values.sort()

                currentIndex = ','.join([str(v) for v in values])
                print(currentIndex)

                ans[currentIndex] = values

    return list(ans.values())


my = Solution()
n = [1, 0, -1, 0, -2, 2]
t = 0

trueAns = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

ans = my.fourSum(n, t)

print("ans", ans, ans == trueAns)
