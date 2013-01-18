Unread Instapaper Articles in Alfred
========================

A python script to display unread articles from Instapaper in the Alfred window. You will need Alfred Version 2 and an Instapaper account to use this.

# Installation

To install the Unread Instapaper Articles workflow, double click on ```Instapaper.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

Next, edit the first script filter by double clicking on it. Edit the line ```print(list(“USERNAME”, “PASSWORD”))``` to fill in your Instapaper account details. Be sure to keep these in quotes.

# How to use

Simply type ```instapaper``` (or whatever you configure) into Alfred. If your Instapaper login is successful, the results should be populated with articles from your unread folder in Instapaper.

Navigating to these items with the arrow keys or selecting one with the corresponding shortcut should open the original article in the default browser. Holding ```alt``` while doing this will open the original article in Google Chrome (useful if you have Flash disabled in Safari and want to open a YouTube link).

# Based upon

[Dan Palmer's reddit workflow](http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html)

[Run BASH built-in commands in Python?](http://stackoverflow.com/questions/5460923/run-bash-built-in-commands-in-python), a question from [duanedesign](http://stackoverflow.com/users/401815/duanedesign)

# Download

[Unread Instapaper Articles]()

# Copyright

The Instapaper name and logo are wholly owned by Marco Arment and Instapaper, LLC. Kai Wells does not own or claim to own anything related to Instapaper.

# Version History

## 1.1 - January 17, 2013

- Cleaned up and condensed code
- Added Instapaper icon
- Made python binary

## 1.0 - January 13, 2013

- Commit: Initial Release as a [gist](https://gist.github.com/4523191)