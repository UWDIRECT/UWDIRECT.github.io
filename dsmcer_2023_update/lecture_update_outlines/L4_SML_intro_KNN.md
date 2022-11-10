# L4 (2p) SML intro using KNN

1. Supervised ML definition (25 min)
  - image of model, inputs, outputs
  - each pair is labeled
  - We have to choose the architecture that we use to relate X to y
  - These choices are called hyperparameters
  - question:
    - given that our data is labeled and our goal is to predict the label, how can we evaluate the model?
    - > error on data
    - given what we saw about how a sample of data can be biased, what data should we compute error on
2. sklearn brief intro (15 min)
  - lots of what we do in ML is done for us, you will see things from this package throughout the rest of the course
  - load DES data and do random split
3.  KNN is one such model (65 min)
  - 2D image of points, classes as colors
  - euclidean distance and K neighbors
  - exercise:
    - how can we compute distances for discrete variables?
    - one hot encoding explanation and picture
    - transform data
    - write function to compute distances between any two points and make a distribution of distances as a whole and for each feature
    - how do the distances in one dimension affect the distance overall?
    - need to normalize
4. Instantialize KNN (55)
  - transform X data and train
  - evaluate on y data, confusion matrix
  - can do the same for regression, by taking average of K neigbors, repeat and compute MSE