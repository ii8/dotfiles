
set background=dark

"set ve=all "cursor can go where there are no characters
set cindent
set cinoptions=(0,u0
set hlsearch "hilight matches

set number "line numbers
set incsearch "match as typing search
set ignorecase "in search
set smartcase "casesensitive if search contains upper
"set textwidth=80
set ruler "show current line,column
"set lazyredraw
syntax on
filetype on
set omnifunc=syntaxcomplete#Complete
autocmd BufWinEnter * call matchadd('Todo', '\%>80v.\+', -1) "highlight text past col 80
match Todo /\s\+$/
set tags=./tags;/ "Search tags file up tree

source /home/murray/.config/vim/askapache
"source /home/murray/.config/vim/bubblegum
"source /home/murray/.config/vim/peaksea
