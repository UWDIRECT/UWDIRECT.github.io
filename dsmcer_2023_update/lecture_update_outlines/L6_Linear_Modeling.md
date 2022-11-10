# L6 Linear Modeling (3 p)

1. Single linear regression
  - Linear model equation
  - Formal introduction to parameters - return to model image
  - Analytical optimal parameters for linear modeling
  - load HCEPDB dataset, use JSC vs e gap alpha (close to linear so that we can view it but it will have bias)
  - exercise
    - lets say that our goal is to predict X of new materials containing the same elements as the one in this dataset, how should we split?
    - random should be sufficient, one could consider substructure splitting
  - train and test
2. Classification from continuous output
  - The method being regression and classification for KNNs was clear
  - many models do not have such a natural disposition to discretization
  - for a continous target, we can threshold
  - even better, we can apply the sigmoid to produce a normalized liklihood
  - repeat make a linear classifier and repeat for above
3. How can we measure the quality of the model on the test set?
  - we have seen Accuracy for classification and MAE for regression
  - there are others - choosing one is important becuase it guides our choice of meodel and hyperparameters
  - loss zoo
    - Regression: MAE, MSE
    - Class: Accuracy, balanced accuracy, Confusion Matrix - precision and recall, auROC
4. Variance
  - We saw earlier that the different data splits produced models with different accuracy, which hints at an important topic: models are dependant on the data with which they are trained
  - we do not want a model to be fickle and be do variable or have "high variance" such that different sets of data produce wildly different models
  - exercise
    - randomly sample from 50 % training set 8 times and train models
    - plot each linear model
    - see that the resulting model is relatively similar
  - plot distribution of parameters and test set error over the fits
  - statement: __Variance is the variability of the model parameters over all possible sets of measurements__
  - note that we can never achieve all possible sets of measurements, so we can only estimate variance
  - question: isn't this estimation dependant on the size of the samples?
      - repeat the above and plot std if params and full training set error vs data sample size, we should see it rapidly decrease and then slowly from there to 0
      - what is the data sample size where it beigns to slow down? 
      - if the variability of error gets low very quickly, we can estimate that the model has lower variance, but if it takes close to the order of the training set size, then it has higher variance
5. Bias
  - What if we had access to all possbile measurements, would our model be good enough?
  - It may not be, it is possible that the model is incapable of caputuring the true relationship
  - exercise
    - plot training error as a function of training sample size
    - is the model error plateauing to zero? If it plateauing to something larger than zero, then it has bias
  - statement: __Bias is the difference between the model parameters and the true best parameters__
6. Bias varaince tradoff
  - trade off image
  - We cannot directly measure either, to do so would require the true relationship defeating the purpose of ML
  - But we can estimate it
    - variance: how much does the model differ if we take subsets of data?
    - bias: does the model we chose have the capability of perfectly fitting the training data as we increase the amount of data?
    
7. Multiple linear regression
  - Assumptions
  
  