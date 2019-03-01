'''
Created on Feb 26, 2019

@author: Sasha
'''
from str.Sudoku import Sudoku
from str.node import node

import time

DONE = 0x888

if __name__ == '__main__':
    s = Sudoku(49)
    
#     if s.getLowestPossibleNode():
#         print('pass')
#     n = True
    while True:
        if s.UpdateAllNodesPossibleNumArray() == False:
#             print("dump out")
            n = s.rollback()
        else:
            n = s.getLowestPossibleNode()
            if n == DONE:
                print('DONE!')
                break
#         print('n=', n.x, n.y, n.possible_data_array)
        s.assignValueintoNode(n.x, n.y, n.possible_data_array[0])
        s.show()
        
#         time.sleep(10)
