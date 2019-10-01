from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os

def createFiles(root, file, path):
    os.system('dd if={} of={}  count=1024000 bs=1024'.format(os.path.join(root, file), os.path.join(path, file)))


pathFrom = '/eavanesyan/folderFrom/'
pathTo = '/eavanesyan/folderTo/'

executor = ThreadPoolExecutor(max_workers=8) # Copying using threads
for root, directories, files in os.walk(pathFrom):
    for file in files:
        executor.submit(createFiles(root, file, pathTo))

executor = ProcessPoolExecutor(max_workers=8) # Copying using processes
for root, directories, files in os.walk(pathFrom):
    for file in files:
        executor.submit(createFiles(root, file, pathTo))