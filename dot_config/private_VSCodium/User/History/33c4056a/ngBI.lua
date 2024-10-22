return {
    'nvimdev/dashboard-nvim',  -- The plugin name
    event = 'VimEnter',  -- Load the dashboard when Neovim enters
    config = function()
      local db = require('dashboard')
  
      -- Custom ASCII Header (replace with your preferred ASCII art)
      db.custom_header = {
        "           ▄▄                                                      ",
        "▀███▀▀▀██▄ ██   ██                                                 ",
        "  ██    ██      ██                                                 ",
        "  ██    █████ ██████▀███▄███ ▄█▀██▄ ▀██▀   ▀██▀  ▄▄█▀██▀████████▄  ",
        "  ██▀▀▀█▄▄ ██   ██    ██▀ ▀▀██   ██   ██   ▄█   ▄█▀   ██ ██    ██  ",
        "  ██    ▀█ ██   ██    ██     ▄█████    ██ ▄█    ██▀▀▀▀▀▀ ██    ██  ",
        "  ██    ▄█ ██   ██    ██    ██   ██     ███     ██▄    ▄ ██    ██  ",
        "▄████████▄████▄ ▀████████▄  ▀████▀██▄    █       ▀█████▀████  ████▄",
        "                                                                   ",
        "                                                                   "
      }
    end,
  }
  