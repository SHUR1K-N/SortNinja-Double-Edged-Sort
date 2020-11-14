# SortNinja: A Double-Edged Sorting Algorithm

## Description & Usage
A conceptually unique sorting algorithm, that sorts *two* integers per iteration (either in ascending or descending order, as per the user's selection) instead of the rather conventional/traditional *one*-integer-per-iteration approach, using the Python-native min() and max() functions.

Upon completion, the initial input list is destroyed and only the final sorted list prevails, which is either displayed on-screen or dumped into a new file (as per the user's selection).

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/SortNinja-Double-Edged-Sort/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, and can be tested using my own [**NumNinja**](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator) and/or [**RandomNinja**](https://github.com/SHUR1K-N/RNumNinja-Random-Number-File-Generator) tools which can help create massive numbered list files within user specified constraints, respectively either in ascending order or randomized order.

### Note
In no way is this algorithm to be considered an effort to be among the explicitly *faster* of sorting algorithms. This is merely a unique/unorthodox algorithm in its manner of sorting cycles. Since the min() and max() functions that lie within a single SortNinja iteration *themselves* involve a single cycle each of scanning the entire list, this already means one iteration of SortNinja's sorting is *two* entire scans of the unsorted list using min() and max(). This gives SortNinja a time complexity of `O(2n)`, which would be the same as sorting one item at a time anyway; SortNinja just sorts both extremities alternatively (hence "Double-Edged").


## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
