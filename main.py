# Data types

# Functions


def pig_latin(word):

    if word.lower()[0] in ['a', 'e', 'i', 'o', 'u']:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

# *args


def variadic_func(*args):
    print(sum(args))


def has_33(nums):
    return "".join([str(num) for num in nums])


def paper_doll(text):
    res = ""
    for letter in text:
        i = 0
        while i < 3:
            res = res + letter
            i += 1
    return res


def bj_num_val(num):
    return 1 <= num <= 11


def blackjack(a,b,c):
    if bj_num_val(a) and bj_num_val(b) and bj_num_val(c):
        bj_num = (a, b,c)
        bj_sum = sum(bj_num)

        if bj_sum == 21:
            return 'Blackjack'
        elif bj_sum < 21:
            return bj_sum
        elif bj_sum > 21 and 11 in bj_num:
            return bj_sum - 10
        else:
            return 'BUST'
    else:
        print("BlackJack Error: Numbers should be between 1 and 11")


def summer_69(arr):
    if 6 in arr and 9 in arr:
        index_6 = arr.index(6)
        index_9 = arr.index(9)

        if index_6 < index_9:
            arr = arr[:index_6] + arr[index_9+1:]

    return sum(arr)


def spy_game(nums):

    if nums.count(0) >= 2 and 7 in nums:
        index_0_1 = nums.index(0)
        index_0_2 = index_0_1 + 1 + nums[index_0_1+1:].index(0)
        index_7 = len(nums) - 1 - nums[::-1].index(7)
        print(index_7)
        return index_0_1 < index_0_2 < index_7
    return False


print(spy_game([7,2,7,0,0,1,5]))
