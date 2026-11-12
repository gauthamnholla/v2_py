from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        return sum(
            1
            for w in words[left:right + 1]
            if w[0] in vowels and w[-1] in vowels
        )