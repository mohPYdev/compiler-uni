# compiler-uni
it's a simple compiler for the c language written in python.

## structure
this project has 2 folders : 
- Lexical
- Syntax

#### Lexical
this folder contains all the files for a lexical analyser part of the compiler that generats tokens from raw text and 
this part also does the preprocessing of the text like removing the comments and dealing with **#define** and **#include**.

#### Syntax
this folder contains all the files related to the syntax analyser of the compiler. it means that this part generate a tree from parsing the input and
grammar using the **TOP-DOWN PARSER**. <br />
so for this to work:
- we need a grammar.
- we need to find the first and follow of the grammar.
- we want a parsing LL(1) table using the first and follow set from the previous step.
- generating tree (parsing the input)

## How it works
you can run every package individualy for testing.
in the syntax package you should run the lexical.py. it automatically runs the preprocessor and cleans the input and outputs the cleanedSource.txt file.<br>
and the input for the lexical analyser is that cleanedSource file. it reads the file character by character and moves the states and generates token using the 
state class and DFA which is a dictionary of dictionaries of states and strings.

