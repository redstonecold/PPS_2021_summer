class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.oldColor=image[sr][sc]
        self.aa=[[0 for i in range(len(image[0]))] for j in range(len(image))]
 
        def search(image,i,j):
            self.aa[i][j]=1
            image[i][j]=newColor
            if i>=1 :
                if image[i-1][j]==self.oldColor and self.aa[i-1][j]==0:
                    search(image,i-1,j)
            if j>=1 :
                if image[i][j-1]==self.oldColor and self.aa[i][j-1]==0:
                    search(image,i,j-1)
            if i<=len(image)-2 :
                if image[i+1][j]==self.oldColor and self.aa[i+1][j]==0:
                    search(image,i+1,j)
            if j<=len(image[0])-2 :
                if image[i][j+1]==self.oldColor and self.aa[i][j+1]==0:
                    search(image,i,j+1)
        search(image,sr,sc)
        return image
 
a=Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
print(a.floodFill(image,1,1,2))