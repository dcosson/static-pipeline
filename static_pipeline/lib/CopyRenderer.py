import os
from shutil import copyfile, copytree, rmtree
from static_pipeline.lib.base import Renderer

class CopyRenderer(Renderer):
    """ Copies files over unchanged (for images, external libraries, etc)
    """
    def __init__(self, input_path, output_path, **kwargs):
        super(CopyRenderer, self).__init__(input_path, output_path, **kwargs)
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

            If output directory already exists, we'll merge in new dir
            (Merge is not recursive, just one level in)
        """
        # if dir doesn't exist yet, copy it
        if not os.path.isdir(outpath):
            copytree(inpath, outpath)
            return

        # else, copy the dirs it contains
        # TODO: find a way around deleting the dir, this is the only place we do this
        for f in os.listdir(inpath):
            inpath_name = os.path.join(inpath, f)
            outpath_name = os.path.join(outpath, f)
            if os.path.isdir(outpath_name):
                rmtree(outpath_name)
            copytree(inpath_name, outpath_name) 
