def solution(arr):
    answer = []
    i = 0
    for j in range(1, len(arr)):
        if j == len(arr) - 1:
            answer.append(arr[i])
            if arr[i] != arr[j]: 
                answer.append(arr[j])
            break
            
        if arr[i] != arr[j]:
            answer.append(arr[i])
            i = j
            if i >= len(arr): break
    return answer


if __name__ == "__main__":
    a = solution([4,4,4,3,3])
    print(a)