sublime-phantypist
==================

A Sublime Text 2 plugin for slowly typing the contents of the clipboard

To add this to your Sublime Text 2 installation, do the following:

* Choose Sublime Text 2 > Preferences > Browse Packages to open your packages folder.
* Copy Phantypist.py into the Packages/User folder
* Choose Sublime Text 2 > Preferences > Keybindings - User and add the following JSON snippet inside the existing JSON array:

```javascript
{ "keys": ["command+shift+v"], "command": "phantypist" }
```

With this in place, you can "shift paste" and the text in your clipboard will slowly appear in the editor window.

Enjoy!
