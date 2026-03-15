def solution(nums):
    answer = 0
    
    pocketmons = len(nums) // 2
    arr = set(nums)

    if len(arr) < pocketmons:
        answer = len(arr)
    else:
        answer = pocketmons
    
    return answer

if __name__ == "__main__":
    a = solution([3,3,3,2,2,4])
    print(a)