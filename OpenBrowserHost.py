import sublime, sublime_plugin
import os, webbrowser
 
class OpenBrowserHostCommand(sublime_plugin.TextCommand):
   def run(self,edit):
      file_name = self.view.file_name()
      if file_name is not None:
        self.settings = sublime.load_settings("OpenBrowserHost.sublime-settings")
        base_file = os.path.basename(file_name)
        webbrowser.open_new_tab(self.settings.get("host") + "/" + base_file)
