CREATE TABLE stock_data (
    stock_id BIGINT PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    open NUMERIC(15, 6),
    high NUMERIC(15, 6),
    low NUMERIC(15, 6),
    close NUMERIC(15, 6),
    adj_close NUMERIC(15, 6),
    volume BIGINT
);

CREATE TABLE crypto_data (
    crypto_id BIGINT PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    open NUMERIC(15, 6),
    high NUMERIC(15, 6),
    low NUMERIC(15, 6),
    close NUMERIC(15, 6),
    adj_close NUMERIC(15, 6),
    volume BIGINT
);

CREATE TABLE currency_data (
    currency_id BIGINT PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    date DATE NOT NULL,
    open NUMERIC(15, 6),
    high NUMERIC(15, 6),
    low NUMERIC(15, 6),
    close NUMERIC(15, 6),
    adj_close NUMERIC(15, 6),
    volume BIGINT
);
