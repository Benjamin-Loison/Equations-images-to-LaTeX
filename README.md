# Equations images to LaTeX

Architecture :
- Input : picture of size (H,W)
- CNN : convert pictures to features at size (H',W',F)
- RNN : to be discussed, should output probability vectors of length V the vocabulary size.
- Word embedding layer : should be used to learn that `{` often comes with `}` for example.

On the RNN :
- could take as input a vector of size (H'\*W',F) which means LSTM would take inputs that are F-dimensionnal
- could take as input the columns of the pictures, which means LSTM would take inputs of size (H',F)

Notes :
- pictures are in black and white
- tokens are encoded as one-hot

To do :

Practical part :
- decide how to normalize the input of the network
  - is it important that all the pictures have the same size ?
  - interpolation should output black and white picture (nearest niehgbour does it already)
- find the number of tokens (size of latex vocabulary) required for the dataset

Theoretical part :
- find how the network decides on the number of probability vectors to output
- understand the effect of stacked/bidirectionnal LSTM

Sources:

A GRU-based Encoder-Decoder Approach with Attention for Online Handwritten Mathematical Expression Recognition https://arxiv.org/pdf/1712.03991.pdf

TC11_package2014.zip http://tc11.cvc.uab.es/datasets/CROHME-2014_2

inkml2img.py https://github.com/RobinXL/inkml2img
