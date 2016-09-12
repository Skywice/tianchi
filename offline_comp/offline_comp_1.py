# -*- coding:utf-8 -*-
import os
import platform

# 获得计算机操作系统的类型
os = platform.platform()
print os
# 用户表及商品表地址，分操作系统
if os.startswith("Windows"):
    base_path = 'C:\\Users\\dell\\Desktop\\file\\tianchi\\fresh_comp_offline'
else:  # mac系统
    # user_table_path = ''
    pass

user_table = open(os.path.join(base_path, 'tianchi_fresh_comp_train_user.csv'))
item_table = open(os.path.join(base_path, 'tianchi_fresh_comp_train_item.csv'))

user_table_file = user_table.readlines()
line_num = len(user_table_file)
for i in range(line_num):
    print user_table_file[i]
