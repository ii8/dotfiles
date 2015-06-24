
set background=dark

"set tabstop=4
"set shiftwidth=4 "auto indent width
"set expandtab
"set ve=all "cursor can go where there are no characters
set hlsearch "hilight matches

set number "line numbers
set incsearch "match as typing search
set ignorecase "in search
set smartcase "casesensitive if search contains upper
"set autoindent "this screws over when pasting
"set textwidth=80
set ruler "show current line,column
set lazyredraw
syntax on
filetype on
set omnifunc=syntaxcomplete#Complete
autocmd BufWinEnter * call matchadd('ErrorMsg', '\%>80v.\+', -1) "highlight text past col 80
match Todo /\s\+$/
set tags=./tags;/ "Search tags file up tree

source /home/murray/.config/vim/askapache
"source /home/murray/.config/vim/bubblegum
"source /home/murray/.config/vim/peaksea


