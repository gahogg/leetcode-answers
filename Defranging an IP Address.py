class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join([char if char != "." else "[.]" for char in address])