class Solution:
    # O(n) runtime, O(n) space
    def sortString(self, s: str) -> str:
        NUM_LETTERS = 26
        START_LETTER_VAL = ord('a') # 97
        letter_to_ind = {chr(i + START_LETTER_VAL):i for i in range(NUM_LETTERS)}
        ind_to_letter = {i:chr(i + START_LETTER_VAL) for i in range(NUM_LETTERS)}
        
        letter_counts = [0] * NUM_LETTERS
        for letter in s:
            letter_counts[letter_to_ind[letter]] += 1
        
        sol_so_far = []
        while not all(letter_counts[i] == 0 for i in range(NUM_LETTERS)):
            for i in range(NUM_LETTERS):
                Solution.letter_counts_helper(letter_counts, i, sol_so_far, ind_to_letter)
            
            i = NUM_LETTERS - 1
            while i >= 0:
                Solution.letter_counts_helper(letter_counts, i, sol_so_far, ind_to_letter)
                i -= 1
        
        return "".join(sol_so_far)
                
    @staticmethod
    def letter_counts_helper(letter_counts, i, sol_so_far, ind_to_letter):
        letter_count = letter_counts[i]
        if letter_count != 0:
            letter_counts[i] -= 1
            sol_so_far.append(ind_to_letter[i])