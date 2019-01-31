from contextlib import contextmanager
import os
import subprocess as sub

@contextmanager
def working_directory(path):
    old_path = os.getcwd()
    sub.check_call(["mkdir", "-p", path])
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)

def make_dir(picture_dir):
    """Try to make a directory named for date and time. If it already exists append a number to the directory name and try again."""

    count = 1

    while True:
        try:
            os.mkdir(picture_dir)
        except FileExistsError:
            picture_dir = picture_dir + '_{0}'.format(count)
            count += 1
    
        if os.path.isdir(picture_dir):
            return picture_dir

