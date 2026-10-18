vim.cmd("filetype plugin indent on")
vim.cmd("syntax enable")

local g = vim.g
local o = vim.o
local api = vim.api

g.maplocalleader = ","
o.number = true
o.relativenumber = true
o.showmatch = true
o.encoding = 'UTF-8'
o.clipboard = 'unnamedplus'
o.ignorecase = true
o.showcmd = true

o.shiftwidth = 4
o.tabstop = 4
o.softtabstop = 4

o.mouse = ""

-- VIMTEX
local g = vim.g
local map = vim.keymap

g.vimtex_view_method = "zathura"
g.vimtex_view_enabled = 1
g.vimtex_compiler_method = 'latexmk'
g.vimtex_compiler_latexmk = { 
	out_dir = "build",
	executable = "latexmk",
	options = { "-xelatex","-synctex=1","-interaction=nonstopmode","-file-line-error" },
}

vim.keymap.set('n','<localleader>v','<plug>(vimtex-view)')

vim.api.nvim_create_autocmd('FileType',{ pattern = 'tex', 
callback = function ()
	vim.opt.shiftwidth = 2 
	vim.keymap.set("","<F9>",'<esc>:w<CR>:VimtexCompile<CR>')
end
})

-- COC
local keyset = vim.keymap.set
keyset("n", "<localleader>a", "<Plug>(coc-codeaction-selected)")
keyset("n", "<localleader>l", ":CocCommand eslint.executeAutofix<CR>")
keyset("n", "gd", "<Plug>(coc-definition)", {silent = true})
keyset("n", "K", ":call CocActionAsync('doHover')<CR>", {silent = true, noremap = true})
keyset("n", "<leader>rn", "<Plug>(coc-rename)", {})
keyset("n", "<leader>f", ":CocCommand prettier.formatFile<CR>", {noremap = true})
keyset("i", "<C-Space>", "coc#refresh()", { silent = true, expr = true })
keyset("i", "<TAB>", "coc#pum#visible() ? coc#pum#next(1) : '<TAB>'", {noremap = true, silent = true, expr = true})
keyset("i", "<S-TAB>", "coc#pum#visible() ? coc#pum#prev(1) : '<C-h>'", {noremap = true, expr = true})
keyset("i", "<CR>", "coc#pum#visible() ? coc#pum#confirm() : '<C-G>u<CR><C-R>=coc#on_enter()<CR>'", {silent = true, expr = true, noremap = true})


