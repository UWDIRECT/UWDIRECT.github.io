# L3 Comparing distributions (1p)
Hypothesis testing content can come from last year's 


1. How do we determine if two distributions are similar?
  - three analytical gaussians, two very similar and one very different
  - introduce KLD, compute pairwise
  - sample each and repeat for empirical
2. A more quantitative method - statistical tests
  - partition HCEPDB up into one dissimilar in one feature and two similar
  - t test and hypothesis test on them
  - place into context - will a model given A be able to be informed on B? if not, the model will be biased
  - exercise:
    - provide a few splits of HCEPDB features
    - for each, run tests on features
    - determine if any will be a biased split
