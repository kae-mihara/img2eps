# Image to eps python script
## Use matplotlib to convert a image file to eps format.

Usage: `img2eps.py imgfile [outputfile][.eps]`

If you don't specify the output file, it will be the same name and location with the input file, but with .eps suffix.

Or type: `im2eps.py --all [imgpath]` to convert all image files in the spcific path. The output files will be the same path as the input files.

## 使用matplotlib将image文件转换为eps格式

使用方法：`img2eps.py imgfile [outputfile][.eps]`

如果你不指定输出目录，输出文件会和输入文件同名，并输出到同一目录下。

或使用 `im2eps.py --all [imgpath]` 将指定目录下的所有图像转换为eps格式。同样，输出会位于同一目录下。