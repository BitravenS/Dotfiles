return {
  "nvim-neo-tree/neo-tree.nvim",

  opts = {
    filesystem = {
      filtered_items = {
        visible = true, -- Show all items (including dotfiles)
        show_hidden_count = true, -- Show count of hidden files
        hide_dotfiles = false, -- Should be false to show dotfiles
        hide_gitignored = false, -- Make sure this is false to include gitignored files
        dotfiles = true, -- Show dotfiles explicitly
        custom = { ".git" }, -- Ignore the .git directory if needed

        hide_by_name = {
          -- Uncomment to hide specific files if needed
        },
        never_show = {},
      },
      sorting = {
        sort_by = "name", -- Sort files alphabetically
      },
    },
  },
}
