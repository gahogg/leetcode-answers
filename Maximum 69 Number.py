class Solution:
    def maximum69Number(self, num: int) -> int:
        num_as_str = str(num)
        new_num_as_lst = list(num_as_str)

        for i, digit in enumerate(num_as_str):
            if digit == "6":
                new_num_as_lst[i] = "9"
                break

        return int("".join(new_num_as_lst))