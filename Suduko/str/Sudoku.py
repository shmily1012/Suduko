'''
Created on Feb 26, 2019

@author: Sasha
'''
from node import node
from math import sqrt

DONE = 0x888


def remove_data(array, value):
    try:
        array.remove(value)
    except ValueError:
        pass 
    return array


class Sudoku(object):
    '''
    classdocs
    '''

    def __init__(self, length=3):
        '''
        Constructor
        '''
        self.length = length
        self.table = list()
        self.footprint = list()
        for i in range(length):
            row = list()
            for j in range(length):
                n = node(i, j, 0)
                row.append(n)
            self.table.append(row)
        self.addconditions('input2.txt')
        self.show()
#         for item in self.table:
#             print(item)
    
    def addNodes(self, nodes):
        for n in nodes:
            self.table[n.y][n.x] = n.value

    def addconditions(self, filename):
        fi = open(filename, 'r')
        buf = fi.readlines()
        for line in buf:
            i = line.split(',')
            x = int(i[0], 10)
            y = int(i[1], 10)
            v = int(i[2], 10)
            n = node(x=x, y=y, value=v, iscondition=True)
            self.table[x][y] = n

    def show(self):
        str = ''
        for i in range(self.length * 3):
            str += '*'
        print(str)
        for y in range(self.length):
            row_str = ''
            for x in range(self.length):
                row_str += '%3d' % self.table[x][y].value
            print(row_str) 
    
        print(str)

    def UpdateAllNodesPossibleNumArray(self):
        
        u = int(sqrt(self.length))
        for line in self.table:
            for node in line:
                if node.iscondition:
                    continue
                else:
                    if node.value != 0:
                        continue
                    y = node.y
                    temp_row = set()
                    # from the same ROW
                    for x in range(self.length):
                        if self.table[x][y].value != 0:
                            temp_row.add(self.table[x][y].value)
                    # from the same column
                    x = node.x
                    temp_column = set()
                    for y in range(self.length):
                        if self.table[x][y].value != 0:
                            temp_column.add(self.table[x][y].value)
                    # from the same box
                    box_x = int((node.x) / u)
                    box_y = int((node.y) / u)
                    temp_box = set()
                    for x in range(u):
                        x += (box_x * u)
                        for y in range(u):
                            y += (box_y * u)
#                             print(self.table[x][y].value)
#                             print(x, y)
                            if self.table[x][y].value != 0:
                                temp_box.add(self.table[x][y].value)
                    # caculate
                    total = temp_box | temp_column | temp_row
                    
                    temp = set(n for n in range(1, self.length + 1))

                    rest = temp - total
                    node.possible_data_array = [n for n in rest]
                    if len(node.possible_data_array) == 0 and node.value == 0:
#                         print()
#                         print("x=%d\ty=%d\t" % (node.x, node.y), "possible=", node.possible_data_array)
#                         print('temp_row=', temp_row)
#                         print('temp_column=', temp_column)
#                         print('temp_box=', temp_box)

                        return False
        return True

    def getLowestPossibleNode(self):
        min = 1000
        theNode = None
        
        for line in self.table:
            for node in line:
                if node.value == 0:
                    if len(node.possible_data_array) == 0:
                        return False
                    elif min > len(node.possible_data_array):
                        min = len(node.possible_data_array)
                        theNode = node
        if theNode == None:
            return DONE
#         print('theNode=', theNode.x, theNode.y, theNode.possible_data_array)
        return theNode
        pass

    def assignValueintoNode(self, x, y, value):
        self.table[x][y].value = value
#         print('value=', value)
#         print('before self.table[x][y].possible_data_array=', self.table[x][y].possible_data_array)
        self.table[x][y].possible_data_array.remove(value)
#         print('after self.table[x][y].possible_data_array=', self.table[x][y].possible_data_array)
        
        self.footprint.append(self.table[x][y])
#         for i in self.footprint:
#             print('self.footprint=', i.x,
#                   i.y,
#                   i.value,
#                   i.possible_data_array)
        
        pass

    def rollback(self):
#         print('rollback...')
        n = self.footprint.pop()
#         print('n=', n.x, n.y, n.value, n.possible_data_array)
        self.table[n.x][n.y].value = 0
        if len(n.possible_data_array) == 0:
            node1 = self.rollback()
            return node1
        else:
#             print('***n=', n.x, n.y, n.value, n.possible_data_array)
            return n


if __name__ == "__main__":
    s = Sudoku(9)
