
#we can import the acse file instead of writing the logic again 

#add the entire path if the file is in another folder (not in the same folder, not a package)
#if we want to just use 'import acse' then we must navigate to cd/src/subacse/acse in the terminal and then run

import src.acse.subacse.acse as acse 
import src.acse.subacse.arithm as arithm

acse.hello('EDSML') #Hello EDSML
print(arithm.add(1,2)) #3


#pip install -e .

#Run using: python edsml.py