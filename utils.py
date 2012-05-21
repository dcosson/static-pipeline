import os
import copy
### Helper Functions
IGNORE_FILE_TYPES = ["swp", "pyc"]
def ls_recursive(current, prepend=[], dir_sep = '/'):
    """ returns a list of the full relative path for
    all FILES (not directories) higher in the directory tree
    """
    children = []
    #print "current: %s" % current
    current_full = os.path.join(*(prepend + [current]))
    if os.path.isdir(current_full):
        new_prepend = copy.copy(prepend)
        new_prepend.append(current)
        for child in os.listdir(current_full):
            files = ls_recursive(child, new_prepend)
            children += files
    else:
        if not current_full.split('.')[-1] in IGNORE_FILE_TYPES:
            children.append(current_full)
    return children

def get_filename_from_pathname(path):
    if os.path.isdir(path):
        raise IOError("path is a directory, not a file")
    return os.path.split(path)[1]

def get_template_name_from_pathname(path):
    if os.path.isdir(path):
        raise IOError("path is a directory, not a file")
    return path.split(os.path.sep, 1)[-1]
