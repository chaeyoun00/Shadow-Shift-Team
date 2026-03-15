def solution(strings, n):
    answer = []
    answer = sorted(sorted(strings), key=lambda x: x[n])
    return answer

if __name__ == "__main__":
    a = solution(["abce", "abcd", "cdx"], 2)
    print(a)