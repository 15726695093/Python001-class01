# Week04 学习笔记
### pandas
1. pandas 基本使用 pandas在当前目录和其他目录读取文件的两种方式，但是对交互模式不支持，还是需要进入目录执行
2. pandas 两大基本类型的使用:series和DataFrame
3. pandas数据导入:大量数据导入，使用read_*()的形式，主要有pd.read_excel(r'1.xlsx',sheet_name = 0)，pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')，df = pd.read_sql(sql,conn)
4. pandas数据预处理，缺失值处理和重复值处理
5. pandas数据调整，列选择、行选择、比较、数值替换（多对一替换、多对多替换）、排序（按照指定列降序排列、多列排序）、删除（删除列、删除行、删除特定行）、行列互换、索引重塑
6. pandas对数据的基本处理
7. pandas分组聚合
8. pandas多表拼接
9. pandas输出和绘图，使用 matplotlib 输出图标
10. 使用jieba和SnowNLP进行分词和情感倾向分析
### 作业说明
作业sql.py文件
### 其他
建议老师可以整理出每周比较好的代码获取提供规范代码供参考学习
