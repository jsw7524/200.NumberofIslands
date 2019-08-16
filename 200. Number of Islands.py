class Solution(object):
    def __init__(self):
        self.stack=[]


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) ==0:
            return 0
        self.map=grid
        self.width=len(self.map[0])
        self.height=len(self.map)
        islands=0

        for x in range(self.width):
            for y in range(self.height):
                if 1==self.DFS(y,x):
                    islands+=1
        return islands

    def DFS(self,y,x):
        foundIsland=0
        if self.map[y][x]=='1':
            foundIsland=1
            self.stack.append((y,x))
        while len(self.stack) > 0:
            y,x=self.stack.pop()
            if (self.map[y][x] == '0'):
                pass
            else:
                self.map[y][x]='0'
                if y-1>=0 :
                    self.stack.append((y-1,x))
                if y+1<self.height :
                    self.stack.append((y+1,x))
                if x-1 >=0:
                    self.stack.append((y,x-1))
                if x+1<self.width:
                    self.stack.append((y,x+1))
        return foundIsland

sln=Solution()
assert 1==sln.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
assert 0==sln.numIslands([])