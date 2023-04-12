# this script is used to refresh the compile_commands.json file, which is used by clangd for code completion
bazel run @hedron_compile_commands//:refresh_all