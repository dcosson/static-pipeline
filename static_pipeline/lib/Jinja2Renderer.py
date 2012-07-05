import os
import jinja2
from static_pipeline.lib.base import Renderer

class Jinja2Renderer(Renderer):
    """ Render Jinja2 Templates
    """

    def __init__(self, input_path, output_path,
            global_vars=None, template_word="jinja2", **kwargs):
        super(Jinja2Renderer, self).__init__(input_path, output_path,
                template_word)
        self.global_vars = global_vars
        self.template_word = template_word
        self._set_jinja_env(global_vars, input_path)
        print "Rendering Jinja2 Templates..."

    def render_content(self, inpath, outpath):
        """ Load and render the template
        """
        filename = os.path.split(inpath)[1]
        t = self.env.get_template(filename)
        content = t.render()
        with open(outpath, 'w') as f:
            f.write(content)

    def _set_jinja_env(self, global_vars, template_path):
        """ no env vars yet, so it's kind of useless other than for inheritance"""
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        env.globals = global_vars
        self.env = env
