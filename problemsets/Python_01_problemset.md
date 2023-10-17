Python 1 Problem Set
==================

Do all work in you github problemset repository.  

1. Start up the Python Interactive Interpreter.
    - `python3` this is how you start the interpreter on the command line
    - Print out "Hello New York"
    - Store your name in a variable
    - Print the contents of this variable.
    - QUIT the Interpreter
    
3. Working with a text editor. Use `vi` to write a script. Name your script something like `python1.py` or `me.py` . Python scripts should always have the `.py` extension.
   - `vi me.py`   
   - Make sure to include `#!/usr/bin/env python3` on line 1 of your script. It has to be line one. Do not leave a blank line above. 
   - Add code to print out, your name
      
        Script Output:
        ```
         My name: Sofia
        ```
    - On the command line make it executable using `chmod` (**only have to do this one time per script**).
    - Run it from the command line. 
    - Remember it is important to write only a bit, test, then write more.
    - If it works, ADD/COMMIT. Make a good message, like "added name to print"
    - Now add some code to print out your favorite color:
   
         Script Output:
         ```
         My name: Sofia
         My favorite color: Green
        ```
   - Save it, and run it from the command line. 
   - Now add some code to create a variable with your favorite activity. Make sure to give your variable a descriptive name.
   - Print out the variable with your favorite activity. You will need to use a comma in your print statement to print text and your variable. `print("some text" , your_variable)`

       ```
         My name: Sofia
         My favorite color: Green
         My favorite activity: Coding
        ```
   - Save it, and run it from the command line. 
   - Now add some code to print out your favorite animal:      
        
        ```
         My name: Sofia
         My favorite color: Green
         My favorite activity: Coding
         My favorite animal: Chicken
        ```
        >  Remember, write a bit, then run your code, write some more, then run again. This makes code easier to debug.
   - Try out [f"" string formatting](../pfb.md#string-formatting). Change one or all of your print statements to use `f""` with your variable in curly braces.
       example: 
       ```
       print(f"My name: {name}") 
       ```
4. Use `sys.argv` (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the [example in the notes](../pfb.md#command-line-parameters-a-special-built-in-list). Print all the variables in one print statement.
    - try using commas to separate your print arguments. 
    - try using '+' to separate your print arguments.

5. Make sure to keep your remote repository synced with your local repo. (ADD/COMMIT/PUSH)


