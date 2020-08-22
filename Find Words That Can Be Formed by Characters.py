from copy import deepcopy

class Solution:
# O(n*s) time, O(n*s) space
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_arr = [0] * 26
        for char in chars:
            count_arr[Solution._char_to_index(char)] += 1
        
        good_words = []
        for word in words:
            if Solution._is_good_word(word, deepcopy(count_arr)):
                good_words.append(word)
        
        return len(''.join(good_words))
    
    def _char_to_index(char):
        return ord(char) - ord('a')
    
    def _is_good_word(word, count_arr):
        for char in word:
            ind = Solution._char_to_index(char)
            if count_arr[ind] == 0:
                return False
            else:
                count_arr[ind] -= 1
                
        return True