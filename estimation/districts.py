# Districts.py
#done
# 

from csv import DictReader
from collections import defaultdict
from math import log
from math import pi as kPI
from math import pi

kOBAMA = set(["D.C.", "Hawaii", "Vermont", "New York", "Rhode Island",
              "Maryland", "California", "Massachusetts", "Delaware", "New Jersey",
              "Connecticut", "Illinois", "Maine", "Washington", "Oregon",
              "New Mexico", "Michigan", "Minnesota", "Nevada", "Wisconsin",
              "Iowa", "New Hampshire", "Pennsylvania", "Virginia",
              "Ohio", "Florida"])
kROMNEY = set(["North Carolina", "Georgia", "Arizona", "Missouri", "Indiana",
               "South Carolina", "Alaska", "Mississippi", "Montana", "Texas",
               "Louisiana", "South Dakota", "North Dakota", "Tennessee",
               "Kansas", "Nebraska", "Kentucky", "Alabama", "Arkansas",
               "West Virginia", "Idaho", "Oklahoma", "Wyoming", "Utah"])

def valid(row):
    return sum(ord(y) for y in row['FEC ID#'][2:4])!=173 or int(row['1']) < 3583



def ml_mean(values):
    #DONE
    """
    Given a list of values assumed to come from a normal distribution,
    return the maximum likelihood estimate of ml_mean of that distribution.
    There are many libraries that do this, but do not use any functions
    outside core Python (sum and len are fine).

    maximum likelihood estimate: textbook pgs 99,105,107,128,152
    week6.txt

    μ = mean
    σ²= variance
    """

    #max_likelihood_mean = 0

    total_values = 0
    total = 0
    for value in values:
        total_values+=1
        total += value

    max_likelihood_mean = total/total_values

    #print(max_likelihood_mean)

   
    # Your code here
    
    return max_likelihood_mean

def ml_variance(values, mean):
    #DONE
    """
    Given a list of values assumed to come from a normal distribution and
    their maximum likelihood estimate of the mean, compute the maximum
    likelihood estimate of the distribution's variance of those values.
    There are many libraries that do something like this, but they
    likely don't do exactly what you want, so you should not use them
    directly.  (And to be clear, you're not allowed to use them.)
    """

    #variance = σ² ; variance = (standard devation)^2
    sum1 = 0
    noValues = 0

    for value in values:
        varianceSum = (value - mean)**2
        sum1 += varianceSum
        noValues += 1

    max_likelihood_variance = sum1/noValues


    # Your code here
    #print (variance)
    return max_likelihood_variance

def log_probability(value, mean, variance):
    #DONE
    """
    Given a normal distribution with a given mean and varience, compute the
    log probability of a value from that distribution.
    """

    # Your code here
    #standard deviation is sqrt of variance

    L1 = -log(variance**(1/2))
    L2 = -(1/2)*log(2*pi)
    L3 = (value - mean)**2

    log_probability = L1+L2+L3
    return log_probability


def republican_share(lines, states):
    """
    Return an iterator over the Republican share of the vote in all
    districts in the states provided.
    """
    # Your code here

    districts = {}
    for line in lines:
        for state in states:
            try:
                if state == line["STATE"]:
                    if line["PARTY"] == "R" and line["GENERAL %"] and not (line["D"] == "UNEXPIRED TERM"):
                        republican_share1 = line["GENERAL %"]
                        republican_share2 = float(republican_share1.replace("%","").replace(",","."))
                        republican_share3 = line["D"]
                        districts[(state, int(republican_share3))] = republican_share2
            except ValueError:
                continue
    return districts

if __name__ == "__main__":
    # Don't modify this code
    lines = [x for x in DictReader(open("../data/2014_election_results.csv"))
             if valid(x)]

    obama_mean = ml_mean(republican_share(lines, kOBAMA).values())
    romney_mean = ml_mean(republican_share(lines, kROMNEY).values())

    obama_var = ml_variance(republican_share(lines, kOBAMA).values(),
                             obama_mean)
    romney_var = ml_variance(republican_share(lines, kROMNEY).values(),
                              romney_mean)

    colorado = republican_share(lines, ["Colorado"])
    print("\t\tObama\t\tRomney\n" + "=" * 80)
    for co, dist in colorado:
        obama_prob = log_probability(colorado[(co, dist)], obama_mean, obama_var)
        romney_prob = log_probability(colorado[(co, dist)], romney_mean, romney_var)

        print("District %i\t%f\t%f" % (dist, obama_prob, romney_prob))
