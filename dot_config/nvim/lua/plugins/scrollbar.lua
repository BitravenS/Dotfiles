local colors = require("tokyonight.colors").setup()

-- Scrollview color settings based on Tokyonight theme
vim.cmd([[
  highlight ScrollView guibg=]] .. colors.bg_highlight .. [[ guifg=]] .. colors.bg .. [[
]])

-- Return the plugin configuration
return {
  "dstein64/nvim-scrollview",
  opts = {
    excluded_filetypes = { 'nerdtree', 'undotree', 'startify' },
    current_only = true, -- Scrollbar only appears for the current window
  }
}
