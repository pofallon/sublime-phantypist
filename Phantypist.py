# A Sublime Text 2 & 3 plugin that outputs the contents of the clipboard one character 
# at a time, with variable amount of time in between each character

# (c) 2014 Paul O'Fallon

import sublime, sublime_plugin, random

class PhantypistCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		originalAutoIndent = self.view.settings().get("auto_indent")
		self.view.settings().set("auto_indent", False)
		text = sublime.get_clipboard()
		sublime.set_timeout(lambda: self.output(text, originalAutoIndent), 0)

	def output(self, text, originalAutoIndent):
		t =  text[0]
		self.view.run_command("insert", {"characters": t})
		if len(text) > 1:
			if t == ' ' and text[1] == ' ':
				# If you're indenting a bunch of spaces, just output those quickly
				nextTime = 0
			else:
				nextTime = random.randrange(50,300)
			sublime.set_timeout(lambda: self.output(text[1:], originalAutoIndent), nextTime)
		else:
			self.view.settings().set("auto_indent", originalAutoIndent)