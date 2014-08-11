# A Sublime Text 2 & 3 plugin that outputs the contents of the clipboard one character 
# at a time, with variable amount of time in between each character

# (c) 2014 Paul O'Fallon

import sublime, sublime_plugin, random

class PhantypistCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = sublime.get_clipboard()
		sublime.set_timeout(lambda: self.output(text), 0)

	def output(self, text):
		t =  text[0]
		point = self.view.sel()[0].begin()
		self.view.run_command("insert", {"characters": t})
		if len(text) > 1:
			if t == ' ' and text[1] == ' ':
				# If you're indenting a bunch of spaces, just output those quickly
				nextTime = 0
			else:
				nextTime = random.randrange(50,300)
			sublime.set_timeout(lambda: self.output(text[1:]), nextTime)