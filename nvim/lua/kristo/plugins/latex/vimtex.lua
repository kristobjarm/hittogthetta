local g = vim.g

g.vimtex_view_general_viewer = 'okular'
g.vimtex_view_general_options = [[--unique file:@pdf\#src:@line@tex]]

--g.vimtex_view_viewer='mupdf'
g.vimtex_quickfix_mode=1

g.vimtex_compiler_latexmk = {
  build_dir = 'build',
    options = {
      '-shell-escape',
  },
}
--g.Tex_DefaultTargetFormat='pdf'

-- g.vimtex_compiler_latexmk = {
--   build_dir = 'build',
--   name = 'latexmk',
--   callback = 1,
--   continuous = 1,
--   executable = 'latexmk',
--     options = {
--       '-shell-escape',
--       '-pdflatex',
--       '-verbose',
--       '-file-line-error',
--       '-synctex=1',
--       '-interaction=nonstopmode',
--   },
-- }

-- spelling 
--vim.opt_local.spell = true
--vim.opt.spelllang = "en_us"

-- keymap for spelling 
--vim.keymap.set('i', '<C-l>', [[<C-g>u<Esc>[s1z=`]a<c-g>u]])

-- filetype plugin indent on
-- syntax enable 
--
-- set conceallevel=0
-- set number
-- set backspace=indent,eol,start "Fixes the backspace
-- set foldlevel=99
-- set foldmethod=indent "fold your code.

