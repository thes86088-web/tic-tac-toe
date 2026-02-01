
def profitableToPlayer( canvas, i, j) :

def profitableToPlayer( canvas, i, j) :

def placeTheMove( canvas, row, column, n=3 ) :
  for i in range( n ) :
    for j in range( n ) :
      if( canvas[i][j} == 0  ) :
        if ( profitableToPlayer( canvas, i, j) ) : 
          occupy( canvas, i, j )
        else if( profitableToSystem( canvas, i, j ) ) :
          occupy( canvas, i, j )

