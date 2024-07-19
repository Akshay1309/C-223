import zipfile
import time

filename=input('Path to the file')
zipf = zipfile.zipFile(filename)

global result
global tried
result = 0
tried = 0
c = 0

if not zipf:
    print(f'the file {filename} is not encrypted . you can open it')

else:
    start_time = time.time()
    wordListFile = open('wordlist.txt','r',errors = 'ignore')
    body = wordListFile.read.lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf-8').strip()
        c = c + 1
        print('Trying to decode password by: {}'.format(word))
        try:
            with zipfile.ZipFile(filename,'r') as zf:
                zf.extractall(pwd=password)
                print("Success! The password is: "+ word)
                end_time = time.time()           
                result = 1                     
            break
        except:
             pass
        
        if (result == 0):
            duration = end_time - start_time
            print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
        
        else:
            duration = end_time - start_time
            print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
