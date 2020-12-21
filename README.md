# SantaOperation
Code to generate 2.2 billion fictional santa letters I made for a project in university.

"letterGenerator.py" is the MAIN file , run that if you want to run the code (make sure you have all the libraries installed)

You can run it in n instances to improve performance (n = number of threads on your CPU), or possibly even with tensorflow-gpu instead of tensorflow for even better performance (if hardware supports it). Beware if ran on more than one instance every instance must output in a DIFFERENT file. And after you're DONE generating you use lettercopier.py to append them all into a single file. 

The "LETTERMULTIPLICATOR.py" is going to get an emergency update soon (tonight) to make it more efficient as for now it can't handle more than 400million letters

WARNING!
Before running the lettercopier.py please check the start and end of each file and delete any EXTRA "n*r=number" that is not associated to any letter
otherwise the whole dataset will be compromised
