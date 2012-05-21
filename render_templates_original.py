import sys
import os
import copy
import jinja2

###
### Jinja 2 renderer
###
class Renderer(object):
    """ Renders all the jinja templates in a directory into files
    """
    def __init__(self, template_path, output_path, 
                 global_vars=None, template_word='.jinja2'):
        if not os.path.exists(template_path) or not os.path.isdir(template_path):
            raise IOError("the specified template_path %s doesn't exist or isn't a directory" % template_path)
        if not os.path.exists(output_path) or not os.path.isdir(template_path):
            raise IOError("the specified output_path %s doesn't exist or isn't a directory" % output_path)
        self.template_path = template_path
        self.output_path = output_path
        self.tword = template_word
        self._set_jinja_env(global_vars, template_path)

    def _set_jinja_env(self, global_vars, template_path):
        """ no env vars yet, so it's kind of useless other than for inheritance"""
        e = jinja2.Environment()
        e.globals = global_vars
        e.loader = jinja2.FileSystemLoader(template_path)
        self.env = e

    def render_files(self, require_template_keyword=True, flatten_dir_structure=True):
        files = ls_recursive(self.template_path)
        if require_template_keyword:
            #filter out files that don't contain the template keyword
            files = filter(lambda x: str_contains(self.tword, get_filename_from_pathname(x)), files)
        #filter out private files (vim swp, etc)
        files = filter(lambda x: not get_filename_from_pathname(x).startswith('.') and not get_filename_from_pathname(x).startswith('_'), files)
        print "rendering files..."
        for f in files:
            print "rendering: %s" % (f,)
            filename = get_filename_from_pathname(f)
            if flatten_dir_structure:
                outpath = os.path.join(self.output_path, self.get_output_filename(filename))
            else:
                raise Exception("flatten_dir_structure=False option not yet implemented")
            self.render_file(f, outpath)

    def render_file(self, inpath, outpath):
        filename = get_filename_from_pathname(inpath)
        # load and render template
        t = self.env.get_template(filename)
        output = t.render()
        # print to file
        with open(outpath, 'w') as f:
            f.write(output)
        print "rendered %s" % (outpath)

    def get_output_filename(self, input_filename):
        """ generates the output path from the input filename
        by removing the template distinguishing word. 
        e.g. wizardhat-jinja2.html -> wizardhat.html
        """
        outfile = ''.join( input_filename.split(self.tword) )
        return outfile

###
### Helper Functions
###
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
        #print "recursing into %s" % (current_full,)
        for child in os.listdir(current_full):
            files = ls_recursive(child, new_prepend)
            children += files
    else:
        children.append(current_full)
    return children

def make_intermediate_dirs(dir_list, starting_point):
    for d in dir_list:
        dirs = os.path.split(d)[0]
        try:
            os.makedirs(os.path.join(starting_point,dirs))
        except OSError:
            print "dir exists: %s" % (dirs,)

def get_filename_from_pathname(path):
    if os.path.isdir(path):
        raise IOError("path is a directory, not a file")
    return os.path.split(path)[1]

def str_contains(word, s):
    if s.find(word) >= 0:
        return True
    else:
        return False

###
### Make script runnable
###
if __name__ == "__main__":
    if len(sys.argv) == 2:
        constants_module = sys.argv[1]
    else:
        constants_module = "constants"
    constants = __import__(constants_module)
    ### filter out private and builtin functions
    globals = dict((k,v) for k,v in constants.__dict__.iteritems() if not k.startswith('_'))
    try:
        paths = globals.pop('RENDER_PATHS')
    except KeyError:
        raise ImportError("your constants file '%s.py' must contain a 'RENDER_PATHS' variable. This should be a list of tuples of the form (input path, output path) of directories in which to look for files to render." % (constants_module,))
    for path_set in paths:
        print >> sys.stderr, "rendering files in ./%s to ./%s" % (path_set[0], path_set[1])
        r = Renderer(path_set[0], path_set[1], globals)
        r.render_files(require_template_keyword=False)
