select
      vendor_id
    , tag_metadata

from 
    tag

where
    tag_metadata@>'{"type": "jersey"}'

limit 10
