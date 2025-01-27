def all_path(maze,start,end):

	visited=set()
	all_path=[]
	
	def backtrack(x,y,path):
		if x<0 or y<0 or x>=m or y>=n or (x,y) in visited or maze[x][y]==1:
            return 
        
        path.append((x,y))
        visited.add((x,y))
        
        if x==end[0] and y==end[1]:
            all_path.append(path[:])
        else:
            backtrack(x-1,y,path)
            backtrack(x+1,y,path)
            backtrack(x,y-1,path)
            backtrack(x,y+1,path)
        
        path.pop()
        visited.remove((x,y))
        
    backtrack(start[0],start[1],[])
    
    return all_path
    
        
		