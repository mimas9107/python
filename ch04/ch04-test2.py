# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:36:56 2024
 012345678
0*********
1
2 *     *
3
4  *   *
5
6   * *
7
8    *

"""

for i in range(9):
    
    if(i==0): print(i,"*"*(9-i),sep='')
    
    if(i%2==1): 
        print(i)    
    else:
        ## Analysis:
        ## Line2,4,6,8: "1st ident" + "1st *" + space + "2nd *" + "2nd ident"
        ##
        ## ident縮排個數: i//2,
        ##         
        ## * 個數: 2個 (i>length) 或是 1個( i== length )
        ##         第2個*, 當 length-i-1 == 0 時不顯示 :"*"*0
        ## space 個數: ( length-i-2) ie 5, 3, 1, 0
        ##         
        ## 
        if(i !=0 ):  
            print(i," "*(i//2),
                  "*"*(1),
                  " "*((9-i-2) if (9-i-2)>0 else 0),
                  "*"*(1 if 9-i-1>0 else 0),
                  " "*(i//2),sep='')
    