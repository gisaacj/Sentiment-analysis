# -*- coding:utf-8 -*-
'''
1、导入模块
      import xlrd
2、打开Excel文件读取数据
       data = xlrd.open_workbook('excelFile.xls')
3、使用技巧
    获取一个工作表 
        table = data.sheets()[0]          #通过索引顺序获取 
        table = data.sheet_by_index(0) #通过索引顺序获取 
        table = data.sheet_by_name(u'Sheet1')#通过名称获取 
    获取整行和整列的值（数组） 　　
         table.row_values(i) 
         table.col_values(i) 
    获取行数和列数　　
        nrows = table.nrows 
        ncols = table.ncols
    循环行列表数据
        for i in range(nrows ):
        print table.row_values(i)
    单元格
        cell_A1 = table.cell(0,0).value
        cell_C4 = table.cell(2,3).value
    使用行列索引
        cell_A1 = table.row(0)[0].value
        cell_A2 = table.col(1)[0].value
    简单的写入
        row = 0
        col = 0
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1 value = '单元格的值'
xf = 0 # 扩展的格式化 
table.put_cell(row, col, ctype, value, xf)
table.cell(0,0)  #单元格的值'
table.cell(0,0).value #单元格的值'
'''
import os,sys
import xlrd
import jieba

#PA 乐 PE 安 PD 敬 PH 赞 PG 信 PB 爱 PK 祝 NA 怒
#NB 悲 NJ 丧 NH 疚 PF 思 NI 慌 NC 惧 NG 羞 NE 烦 ND 憎 NN 责 NK 妒 NL 疑 PC 惊
emotion={'PA':'乐','PE':'安','PD':'敬','PH':'赞','PG':'信','PB':'爱','PK':'祝','NA':'怒','NB':'悲','NJ':'丧','NH':'疚','PF':'思','NI':'慌','NC':'惧','NG':'羞','NE':'烦','ND':'憎','NN':'责','NK':'妒','NL':'疑','PC':'惊'}
emotion_num={'PA':0,'PE':0,'PD':0,'PH':0,'PG':0,'PB':0,'PK':0,'NA':0,'NB':0,'NJ':0,'NH':0,'PF':0,'NI':0,'NC':0,'NG':0,'NE':0,'ND':0,'NN':0,'NK':0,'NL':0,'PC':0}
data=xlrd.open_workbook("qgch.xlsx")
table = data.sheets()[0]
nrows = table.nrows
word=input()
s=0
words=jieba.cut(word)
for w in words:
    for i in range(nrows):
        if(table.cell(i,0).value == w):
            emotion_num[table.cell(i,4).value]+=1
            s+=1
for key,num in emotion_num.items():
    if num > 0:
        print(emotion[key]+':'+str(format(num/s,'.2%')))



