-- import mason plugin safely
local mason_status, mason = pcall(require, "mason")
if not mason_status then
	return
end

-- import mason-lspconfig plugin safely
local mason_lspconfig_status, mason_lspconfig = pcall(require, "mason-lspconfig")
if not mason_lspconfig_status then
	return
end


-- enable mason
mason.setup()

mason_lspconfig.setup({
	-- list of servers for mason to install
	ensure_installed = {
    "clangd",   -- c++
    --"dockerls", -- docker
    "julials",  --julia
    "ltex",     --latex language server
    "texlab",
    --"pyright",  --python 
    "sumneko_lua", --lua
    -- should also be configured in the lspconfig file
    -- maybe something for markdown? 
	},
	-- auto-install configured servers (with lspconfig)
	automatic_installation = true, -- not the same as ensure_installed
})


