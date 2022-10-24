Telescope works, however NEEDS "ripgrep" and optionally "fd" to be installed. Easiest through Chocolatey 
or Homebrew. Think those are the only two external dependancies. Could be wrong. 

Minimal setup if the lsp. Most everything is in place however python support does for some reason not work.
Throws the error that npm.cmd executable not found. Could be installed through Nodejs but that seems to be 
a lousy work around. 

Latex lsp support should be configured. Not tested. Needs a compiler and implimentation of latex specific 
snippets. Live preview through some pdf viewer should also be added. Insperation for this can be found at:
https://github.com/SirCharlieMars/dotfiles/tree/master/.local

The setup is copied from: https://www.youtube.com/watch?v=vdn_pKJUda8&t=3308s&ab_channel=JoseanMartinez
and https://github.com/josean-dev/dev-environment-files/tree/main/.config/nvim
Type and javascript lsp has been removed from my nvim setup.

Added "spacebar" as extra leader key. Currently working keybinds for the specific setup are: 

"MODE", "KEYBIND", "ACTION"
---------------------
-- General Keymaps
---------------------

-- use jk to exit insert mode
"i", "jk", "<ESC>"

-- clear search highlights
"n", "<leader>nh", ":nohl<CR>"

-- delete single character without copying into register
"n", "x", '"_x"

-- increment/decrement numbers
"n", "<leader>+", "<C-a>" -- increment
"n", "<leader>-", "<C-x>" -- decrement

-- window management
"n", "<leader>sv", "<C-w>v" -- split window vertically
"n", "<leader>sh", "<C-w>s" -- split window horizontally
"n", "<leader>se", "<C-w>=" -- make split windows equal width & height
"n", "<leader>sx", ":close<CR>" -- close current split window

"n", "<leader>to", ":tabnew<CR>" -- open new tab
"n", "<leader>tx", ":tabclose<CR>" -- close current tab
"n", "<leader>tn", ":tabn<CR>" --  go to next tab
"n", "<leader>tp", ":tabp<CR>" --  go to previous tab

----------------------
-- Plugin Keybinds
----------------------

-- vim-maximizer
"n", "<leader>sm", ":MaximizerToggle<CR>" -- toggle split window maximization

-- nvim-tree
"n", "<leader>e", ":NvimTreeToggle<CR>" -- toggle file explorer

-- telescope
"n", "<leader>ff", "<cmd>Telescope find_files<cr>" -- find files within current working directory, respects .gitignore
"n", "<leader>fs", "<cmd>Telescope live_grep<cr>" -- find string in current working directory as you type
"n", "<leader>fc", "<cmd>Telescope grep_string<cr>" -- find string under cursor in current working directory
"n", "<leader>fb", "<cmd>Telescope buffers<cr>" -- list open buffers in current neovim instance
"n", "<leader>fh", "<cmd>Telescope help_tags<cr>" -- list available help tags

-- restart lsp server (not on youtube nvim video)
"n", "<leader>rs", ":LspRestart<CR>" -- mapping to restart lsp if necessary


---------
-- LSP --
---------

"n", "gf", "<cmd>Lspsaga lsp_finder<CR>" -- show definition, references
"n", "gD", "<Cmd>lua vim.lsp.buf.declaration()<CR>" -- got to declaration
"n", "gd", "<cmd>Lspsaga peek_definition<CR>" -- see definition and make edits in window
"n", "gi", "<cmd>lua vim.lsp.buf.implementation()<CR>" -- go to implementation
"n", "<leader>ca", "<cmd>Lspsaga code_action<CR>" -- see available code actions
"n", "<leader>rn", "<cmd>Lspsaga rename<CR>" -- smart rename
"n", "<leader>d",  "<cmd>Lspsaga show_line_diagnostics<CR>" -- show  diagnostics for line
"n", "<leader>d", "<cmd>Lspsaga show_cursor_diagnostics<CR>" -- show diagnostics for cursor
"n", "[d", "<cmd>Lspsaga diagnostic_jump_prev<CR>" -- jump to previous diagnostic in buffer
"n", "]d", "<cmd>Lspsaga diagnostic_jump_next<CR>" -- jump to next diagnostic in buffer
"n", "K", "<cmd>Lspsaga hover_doc<CR>" -- show documentation for what is under cursor
"n", "<leader>o", "<cmd>LSoutlineToggle<CR>" -- see outline on right hand side

-- keybinds for navigation in lspsaga window
move_in_saga: prev = "<C-k>", next = "<C-j>" 
-- use enter to open file with finder
finder_action_keys: open = "<CR>",
-- use enter to open file with definition preview
definition_action_keys: edit = "<CR>",

