'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# **** O(n) runtime? ****
#  **********************


def count_th(word, count=0, th_count=0):
    # if word is empty
    if not len(word):
        return 0

    length = len(word)-1
    # TBC
    if count <= length-1:
        # set our pointers to look at 2 letters side by side
        first = count
        second = count+1

        if word[first] == 't' and word[second] == 'h':
            # count 'th' occurences
            th_count += 1
        count += 1
        return count_th(word, count, th_count)

    return th_count

# word= 'abcthefthghith' #len 14, last ind= 13
# should return 3

# print(count_th(word))
