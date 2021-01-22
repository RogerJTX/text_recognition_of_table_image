'''
camelot功能
功能完备性
camelot是一个可以从可编辑的pdf文档中抽取表格的开源框架，
与pdfplumber相比，其功能的完备性要差不少，因为除了表格抽取之外，
并不能用它从pdf文档中解析出字符、单词、文本、线等较为低层次的对象。
在表格抽取的过程中，camelot使用pdfminer实现底层对象的解析，
但是这些底层对象的抽取逻辑并没有封装成通用的函数或方法，
所以用camelot获取底层对象还是不太方便的。

两种表格抽取模式
camelot的主要功能是表格抽取，支持lattice和stream两种不同的模式，
其中lattice用来抽取线框类的表格，stream用来抽取非线框类的表格。

在抽取线框类表格的时候，lattice包含以下几步：
1.把pdf页面转换成图像
2.通过图像处理的方式，从页面中检测出水平方向和竖直方向可能用于构成表格的直线。
3.根据检测出的直线，生成可能表格的bounding box确定表格各行、
4.列的区域根据各行、列的区域，水平、竖直方向的表格线以及页面文本内容，
5.解析出表格结构，填充单元格内容，最终形成表格对象。
'''

'''
原理：
这个是把pdf每一页先转化成图像，然后使用形态学技术找到图像中的表格。
可以看下里面表格是怎么检测的，这里里面包含了表格的行列，和每个cell的坐标。
如果你的表格是图片，可以根据cell坐标提出roi，然后使用ocr进行识别。
'''

'''
两种表格抽取模式

camelot的主要功能是表格抽取，支持lattice和stream两种不同的模式，其中lattice用来抽取线框类的表格，stream用来抽取非线框类的表格。

在抽取线框类表格的时候，lattice包含以下几步：

    把pdf页面转换成图像
    通过图像处理的方式，从页面中检测出水平方向和竖直方向可能用于构成表格的直线。
    根据检测出的直线，生成可能表格的bounding box
    确定表格各行、列的区域
    根据各行、列的区域，水平、竖直方向的表格线以及页面文本内容，解析出表格结构，填充单元格内容，最终形成表格对象。

在抽取非线框类表格的时候，stream包含以下几步：

    通过pdfminer获取连续字符串
    通过文本对齐的方式确定可能表格的bounding box
    确定表格各行、列的区域
    根据各行、列的区域以及页面上的文本字符串，解析表格结构，填充单元格内容，最终形成表格对象。
'''


import camelot
tables = camelot.read_pdf(filepath='camelot_10_14.pdf',)

print(tables)

print(tables[0])
tables[0].df.to_html('camelot_temp_10_14.html')
# tables.export('temp.csv', f='csv', compress=True) # json, excel, html
# tabke[0].to_csv('camelot_temp.csv') # to json, to excel, to html
pandas_dataframe = tables[0].df
print(pandas_dataframe)

'''
以上的temp.html就是我希望得到的数据了，然后根据我的分析发现，在read_pdf方法里一定带上参数  【flavor='stream'】，不然的话就报这个错：
RuntimeError: Please make sure that Ghostscript is installed
原因就是，read_pdf默认的flavor参数是lattice，这个模式的话需要安装ghostscript库，
然后你需要去下载Python的ghostscript包和ghostscript驱动（跟使用selenium需要下载浏览器驱动一个原理），
而默认我们的电脑肯定是没有安装这个驱动的，所以就会报上面那个错。我试着去装了这个驱动和这个包，
去read_pdf时其实感觉没有本质区别，是一样的，所以带上参数flavor='stream'即可，当然如果你硬要用lattice模式的话，
安装完ghostscript包和ghostscript驱动之后，记得在当前py文件用  【import ghostscript】导入下这个包，不然还是会报如上错误
'''
