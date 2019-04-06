# DataStructure_exercises

The exercise consist of taking 
an integer and returning it in 
a reversed manner. 

The puzzling part is what to do with a negative 
number? This becomes peculiar when we 
acknowledge that the negative symbol has to 
remain in front of the output.

The program also gets rid of leading zeros after 
reversing the original value. For example: 1130
after being reversed will read 0311, but the prompt wants
it to return only 311 since it is the same value as
0311.

Another issue to take into consideration is what to 
do with an input of a single zero? Previously, I mentioned
that a leading zero will be discarded, but a single zero
is a leading zero, so it cannot be discarded.

I solved the problem without checking for a bit 
overflow by using list. I am familiar with list, so 
that was my innate approach. 

First, I split the integer value into a list so that
each single digit has its own index. Then I 
reverse the list and check for a leading zero. If a leading
zero is found, it is discarded. None of this occurs 
however until the program determines if it is dealing
with positive or negative value. With a negative value, the original
integer not only gets put into a list and reversed, but it is also
separated from the negative symbol and later on 
concatenated after the necessary manipulation 
is completed.
