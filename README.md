# Double-Edged Sort: A Double Sort/Iteration Algorithm

A pretty fast sorting algorithm I created, that takes the following as input:

- Custom list of integers to be sorted (either via manual integer entry or via a supplied custom dictionary/list file)

...and then generates a sorted list with all the integers in either ascending or descending order, depending on the user's selection. Also supports duplicate entries flawlessly. Upon completion, the initial input list is destroyed and only the final sorted list prevails (super clean implementation). The algorithm is considered fast due to both the min() and max() functions residing in a single iteration itself, filling the sorted list *two* integers per iteration instead of the rather conventional/traditional *one*-integer-per-iteration approach. This project was created in Python, and can be tested using my own [NumNinja](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator) and/or [R.NumNinja](https://github.com/SHUR1K-N/RNumNinja-Random-Number-File-Generator) tools which can help create massive numbered list files within user specified constraints, respectively either in ascending order or randomized order.

**Dependencies you may have to "pip install" before being able to run the Python file(s):**

**colorama** (for colors)

**termcolor** (for colors)

My website: http://bit.do/SHUR1KN
