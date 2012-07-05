import lib
import utils

def render(pipeline, settings_module):
    """ the main render function
    """
    for kwargs in pipeline:
        template_word = kwargs.pop('type')
        # give renderers a dict of global variable (from settings file)
        kwargs['global_vars'] = vars(settings_module)
        RendererClass = lib.get_renderer_from_template_word(template_word)
        renderer = RendererClass(**kwargs)
        renderer.render_files()
