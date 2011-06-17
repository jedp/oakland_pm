Oakland:PM
==========

A mobile application for connecting with after-school enrichment programs

What We Are Building
--------------------

We propose to develop a web-based, mobile application that connects Oakland
youth to after-school programs and enrichment opportunities.

Oakland offers many opportunities for after-school enrichment, but there is
presently no on-line method for students to discover them according to their
interests, their location, or their friendships.  Our application will leverage
the social media that youth are already using, such as facebook, twitter, and
tumblr, to bring current and personalized information to them.
 
Contributors
------------

[Jed Parsons](https://github.com/jedp), Kristi Holohan, Sonja Totten-Harris,
Telly Koosis, Joshua Goldenberg, Christopher Yap, Dave Meyer, Aditya Pai,
Greg Martin, Raimundo Martinez, [Andrew Hao](https://github.com/andrewhao)


:Version: 0.0.1 of 2011/17/11 
:Dedication:  HEP!


Set-up
------------
	
----------
 System
----------
*Required*	
* Xcode > 3.1
* `sudo pip install -U virtualenv`
* `sudo pip install -U virtualenvwrapper`
* Add in bash source /usr/local/bin/virtualenvwrapper.sh
* [Mercurial]: http://mercurial.selenic.com/

*Recommended*
* [Homebrew](http://mxcl.github.com/homebrew/)::

    ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

----------
 Database
----------
* _Local_: Sqlite3 (or [Postgres](http://www.enterprisedb.com/products-services-training/pgdownload) if you want to set it up)
* _Production_: [Postgres](http://www.enterprisedb.com/products-services-training/pgdownload)
----------
 Python
----------
* See requirements.txt