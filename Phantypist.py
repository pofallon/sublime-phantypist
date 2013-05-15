# A Sublime Text 2 plugin that outputs the contents of the clipboard one character 
# at a time, with variable amount of time in between each character

# (c) 2013 Paul O'Fallon

import sublime, sublime_plugin, random

class PhantypistCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = sublime.get_clipboard()
		sublime.set_timeout(lambda: self.output(edit, text), 0)

	def output(self, edit, text):
		t =  text[0]
		point = self.view.sel()[0].begin()
		self.view.insert(edit, point, t)
		if len(text) > 1:
			if t == ' ' and text[1] == ' ':
				# If you're indenting a bunch of spaces, just output those quickly
				nextTime = 0
			else:
				nextTime = random.randrange(50,300)
			sublime.set_timeout(lambda: self.output(edit, text[1:]), nextTime)