import random
import os
trainval = 0.9
train = 0.9

filename = ['./dataset/train.txt','./dataset/val.txt', './dataset/test.txt']
datafile = './dataset/train'
classes = ['calling','normal','smoking']

def split_train(file,classname):
    classnames = os.listdir(os.path.join('dataset/train',classname+'_images'))
    print(os.path.join('dataset',classname+'_images'))
    random.shuffle(classnames)
    size = len(classnames)
    print(size)
    for i in range(0,int(size*trainval*train)):
        print(classname,':',i)
        file[0].write(datafile+'/'+classname+'_images'+'/'+classnames[i]+'\t'+classname+'\n')
    for i in range(int(size*trainval*train),int(size*trainval)):
        file[1].write(datafile+'/'+classname+'_images'+'/'+classnames[i]+'\t'+classname+'\n')
    for i in range(int(size * trainval),size):
        file[2].write(datafile+'/'+classname+'_images'+'/'+classnames[i]+'\t'+classname+'\n')

if __name__ == "__main__":
    random.seed(0)
    file = []
    for i in filename:
        file.append(open(i, 'w'))
    for i in classes:
        split_train(file,i)
    for i in file:
        i.close()
