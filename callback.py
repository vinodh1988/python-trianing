def filereader(files,userprocess):
    if(callable(userprocess)):
        for x in files:
            print('########### Reading ##############',x,'\n')
            f=open(x,'r')
            userprocess(f.read())
            f.close()
            print('########### Close ###############',x,'\n')

def stringprocessing(data):
    print('Going to process the Data --------------------------->')
    print(data)
    print('Finished processing data --------------------------->')


filereader(['collections.py','first.py','functions.py','lambda.py'],stringprocessing)