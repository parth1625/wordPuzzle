import sys

def writeFile(get_result):
    f = open(fname.split(".")[0]+".out","a+")
    if get_result[0] in duplicate:
        return "Duplicate"
    duplicate.append(get_result[0])
    f.write(" ".join(get_result))
    f.write("\n")
    f.close()

def rightWord(word,row,a,start,b=1):
    if b<len(word) and a+1<=total_col and word[b] == newArray[row][a+1]:
        if b+1>=len(word):
            # print(word,(row+1,start),(row+1,start+b))
            writeFile([word,str((row+1,start)),str((row+1,start+b))])
            return True
        rightWord(word,row,a+1,start,b+1)
    else:
        return "not found"
    return True

def downWord(word,col,a,start,b=1):
    if b<len(word) and a+1<=total_row and word[b] == newArray[a+1][col]:
        if b+1>=len(word):
            # print(word,(start,col+1),(start+b,col+1))
            writeFile([word,str((start,col+1)),str((start+b,col+1))])
            return True
        downWord(word,col,a+1,start,b+1)
    else:
        return "not found"
    return True

def leftWord(word,row,a,start,b=1):
    if b<len(word) and a-1>=0 and word[b]==newArray[row][a-1]:
        if b+1>=len(word):
            # print(word,(row+1,start),(row+1,start-b))
            writeFile([word,str((row+1,start)),str((row+1,start-b))])
            return True
        leftWord(word,row,a-1,start,b+1)
    else:
        return "not found"
    return True

def upWord(word,col,a,start,b=1):
    if b<len(word) and a-1>=0 and word[b]==newArray[a-1][col]:
        if b+1>=len(word):
            # print(word,(start,col+1),(start-b,col+1))
            writeFile([word,str((start,col+1)),str((start-b,col+1))])
            return True
        upWord(word,col,a-1,start,b+1)
    else:
        return "not found"
    return True

def matchAllWords(word,row,col):
    if (row-1)>=0 and word[1] == newArray[row-1][col]: #Up
        res = upWord(word,col,row,start=row+1)
        if res == True:
            return True
        else:
            return "not found"
    elif (col-1)>=0 and word[1] == newArray[row][col-1]: #Left
        res = leftWord(word,row,col,start=col+1)
        if res == True:
            return True
        else:
            return "not found"
    elif row+1<total_row and word[1] == newArray[row+1][col]: #Down
        res = downWord(word,col,row,start=row+1)
        if res == True:
            return True
        else:
            return "not found"
    elif col+1<total_col and word[1] == newArray[row][col+1]: #Right
        res = rightWord(word,row,col,start=col+1)
        if res == True:
            return True
        else:
            return "not found"
    else:
        return False

def main(filename):
    global newArray,total_col,total_row,fname,duplicate
    fname = filename
    f = open(fname,'r')
    puzzle = f.read().split("\n")
    f.close()
    gridlines,words,duplicate = [],[],[]
    newline = False
    for p in puzzle:
        if p == '':
            newline = True
            continue
        if newline == False:
            gridlines.append(p)
        if newline == True:
            words.append(p)

    for grid in gridlines:
        if len(gridlines) != len(grid):
            print("Grid is not valid!")
        total_row = len(gridlines)
        total_col = len(grid)

    newArray = []
    for grid in gridlines:
        newArray.append(list(grid))

    for word in words:
        result = False
        for i in range(len(list(word))):
            row = 0
            for grid in gridlines:
                col = 0
                for j in range(len(list(gridlines))):
                    if word[i] == grid[j]:
                        final = matchAllWords(word,row,col)
                        if final == True:
                            result = True
                            # print(word,start)
                            break
                    col += 1
                row += 1
        if result == False:
            # print(word, "not found")
            writeFile([word, "not found"])

if __name__== '__main__':
    if len(sys.argv) < 2:
        print("No input file is given")
        sys.exit()
    if sys.argv:
        f = open(sys.argv[1].split(".")[0]+".out",'w')
        f.close()
        main(sys.argv[1])