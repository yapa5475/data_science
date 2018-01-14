from math import sqrt

from scipy.stats import t
from numpy import mean

def degrees_of_freedom(s1, s2, n1, n2):
    """
    Compute the number of degrees of freedom using the Satterhwaite Formula

    @param s1 The unbiased sample variance of the first sample
    @param s2 The unbiased sample variance of the second sample
    @param n1 Thu number of observations in the first sample
    @param n2 The number of observations in the second sample
    """
    numerator = (s1**2/n1 + s2**2/n2)**2
    denominator = ((s1**2/n1)**2)/(n1-1) + ((s2**2/n2)**2)/(n2-1)

    degrees_of_freedom = numerator/denominator

    return degrees_of_freedom

def unbiased_sample_variance(observations, mean):
    """
    Compute the unbiased sample variance
    http://mathworld.wolfram.com/SampleVariance.html

    @param observations Iterable set of observations
    @param mean The estimated mean
    """
    inner_sum = 0
    for x in observations:
        inner_sum += (x-mean)**2

    coefficient = 1/(len(observations)-1)
    unbiased_sample_variance = coefficient * inner_sum
    
    return unbiased_sample_variance

def t_statistic(mean1, mean2, n1, n2, svar1, svar2):
    """
    Compute the t-statistic for the given estimates
    http://beheco.oxfordjournals.org/content/17/4/688.full
    """
    #Complete this function
    numerator = mean1-mean2
    denominator = sqrt(svar1/n1+svar2/n2)

    t_statistic = numerator/denominator
    #test statistic, 110, 111, 114, 116, 118,124, 211
    return t_statistic

def t_test(sample1, sample2):
    """
    Return the p-value of a t test with unequal variance for two samples.

    @param sample1 An iterable of the first sample
    @param sample2 An iterable of the second sample
    ***http://formulas.tutorvista.com/math/t-test-formula.html***
    """

    #standard deviation
    #num_items1 = len(sample1)
    mean1 = sum(sample1)/len(sample1)
    differences1 = [x - mean1 for x in sample1]
    sq_differences1 = [d ** 2 for d in differences1]
    sd1 = sum(sq_differences)

    mean2 = sum(sample2)/len(sample2)
    differences2 = [y - mean2 for y in sample2]
    sq_differences2 = [e ** 2 for e in differences2]
    sd2 = sum(sq_differences2)

    n1 = len(sample1)
    n2 = len(sample2)

    numerator = mean1 - mean2
    denominator = sqrt((sd1)**2/n1 + (sd2)**2/n2)

    t = numerator/denominator

    p = t**2
    
    return p

if __name__ == "__main__":
    v1 = [5, 7, 5, 3, 5, 3, 3, 9]
    v2 = [8, 1, 4, 6, 6, 4, 1, 2]

    print("p-value is %f" % t_test(v1, v2))
    