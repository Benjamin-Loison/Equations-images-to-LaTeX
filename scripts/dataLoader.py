#(data_size, channel_size, height, width),   (data_size, max_length, vocab_size)

import os
import glob
import torch
import numpy as np
# import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
# from torchvision import transforms, utils
from PIL import Image

#sentences  # list of list of ints corresponding to tokens
#vocab_size=len(wordToIndexes)
"""
to do :
    #ground_truth
    convert sentences to list of tensor of size (len_sentence)
    use list_to_tensor_normalized from main.ipynb on that list with pad value tensor for "pad"
    import big tensor to dataloader
    #pictures

torch_sentences=[torch.FloatTensor(sentence) for sentence in sentences]
big_tensor=torch.nn.utils.pad_sequence(tensor_sentences,batch_first=True,padding_value=wordToIndexes[pad])
"""

class LatexDataset(Dataset) :

    def __init__(self, root_dir):
        # Root directory
        self.root_dir = root_dir
        # Items :
        # self.formulas_lines
        # self.train_filter
        # self.test_filter
        # self.line_is_train
        # self.name_is_train
        # self.train_set
        # self.test_set
        
        # Lines of formulas
        formulas = open(self.root_dir + "formulas.lst")
        self.formulas_lines = formulas.read().splitlines() # list of strings
        formulas.close()
        
        # Train filter
        train = open(self.root_dir + "filter_train.lst")
        self.train_filter = train.read().splitlines()
        train.close()
        for i in range(len(self.train_filter)) :
            self.train_filter[i] = self.train_filter[i].split()
            self.train_filter[i][1] = int(self.train_filter[i][1])
        
        # Test filter
        test = open(self.root_dir + "filter_test.lst")
        self.test_filter = test.read().splitlines()
        test.close()
        for i in range(len(self.test_filter)) :
            self.test_filter[i] = self.test_filter[i].split()
            self.test_filter[i][1] = int(self.test_filter[i][1])

        # Reverse dictionnaries

            # key = line number | value = True iff it belongs to the train set
        self.line_is_train = {}
            # key = image_name  | value = True iff it belongs to the train set
        self.name_is_train = {}

        for i in range(len(self.train_filter)) :
            self.line_is_train[self.train_filter[i][1]] = True
        for i in range(len(self.test_filter)) :
            self.line_is_train[self.test_filter[i][1]] = False

        for i in range(len(self.train_filter)) :
            self.name_is_train[self.train_filter[i][0]] = True
        for i in range(len(self.test_filter)) :
            self.name_is_train[self.test_filter[i][0]] = False

        # Parting images
        self.train_set = []
        self.test_set = []
        
        for path in glob.glob(self.root_dir + "images/*") :
            img = Image.open(path).load()
            name = path.split('/')[2]
            if self.name_is_train[name] :
                self.train_set.append(img)
            else :
                self.test_set.append(img)
        # TODO : "big_tensor"

        

    def __len__(self):
        return len(self.line_is_train)



    # TODO :
    # def __getitem__(self, idx) :