def longestPalindrome(s):
        T = '#'.join('^{}$'.format(s))
        P = [0] * len(T)
        center = right = 0
        max_len = index = 0
        char_used = ['$', '^', '#']

        for i in range(1, len(T) - 1):
            mirror = 2 * center - i
            if i < right:
                P[i] = min(right - i, P[mirror])

            while T[i + P[i] + 1] == T[i - (P[i] + 1)]:
                P[i] += 1

            if i + P[i] > right:
                right = i + P[i]
                center = i

            if P[i] > max_len:
                print('max_len before: ', max_len)
                max_len = P[i]
                index = i

        t_arr = T[ index - max_len: index + max_len + 1 ]
        word_arr = [ c for c in t_arr if c not in char_used ]
        word = "".join(word_arr)

        return word

print(longestPalindrome('aaaaddddd'))