
set background=dark

"set ve=all "cursor can go where there are no characters
set cindent
set cinoptions=(0,u0
"set cinoptions+=:0 "linux kernel style switch

set hlsearch "hilight matches
set incsearch "match as typing search
set ignorecase "in search
set smartcase "casesensitive if search contains upper

set relativenumber "line numbers
set ruler "show current line,column

"set textwidth=80
"set lazyredraw
syntax on
filetype on
filetype plugin on
set autochdir
set omnifunc=syntaxcomplete#Complete
"autocmd BufWinEnter * call matchadd('Todo', '\%>80v.\+', -1) "highlight text past col 80
set colorcolumn=80
match Todo /\s\+$/
set tags=./tags;/ "Search tags file up tree

"scary remaps
inoremap <C-j> <C-n>
inoremap <C-k> <C-p>

source /home/murray/.config/vim/askapache
"source /home/murray/.config/vim/bubblegum
"source /home/murray/.config/vim/peaksea
