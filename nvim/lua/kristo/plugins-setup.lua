local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end
local packer_bootstrap = ensure_packer()

-- Autocommand that reloads neovim whenever you save this file 
vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins-setup.lua source <afile> | PackerSync
  augroup end
]])

local status, packer = pcall(require, "packer")
if not status then
  return  
end

return packer.startup(function(use)
  use("wbthomason/packer.nvim")
  
  -- lua functions the many plugins use 
  use("nvim-lua/plenary.nvim")

  use("dracula/vim") -- colorscheme

  -- tmux & split window navigation
  use("christoomey/vim-tmux-navigator")

  use("szw/vim-maximizer") -- maximizes and restores current window

  -- essential plugins
  use("tpope/vim-surround")
  use("vim-scripts/ReplaceWithRegister")

  -- commenting with gc
  use("numToStr/Comment.nvim")

  -- file explorer
  use("nvim-tree/nvim-tree.lua")

  -- icons 
  use("kyazdani42/nvim-web-devicons")

  -- statusline
  use("nvim-lualine/lualine.nvim")

  -- fuzzy finding
  use({ "nvim-telescope/telescope-fzf-native.nvim", run = "make"})
  use({ "nvim-telescope/telescope.nvim", branch = "0.1.x" })

  -- autocompletion 
  use("hrsh7th/nvim-cmp")
  use("hrsh7th/cmp-buffer")
  use("hrsh7th/cmp-path")

  -- snippets
	use("L3MON4D3/LuaSnip") -- snippet engine
	use("saadparwaiz1/cmp_luasnip") -- for autocompletion
	use("rafamadriz/friendly-snippets") -- useful snippets

  -- managing & installing lsp servers, linters & formatters
	--use("williamboman/mason.nvim") -- in charge of managing lsp servers, linters & formatters
	--use("williamboman/mason-lspconfig.nvim") -- bridges gap b/w mason & lspconfig

  --use("neovim/nvim-lspconfig") -- easily configure language servers
  --se("hrsh7th/cmp-nvim-lsp") -- for autocompletion
  --use({ "glepnir/lspsaga.nvim", branch = "main" }) -- enhanced lsp uis
  --use("onsails/lspkind.nvim") -- vs-code like icons for autocompletion

  --Trying Coc.vim instaead of mason for lsp 
  use({'neoclide/coc.nvim', branch = 'release', run = ':CocUpdate'}) 

  -- treesitter configuration
	use({
		"nvim-treesitter/nvim-treesitter",
		run = function()
			require("nvim-treesitter.install").update({ with_sync = true })
		end,
	})

	-- auto closing
	use("windwp/nvim-autopairs") -- autoclose parens, brackets, quotes, etc...
	use({ "windwp/nvim-ts-autotag", after = "nvim-treesitter" }) -- autoclose tags

  -- Latex, VimTex
  use("lervag/vimtex")

  if packer_bootstrap then 
    require("packer").sync()
  end
end)
