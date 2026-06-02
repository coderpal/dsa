class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # convert string to list
        lst = list(s)
        # create set of all vowels
        vowels = ("aeiouAEIOU")

        # initialize start and end pointers
        left = 0
        right = len(lst) - 1

        # loop until pointers meet in middle
        while left < right:

            # move left pointer forward if it is NOT pointing to a vowel
            if lst[left] not in vowels:
                left += 1
            # move right pointer forward if it is NOT pointing to a vowel
            elif lst[right] not in vowels:
                right -= 1
            # if both are pointing towards a vowel, swap them and move inwards
            else:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        # convert the list back to string and return it
        return "".join(lst)