==========
Oakland:PM
==========

A web-based application for connecting youth with after-school enrichment programs

What We Are Building
--------------------

We propose to develop a versatile, web-based application also accessible via mobile devices 
that connects Oakland youth to after-school programs and enrichment opportunities.

Oakland offers many opportunities for after-school enrichment, but there is
presently no on-line method for students to discover them according to their
interests, their location, or their friendships.  Our application will leverage
the social media that youth are already using, such as facebook, twitter, and
tumblr, to bring current and personalized information to them.
 
Contributors
------------

`Jed Parsons`_
Kristi Holohan, 
Sonja Totten-Harris,
`Telly Koosis`_, 
Joshua Goldenberg, 
`Christopher Yap`_, 
Dave Meyer, 
Aditya Pai,
Greg Martin, 
Raimundo Martinez, 
`Andrew Hao`_ 


:Version: 0.0.1 of 2011/17/11 
:Dedication:  HEP!


Set-up
------


Required
''''''''
- [Source- Read-only](https://github.com/jedp/oakland_pm.git)
- (Mac) Xcode >= 3.2
- `sudo pip install -U virtualenv`
- `sudo pip install -U virtualenvwrapper`
- `sudo pip install Mercurial`
- Add in bash: `source /usr/local/bin/virtualenvwrapper.sh`

You don't need these for dev, but the live server requires:

- `python-openid`_
- `python-oauth2`_
  
.. _python-openid: https://github.com/openid/python-openid
.. _python-oauth2: https://github.com/simplegeo/python-oauth2

Recommended
'''''''''''

- (Mac) `Homebrew`_ ::

    ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

Database
''''''''

:Local: Sqlite3 (default)  (or `Postgres`_)
:Production: [Postgres](http://www.enterprisedb.com/products-services-training/pgdownload)

Python Modules
''''''''''''''

- See `requirements.txt`

.. _Homebrew: http://mxcl.github.com/homebrew/
.. _Postgres: http://www.enterprisedb.com/products-services-training/pgdownload
.. _Mercurial: http://mercurial.selenic.com/

.. _Telly Koosis: https://github.com/tkoosis/
.. _Jed Parsons: https://github.com/jedp/
.. _Andrew Hao: https://github.com/andrewhao/
.. _Christopher Yap: https://github.com/buzzyapyear/
.. _Greg Martin: https://github.com/lygg/
