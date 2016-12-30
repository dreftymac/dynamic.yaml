```
### <beg-file_info>
### document_metadata:
###   - date: created="2016-12-29"
###     last: lastmod="2016-12-29"
###     tags: tags
###     author: created="__author__"
###     dmid: "emptily_obeys_disaster"
###     filetype: "markdown"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * __desc__
###     seealso: |
###         * __seealso__
### <end-file_info>
```

## Overview

The transclusion topic deals with any scenario where we want to 'include' one file into another.

There are three transclusion scenarios we care about.

* Template transclusion
* Data transclusion
* Config transclusion

## Template transclusion

Scenario where we have one set of data and one template and we want multiple other templates to be transcluded into the primary template.

### Issues

* make it easy as possible to include templates
* make it easy as possible to go from plain file to template-compatible file that supports looping and variables
* syntax that is clean and unobtrusive when going from plain file to template



## Data transclusion

Scenario where there are multiple data files and we want them all reachable by a set of templates.


## Config transclusion

Scenario where we want global configuration settings to be swappable by specifying different files.


