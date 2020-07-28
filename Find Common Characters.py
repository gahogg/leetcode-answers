# O(n) runtime, O(n) space
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        letter_to_index = {chr(i + 97):i for i in range(26)}
        index_to_letter = {i:chr(i + 97) for i in range(26)}
        num_words = len(A)
        letter_count_matrix = [[0]*num_words for i in range(26)]
        
        for i in range(num_words):
            for letter in A[i]:
                letter_count_matrix[letter_to_index[letter]][i] += 1
        
        ret_chars = []
        for i in range(26):
            ret_chars += [index_to_letter[i]] * min(letter_count_matrix[i])
        
        return ret_chars