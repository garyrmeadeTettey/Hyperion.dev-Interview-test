## Section A: Code Review

### Instructions

- Please present your review in a Markdown file.
- Please refer to line numbers in your review.
- Please review the hypothetical student sumbissions by commenting on
    - Correctness
    - Efficiency
    - Style
    - Documentation
- Please comment on the postive aspects and improvements that are necessary while being encouraging.

### Option 1: Python Task

Compulsory Task 1
Follow these steps:

- In a file called anagram.py, create:

- Given an array of strings strs, group the anagrams together. 
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    - You can return the answer in any order.
    - Strings consists of lowercase English letters.
      
- Example input
- Input: strs = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

```Python
class Solution:
       def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

```
## The review of this code is visble here [**here**](https://github.com/garyrmeadeTettey/Hyperion.dev-Interview-test/blob/main/Section_A/Code-review.md)
