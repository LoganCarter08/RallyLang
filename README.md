# RallyLang
RallyLang is a very simplistic interpretation of a programming language using rally pace notes. 
This style of "hiding" a language within text that looks like something else is inspired by the language Chef. 
The following syntax may not match what your pacenotes exactly as everybody's notes may be slightly different. 
Over time the syntax may evolve slightly, so if for some reason you find yourself messing around with RallyLang 
please check for updates after pulling the latest version. 

## Syntax
The following will continue to change and be added to as progression is made. Right now only simple math and
string manipulation is supported. It is unclear how much will be added in the future, but the following table
represents what is currently supported along with their real world representation. Check the test files for
examples on the usage. Those are used for testing syntax as it is developed and should give an idea of how 
things are working. 

| Symbol           | Pronunciation | Rally Usage                   | RallyLang Operation     |
| ---------------- |:-------------:|:-----------------------------:|:-----------------------:|
| L(1-6)           | Left #        | Sharpness rating of left turn |Variable                 |
| R(1-6)           | Right #       | Sharpness rating of right turn|Variable                 |
| ->               | Into          | Next feature is very close    |Variable Assignment      |
| +                | Plus          | Corner sharpness lessens      |Addition                 |
| -                | Minus         | Corner sharpness increases    |Subtraction              |
| cr               | Crest         | Go over a small hill          |Multiplication           |
| /                | Over          | Combine features              |Division                 |
| slpy             | Slippy        | Corner is slippery            |String Identifier        |
| lg               | Long          | Corner length is long         |Double/Float Identifier  |
| sh               | Short         | Corner length is short        |Boolean Identifier       |
| cut              | Cut           | Corner is safe to cut         |Print variable           |
| oc               | Off Camber    | Road is slanted poorly        |Command line input       |
| unseen           | Unseen        | Corner is hidden from view    |Multiply by -1           |
| finish           | Finish        | Stage is over                 |Program is finished      |

## Why?
Why would I create this language with seamingly no true usage? Well, for fun of course. I thought this would 
be a fun opportunity to try and combine motorsports with programming. This baby transpiler is more of a fun
learning experience than anything else. I hope you find it at least comical or interesting. 

## Plans
The current plans for this are to just support simplistic loops, conditionals, integer and double math, and string
manipulation. Outside of that I have no major plans. Currently the interpretation only supports a total of 12 unique
variables and I don't see that part changing. I doubt anybody will ever find this truly useful, but that's okay.  

### To Do
1. Add statements and loops
2. Add jmp?, <, >, !, dc, keepm, and other common rally callouts we could incorporate
3. Add boolean logic
4. Add error handling that returns errors within RallyLang and not the underlying Python  
