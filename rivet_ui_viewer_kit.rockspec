package = "rivet-ui-viewer-kit"
version = "0.1-1"
source = { url = "." }
description = { summary = "Develop a Lua command-oriented project for viewer scenarios with bounded scenario files, conflict explanations, and explicit failure cases.", license = "MIT" }
build = { type = "builtin", modules = { policy = "src/policy.lua" } }
