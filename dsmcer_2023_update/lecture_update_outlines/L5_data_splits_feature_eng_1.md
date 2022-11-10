# L5 (1.5p) Data splits and feature engineering 1

1. Is the random split we used testing what we want? (50 m)
  - we have seen that testing and training are statistically similar across features, suggesting that the test set is a good test of what the model learned from training
  - but is this test set testing what we want from the question
  - plot for a bunch of pairs the molar ratios, whether solid or not, and colored by training or testing
  - the model is basically just an interpolator, and the testing set is testing how good an interpolator it is
  - question
    - if our goal is to make predictions on never before seen compounds, how would we split it?
2. split by what you are trying to test (60 m)
  - split by HBD
  - but see that the distribution is different by t test
  - exercise
    - train new model with this split and test
    - it sucks
  - this tells us that our choice of features is not sufficient for this test
  - image of a few of the compounds, description of new features
  - use dict to compute a few of features
  - run test and see that they better overlap
  - normalize, train, test model and see improvement