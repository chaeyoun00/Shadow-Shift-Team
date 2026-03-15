# def solution(board, moves):
#     answer = 0
#     x = []
#     for i in range(0, len(moves)):
#         if board[moves[i] - 1][-1] == 0:
#             board[moves[i] - 1].pop()
#             continue
        
#         if len(x) == 0:
#             x.append(board[moves[i] - 1][-1])
#             board[moves[i] - 1].pop()
#             continue
        
#         if x[-1] == board[moves[i] - 1][-1]:
#             answer += 2
#             x.pop()
#             board[moves[i] - 1].pop()
#         else:
#             x.append(board[moves[i] - 1][-1])

#     return answer
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            print(i, j, board[j][i-1])
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

if __name__ == "__main__":
    a = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    print(a)