from collections import defaultdict
from csv import DictReader, DictWriter
import heapq

kHEADER = ["STATE", "DISTRICT", "MARGIN"]

def district_margins(state_lines):
    """
    Return a dictionary with districts as keys, and the difference in
    percentage between the winner and the second-place as values.

    @lines The csv rows that correspond to the districts of a single state
    """
    
    #First figure out what districts exist for this state
    stateDistricts = set()
    for line in state_lines:
        stateDistricts.add(line["D"])
    if('H' in stateDistricts):
        stateDistricts.remove('H')
    if('' in stateDistricts):
        stateDistricts.remove('')
    print(stateDistricts)
    print("\n")

    
    #Next figure out 1st, 2nd place for each district
    margins = {}
    for Num in stateDistricts:
        sortingArray = []
        for line in state_lines:
            if(line["D"] == Num and line["GENERAL %"] != ""):
                percentageStr = line["GENERAL %"]
                percentageStr = percentageStr.replace("%","")
                percentageStr = percentageStr.replace(",",".")
                percentageFloat = float(percentageStr)
                sortingArray.append(percentageFloat)
        if(len(sortingArray) <= 1):
            margins[Num] = 100
        elif("TERM" in Num):
            Num = Num[:1]
            sortingArray.sort
            difference = sortingArray[0] - sortingArray[1]
            margins[int(Num)] = difference
        else:
            sortingArray.sort
            difference = sortingArray[0] - sortingArray[1]
            margins[int(Num)] = difference
        
    return margins
        
                
    # Complete this function
    #return dict((int(x["D"]), 25.0) for x in state_lines if x["D"] and x["D"] != "H")

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """
    stateSet = set()
    for row in lines:
        stateSet.add(row["STATE"])
    
    return set(stateSet)

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.

    @state Only return lines from this state
    @lines Only return lines from this larger list
    """
    stateDistricts = []
    # Complete/correct this function
    for row in lines:
        if(row["STATE"] == state):
            stateDistricts.append(row)
    return stateDistricts

if __name__ == "__main__":
    # You shouldn't need to modify this part of the code
    lines = list(DictReader(open("../data/2014_election_results.csv")))
    output = DictWriter(open("district_margins.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()
    
    
    
    summary = {}
    for state in all_states(lines):
        margins = district_margins(all_state_rows(lines, state))

        for ii in margins:
            summary[(state, ii)] = margins[ii]

    for ii, mm in sorted(summary.items(), key=lambda x: x[1]):
        output.writerow({"STATE": ii[0], "DISTRICT": ii[1], "MARGIN": mm})
    
