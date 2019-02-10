#started @ 4:55 PM
class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        morse_code= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {}
        morse_string = ''
        results = []
        for idx, code in enumerate(morse_code):
            morse_dict[chr(97+idx)] = code
        for word in words:
            for char in word:
                morse_string += morse_dict[char]
            results.append(morse_string)
            morse_string = ''
        print(results)
        return len(set(results))

solution = Solution()

result = solution.uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg'])

print(result)

#finished at 5:06PM


# Runtime: 36 ms, faster than 99.38% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 6.5 MB, less than 80.50% of Python3 online submissions for Unique Morse Code Words.