# Equations images to LaTeX

Architecture :
- Input : picture of size (H,W)
- CNN : convert pictures to features at size (H',W',F)
- RNN : to be discussed, should output probability vectors of length V the vocabulary size.
- Word embedding layer : should be used to learn that `{` often comes with `}` for example.
  - word embedding is used before the RNN
- attention mechanism : is used to put weights on the input of the RNN
  - uses output of CNN and hidden state of RNN block t-1 to compute weights for RNN block t

On the RNN :
- could take as input a vector of size (H'\*W',F) which means LSTM would take inputs that are F-dimensionnal
- could take as input the columns of the pictures, which means LSTM would take inputs of size (H',F)

Notes :
- pictures are in black and white
- tokens are encoded as one-hot
- attention mechanism isn't implemented

To do :

Practical part :
- [ ] decide how to normalize the input of the network
  - is it important that all the pictures have the same size ?
    > it's necessary for batch learning
  - interpolation should output black and white picture (nearest niehgbour does it already)
- [x] find the number of tokens (size of latex vocabulary) required for the dataset
  > we know have a script to get that back from dataset

Theoretical part :
- [x] find how the network decides on the number of probability vectors to output
  > this works by padding, we pad with 0 in order to get the desired length. Learning and RNNs will do the rest of the work
- [x] understand the effect of stacked/bidirectionnal LSTM
  > Stacking multiple layers of LSTM increase the depth of the RNN and thus helps to capture more complex language semantics. Using bidirectional cells in each layer helps to capture the contexts from both forward and backward directions between tokens.
  
  Source : https://arxiv.org/ftp/arxiv/papers/1908/1908.11415.pdf

Sources:

A GRU-based Encoder-Decoder Approach with Attention for Online Handwritten Mathematical Expression Recognition https://arxiv.org/pdf/1712.03991.pdf

TC11_package2014.zip http://tc11.cvc.uab.es/datasets/CROHME-2014_2

inkml2img.py https://github.com/RobinXL/inkml2img
