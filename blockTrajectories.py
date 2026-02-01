
def blockOnRows( canvas ) :
  blockOnRowOne( canvas )
  blockOnRowTwo( canvas )
  blockOnRowThree( canvas )

def blockOnColumns( canvas ) :
  blockOnColumnOne( canvas )
  blockOnColumnTwo( canvas )
  blockOnColumnThree( canvas )

def blockOnDiagonals( canvas ) :
  blockOnUpDiagonal( canvas )
  blockOnDownDiagonal( canvas )

def blockUserMoves( canvas ) :
  blockOnRows( canvas )
  blockOnColumns( canvas )
  blockOnDiagonals( canvas )
