# L2 Distributions, stat basics, distro zoo (2 period)
Prereqs: SEDS python, DSMCER data vis

Previous year L3 and L4 content is pretty close, just a few modifications/cut downs.

1. What is a distribution (25 min)
  - description of the liklihood of an event: PDF
    - image of PDF
    - any point describes the liklihood of getting a particular value
  - basic statistics: mean, median, most likely point, standard deviation
    - image of these added to previous distro
  - compare two distribution images and discuss
  - cumulative liklihood CDF
  - how to represent a distro in python
    - create analytical distribution with scipy
    - get mean, std, median etc.
    - sample from distro as well as using numpy random
2. Distribution zoo (25 min)
  - picture, brief description. and python functions for
    - normal
    - uniform
      - exerices, what is the standard deviation, mode, median, and mean
    - binomial
    - poisson
    - gamma
    - binomial (use to introduce descrete RVs)
3. Empirical distribution (40 min)
  - You have some data sampled from some unknown distribution that represents and empirical distribution
  - view histogram
  - for the sake of argument let's _naively_ say that this empirical distribution is the same as the population distribution
  - compute basic stats
  - fit empirical distribution
    - assume form (maybe cut)
    - or KDE
    - or inverse CDF interpolate
  - exercise
    - how good was our naive assumption?
    - how good will this estimated distribution be as a function of size of the distribution
    - plot the sum absolute difference in probabilities on a grid for each sample size
    - motivate that the empirical distrbution gets better with size, but is NOT the true distribution
4. Samples vs population (70 min)
  - given that a sample does not equal the population, what can we determine about the population from the sample?
    - estimate population mean
    - randomly downsample normal distribution, compute standard error
    - margin of error
  - but what if out distribution is not normal? use a different one
    - randomly sample N, M times, plot mean of means and standard deviation of means
    - observe it is normal
    - we can estimate mean of population as such
  - central limit theorem, SV has some good images
  - question: if we can't assume the distribution is normal and compute standard error, and also we do not have many samples from the true distribution, what do we do?
  - exercise
    - write function to sample N M times from empirical data, compute mean of means and standard deviation of means
    - plot as a function of N and M
  - This is bootstrapping! and we can apply it to more than just the mean - we can estimate variability of any summary statistic of empirical data
    
  