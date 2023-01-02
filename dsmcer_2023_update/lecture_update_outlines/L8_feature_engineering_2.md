# L8 Feature Engineering 2 (1 period)

1. Feature selection by filtering (15 min)
  - univariate correlation
    - this will reflect vary well on a linear model
  - information gain
  - etc. see scikit learn
2. Forward selection (40 min)
  - start with the single best feature and build
  - for a linear model you might as well just use a univariate filter method from above, but for nonlinear it is hard to predict the relationships that can be created
    - consider x + 0.2y = z (sample some data) and a linear model
    - the contribution of x or y can easily be correlated with the target, the above methods are quantitative to the effect on the model
      - measure increase in accuracy from adding the second feature
    - now consider x + (.2y)^2 = z and a nonlinear model (sample data space such that the correlation is about the same)
      - measure increase in accuracy from adding the second feature
    - the methods above are no longer quantitative - the improvement of model is not proportional to correlation
  - we can instead increase out model empirically
  - write function that takes in a list of set features, then tests adding one feature to each and testing the improvement, give back best improvement, time the test
  - start with one feature, train a kernel model for each feature and see which feature is best
  - exercise:
    - repeat until you add all features, measure the cumulative cost (time) to run all tests
    - plot cost as number of features goes up as well as accuracy
  - as we increase the number of features the cumualtive cost goes up, this translates to carbon
3. PCA (25 min)
  - We can also attempt to transform the data using clever algortithms to get features
  - picture of 2d PCA
  - run it, show variance captures
  - train model on 2
  - exercise
    - for 1, 2, 3, 4 PCAs, train and measure cost and accuracy
  