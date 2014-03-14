" Support for coloring latex source that uses ttquot.
" Put this in your .vimrc:
" au BufNewFile,BufReadPost *.tex              so $HOME/.../ttquot.vim
" 
" where the ... is chosen appropriately.
"
so $VIM/syntax/tex.vim
syn match noquotes "[^\"]+"
syn match nous "[^_]+"
syn region codeString	start=+"+ end=+"+ contains=noquotes
syn region italics	start=+_+ end=+_+ contains=nous
hi link codeString Statement
hi link italics Type
