import os
import datetime
import fnmatch

# 파일 기본
print(os.getcwd())

ctime = os.path.getctime('11_file_system.py')
print(ctime)
print(datetime.datetime.fromtimestamp(ctime)
  .strftime('%Y%m%d %H:%M:%S'))

mtime = os.path.getmtime('11_file_system.py')
print(mtime)
print(datetime.datetime.fromtimestamp(mtime)
  .strftime('%Y%m%d %H:%M:%S'))

atime = os.path.getatime('11_file_system.py')
print(atime)
print(datetime.datetime.fromtimestamp(atime)
  .strftime('%Y%m%d %H:%M:%S'))

size = os.path.getsize('11_file_system.py')
print(size)

print(os.listdir())

pattern = '*.py'
result = []
for root, dirs, files in os.walk('.'):
  for name in files:
    if fnmatch.fnmatch(name, pattern):
      result.append(os.path.join(root, name))
print(result)

print(os.path.isdir('11_file_system.py'))
print(os.path.isfile('11_file_system.py'))

if os.path.exists('11_file_system.py'):
  print('파일 또는 폴더가 존재합니다.')

# open('new_file.txt', 'a').close()
# os.rename('new_file.txt', 'new_file_rename.txt')
# os.remove('new_file_rename.txt')

# os.mkdir('new_folder')
# os.rmdir('new_folder')
