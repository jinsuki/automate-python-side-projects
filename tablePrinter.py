tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(table) #List of rjust values to be used
    
    for i in range(len(table)): #iterates through the 3 lists
        rjustlength = 0 
        for j in table[i]: #loops each index of list and keeps larger number
            if len(j) > rjustlength:
                rjustlength = len(j)
                colWidth[i] = rjustlength

    #formats the columns of print
    for y in range(len(table[0])): #iterates through number of strings in sublist
            for x in range(len(table)): #for each x        
                word = table[x][y]
                print(word.rjust(colWidth[x]),end = ' ')
            print("")
            
printTable(tableData)


