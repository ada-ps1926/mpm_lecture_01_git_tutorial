
#conda create -n acse python=3.14
#conda activate acse
# when this file is imported, it is run completely so it will also print 'Hello Alice'
 
def hello(name):
    print(f'Hello, {name}')

if __name__ == '__main__': #by adding this line, we avoid printing 'Hello Alice' while running edsml.py
    hello('Alice')








#Run using: python acse.py