
def profitableCell( canvas, i, j, value, n=3 ) :
  left = j-1>-1 and (canvas[i][j-1] == value)
  right = j+1<n and (canvas[i][j+1] == value)
  
  up = i-1>-1 and (canvas[i-1][j] == value)
  down = i+1<n and (canvas[i+1][j] == value)

  left_up = j-1>-1 and i-1>-1 and (canvas[i-1][j-1] == value)
  right_up = j+1<n and i-1>-1 and (canvas[i-1][j+1] == value)

  left_down = i+1<n and j-1>-1 and (canvas[i+1][j-1] == value)
  right_down = i+1<n and j+1<n and (canvas[i+1][j+1] == value)
  
  if( left_up or right_down ) :
    return 1
  elif( right_up or left_down ) :
    return 1
  elif( (left and right) or ( up and down  ) ) :
    return 1
    else :
      return 1
  

def occupy( canvas, i, j ) :
  canvas[i][j] = -1

def placeTheMove( canvas, n=3 ) :
  for i in range( n ) :
    for j in range( n ) :
      if( canvas[i][j] == 0  ) :
        if ( profitableCell( canvas, i, j, 1, n=3 ) ) : 
          occupy( canvas, i, j )
        elif( profitableCell( canvas, i, j, -1, n=3 ) ) :
          occupy( canvas, i, j )

