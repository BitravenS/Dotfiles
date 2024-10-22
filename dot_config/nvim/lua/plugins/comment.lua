return {
  "terrortylor/nvim-comment",
  keys = {
    { "gc", mode = "n" }, -- for normal mode
    { "gc", mode = "v" }, -- for visual mode
  },
  config = function()
    require("nvim_comment").setup({
      comment_empty = false, -- Don't comment empty lines
      -- Add any other configuration options as needed
    })
  end,
}
