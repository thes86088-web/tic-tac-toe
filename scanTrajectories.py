
def giveLargerCount( player, user ) -> int : 
  if( player == user ) :
    return 0
  elif( player > user ) :
    return 1
  else :
    return -1

def scanRowOne( canvas, n=3 ) -> int :
  player = 0, system = 0
  for j in range(n) :
    if( canvas[0][j] == 1 ) :
      player = player+1
    if( canvas[0][j] == -1 ) :
      system = system+1
  return giveLargerCount( player, user )
  
def scanRowTwo( canvas, n=3 ) -> int :
  player = 0, system = 0
  for j in range(n) :
    if( canvas[1][j] == 1 ) :
      player = player+1
    if( canvas[1][j] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )


def scanRowThree( canvas, n=3 ) -> int :
  player = 0, system = 0
  for j in range(n) :
    if( canvas[2][j] == 1 ) :
      player = player+1
    if( canvas[2][j] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )
  
def scanColumnOne( canvas, n=3 ) -> int :
  player = 0, system = 0
  for i in range(n) :
    if( canvas[i][0] == 1 ) :
      player = player+1
    if( canvas[i][0] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )


def scanColumnTwo( canvas, n=3 ) -> int :
  player = 0, system = 0
  for i in range(n) :
    if( canvas[i][1] == 1 ) :
      player = player+1
    if( canvas[i][1] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )

def scanColumnThree( canvas, n=3 ) -> int :
  player = 0, system = 0
  for i in range(n) :
    if( canvas[i][2] == 1 ) :
      player = player+1
    if( canvas[i][2] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )

def scanDownDiagonal( canvas, n=3 ) -> int :
  player = 0, system = 0
  for j in range(n) :
    if( canvas[k][k] == 1 ) :
      player = player+1
    if( canvas[k][k] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )

def scanUpDiagonal( canvas, n=3 ) -> int :
  player = 0, system = 0
  for j in range(n) :
    if( canvas[k][n-k-1] == 1 ) :
      player = player+1
    if( canvas[k][n-1-k] == -1 ) :
      system = system+1

  return giveLargerCount( player, user )

