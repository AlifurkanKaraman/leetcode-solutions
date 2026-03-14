for num in hash_set:
    if num - 1 not in hash_set:
        curr_streak = 1
        curr_num = num
        while curr_num + 1 in hash_set:
            curr_streak += 1
            curr_num += 1
        longest_streak = curr_streak
    