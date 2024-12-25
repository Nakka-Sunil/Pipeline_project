CREATE TABLE stock_data (
    trade_date VARCHAR2(20) NOT NULL,
    open_price NUMBER(10, 2),
    high_price NUMBER(10, 2),
    low_price NUMBER(10, 2),
    close_price NUMBER(10, 2),
    volume NUMBER,
    PRIMARY KEY (trade_date)
);

select * from stock_data;
