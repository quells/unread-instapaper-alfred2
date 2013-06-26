Instapaper Articles in Alfred
===================

A python script to display unread articles from Instapaper in the Alfred window. You will need Alfred Version 2 and an Instapaper subscription **in addition to a normal account** to use this.

# Installation

To install the Unread Instapaper Articles workflow, double click on ```Instapaper.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

Next, edit the first script filter by double clicking on it. Edit the line ```print(list(“USERNAME”, “PASSWORD”, ‘{query}’))``` to fill in your Instapaper account details. Be sure to keep these in quotes.

# How to use

Simply type ```instapaper``` (or whatever you configure) into Alfred. If your Instapaper login is successful, the results should be populated with articles from your Unread folder in Instapaper.

To display the Archive instead of the Unread folder, type ```instapaper archive```. Similarly, articles in the Liked/Starred folder can be displayed with ```instapaper liked``` or ```instapaper starred```.

To filter the results, add your query after a space. For example, ```instapaper apple``` will only display results with ```apple``` in the title or description of the article. This is case insensitive and is compatible with regular expression syntax, if you’re into that.

Navigating to these items with the arrow keys or selecting one with the corresponding shortcut should open the original article in the default browser. Holding ```alt``` while doing this will open the original article in Google Chrome (useful if you have Flash disabled in Safari and want to open a YouTube link).

Based upon [Dan Palmer's reddit workflow](http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html)

# Download

[Instapaper Alfred Workflow](https://github.com/quells/unread-instapaper-alfred2/blob/master/Instapaper.alfredworkflow?raw=true)

# Copyright

The Instapaper name and logo are owned by [betaworks](http://betaworks.com) and [Marco Arment](http://www.marco.org). Kai Wells does not own or claim to own anything related to Instapaper.

# Version History

## 1.2.1 - June 26, 2013

- Added an item at the top of the list that points to [the Instapaper website](http://www.instapaper.com) to make it easy to manage your saved articles.
- Updated Copyright section to reflect the change in ownership of Instapaper.

## 1.2 - January 27, 2013

- Uses the urllib2 module to download the JSON data from Instapaper instead of a bash script. This significantly reduces the complexity of the script by eliminating regular expression filtering and improves results by using UTF strings.
- To compensate for the reduced complexity, searching is implemented! Supports regular expressions in your query, but not boolean logic strings like ```and```, ```or```, and ```not```.
- Also implemented other folders. ```archive```, ```starred```, and ```liked``` are reserved words for searching these folders instead of the unread folder.

## 1.1 - January 17, 2013

- Cleaned up and condensed code
- Added Instapaper icon
- Made python binary

## 1.0 - January 13, 2013

- Commit: Initial Release as a [gist](https://gist.github.com/4523191)