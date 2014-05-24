My .vimrc file
==============

.. code-block:: bash

    execute pathogen#infect()
    execute pathogen#helptags()
    syntax on
    filetype plugin indent on

    autocmd FileType ruby setlocal expandtab softtabstop=2 tabstop=2 shiftwidth=2
    autocmd FileType html setlocal expandtab shiftwidth=2 tabstop=2 shiftwidth=2
    autocmd FileType css setlocal expandtab shiftwidth=4 tabstop=4 shiftwidth=4
    autocmd FileType javascript setlocal expandtab shiftwidth=4 tabstop=4
    autocmd FileType python setlocal expandtab softtabstop=4 tabstop=4 shiftwidth=4
    autocmd FileType go setlocal noexpandtab softtabstop=4 tabstop=4 shiftwidth=4

    set omnifunc=syntaxcomplete#Complete
    imap </: </<C-X><C-O>
