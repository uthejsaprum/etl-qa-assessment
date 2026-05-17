select
    ad_id,
    round(
        coalesce(
            (
                (
                    sum(
                        case
                            when action = 'Clicked' then 1
                            else 0
                        end
                    ) + 0.0
                ) * 100 / nullif(
                    sum(
                        case
                            when action in ('Clicked', 'Viewed') then 1
                            else 0
                        end
                    ),
                    0
                )
            ),
            0
        ),
        2
    ) as ctr
from
    ads
group by
    ad_id
order by
    ctr desc,
    ad_id