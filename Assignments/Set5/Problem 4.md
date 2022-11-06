# Set 5
## Problem 4 - Sorting
### Description
There is a conference room that can be booked by submitting the start time and end time of each conference. Each conference can end right after starting them (start time can be the same value as end time). Only one conference can occupy the conference room at once.
### Requirement
Create a function that returns the maximum number of meeting that can happen considering the submission data. Your function sould be named as <b>roomAssignment</b>. Your function will accept the booking information as nested list. Each time data is 0 or positive integer. You are not required to use recursive function for this task.

### Sample Case 1
<b>Sample parameter:</b><br>
<i>
[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10],[8, 11], [8, 12], [2, 13], [12, 14]]</i>
<br>
<b>Sample return:</b><br>
<i>
4<br>
</i>
<b>hint</b><br>
<i>[1, 4], [5, 7], [8, 11], [12, 14]</i> these are the usable slots

### Sample Case 2
<b>Sample parameter:</b><br>
<i>
[[326, 681], [621, 915], [992, 1747], [48, 1278], [912, 1048], [489, 1117], [338, 1218], [812, 825], [969, 1713], [481, 916]]
</i>
<br>
<b>Sample return:</b><br>
<i>
3<br>
</i>
<b>hint</b><br>
<i>[326, 681], [812, 825], [912, 1048]</i> these are the usable slots

### Sample Case 3
<b>Sample parameter:</b><br>
<i>
[[19, 40], [10, 39], [10, 63], [24, 45], [12, 33], [19, 53], [22, 52], [18, 39], [16, 63], [1, 30]]
</i>
<br>
<b>Sample return:</b><br>
<i>
1<br>
</i>
<b>hint</b><br>
<i>any of the list</i> is the usable slots
