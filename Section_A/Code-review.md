<h1>Python Code Review</h1>


#### Reviewer: Gary-Ross Meade Tettey
#### Contact: [Twitter](https://twitter.com/Garyrmeade1 )

<h3 align="left">Starting Mark: 100</h3>

## Correctness: -36 marks [ 64/100 ]
<br />

You have grasped the general understanding and use of the avaiable python syntax and data strcutures. The logic you in corporated in your solution is correct, there are a few **minor issues** that can be addressed to help you progress.


*Code does not initially run due to the following errors: **-25 marks**<br /> 
    1. Indentation errors: Line 3; 4 & 10 **-6 marks**
    2. The sprted() method on Line 5 is missing an argument for it sort. **[i]** **-3 marks**

Once these are sorted out in an IDE, the code will run.

The ouput of the code shows your general undersatnding of the logic required to solve problems using code.

*Finally, the output is not list should have been ordered by the amount of anagrams per list, beginning with the least. Therefore, the **ob1** variable requires one final sorting to arrange them accordingly to the given output in the question. **-2 marks**


## Efficiency: 
<br />
Your solution shows a great grasp syntax; data structure's; and methods in python, through your use of dictionaries and sorting methods. 

While your slotuion is correct, there are ways to get the same result with fewer, cleaner lines of code, by importing certain tools. An example of this could be seen:

```python
from itertools import groupby
 
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
 
# print given list
print("Input list : " + str(input_list))
 

# Grouping the Anagrams
sorted_list = lambda input_list: sorted(input_list)
# using Sorted() + lambda functions + Groupby() method
result = [list(val) for key, val in groupby(sorted(input_list, key = sorted_list), sorted_list)]
 
print("Grouped Anagrams : " + str(result))
```
Check out the groupby() method & Lamba functions for more information.:

* [groupby()](https://www.pythonpool.com/pythons-itertools-groupby/)
* [Lamba](https://www.codecademy.com/article/lambda-functions)
<br /><br /> 

## Style: -2 marks [ 62/100 ]

The general style of your code is corect, there is work that can be done on the structure of your code blocks to increase the readability for other developers. 

**Remember**:

* be consistent with the indentation of your code blocks, either choosing spaces or tabs, not both. **-1 mark**
* to use line spacing to your advantage, certain spacing conventions can be used to imporve the style of your code. **-1 mark**
* use an IDE like VS Code or Pycharm to help you with your code style.
* to use variable names that are easily identifiable, that can be clearly described what you're storing in tha variable. For future use, and for others.

Please refer to a Python style guide if you get stuck:

* [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [VS Code](https://code.visualstudio.com/)
* [Pycharm](https://www.jetbrains.com/pycharm/)


<br />

## Documentation: -5 marks [ 57/100 ]

This script does not have any doc-strings or comments to assist people reading the code, in understanding the logical steps taken to solve the problem. Both of these could also come back to help you, as you may forget how and why you used particular pieces of code.

If you are unsure on how doc-strings and comments work, please refer to the following links:

* [Doc-Strings](https://www.python.org/dev/peps/pep-0257/)
* [Comments](https://www.python.org/dev/peps/pep-0020/)




<br /><br />

## To conclude:

In general, **Congratulations** on solving this problem. Each new problem solved is a step closer to your mastery of the Python language. 

The majority of the issues i have raised in this review can be classified as Superficial issues, in my opinion, as they do not occur as any serious logical, syntactic or application errors. The main issues can be summarised as follows:
    1.Indentation errors: Line 3; 4 & 10
    2.The sorted() method on Line 5 is missing an argument for it sort. **[i]** 
    3.Understanding the tools in the python language that are available to help you with your code.
    4.Naming your variables. Variables like **ob1** ; **i**

The reason i can call these Superficial is that they do not look serious now in the solving of this problem, but their importance and impact will be felt more in large scale code bases and if your are working with other developers who need to understand your code.

<br />

## Next Steps: <br/>
*Downloading & setting up an IDE like VS Code or Pycharm on main development workspace.
*Reviewing the code of more experienced developers that have solved problems that you are interested ion solving and take note of how they use the tools in the language.
*Use Youtube to discover new probelms and tutorials to improve your knowledge of programming principle in general.

<h2 align="left">Final Mark: 57/100</h2>


Thanks and Goodluck for the next one!
