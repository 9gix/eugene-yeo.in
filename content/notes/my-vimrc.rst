My .vimrc file
==============

.. code-block:: vim

    execute pathogen#infect()
    execute pathogen#helptags()
    syntax on
    filetype plugin indent on

    autocmd FileType ruby,html setlocal expandtab softtabstop=2 tabstop=2 shiftwidth=2
    autocmd FileType python,rst,javascript,css setlocal expandtab softtabstop=4 tabstop=4 shiftwidth=4
    autocmd FileType go setlocal noexpandtab softtabstop=4 tabstop=4 shiftwidth=4

    set softtabstop=4
    set shiftwidth=4
    set tabstop=4

    set omnifunc=syntaxcomplete#Complete
    imap </: </<C-X><C-O>

    "set colorcolumn to 80 character limit
    set cc=80
