from static_pipeline.utils import get_template_name_from_pathname
from static_pipeline.lib.base import Renderer
import jinja2

class Jinja2Renderer(Renderer):
    """ Render Jinja2 Templates
    """

    def __init__(self, input_path, output_path,
            global_vars=None, template_word="jinja2"):
        super(Jinja2Renderer, self).__init__(input_path, output_path,
                template_word)
        self.global_vars = global_vars
        self.template_word = template_word
        self._set_jinja_env(global_vars, input_path)
        print "Rendering Jinja2 Templates..."

    def render_content(self, inpath, outpath):
        filename = get_template_name_from_pathname(inpath)
        # load and render template
        t = self.env.get_template(filename)
        content = t.render()
        with open(outpath, 'w') as f:
            f.write(content)

    def _set_jinja_env(self, global_vars, template_path):
        """ no env vars yet, so it's kind of useless other than for inheritance"""
        env = jinja2.Environment()
        env.globals = global_vars
        env.loader = jinja2.FileSystemLoader(template_path)
        self.env = env
