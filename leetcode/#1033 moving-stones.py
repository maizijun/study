class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        x = min([a,b,c])
        z = max([a,b,c])
        y = a+b+c-x-z
        
        if any([z==y+2,y==x+2]):
            return [1,z-x-2]
        else:
            return [min(1,z-y-1)+min(1,y-x-1),z-x-2]