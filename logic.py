import numpy as np

#train on array first
canvas = np.zeros( (3, 3) )

def playerAboutToWin( canvas ) : '''
{
      return [ player_with_more_chances_to_win, row, column ]
                                                \         /
                                                where to place such that he wins
}
'''

def blockUserMoves( canvas, i, j ) : '''
{
      return [ player_with_more_chances_to_win, row, column ]
                                                \         /
                                                where to place such that he wins
}
'''

def completeOwnMoves( canvas, i, j ) : '''
{
      return [ player_with_more_chances_to_win, row, column ]
                                                \         /
                                                where to place such that he wins
}
'''

if ( playerAboutToWin() == 1 ) :
  blockUserMoves()
else
  completeOwnMoves()

'''
 0 -> open to occupy
 1 -> occupied by player/user
-1 -> occupied by system

'''
