
#train on array first

if ( playerAboutToWin() == 1 ) :
  blockUserMoves()
else
  completeOwnMoves()

'''
 0 -> open to occupy
 1 -> occupied by player/user
-1 -> occupied by system

'''
