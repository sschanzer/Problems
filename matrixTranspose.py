#! /usr/bin/env python3

'''
Matrix Transpose
'''

def transpose(A: list[list[int]]) -> list[list[int]]:
        N = len(A)
        M = len(A[0])

        print(A[0])
        
        trans = [[0] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                trans[i][j] = A[j][i]
            
        return trans

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))
    

    