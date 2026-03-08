def solution(numbers):
    answer = []
    answer.append(numbers[0] + numbers[1])
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
                print(i, numbers[i] , j, numbers[j])
                print(numbers[i] + numbers[j])

    return sorted(answer)

if __name__ == "__main__":
    a = solution([5,0,2,7])
    print(a)