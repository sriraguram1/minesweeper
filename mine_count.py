#check_mine()
'''
matrix_1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
matrix_2 = [' ',1,' ',' ',' ',' ',' ',' ',' ']
matrix_3 = [' ',' ',' ',' ',' ',1,' ',' ',' ']
matrix_4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
matrix_5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
matrix_6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
matrix_7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
matrix_8 = [' ',' ',1,' ',' ',' ',' ',' ',' ']
matrix_9 = [' ',' ',' ',' ',' ',' ',1,' ',' ']
'''
matrix_1 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
matrix_2 = [0, 0, 0, 1, 1, 0, 0, 0, 0]
matrix_3 = [0, 0, 0, 0, 0, 1, 0, 0, 1]
matrix_4 = [0, 0, 0, 0, 0, 1, 0, 0, 0]
matrix_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix_6 = [0, 0, 0, 0, 1, 0, 0, 0, 0]
matrix_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix_9 = [0, 0, 1, 0, 0, 0, 0, 0, 0]
	 
matx = [matrix_1,matrix_2,matrix_3,matrix_4,matrix_5,matrix_6,matrix_7,matrix_8,matrix_9]
print("     1    2    3    4    5    6    7    8    9\n")

x = 0
for i in matx:
	x += 1
	print(x,*i,sep='    ')
	print('\n')

def check_mine(row_in,col_in):
    row_in -= 1
    col_in -= 1
    mine_count = 0
    #for corner rows
    if row_in == 0:
        row_min = row_in
    else:
        row_min =  row_in - 1
    if row_in == len(matx):
        row_max = row_in
    else:
        row_max = row_in + 1
    #for corner columns
    if col_in == 0:
        col_min = col_in
    else:
        col_min =  col_in - 1
    if col_in == len(matx):
        col_max = col_in
    else:
        col_max = col_in + 1
    
    for row in range(row_min,row_max):
        for col in range(col_min,col_max):
            if matx[row][col] == 1:
                mine_count += 1
    
    return mine_count
print(check_mine(3,5))
