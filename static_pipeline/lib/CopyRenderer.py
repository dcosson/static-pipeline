from shutil import copyfile
from static_pipeline.lib.base import Renderer

class CopyRenderer(Renderer):
    """ Copies files over unchanged (for images, external libraries, etc)
    """
    def __init__(self, input_path, output_path, template_word=None, **kwargs):
        super(CopyRenderer, self).__init__(input_path, output_path,
                template_word)
        print "Copying files..."

    def render_content(self, inpath, outpath):
        copyfile(inpath, outpath)
