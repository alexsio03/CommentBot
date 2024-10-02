import glob
import os

if __name__ == "__main__":
    for file in glob.glob('audio.*'):
        os.remove(file)
    for file in glob.glob('text.txt'):
        os.remove(file)
    for file in glob.glob('comment.txt'):
        os.remove(file)
