# L6 Linear Modeling (3 p)

1. Single linear regression (20 min)
  - Linear model equation
  - Formal introduction to parameters - return to model image
  - Analytical optimal parameters for linear modeling
    - show image of data and a line with distances from line shown
  - load HCEPDB dataset, use JSC vs e gap alpha (close to linear so that we can view it but it will have bias)
  - exercise
    - lets say that our goal is to predict X of new materials containing the same elements as the one in this dataset, how should we split?
    - random should be sufficient, one could consider substructure splitting
  - train and test
2. Classification from continuous output (20 min)
  - The method being regression and classification for KNNs was clear
  - many models do not have such a natural disposition to discretization
  - for a continous target, we can threshold
  - even better, we can apply the sigmoid to produce a normalized liklihood
  - repeat make a linear classifier and repeat for above
 
3. How can we measure the quality of the model on the test set? (20 min)
  - we have seen Accuracy for classification and MAE for regression
  - there are others - choosing one is important becuase it guides our choice of meodel and hyperparameters
  - loss zoo
    - Regression: MAE, MSE
    - Class: Accuracy, balanced accuracy, Confusion Matrix - precision and recall, auROC
4. Variance (50 min)
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
5. Bias (40 min)
  - What if we had access to all possbile measurements, would our model be good enough?
  - It may not be, it is possible that the model is incapable of caputuring the true relationship
  - exercise
    - plot training error as a function of training sample size
    - is the model error plateauing to zero? If it plateauing to something larger than zero, then it has bias
  - statement: __Bias is the difference between the model parameters and the true best parameters__
6. Bias varaince tradoff (10 min)
  - trade off image, too simple, overfit, just right
  - trade off image of MSE
  - We cannot directly measure either, to do so would require the true relationship defeating the purpose of ML
  - But we can estimate it
    - variance: how much does the model differ if we take subsets of data?
    - bias: does the model we chose have the capability of perfectly fitting the training data as we increase the amount of data?
    
7. Multiple linear regression (30 min)
  - Assumption of each feature being linearly independant, give general forumula
  - each parameter is stil analytical
  - add 2 more features to the previous problem and fit, see if it is a better relationship
  - show that it has less bias, since it can capture some of the variability in y that was not captured by one feature

8. Regularization (50 min)
 - Before discussing vias and variance we have have assumed the training and testing set were both good approximations of the true distribution in features
 - Question: given what we know about variance, what is the consequence to our model of being wrong about that assumption?
 - There is a distinct danger that our model will be overfit to this sample of data compared to the true distribution. 
   - some of this is observable if the testing set is different enough from the training set, but the testing set could also be imperfect, so how can we avoid creating a model that is overfit comapred to the true distribution?
   - we cant be for sure, but there are some strategies to limit the effect of variance
 - Show 3d image of the true relationship of a 2d relationship (eg a disk), with one feature having a much higher impact than another
   - show the density of both features as two 2d plots, one will be much tigher than another
   - highlight a small sample, one side will be damn close to a line, the other will be wider and make it have a trend that is misleading
   - it might be better to be cautious and "assume" that no relationship should be too stron, eg. y is about the same for all x
 - we do this by adding a penalty on large slopes
   - show formula, turns out this is also analytical
   - now the optimization is a balance: __the right term will suppress large slopes, but if there is truly a strong relationship then the left term will bring it up because the error is so high__
 - introduce lasso and ridge regressor classes
 - for 5 random small samples of the data, plot the line for each feature over the KDE for regularized and non regularized
   - plot on the right will change a bunch for non regularized
  
  