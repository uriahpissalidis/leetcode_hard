class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # ls = letter and score, I only want each instance of a letter paired to a single score
        ls, pointer = {}, 0
        for letter in letters: 
            if letter not in ls: # put UNIQUE letters in the dictionary
                 for i in range(pointer, len(score)): # attach each score to the unique letter
                        if score[i] > 0:
                            ls[letter] = score[pointer]
                            pointer += 1
                            break
                        else:
                            pointer += 1
        scoreStore = []
        for word in words:
            temp = 0
            for char in word:
                if char not in ls:
                    temp = 0
                    break
                temp += ls[char]
            scoreStore.append(temp)
        scoreStore.sort()
        
