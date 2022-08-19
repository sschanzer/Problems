#! /usr/bin/env python3

'''
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a 
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), 
and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
'''


def floodFill(image, sr: int, sc: int, color: int):

    row = len(image)
    col = len(image[0])
    initial_color = image[sr][sc]

    if initial_color == color:
        return image

    def df_search(r,c):
        if image[r][c] == initial_color:
            image[r][c] = color
            if r >= 1:
                df_search(r - 1, c)
            if r + 1 < row:
                df_search(r + 1, c)
            if c >= 1:
                df_search(r, c - 1)
            if c + 1 < col:
                df_search(r, c + 1)
    
    df_search(sr, sc)

    return image


if __name__ == '__main__':
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print(floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
    # [[0, 0, 0], [0, 0, 0]]
    print(floodFill([[0,0,0],[0,0,0]], 1, 0, 2))
    # [[2, 2, 2], [2, 2, 2]]
    