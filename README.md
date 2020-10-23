1. Problem Statement
Amazon Warehouse in Bangalore was expecting a freight shipment at 10 am on a Monday. However, the company responsible for the shipment mistook the destination as Amazon Development Centre, Bangalore. In order to save the extra cost of transportation back to the warehouse, the warehouse manager wants to help them find the fastest route from the DC to warehouse. He has the location map available which is given below (the weightage given is the distance in km between each location). However, as he did not take DSAD course, he turns to you for help.

 Your job is to help the manager with the following queries.
1. Which is the shortest route to reach Warehouse from the DC? The warehouse and DC nodes should be taken as an input and is not fixed to the nodes mentioned in the graph above.
2. How long would it take for the shipment to reach from the DC to the warehouse if the truck travels at an average speed of 40 km/hr.
Requirements:
1. Formulate an efficient algorithm to perform the above task.
2. Provide a description about the design strategy used
3. Analyse the time complexity of the algorithm and show that it is an “efficient” one.
4. Implement the above problem statement using Python 3.7
 
Sample Input:
Input should be taken in through a file called “inputPS3.txt” which has the fixed format mentioned below using the “/” as a field separator:
<location 1> / <location 2> / <distance in km>
Ex:
a / b/ 3 a / c/ 5 a / d/ 2 ...
DC Node: a WH Node: j
Note that the input data shown here is only for understanding and testing, the actual file used for evaluation will be different.
Sample Output:
Shortest route from DC 'a' to reach Warehouse 'j' is [ a d g k j ] and it has minimum travel distance 18km
it will take him 27 minutes to travel from DC to Warehouse.
Display the output in outputPS3.txt. 2. Deliverables
• Word document designPS3_<group id>.docx detailing your algorithm design and time complexity of the algorithm.
• Zipped AS2_PS3_SP_[Group id].py package folder containing all the modules classes and functions and the main body of the program.
• inputPS3.txt file used for testing
• outputPS3.txt file generated while testing
3. Instructions
a. It is compulsory to make use of the data structures or algorithm mentioned in the problem statement.
b. It is compulsory to use Python 3.7 for implementation.

c. Ensure that all data structures and functions throw appropriate messages when their capacity is empty or full.
d. For the purposes of testing, you may implement some functions to print the data structures or other test data. But all such functions must be commented before submission.
e. Make sure that your read, understand, and follow all the instructions
f. Ensure that the input, prompt and output file guidelines are adhered to. Deviations from the mentioned formats will not be entertained.
g. The input, prompt and output samples shown here are only a representation of the syntax to be used. Actual files used to test the submissions will be different. Hence, do not hard code any values into the code.
h. Run time analysis is provided in asymptotic notations and not timestamp based runtimes in sec or milliseconds.
4. Deadline
a. The strict deadline for submission of the assignment is 16th Feb, 2020.
b. The deadline is set for a month from the date of rollout to accommodate for the semester exams. No further extension of the deadline will be entertained.
c. Late submissions will not be evaluated.
5. How to submit
a. This is a group assignment.
b. Each group has to make one submission (only one, no resubmission) of solutions.
c. Each group should zip the deliverables and name the zipped file as below
“ASSIGNMENT2_[BLR/HYD/DLH/PUN/CHE]_[G1/G2/...].zip”
and upload in CANVAS in respective location under ASSIGNMENT Tab.
d. Assignment submitted via means other than through CANVAS will not be graded.
6. Evaluation
a. The assignment carries 13 Marks.
b. Grading will depend on
a. Fully executable code with all functionality
b. Well-structured and commented code
c. Accuracy of the run time analysis and design document.
c. Every bug in the functionality will have negative marking.

d. Source code files which contain compilation errors will get at most 25% of the value of that question.
