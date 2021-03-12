[![Build Status](https://travis-ci.com/hopex-hk/hopex_Python.svg?branch=main)](https://travis-ci.com/hopex-hk/hopex_Python)
# Hopex Python SDK 

This is Hopex Python SDK, you can import to your python project and use this SDK to query all market data, trading and manage your account. The SDK supports RESTful API invoking.

## Table of Contents

- [Quick Start](#Quick-Start)
- [Usage](#Usage)
    - [Folder structure](#Folder-structure)
    - [Run Examples](#Run-examples)
    - [Client](#client)
- [Request example](#Request-example)
    - [Reference data](#Reference-data)
    - [Market data](#Market-data)
    - [Account](#account)
    - [Wallet](#wallet)
    - [Trading](#trading)
    - [Margin Loan](#margin-loan)



## Quick Start

*The SDK is compiled by Python 3.7 and above*

You can download and open the source code directly in your python project, and then you can follow below steps:

* Create the client instance.
* Call the interfaces provided by client.

```python
# Create home client instance and get the index notify
home_client = HomeClient()
list_obj = home_client.get_index_notify()
LogInfo.output_list(list_obj)

# Create the market client instance and get the markets
market_client = MarketClient()
list_obj = market_client.get_markets()
LogInfo.output_list(list_obj)
```

## Usage

After above section, this SDK should be already download to your local machine, this section introduce this SDK and how to use it correctly.

### Folder structure

This is the folder and package structure of SDK source code and the description

- **Hopex**: The core of the SDK
  - **client**: The client that are responsible to access data, this is the external interface layer.
  - **connection**: Responsible to manage the remote server connection
  - **constant**: The constant configuration
  - **exception**: The wrapped exception
  - **service**: The internal implementation for each **client**.
  - **utils**:The utility classes, including signature, json parser, logging etc.
- **performance**: This is for internal performance testing
- **example**: The main package is defined here, it provides the examples how to use **client** instance to access API and read response.

### Run examples

This SDK provides examples that under **/example** folder, if you want to run the examples to access private data, you need below additional steps:

1. Create an **API Key** first from Hopex official website
2. Create **privateconfig.py** into your **Hopex** folder. The purpose of this file is to prevent submitting SecretKey into repository by accident, so this file is already added in the *.gitignore* file. 
3. Assign your API access key and secret key to as below:
```python
t_api_key = "hrf5gdfghe-e74bebd8-2f4a33bc-e7963"
t_secret_key = "fecbaab2-35befe7e-2ea695e8-67e56"
```

If you don't need to access private data, you can ignore the API key.

Regarding the difference between public data and private data you can find details in [Client](#Client) section below.

### Client

In this SDK, the client is the struct to access the Hopex API. In order to isolate the private data with public data, and isolated different kind of data, the client category is designated to match the API category. 

All the client is listed in below table. Each client is very small and simple, it is only responsible to operate its related data, you can pick up multiple clients to create your own application based on your business.

| Data Category | Client        | Privacy | API Protocol       |
| ------------- | ------------- | ------- | ------------------ |
| Market        | MarketClient  | Public  | Rest               |
| Home          | HomeClient    | Public  | Rest               |
| Account       | AccountClient | Private | Rest               |
| Wallet        | WalletClient  | Private | Rest               |
| Trade         | TradeClient   | Private | Rest               |



#### Customized Host
The client class support customized host so that you can define your own host, refer to example in later section.

#### Public and Private

There are two types of privacy that is correspondent with privacy of API:

**Public client**: It invokes public API to get public data (Home data and Market data), therefore you can create a new instance without applying an API Key.

```python
// Create a GenericClient instance
generic_client = GenericClient()

// Create a MarketClient instance with customized host
market_client = MarketClient(url="https://api2.hopex.com")
```

**Private client**: It invokes private API to access private data, you need to follow the API document to apply an API Key first, and pass the API Key to the init function

```python
// Create an AccountClient instance with APIKey
account_client = AccountClient(api_key=t_api_key, secret_key=t_secret_key)

// Create a TradeClient instance with API Key and customized host
trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key, url="https://api2.hopex.com")
```

The API key is used for authentication. If the authentication cannot pass, the invoking of private interface will fail.

#### Rest 

It invokes Rest API and get once-off response, it has two basic types of method: GET and POST

In this python SDK,  the method name are prefixed and can be easily identified, take TradeClient as an example, the method prefix and their examples are:

- **get**: get_kline, get_market_ticker
- **post**: post_create_order, post_cancel_order
- **req**: req_history_orders


## Request example

### Home data

#### Notify 

```python
home_client = HomeClient()
list_obj = home_client.get_index_notify()
```

#### Statistics

```python
home_client = HomeClient()
statistics = home_client.get_index_statistics()
```

### Market data

#### Kline

```python
market_client = MarketClient()
contract_code = 'BTCUSDT'
end_time = int(time.time())
before_24h = end_time - 60 * 60 * 24
list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_24h,
                                   interval=CandlestickInterval.MIN5)
```

#### Depth

```python
market_client = MarketClient()
list_obj = market_client.post_query_market_depth(contract_code='BTCUSDT', page_size=10)
```

#### Latest trade

```python
market_client = MarketClient()
list_obj = market_client.get_trades(contract_code='BTCUSDT', page_size=10)
```

### Account

*Authentication is required.*

#### User information

```python
account_client = AccountClient(api_key=t_api_key, secret_key=t_secret_key)
user_info = account_client.get_user_info()
```

### Wallet

*Authentication is required.*

#### User wallet

```python
wallet_client = WalletClient(api_key=t_api_key, secret_key=t_secret_key)
user_wallet = wallet_client.get_user_wallet()
```

#### Withdraw and deposit history

```python
wallet_client = WalletClient(api_key=t_api_key, secret_key=t_secret_key)
list_deposit_withdraw_history = wallet_client.get_deposit_withdraw(page=1, limit=10)
```

### Trading

*Authentication is required.*

#### Create order

```python
trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
res = trade_client.create_order(contract_code='BTCUSDT', side=OrderTradeType.BUY_LONG, order_quantity=10,
                                order_price=40000)
if res and len(res) and res.get('ret', -1) == 0:
    order_id = res.get('data', 0)
```

#### Cancel order

```python
trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
cancel_res = trade_client.cancel_order(contract_code='BTCUSDT', order_id=20210220)
```

#### Open orders 

```python
trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
list_Obj = trade_client.get_open_orders(contract_code='BTCUSDT')
```

#### Historical orders

```python
trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
contract_code_list = ['BTCUSDT', 'ETHUSDT']
type_list = []
list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=0,
                                             start_time=0,end_time=0, page=1, limit=10)
```



