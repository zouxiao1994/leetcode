# encoding='utf-8'

'''
   author:zhangyu
   date:2019.8.29
   description:找出是否能跳出这个数组2
'''


def get_judge_jump_arr(arr):
    max = 0
    length = len(arr)
    for index in range(1, length):
        if arr[index - 1] == 0 and index > arr[max] + max:
            return False
        if arr[max] - (index - max) < arr[index]:
            max = index
    return True


def get_judge_jump_arr2(arr):
    '''
         跳远数组
    Args:
        arr: 数组

    Returns:
        是否能调到最后，布尔值

    '''''
    max = 0
    for i in range(1, len(arr)):
        if arr[i - 1] == 0 and i > max + arr[max]:
            return False
        if arr[i] > arr[max] - (i - max):
            max = i
    return True


if __name__ == '__main__':
    arr = [2, 3, 1, 1, 4]
    flag = get_judge_jump_arr(arr)
    print(flag)
