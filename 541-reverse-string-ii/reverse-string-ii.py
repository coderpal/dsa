class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        # convert string to list, as string is immutable 
        lst = list(s)
        n = len(lst)    # length of the list

        # jump through the list in stels of 2k
        for i in range(0, n, 2*k):

            # set up pointer for first k characters of the current chunk
            left = i
            # right pointer is either i + k - 1, OR,
            # n - 1, i.e. the very end of the list if fewer than k items remain
            right = min(i + k -1, n - 1)

            # now the two pointer swap logic
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        # convert the list back into the string and return
        return "".join(lst)

            
        