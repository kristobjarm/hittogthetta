call plug#begin('~/.local/share/nvim/plugged')
Plug 'lervag/vimtex'
Plug 'SirVer/ultisnips'
Plug 'jiangmiao/auto-pairs' 
call plug#end()


let g:tex_flavor='latex'
" let g:tex_program_pdfmode='pdflatex'
let g:vimtex_view_method='skim'
let g:vimtex_view_skim_sync = 1
let g:vimtex_view_skim_activate = 1
let g:vimtex_quickfix_mode=1
"let g:tex_conceal='abdmg'

let g:Tex_DefaultTargetFormat='pdf'

let g:vimtex_compiler_latexmk = {
	\ 'build_dir' : 'build',
	\ 'name' : 'latexmk',
	\ 'callback' : 1,
	\ 'continuous': 1,
     	\ 'executable' : 'latexmk',
     	\ 'options' : [
      	\   '-shell-escape',
	\   '-pdflatex',
      	\   '-verbose',
      	\   '-file-line-error',
     	\   '-synctex=1',
      	\   '-interaction=nonstopmode',
      \ ],
    \}

let g:UltiSnipsExpandTrigger='<Tab>'
let g:UltiSnipsJumpForwardTrigger='<Tab>'
let g:UltiSnipsJumpBackwardTrigger='<S-Tab>'
let g:AutoPairsFlyMode = 0
let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/nvim/UltiSnips']

filetype plugin indent on
syntax enable 

set conceallevel=0
set number
set backspace=indent,eol,start "Fixes the backspace
set foldlevel=99
set foldmethod=indent "fold your code.

setlocal spell
set spelllang=en_us
inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u
