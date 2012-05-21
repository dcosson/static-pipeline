#!/usr/bin/env python
from lib import get_renderer_from_template_word


PIPELINE = [
    {'type': 'jinja2',
     'input_path': 'tmp',
     'output_path': 'out/_tmp'},
    {'type': 'filter/rename',
     'input_path': 'out/_tmp',
     'output_path': 'out',
     'filter_list': ['base.html'],
     'rename_list': [('.html', '')]},
     ## Clean up
     {'type': 'delete',
      'input_path': 'out/_tmp'}]


if __name__ == "__main__":
    for kwargs in PIPELINE:
        template_word = kwargs.pop('type')
        RendererClass = get_renderer_from_template_word(template_word)
        renderer = RendererClass(**kwargs)
        renderer.render_files()
