CREATE TABLE nab_ventures_deals_done
(
        company_name    VARCHAR(250),
        deal_done_Date  DATE,
        invested_in     VARCHAR(1000),
        aud_invested    REAL
) ;


CREATE TABLE nab_ventures_deals_leveraged
(
        company_name            VARCHAR(250),
        deal_dleveraged_Date    DATE,
        leverage_desc           VARCHAR(1000)
) ;

