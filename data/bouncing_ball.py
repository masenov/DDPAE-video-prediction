import torch
from torch.utils.data.dataset import Dataset  # For custom datasets
from torchvision import transforms, datasets
import numpy as np
import cv2

def bouncing_ball_images(folder="datasets/bouncing_ball/BouncingBall"):
    images = np.zeros((100,500,64,64))
    for i in range(100):
        for j in range(500):
            im = (cv2.imread(folder+"/"+str(i)+"/"+str(j)+".png"))
            #im = (im+np.random.random_sample(im.shape))/255.0-0.5
            im = (im+np.random.random_sample(im.shape))/255.0
            im = cv2.resize(im, (64, 64))
            #im = cv2.resize((cv2.imread(folder+"/"+str(i)+"/"+str(j)+".png"))/255.0, (25, 25))
            images[i,j,:,:] = im[:,:,0]
            print (i, j)
    return images


class BouncingBall(Dataset):
    def __init__(self):
        self.to_tensor = transforms.ToTensor()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        ntotal = 500
        nsample = 500
        self.orig_trajs = bouncing_ball_images()
        self.orig_trajs = torch.from_numpy(self.orig_trajs.reshape(100,ntotal,4096) + np.random.rand(100,ntotal,4096)/100).float()
        #np.take(self.orig_trajs,np.random.rand(self.orig_trajs.shape[0]).argsort(),axis=0,out=self.orig_trajs)
        self.samp_trajs = self.orig_trajs[:,::ntotal//nsample,:]
        self.orig_ts = np.linspace(0,4,500)
        self.samp_ts = self.orig_ts[::ntotal//nsample]
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


    def __getitem__(self, index):
        input = self.orig_trajs[index,:250,:].view(250,1,64,64)
        output = self.orig_trajs[index,250:,:].view(250,1,64,64)
        return input, output

    def __len__(self):
        return 50



#dataset = CustomDatasetFromImages()
