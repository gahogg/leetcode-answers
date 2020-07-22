class Solution:
    # O(n) runtime,  O(n) space
    def reverseWords(self, s):
        words = s.split(' ')
        return "".join(["".join(list(reversed(word)) + [' ']) for word in words])[:-1]