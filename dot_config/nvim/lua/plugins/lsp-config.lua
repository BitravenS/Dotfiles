return {
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({
        ensure_installed = {
          "lua_ls", -- Lua
          "rust_analyzer", -- Rust
          "bashls", -- Bash
          "clangd", -- C/C++
          "glint", -- Glimmer/Ember.js
          "jsonls", -- JSON
          "jdtls", -- JAVA
          "marksman", -- Markdown
          "pylsp", -- Python
          "cssls", -- CSS
        },
      })
    end,
  },
  {
    "neovim/nvim-lspconfig",
    lazy = false,
    config = function()
      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      local lspconfig = require("lspconfig")

      -- Lua LSP setup
      lspconfig.lua_ls.setup({ capabilities = capabilities })

      -- Rust Analyzer setup
      lspconfig.rust_analyzer.setup({ capabilities = capabilities })

      -- Bash LSP setup
      lspconfig.bashls.setup({ capabilities = capabilities })

      -- Clangd (C/C++) setup
      lspconfig.clangd.setup({ capabilities = capabilities })

      -- Java LSP setup
      lspconfig.jdtls.setup({ capabilities = capabilities })

      -- Glint (Glimmer/Ember.js) setup
      lspconfig.glint.setup({ capabilities = capabilities })

      -- JSON LSP setup
      lspconfig.jsonls.setup({ capabilities = capabilities })

      -- Marksman (Markdown) LSP setup
      lspconfig.marksman.setup({ capabilities = capabilities })

      -- Python LSP (pylsp) setup
      lspconfig.pylsp.setup({ capabilities = capabilities })

      -- CSS LSP setup
      lspconfig.cssls.setup({ capabilities = capabilities })
    end,
  },
}
