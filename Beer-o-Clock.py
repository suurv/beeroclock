import sublime_plugin
import sublime


class BeerclockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.message_dialog("Yes, it's Beer-o-clock!")