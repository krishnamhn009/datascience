# hashing function

import math
import datetime
from itertools import groupby

# convert string to date in given format
def stringToDate(dateString, pattern):
    return datetime.datetime.strptime(dateString, pattern).date()


# get working folder path
def getfolderPath():
    from inspect import currentframe, getframeinfo
    from pathlib import Path

    filename = getframeinfo(currentframe()).filename
    parent = Path(filename).resolve().parent
    return str(parent.joinpath())


# get max prome factor for given number
def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor


class ThemePark:
    def readPromptsFile():
        f = open(getfolderPath() + "\\promptsPS2.txt", "r")
        prompts = []
        for x in f:
            prompts.append(x.rstrip())
        return prompts

    def readInputFile():
        f = open(getfolderPath() + "\\inputPS2.txt", "r")
        visitorList = []
        for x in f:
            fields = x.rstrip().split(",")
            visitor = Visitor(
                fields[0].strip(),
                fields[1].strip(),
                fields[2].strip(),
                fields[3].strip(),
                fields[4].strip(),
            )
            visitorList.append(visitor)
        return visitorList


# visitor class
class Visitor:
    def __init__(self, fullName, dateOfVisit, dateOfBirth, homeCity, phoneNumber):
        self.fullName = fullName
        self.dateOfVisit = dateOfVisit
        self.dateOfBirth = dateOfBirth
        self.homeCity = homeCity
        self.phoneNumber = phoneNumber

    def print(self):
        print(
            self.fullName,
            self.dateOfVisit,
            self.dateOfBirth,
            self.homeCity,
            self.phoneNumber,
        )


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


class HashTable:
    def __init__(self, size, table, totalCount, loadFactor):
        self.size = size
        self.table = table
        self.totalCount = totalCount
        self.loadFactor = loadFactor

    def hashing(self, visitor_name):
        prime_num = 31
        m = self.loadFactor
        hash_value = 0
        len = 0
        for x in visitor_name:
            # print(ord(x),pow(prime_num,len),m)
            hash_value = (hash_value + (ord(x) + 31) * pow(prime_num, len)) % m
            # ∑i=0n−1s[i]⋅pimodm  =>  polynomial rolling hash function
            len += 1

        # print(visitor_name ,hash_value)
        return hash_value

    # insert visitor
    def insertVisitor(self, key, value):
        index = self.hashing(key)
        node = Node(value)
        if len(self.table[index]) == 0:
            hNodeList = SLinkedList()
            hNodeList.headval = node
            self.table[index].append(hNodeList)
        else:
            laste = self.table[index][0].headval
            while laste.nextval:
                laste = laste.nextval

            laste.nextval = node

        self.totalCount += 1
        print("...............insert................")
        print("Total visitor details entered:", self.totalCount)
        print(".....................................")

    # find visitor
    def findVisitor(self, name=None):
        index = self.hashing(name)
        print("---------- findVisitor: ----------")
        if len(self.table[index]) == 0:
            print("no visitors with name : ", name, "found visiting on 12-Jan-2020")
        else:
            nodes = self.table[index]
            visitorsList = []
            printval = nodes[0].headval
            now = datetime.date.today()
            dateToString = now.strftime("%d-%b-%Y")
            while printval is not None:
                if printval.dataval.fullName.find(name) >= 0:
                    visitorsList.append(printval.dataval)
                printval = printval.nextval

            print(
                len(visitorsList),
                " visitors with name",
                name,
                "found visiting on",
                datetime.date.today(),
            )
            for v in visitorsList:
                print(v.fullName, ",", v.homeCity, ",", v.phoneNumber)
#visitor count
    def visitorCount(self, visitDate=None):
        totalVisitors = 0
        if visitDate is None:
            print('Invalid visit date')
        else:
            for row in self.table:
                if len(row) != 0:
                    head = row[0].headval
                    while head is not None:
                        vDate = stringToDate(visitDate, "%d-%b-%Y")
                        if stringToDate(head.dataval.dateOfVisit, "%d-%b-%Y") == vDate:
                            totalVisitors += 1
                        head = head.nextval

        
        print("---------- visitorCount: ----------")
        print(totalVisitors, " visitors found visiting on", visitDate)
        print("-----------------------------")

    def cityVisitor(self):
        max = 0
        now = datetime.date.today()
        dateToString = now.strftime("%d-%b-%Y")
        visitorsList = []
        for row in self.table:
            if len(row) != 0:
                printval = row[0].headval
                while printval is not None:
                    if printval.dataval.dateOfVisit == dateToString:
                        visitorsList.append(printval.dataval)
                    printval = printval.nextval

        if len(visitorsList) != 0:
            keyFunc = lambda f: f.homeCity
            groupedData = groupby(visitorsList, keyFunc)
            op = ()
            for k, v in groupedData:
                length = len(list(v))
                if max < length:
                    max = length
            op = (k, max)

        print("---------- trendCity: ----------")
        if len(visitorsList):
            print(op[1], "visitors from", op[0], "visiting today")
        else:
            print("No visitors visiting today")

        print("-----------------------------")

    # not completed yet
    def birthdayVisitor(self, birthDateFrom, birthDateTo):
        visitorsList = []
        for row in self.table:
            if len(row) != 0:
                printval = row[0].headval
                while printval is not None:
                    dateOfBirth = stringToDate(printval.dataval.dateOfBirth, "%d-%b-%Y")
                    bDateFrom = stringToDate(
                        birthDateFrom + "-" + str(dateOfBirth.year), "%d-%b-%Y"
                    )
                    bDateTo = stringToDate(
                        birthDateTo + "-" + str(dateOfBirth.year), "%d-%b-%Y"
                    )
                    # setting year similer to birth year ..to compare simplly
                    if bDateFrom <= dateOfBirth <= bDateTo:
                        visitorsList.append(printval.dataval)
                    printval = printval.nextval

        print("---------- birthdayVisitor: ----------")
        print(
            len(visitorsList),
            " visitors have upcoming birthdays between",
            birthDateFrom,
            "and ",
            birthDateTo,
        )
        for v in visitorsList:
            print(v.fullName, ",", v.dateOfBirth, ",", v.phoneNumber)


# Driver Code
if __name__ == "__main__":
    themePark = ThemePark
    visitors = themePark.readInputFile()
    table = [[] for _ in range(len(visitors))]
    factor = Largest_Prime_Factor(len(visitors))
    ht = HashTable(len(visitors), table, 0, factor)
    # pushing visitors data into Hashtable

    for visitor in visitors:
        firstName = visitor.fullName.split(" ")[0]  # first name is key
        ht.insertVisitor(firstName, visitor)

    prompts = themePark.readPromptsFile()
    for prompt in prompts:
        if prompt.find("findVisitor") >= 0:
            fields = prompt.split(":")
            ht.findVisitor(fields[1].strip())
        elif prompt.find("visitorCount") >= 0:
            fields = prompt.split(":")
            ht.visitorCount(fields[1].strip())
        elif prompt.find("trendCity") >= 0:
            ht.cityVisitor()
        elif prompt.find("birthdayVisitor") >= 0:
            fields = prompt.split(":")
            ht.birthdayVisitor(fields[1].strip(), fields[2].strip())

