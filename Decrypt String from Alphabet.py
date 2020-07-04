class Solution:
    def freqAlphabets(self, s: str) -> str:
        str_so_far = ""
        mapping = {str(i): chr(i - 1 + 97) for i in range(1, 27)}
        to_add = []

        for char in s:
            if char == "#":
                last = to_add.pop()
                second_last = to_add.pop()
                str_so_far += "".join([mapping[char] for char in to_add])
                to_add = []
                str_so_far += mapping[second_last + last]
            else:
                to_add.append(char)

        str_so_far += "".join([mapping[char] for char in to_add])

        return str_so_far

