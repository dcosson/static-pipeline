import os
import logging
import ipdb; ipdb.set_trace()
from static_pipeline.lib import get_renderer_from_template_word
from static_pipeline.utils import ls_recursive, get_filename_from_pathname

def render(pipeline, settings_module):
    """ the main render function
    """
    for kwargs in pipeline:
        template_word = kwargs.pop('type')
        # give renderers a dict of global variable (from settings file)
        kwargs['global_vars'] = vars(settings_module)
        RendererClass = get_renderer_from_template_word(template_word)
        renderer = RendererClass(**kwargs)
        renderer.render_files()

class Renderer(object):
    """ Renders the content into files
    """
    def __init__(self, input_path, output_path, template_word,
            copy_not_matching=False, keep_dir_structure=False, **kwargs):
        if not os.path.exists(input_path) or not os.path.isdir(input_path):
            raise IOError("the specified input_path %s doesn't exist or isn't a directory" % input_path)
        if not os.path.exists(output_path) or not os.path.isdir(input_path):
            print "the specified output dir %s doesn't exist," \
                    "creating it now" % (output_path,)
            os.makedirs(output_path)
        self.input_path = input_path
        self.output_path = output_path
        self.tword = template_word
        self.copy_not_matching = copy_not_matching
        self.keep_dir_structure = keep_dir_structure

    def render_files(self):
        """ Renders all files in the path appropriately
            Calls render_content or render_content_recursive
        """
        if self.keep_dir_structure:
            print "keeping directory structure"
            self.render_content_recursive(self.input_path, self.output_path)
            return
        ## Else recurse into directory, render files one by one
        files = ls_recursive(self.input_path)
        for f in files:
            filename = get_filename_from_pathname(f)
            outpath = os.path.join(self.output_path, self.get_output_filename(filename))
            if not self.tword or self.tword in f.split('.'):
                print "  rendering: %s" % (f,)
                self.render_content(f, outpath)
            else:
                if self.copy_not_matching:
                    print "  copying:   %s" % (outpath,)
                    self.simple_copy(f, outpath)
                else:
                    print "  ignoring:  %s" % (f,)

    def render_content(self, inpath, outpath):
        """ Not defined for base class """
        logging.warn("render_content not defined for base class")

    def simple_copy(self, inpath, outpath):
        with open(inpath, 'r') as f:
            content = f.read()
        with open(outpath, 'w') as f:
            f.write(content)

    def get_output_filename(self, input_filename):
        """ generates the output path from the input filename
        by removing the template distinguishing word
        e.g. wizardhat.jinja2.html -> wizardhat.html
        """
        if not self.tword:
            return input_filename
        outfile = ''.join( input_filename.split('.{0}'.format(self.tword)) )
        return outfile
