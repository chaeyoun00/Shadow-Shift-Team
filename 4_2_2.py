def solution(s):

    a = 0
    b = 0
    for i in s:
        if i == "(":
            a += 1
        
        if i == ")":
            b += 1

        if b > a:
            return False
        
    if (a == b):
        return True
    else:
        return False


if __name__ == "__main__":
    a = solution("(()(")
    print(a)