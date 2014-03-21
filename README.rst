Personal Blog
=============

My personal blog content management.
Kindly go to `eugene-yeo.in <http://eugene-yeo.in/>`_ for a better reading experience.

Core Technology: 
----------------

* Blog Engine: `Pelican <http://getpelican.com/>`_
* Blog Server: `Amazon S3 <http://aws.amazon.com/s3/>`_
* Markup Syntax: `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
* UI Design Framework: `inuit.css <https://github.com/csswizardry/inuit.css/>`_
* Programming Language: `Python 2.7 <http://www.python.org/>`_
* And Many More... (Plugins, PYPI)

Personal Installation Guide:
----------------------------

.. code-block:: bash

    git clone git@github.com:9gix/eugene-yeo.in.git
    cd eugene-yeo.in
    mkvirtualenv eugene-yeo.in
    workon eugene-yeo.in
    pip install -r requirements.txt

    # Setup S3 config and change access_key & secret_key
    cp utility/.s3cfg.sample ~/.s3cfg

    # Development
    make devserver
    ./devserver.sh stop

    # Upload to S3
    make s3_upload


Available tags:
---------------

* Content Related:
    * quote
* Programming Related:
    * python
    * django
    * javascript
    * css
* Activity Related:
    * errors
    * setup
* Event Related
    * cyberwarfare
* Tool & Technology Related:
    * git
    * email
