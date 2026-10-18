local map = vim.keymap
vim.g.mapleader = ","

map.set('n','<C-n>',':Neotree toggle<CR>')

vim.cmd('nnoremap <c-z> <nop>')

map.set('n','<C-j>','<C-w>j')
map.set('n','<C-k>','<C-w>k')
map.set('n','<C-h>','<C-w>h')
map.set('n','<C-l>','<C-w>l')
