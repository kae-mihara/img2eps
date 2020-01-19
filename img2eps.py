############################################################################
# File image_to_eps.py
# Date: 2020-01-19 
# Author: kae mihara
############################################################################

import sys
import os

try:
    import matplotlib.pyplot as plt
except ImportError:
    print('Error: matplotlib not exist!')
    print('try: ')
    print('    pip install matplotlib --user')
    print('then excute this script')

def convert_file(img_path, out_path):
    img = plt.imread(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(out_path)
    print(str.format('saved at {}.', out_path))

def print_usage():
    print('Use matplotlib to convert a image file to eps format.')
    print('Usage: img2eps.py imgfile [outputfile][.eps]')
    print("If you don't specify the output file, it will be the same name and location with the input file, but with .eps suffix.")
    print()
    print('Or type: im2eps.py --all [imgpath]')
    print('to convert all image files in the spcific path.')

def convert_single(args):
    img_path = args[1]
    img_name = img_file = out_path = ''
    try:
        img_dir, img_file = os.path.split(img_path)
        img_name,_ = os.path.splitext(img_file)
        out_path = os.path.join(img_dir, img_name + '.eps')
    except:
        print('Error: Invalid input file path!')
        exit()
    
    if len(args) > 2:
        out_path = args[2]
        try:
            os.path.split(out_path)
            if out_path.find('.eps') == -1:
                out_path = out_path + '.eps'
        except:
            print('Error: Invalid output file path!')
            exit()
    convert_file(img_path, out_path)

def is_img(file):
    for s in ['.jpg', '.png', '.bmp','.gif','.jpeg', 'jpe']:
        if file.endswith(s):
            return True
    return False

def convert_all(dir):
    files = os.listdir(dir)
    for file in files:
        if not is_img(file):
            continue
        name,_ = os.path.splitext(file)
        img_path = os.path.join(dir,file)
        out_path = os.path.join(dir,name+'.eps')
        convert_file(img_path,out_path)

def main():
    args = sys.argv
    if len(args)== 1:
        print_usage()
        exit()
    arg1 = args[1]
    if(arg1 == '--all'):
        dir = '.' if len(args) <= 2 else args[2]
        convert_all(dir)
        exit()
    if(arg1 == '--help'):
        print_usage()
        exit()
    convert_single(args)

main()




