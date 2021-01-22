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


目前，Camelot仅支持使用ASCII密码和算法代码1或2加密的PDF 。如果无法读取PDF，则抛出异常。这可能是由于未提供密码，密码不正确或加密算法不受支持。
Note:
    Camelot only works with text-based PDFs and not scanned documents. (As Tabula explains,
    "If you can click and drag to select text in your table in a PDF viewer, then your PDF is text-based".)
'''


import camelot
tables = camelot.read_pdf(filepath='camelot_chinese_test.pdf')

print(tables)

print(tables[0])
tables[0].df.to_html('camelot_chinese_test.pdf.html')
# tables.export('temp.csv', f='csv', compress=True) # json, excel, html
# tables[0].to_csv('camelot_temp.csv') # to json, to excel, to html
pandas_dataframe = tables[0].df
print(pandas_dataframe)



