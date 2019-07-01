# asciilines
Copyright © 2019 Sunanth Sakthivel

## Explanation of Program
This is a command line program that takes a .tvg file as an input and output the resulting canvas as an ascii on standard output. In order for the canvas to properly be outputed in standard output, the .tvg must be formated correctly. For example,

    $ cat tests/test1.tvg
    3 4
    * 1 -1 h 5
    # -1 1 v 5
    
The first line should include the canvas size. First number is row and second number is column. The subsequent lines are the commands to
draw on the canvas. Each command is executed in order from top to bottom. The first character indicates the character to fill in the canvas. Second and third indicate the row and column starting position. Fourth is to indicate whether the characters should be drawn horizontally (h) or vertically (v). Lastly, the last option is the length for the rendered line. 

Commands are processed with a for loop and eventually the final canvas (2d array) is created using a series of nested loops and range bound checks. For example, the test1.tvg will output the following:

    $ python asciilines.py tests/test1.tvg
    .#..
    *#**
    .#..

## Build and Run
Build and run the program using `python asciilines.py <.tvg path>`</br>
Tests can be checked by comparing the output of the program with respective .out file. 

## bugs, defects, failing tests, etc
There are no bugs, defects or failing tests in the current build of asciilines. Tests are done visually using cat and comparing with the standard output of the program. Ideally these tests should be made more automated and comparisons made via file comparison rather than visual inspection, nevertheless all the tests provided pass.

## License Information
Licensed with MIT License. See [LICENSE](/LICENSE)
