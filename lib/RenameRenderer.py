import os
from base import Renderer

class RenameRenderer(Renderer):
    """ Rename files, and filter some
    """
    def __init__(self, input_path, output_path, template_word='filter/rename',
            filter_list=None, rename_list=None):
        super(RenameRenderer, self).__init__(input_path, output_path,
                template_word)
        self.filter_list = filter_list or []
        self.rename_list = rename_list or []
        print "Filtering/Renaming files..."

    def render_content(self, inpath, outpath):
        indir, infile = os.path.split(inpath)
        if infile in self.filter_list:
            print "Not rendering %s based on file name" % (inpath,)
        outdir, outfile = os.path.split(outpath)
        with open(inpath, 'r') as f:
            content = f.read()
        for rename_rule, replacement in self.rename_list:
            outfile = outfile.replace(rename_rule, replacement)
        outpath = os.path.join(outdir, outfile)
        with open(outpath, 'w') as f:
            f.write(content)
