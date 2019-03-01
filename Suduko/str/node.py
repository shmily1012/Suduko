'''
Created on Feb 26, 2019

@author: Sasha
'''


class node(object):
    '''
    classdocs
    '''

    def __init__(self, x, y, value, iscondition=False):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.value = value
        self.iscondition = iscondition
        self.possible_data_array = [n for n in range(1, 50)]
#         print(self.possible_data_array)

        
if __name__ == "__main__":
    node(1, 2, 3)
