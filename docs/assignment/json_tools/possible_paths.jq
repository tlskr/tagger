#   Get all possible paths in a json file
#       https://github.com/stedolan/jq/issues/243 -- joelpurra

[
    path(..)
    | map(
        if type == "number" then
            "[]"
        else
            tostring
        end
    )
    | join(".")
    | split(".[]")
    | join("[]")
]
| unique
| map("." + .)
| .[]
