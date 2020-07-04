class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        distinct_morse_words = set(map(Solution.word_to_morse, words))
        return len(distinct_morse_words)

    @staticmethod
    def word_to_morse(word):
        morse_array = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter_to_morse = {chr(i + 97): m for i, m in enumerate(morse_array)}
        return "".join(list(map(letter_to_morse.__getitem__, word)))