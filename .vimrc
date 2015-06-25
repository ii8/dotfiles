
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
autocmd FocusLost * :set number
autocmd WinLeave * :set number
autocmd WinEnter * :set relativenumber
autocmd InsertEnter * :set number
autocmd InsertLeave * :set relativenumber
"autocmd CursorMoved * :set relativenumber

"normal numbers when jumping greater distance
nnoremap <silent> <C-u> <C-u>:set<Space>number<cr>
nnoremap <silent> <C-d> <C-d>:set<Space>number<cr>
nnoremap <silent> <C-f> <C-f>:set<Space>number<cr>
nnoremap <silent> <C-b> <C-b>:set<Space>number<cr>
nnoremap <silent> n n:set<Space>number<cr>
nnoremap <silent> N N:set<Space>number<cr>

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
"TODO wite tags on save

"scary remaps
inoremap <C-j> <C-n>
inoremap <C-k> <C-p>

source /home/murray/.config/vim/askapache
"source /home/murray/.config/vim/bubblegum
"source /home/murray/.config/vim/peaksea
