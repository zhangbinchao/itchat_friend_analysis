
import PIL.Image as Image
import os
from math import sqrt

headImgPath = 'F:\Python_code\Web_Spider\wechat\img'
pathList = []
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
for item in os.listdir(headImgPath):
    imgPath = os.path.join(headImgPath, item)
    pathList.append(imgPath)

total = len(pathList)#total是好友头像图片总数
line = int(sqrt(total))#line是拼接图片的行数（即每一行包含的图片数量）
NewImage = Image.new('RGB', (128*line,128*line))
x = y = 0
for item in pathList:
    try:
        img = Image.open(item)
        # Image.ANTIALIAS：平滑滤波。对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。
        img = img.resize((128,128),Image.ANTIALIAS)
        NewImage.paste(img, (x * 128 , y * 128))
        x += 1
    except IOError:
        print("第%d行,%d列文件读取失败！IOError:%s" % (y,x,item))
        x -= 1
    if x == line:
        x = 0
        y += 1
    if (x+line*y) == line*line:
        break
NewImage.save("final.jpg")

