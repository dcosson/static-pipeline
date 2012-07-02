from Jinja2Renderer import Jinja2Renderer
from RenameRenderer import RenameRenderer
from CopyRenderer import CopyRenderer
from CommandLineRenderer import (DeleteRenderer,
                                 CommandLineRenderer,
                                 LessCssRenderer)


def get_renderer_from_template_word(word):
    map_ = {'jinja2': Jinja2Renderer,
            'less': LessCssRenderer,
            'less-css': LessCssRenderer,
            'command-line': CommandLineRenderer,
            'filter/rename': RenameRenderer,
            'copy': CopyRenderer,
            'delete': DeleteRenderer}
    out = map_.get(word)
    if not out:
        raise Exception("Unsupported template type: %s" % (word,))
    return out
