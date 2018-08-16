-- fails on present data because data is not load as an array

select
      tag_id
    , tag_metadata->1 as second_item

from 
    tag

limit 10;
