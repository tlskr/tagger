select 
    *
from
    tag
where
    tag_metadata::text != '{}'
limit 10
