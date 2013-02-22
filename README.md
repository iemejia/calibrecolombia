README
==========

Some scripts to grab news from Colombian media to use with
[calibre](http://calibre-ebook.com) ebook management software.

Use
----------
Install calibre and its command-line tools (Preferences->Miscelanous)
and execute the command:

    ebook-convert myrecipe.recipe myrecipe.epub

You can view the results with the command:

    ebook-viewer myrecipe.epub

For development purposes you must run:

    ebook-convert myrecipe.recipe .epub --test -vv --debug-pipeline debug

Some links
----------
- [Calibre Develop](http://manual.calibre-ebook.com/develop.html)
- [Calibre Tips for developing new recipes](http://manual.calibre-ebook.com/news.html#tips-for-developing-new-recipes)
