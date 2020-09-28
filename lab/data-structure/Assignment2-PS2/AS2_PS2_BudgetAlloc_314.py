# hashing function

import math


# Project/Mission plain class
class Mission:
    def __init__(self, missionId, budget, value):
        self.missionId = missionId
        self.budget = float(budget)
        self.value = float(value)
        self.valueBudgetRatio = self.value/self.budget

    def print(self):
        print(
            self.missionId,
            self.budget,
            self.value
        )

    def getValueBudgetRatio(self):
        return self.valueBudgetRatio


# get working folder path
def getfolderPath():
    from inspect import currentframe, getframeinfo
    from pathlib import Path

    filename = getframeinfo(currentframe()).filename
    parent = Path(filename).resolve().parent
    return str(parent.joinpath())


'''
Function to read mission details
'''


def readMissionDetails():
    f = open(getfolderPath() + "\\inputPS2.txt", "r")
    missionList = []
    for x in f:
        fields = x.rstrip().split("/")
        mission = Mission(
            fields[0].strip(),
            fields[1].strip(),
            fields[2].strip()
        )
        missionList.append(mission)
    return missionList


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].valueBudgetRatio > R[j].valueBudgetRatio:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


class ISROBudgetHelper:

    def __init__(self, missionList, budget):
        self.missionList = missionList
        self.budget = budget
        self.result = ''

    def print(self):
        for target_list in self.missionList:
            target_list.print()

    '''
    function to perform analysis on project to select to fund having maximum value
    '''

    def findFundingProjects(self):
        print("funded projects")
        missionBudget = self.budget
        missionTotalValue = 0.0
        missionTotalBudget = 0.0
        fundedMission = []
        for mission in self.missionList:
            if (missionTotalBudget < self.budget):
                missionTotalBudget += mission.budget
                if (missionTotalBudget) < (self.budget):
                    missionTotalValue += mission.value
                    fundedMission.append(mission)
                else:
                    missionTotalBudget -= mission.budget

            else:
                break

        self.result += 'The missions that should be funded:  '
        for fm in fundedMission:
            self.result += fm.missionId + ","
        self.result += '\nTotal value: ' + str(missionTotalValue)
        self.result += '\nBudget remaining:' + \
            str((self.budget - missionTotalBudget))
        print(self.result)

    def writeOutputFile(self):
        f = open(getfolderPath() + "\\outputPS2.txt", "a")
        f.write(self.result)
        f.close()


# Driver Code
if __name__ == "__main__":
    missionList = readMissionDetails()
    isroBudgetHelper = ISROBudgetHelper(missionList, 100)
    # sort by value/budget ratio (Descending order)
    # isroBudgetHelper.missionList.sort(
    #     key=lambda x: x.getValueBudgetRatio(), reverse=True)
    mergeSort(isroBudgetHelper.missionList)
    isroBudgetHelper.findFundingProjects()
    isroBudgetHelper.writeOutputFile()    
