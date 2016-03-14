## Task 1

When working with sequence data, you often need to iterate over two files at the same time (think of iterating over Read 1 and Read 2 fastq files simultaneously). Using the `argparse`, `itertools`, `glob`, and `os` package, write a program that iterates over the lines of the two files in the task-1 directory, simultaneously.  Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.  You should run a linter against your code to make sure you have formatted it according to PEP8.

- [ ] Program is correctly formatted (2.0 pt)
- [ ] Program `argparse`, `itertools`, `glob`, and `os` (1.0 pt)
- [ ] Program functions as requested (2.0 pt)

## Task 2

When you're working with field data, you often need to manipulate dates. Using the `datetime` module, write a program that determines, from now until the end of 2016, how many weekend days there are.  You don't need to take any input from the user, and you can output the answer to the screen (it would be helpful if you could format this reasonably to explain what is being output). Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.  You should run a linter against your code to make sure you have formatted it according to PEP8.

- [ ] Program is correctly formatted (2.0 pt)
- [ ] Program uses `datetime` (1.0 pt)
- [ ] Program functions as requested (2.0 pt)

## Task 3

Generalize the program you wrote above to take an arbitrary start and stop date and compute the number of weekend days between those two times (inclusive).  Use `argparse` to take the start and end times on the command line, and make sure that you make it clear for the user exactly how they are supposed to enter these start and stop dates. Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.  You should run a linter against your code to make sure you have formatted it according to PEP8.

- [ ] Program is correctly formatted (2.0 pt)
- [ ] Program uses `argparse` and `datetime` (1.0 pt)
- [ ] Program functions as requested (2.0 pt)
