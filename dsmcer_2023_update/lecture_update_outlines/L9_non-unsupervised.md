# L9 Non supervised learning (1 period)

1. What if we don't have labels, eg. we don't have a y? (10 min)
  - examples discussed here:
    - reduce dimensions
    - catagorize data that do not inherantly have catagories
    - suggest new samples to take
  - we cannot measure "error"
  - we instead have to measure quantities inherant to the data and the model, eg. distances in dimensional space
  
2. Dimensionality reduction (10 min)
  - you already saw this, so will not repeat
  - some other algorithms on sklearn
  - autoencoders at a glance
  
3. Clustering (SV has this done basically) (30 min)
  - intro to k-means
  - run on Hawley data with correct number of classes
  - plot overlap of concieved clusters and tru classes
  - we had to choose K, what if we didn't know?
  - SV plot metric as a function of k
  
4. Active learning (30 min)
  - what if we want a continuously improving model
  - taking data is expensive, which data sould we take?
  - we can either take the next data point that maximized the reward, or we can choose one that maximized __learning__
    - how do we measure increase in learning?
  - the analytical side of this topic is too deep for right now, feel free to look up bandits or otherwise look into active learning
  - something that empirically works well is GPs, which inhherantly return a variance on predictions
  - choose example with the most variance
  - test of marias dataset
  - exercise
    - train model to explor HBDs, choose between two new HBDs