import torch
import cv2
import numpy as np
import torch.nn as nn
datalist = ['calling','normal','smoking']
if __name__ =="__main__":
    net = torch.load('cpkt/ep020-train_acc0.952-val_acc0.814.pth').to('cpu')
    img_path = 'q.jpeg'
    img = cv2.imread(img_path)
    img = torch.tensor(np.transpose(img/255,(2,0,1)),device='cpu',dtype=torch.float32).view(-1,3,img.shape[0],img.shape[1])
    net.eval()
    result = net(img)
    print(datalist[torch.argmax(result).item()])