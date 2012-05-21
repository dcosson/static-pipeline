#!/usr/bin/env python
from lib import get_renderer_from_template_word

if __name__ == "__main__":
    settings_file = "pipeline_settings"
    pipeline_settings = __import__(settings_file)
    for kwargs in pipeline_settings.PIPELINE:
        template_word = kwargs.pop('type')
        RendererClass = get_renderer_from_template_word(template_word)
        renderer = RendererClass(**kwargs)
        renderer.render_files()
