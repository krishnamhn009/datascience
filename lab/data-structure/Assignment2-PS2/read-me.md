Assignment 2 – PS2 - [Budget Allocation]
1. Problem Statement
The Indian space agency ISRO must deal with budgeting decisions to choose how to
optimally divide the budget among its N competing missions. Each mission head has
submitted the cost to be incurred and its overall value (or profit) for consideration. The budget
available with the agency is 100 crores. They need your help in selecting as many projects
as possible with the budget constraints such that the total value returned is maximized.
For this problem we can assume that there is no dependency of launching one project on the
other. If there are multiple solutions with same value, choose the one which results in
maximum utilization of budget and selection of missions as well.
Requirements:
1. Formulate an efficient recursive algorithm using dynamic programming to determine
how to select the missions to be funded and maximize value.
2. Analyse the time complexity of your algorithm.
3. Implement the above problem statement using Python 3.7.
Sample Input:
For example, if there are 10 different missions in total and their budget requirements and
values are given as shown:
Mission (i) Budget bi(crores) Value vi
1 10 20
2 15 70
3 25 55
4 10 30
5 13 46
6 30 60
7 18 45
8 25 50
9 17 35
10 10 10
Input should be taken in through a file called “inputPS2.txt” which has the fixed format
mentioned below using the “/” as a field separator:
<Mission name i> / < Budget bi(crores)> / < Value vi>
Ex:
1 / 10 / 20
2 / 15 / 70
3 / 25 / 55
…
Note that the input data shown here is only for understanding and testing, the actual file used
for evaluation will be different.
Sample Output:
The missions that should be funded: 1,2,3,4,5,8
Total value: 271
Budget remaining: 2
Note that the output data shown here is only for understanding and testing, the actual file
used for evaluation will be different. The output need not match the sample input provided
earlier.
The output should be written to the file outputPS2.txt
2. Deliverables
• Word document designPS2_<group id>.docx detailing your algorithm design and time
complexity of the algorithm.
• [Group id]_Contribution.xlsx mentioning the contribution of each student in terms of
percentage of work done. Download the Contribution.xlsx template from the link shared in
the Assignment Announcement.
• Zipped AS2_PS2_BudgetAlloc_[Group id].py package folder containing all the
modules classes and functions and the main body of the program.
• inputPS2.txt file used for testing
• outputPS2.txt file generated while testing
3. Instructions
a. It is compulsory to make use of the data structure(s) / algorithms mentioned in the problem
statement.
b. Use only native data types like lists and tuples in Python. Use of libraries like graph, numpy,
pandas library etc. is not allowed. The purpose of the assignment is for you to learn how these
data structures are constructed and how they work internally.
c. It is compulsory to use Python 3.7 for implementation.
d. Ensure that all data structure insert and delete operations throw appropriate messages when
their capacity is empty or full.
e. For the purposes of testing, you may implement some functions to print the data structures or
other test data. But all such functions must be commented before submission.
f. Make sure that your read, understand, and follow all the instructions.
g. Ensure that the input, prompt and output file guidelines are adhered to. Deviations from the
mentioned formats will not be entertained. If your program fails to read the input file used for
evaluation, your program will not be evaluated.
h. The input, prompt and output samples shown here are only a representation of the syntax to
be used. Actual files used to test the submissions will be different. Hence, do not hard code
any values into the code.
i. Run time analysis is provided in asymptotic notations and not timestamp based runtimes in
sec or milliseconds.
4. Deadline
a. The strict deadline for submission of the assignment is 6
th Sep, 2020.
b. The deadline has been set considering extra days from the regular in order to accommodate
any challenges you might face. No further extensions will be entertained as comprehensive
exams will commence in the subsequent weeks.
c. Late submissions will not be evaluated.
5. How to submit
a. This is a group assignment.
b. Each group has to make one submission (only one, no resubmission) of solutions.
c. Each group should zip all the deliverables in one zip file and name the zipped file as below
“ASSIGNMENT2_[G1/G2/…].zip”
and upload in CANVAS in respective location under ASSIGNMENT Tab.
d. Assignment submitted via means other than through CANVAS will not be graded.
6. Evaluation
a. The assignment carries 13 Marks.
b. Grading will depend on
a. Fully executable code with all functionality
b. Well-structured and commented code
c. Accuracy of the run time analysis and design document.
c. Every bug in the functionality will have negative marking.
d. Use of only native data types and avoiding libraries like numpy, graph and pandas will get
additional marks.
e. Source code files which contain compilation errors will get at most 25% of the value of that
question.
7. Readings
Text book: Algorithms Design: Foundations, Analysis and Internet Examples Michael T.
Goodrich, Roberto Tamassia, 2006, Wiley (Students Edition). Chapters: 5.3


1.clone this repo
2.open command line terminal
3.make sure input fiels are in same folder
3.run python3 ps2.py
