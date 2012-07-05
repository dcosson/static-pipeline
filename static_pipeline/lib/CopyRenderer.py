from shutil import copyfile, copytree
from static_pipeline.lib.base import Renderer

class CopyRenderer(Renderer):
    """ Copies files over unchanged (for images, external libraries, etc)
    """
    def __init__(self, input_path, output_path, template_word=None, **kwargs):
        super(CopyRenderer, self).__init__(input_path, output_path,
                template_word)
        print "Copying files..."

    def render_content(self, inpath, outpath):
        """ Copy a single file
            @inpath:=a file to render
            @outpath:=output location
        """
        copyfile(inpath, outpath)

    def render_content_recursive(self, inpath, outpath):
        """ Copy a directory, maintaining subdirectory structure
            @inpath:=a file to render
            @outpath:=output location
        """
        import ipdb; ipdb.set_trace()
        copytree(inpath, outpath)
