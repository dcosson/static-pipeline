import subprocess
from static_pipeline.lib.base import Renderer

class DeleteRenderer(Renderer):
    """ Deletes a directory, e.g. one of the intermediary pipeline directories
    """

    def __init__(self, input_path, output_path=None, **kwargs):
        command = 'rm -rf'
        self.command_list = command.split(' ') + [input_path]
        print "Running Shell Command: %s" % (self.command_list,)

    def render_files(self):
        """ overwrite this method to just delete things
        """
        status = subprocess.call(self.command_list)
        print "  status: %s" % (status,)

class CommandLineRenderer(Renderer):
    """ Runs an arbitrary command in command line on each file
        matching the pattern
    """
    def __init__(self, input_path, output_path, command, **kwargs):
        super(CommandLineRenderer, self).__init__(input_path, output_path,
                **kwargs)
        self.command_base = command.split(' ')
        print "Command line renderer: %s" % (command,)

    def render_content(self, input_path, output_path):
        command = self.command_base + [input_path, output_path]
        print "  running: %s" % (command,)
        subprocess.call(command)

class LessCssRenderer(CommandLineRenderer):
    def __init__(self, *args, **kwargs):
        kwargs['template_word'] = "less"
        if not kwargs.get('command'):
            kwargs['command'] = 'lessc'
        super(LessCssRenderer, self).__init__(*args, **kwargs)
        print "Less CSS renderer..."
