# f = open("puzzle1.pzl",'r')
f = open("puzzle2.pzl",'r')
# puzzle = f.readlines()
puzzle = f.read().split("\n")
# print(puzzle)

## Get Grid lines and Words to find 
gridlines = []
words = []
newline = False
for p in puzzle:
    if p == '':
        newline = True
        continue
    if newline == False:
        gridlines.append(p)
    if newline == True:
        words.append(p)
print(gridlines,words)

## Find if Rows and Columns are same.
for grid in gridlines:
    if len(gridlines) != len(grid):
        print("Grid in not valid!")
    total_row = len(gridlines)
    total_col = len(grid)
# print(total_row,total_col)

newArray = []

for grid in gridlines:
    newArray.append(list(grid))

def rightWord(word,row,a,b=1):
    if b<len(word) and a<=total_col and word[b] == newArray[row][a+1]:
        # print("Matched {}".format(word[b]))
        rightWord(word,row,a+1,b+1)
        if b>=len(word):
            return True
    else:
        # print("Not matched")
        return False 

def downWord(word,col,a,b=1):
    if b<len(word) and a+1<=total_row and word[b] == newArray[a+1][col]:
        # print("Matched {}".format(word[b]))
        downWord(word,col,a+1,b+1)
    else:
        # print("Not matched")
        return False
    return True

def leftWord(word,row,a,b=1):
    if b<len(word) and a-1>=0 and word[b]==newArray[row][a-1]:
        leftWord(word,row,a-1,b+1)
    else:
        return False
    return True

def upWord(word,col,a,b=1):
    if b<len(word) and a-1>=0 and word[b]==newArray[a-1][col]:
        upWord(word,col,a-1,b+1)
    else:
        return False
    return True

def matchAllWords(word,row,col):
    # print(newArray[row][col],row+1,col+1)
    if (row-1)>=0 and word[1] == newArray[row-1][col]:
        # print("Letter {} matched".format(word[1]), "Up")
        result = upWord(word,col,row)
        if result == True:
            return True
        else:
            return False
    elif (col-1)>=0 and word[1] == newArray[row][col-1]:
        # print("Letter {} matched".format(word[1]), "Left")
        result = leftWord(word,row,col)
        if result == True:
            return True
        else:
            return False
    elif row+1<total_row and word[1] == newArray[row+1][col]:
        # print("Letter {} matched".format(word[1]), "Down")
        result = downWord(word,col,row)
        if result == True:
            return True
        else:
            return False
    elif col+1<total_col and word[1] == newArray[row][col+1]:
        # print("Letter {} matched".format(word[1]), "Right")
        result = rightWord(word,row,col)
        if result == True:
            return True
        else:
            return False
    else:
        return False

## Check String horizontally.
for word in words:
    for i in range(len(list(word))):
        row = 0
        for grid in gridlines:
            col = 0
            for j in range(len(list(gridlines))):
                if word[i] == grid[j]:
                    # print(row,col)
                    start = [row+1,col+1]
                    result = matchAllWords(word,row,col)
                    if result == True:
                        print(word,start)
                        break
                col += 1
            row += 1