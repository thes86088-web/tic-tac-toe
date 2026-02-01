
available = []

 def takeUserMove(canvas) :
   i = int(input("row value : "))
   j = int(input("column value : "))
   canvas[i][j] = 1
   
for i in range(n) :
  for j in range(n) :
    available.append( [i,j] )

while( available.len() > 0  ) :
  takeUserMove( canvas )
  placeTheMove( canvas )

if(  )

