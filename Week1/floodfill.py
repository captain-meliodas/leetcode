#Link -> https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ini = image[sr][sc] # initial color before removing with new color
        n = len(image)
        m = len(image[0])
        
        #setting the delta row and col (row,col+1), (row,col-1), (row+1,col), (row-1,col)
        delRow = [0,0,1,-1]
        delCol = [1,-1,0,0]

        #set the new color to sr and sc
        image[sr][sc] = color

        #set the new color to neighbours 
        for i in range(4):
            nrow = sr + delRow[i]
            ncol = sc + delCol[i]

            if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and image[nrow][ncol] == ini and image[nrow][ncol] != color):
                self.floodFill(image,nrow,ncol,color)

        
        return image
        