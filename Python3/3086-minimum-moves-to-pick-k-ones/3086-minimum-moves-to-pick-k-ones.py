class Solution:
    def minimumMoves(self, nums: List[int], k: int, max_changes: int) -> int:
        one_indexes = [index for index in range(len(nums)) if nums[index] == 1]
        min_moves = float('inf')
        if max_changes >= k: # with 0 step 2
            min_moves = 2 * k

        prefix_sums = one_indexes.copy()
        for i in range(1, len(one_indexes)):
            prefix_sums[i] += prefix_sums[i - 1]

        def get_sum(left, right):
            if left > right:
                return 0
            if left == 0:
                return prefix_sums[right]
            return prefix_sums[right] - prefix_sums[left - 1]

        min_step_twos = max(1, k - max_changes)
        # step_twos is the number of times using step 2
        for step_twos in range(min_step_twos, min_step_twos + 3):
            if step_twos > k:
                break

            for left in range(len(one_indexes)):
                right = left + step_twos - 1
                if right >= len(one_indexes):
                    break

                stand_index = (right + left) // 2
                # number moves that using step 1
                curr_moves = (k - step_twos) * 2
                # total distance from mid to right
                curr_moves += get_sum(stand_index + 1, right) - (right - stand_index) * one_indexes[stand_index]
                # total distance from left to mid
                curr_moves += (stand_index - left) * one_indexes[stand_index] - get_sum(left, stand_index - 1)

                min_moves = min(min_moves, curr_moves)

        return min_moves