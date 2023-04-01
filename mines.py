import random as rd
row_1 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_2 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_3 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_4 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_5 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_6 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_7 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_8 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
row_9 = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
	 
matx = [row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9]
for i in range(8):
	matx[rd.randint(1,9 - 1)][rd.randint(1,9) -1] = '💣️'
x = 0
for i in matx:
	x += 1
	print(x,*i,sep='    ')
	print('\n')
matrix_sample = matx

def mine_count_list(row_in,col_in):
    row_in -= 1
    col_in -= 1
    mine_count = 0
    #for corner rows
    if row_in == 0:
        row_min = row_in
    else:
        row_min =  row_in - 1
    if row_in == len(matx)-1:
        row_max = row_in
    else:
        row_max = row_in + 1
    #for corner columns
    if col_in == 0:
        col_min = col_in
    else:
        col_min =  col_in - 1
    if col_in == len(matx)-1:
        col_max = col_in
    else:
        col_max = col_in + 1
        x = {'row':row_in,'row_s':row_min,'row_l':row_max,'col':col_in,'col_s':col_min,'col_l':col_max}
        return x
    
def mine_count(row_in,col_in):
    mine_count = 0
    #for corner rows
    if matx[row_in][col_in] == '💣️':
        return
    else:
        if row_in == 0:
            row_min = row_in
        else:
            row_min =  row_in - 1
        if row_in == len(matx)-1:
            row_max = row_in
        else:
            row_max = row_in + 1
    #for corner columns
        if col_in == 0:
            col_min = col_in
        else:
            col_min =  col_in - 1
        if col_in == len(matx)-1:
            col_max = col_in
        else:
            col_max = col_in + 1
    
        for row in range(row_min,row_max+1):
            for col in range(col_min,col_max+1):
                if matx[row][col] == '💣️':
                    mine_count += 1
        matrix_sample[row_in][col_in] = mine_count
                


def is_mine(row,col):
    if matx[row-1][col-1] == '💣️':
        return True
    else:
        return False

def check_for_mines(row_in,col_in):
        row_in -= 1
        col_in -= 1
        mine_count = 0
        #for corner rows
        if row_in == 0:
           row_min = row_in
        else:
            row_min =  row_in - 1
        if row_in == len(matx)-1:
            row_max = row_in
        else:
            row_max = row_in + 1
        #for corner columns
        if col_in == 0:
            col_min = col_in
        else:  
            col_min =  col_in - 1
        if col_in == len(matx)-1:
            col_max = col_in
        else:
            col_max = col_in + 1
        row = 0
        col = 0
    
        for row in range(row_min,row_max+1):
            for col in range(col_min,col_max+1):
                if matx[row][col] == '💣️':
                    mine_count += 1
        matrix_sample[row_in][col_in] = mine_count



row_inp = int(input("Enter row number: "))
col_num = int(input("Enter col num: "))
if is_mine(row_inp,col_num) == False:
    y = mine_count_list(row_inp,col_num)
    print(y)
    print(check_for_mines(row_inp,col_num))
    mine_count(y["row"],y["col_s"])
    mine_count(y["row"],y["col_l"])
    mine_count(y["row_s"],y["col"])
    mine_count(y["row_l"],y["col"])


else:
    print("Blast")

    

x = 0
for i in matrix_sample:
	x += 1
	print(x,*i,sep='    ')
	print('\n')


