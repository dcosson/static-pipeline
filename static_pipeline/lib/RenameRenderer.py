import os
from static_pipeline.lib.base import Renderer

class RenameRenderer(Renderer):
    """ Rename files, and filter some
    """
    def __init__(self, input_path, output_path, template_word=None,
            filter_list=None, rename_list=None, **kwargs):
        super(RenameRenderer, self).__init__(input_path, output_path,
                template_word)
        self.filter_list = filter_list or []
        self.rename_list = rename_list or []
        print "Filtering/Renaming files..."

    def render_content(self, inpath, outpath):
        indir, infile = os.path.split(inpath)
        if infile in self.filter_list:
            print "    filtered out based on name: %s" % (infile,)
            return
        outdir, outfile = os.path.split(outpath)
        with open(inpath, 'r') as f:
            content = f.read()
        # rename based on rules
        renamed = False
        for rename_rule, replacement in self.rename_list:
            outfile = outfile.replace(rename_rule, replacement)
            renamed = True
        if renamed:
            print "    renamed: %s" % (outfile,)
        # write file
        outpath = os.path.join(outdir, outfile)
        with open(outpath, 'w') as f:
            f.write(content)
