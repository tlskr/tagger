-- fails on present data because data is not loaded as an array

select
    tag_metadata->0 as first_item

from 
    tag

where
    tag_metadata::text != '{}'

limit 10
