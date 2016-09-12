# -*- coding:utf-8 -*-
import os
import platform

# 获得计算机操作系统的类型
os = platform.platform()
print os
# 用户表及商品表地址，分操作系统 Windows and Mac
if os.startswith("Windows"):  # windows系统
    base_path = 'C:\\Users\\dell\\Desktop\\file\\tianchi\\fresh_comp_offline'
    user_table = open(base_path+'\\'+'tianchi_fresh_comp_train_user.csv')
    item_table = open(base_path+'\\'+'tianchi_fresh_comp_train_item.csv')
elif os.startswith('Darwin'):  # mac系统
    base_path = '/Users/Skywice/Desktop/Python_App/tianchi_data/fresh_comp_offline'
    user_table = open(base_path+'/'+'tianchi_fresh_comp_train_user.csv')
    item_table = open(base_path+'/'+'tianchi_fresh_comp_train_item.csv')

user_table_content = user_table.readlines()
line_num = len(user_table_content)
for i in range(10):
    # print user_table_content[i]
    pass

# close files, can't be forgot
user_table.close()
item_table.close()
