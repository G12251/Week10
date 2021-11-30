import os


cwd = os.getcwd()

print('my current directory', cwd)
print(os.listdir(cwd))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk('.')
try:
    fin = open('bad_file')
except:
    print('Something went wrong')
finally:
    print ('Finally except is finished')

