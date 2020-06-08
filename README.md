
# T3020   Repo for ELEN3020

Name: Zhuofeng Wu
Date: 7 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

E1: The row list was ran from index 2-9 which mean it was ran from T2 - T8, rather than the desired T1 - T8.

E1 fix: The index range was changed from [2:9] to [1:9]


E2: The check also errors out if they are equal, while that was not intended.

E2 fix: The comparison operator changed from <= to <

E2++(bonus?): The loop runs for 9 times, but the loop should run from T1 - T7 with total to be 7 times. Excluding the TALL due to TALL includes T8 as part of the sum

E2++ fix: Change the loop's range from (7) to (1,8)

E2++2: In the print statement, the n value used was a global rather than it been pass through as a paremeter. It would be better to pass it as a paremeter to keep it consistent(as the check_row had it as a paremeter)

E2++2 fix: Add n as an additional paremeter


E3: The program counts the empty OTHER column when it was not suppose to.

E3 fix: Have the list leave out the last element in the for loop by changing curr_str to curr_str[:-1]

E3++: The data[] list was never used and do not know the intent of it

E3++fix: data[] removed

Note: Please run 'python3 -m unittest discover test' rather than 'python3 -m unittest discover'
