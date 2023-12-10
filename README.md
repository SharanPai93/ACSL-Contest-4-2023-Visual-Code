# ACSL Contest 4, 2023 --> Visual representation of code  
This is a visual representation of the ACSL Contest 4 programming problem in 2023.  
This program is meant to be executed, not imported. There are few functions in this code of use for other files.  
The problem is as follows (NOTE: I do not have the exact problem, so this is one very similar to it):  
### Given
1. A graph consisting of a constant number of rows and columns
2. The number of "Targets" in the graph
3. The coordinates of the targets in each graph (Notated by ab, where a is the row number, and b is the column number)
### What we need to find
We are given a code of letters, from "A" to "F", where each letter represents a different orientation of an arrow (ie. up, down, right, left, diagonal up right, diagonal up left, diagonal down right, diagonal down left).  
We need to find the best orientation of the arrow that passes throw the most targets in their coordinated positions.
#### Constraints
The arrows will only be placed in the outermost ring of rectangles on the graph, and if a tie occurs betweeen arrows, choose the minimum answer. This is further explained in the code via comments.  
Answers will be formatted in the form abX, where a is the row number, b is the column number, and X is the type of the arrow.  
