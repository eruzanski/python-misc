# Given an array of length N (even), keep only k elements of the array and return the maximum number of unique elements in that array. 
# The best time complexity of this algorithm is O(N), average and worst time complexities are O(klogN).

from collections import Counter

def max_unique_vals(T, k):
    input_cnt_arr = sorted(T, key=Counter(T).get)
    unique_val_arr = []
    for i in range(len(input_cnt_arr)):
        if input_cntr_arr[i] not in unique_val_arr:
            unique_val_arr.append(input_cnt_arr[i])
    return k if k < len(unique_val_arr) else len(unique_val_arr)
