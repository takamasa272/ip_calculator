# ip_calculator
IP アドレスの詳細を知りたくなって計算したいとき、いちいちブラウザで計算機を検索して、計算させていました。

その手間もめんどくさいし、ローカルでできたほうが色々良さそうということで CLI ツールにしました。

## USAGE
ターミナルで
```
ipcal 192.0.2.1/27
```
のように打つだけ．

裏では ipaddress オブジェクトが待ち構えているので、`192.0.2.1` でも、`192.0.2.1/255.255.253.0`、`3fff::1/64` とかでもOK（なはず）

### example
- `[ADDRESS]`: 入力アドレスについての情報、ホスト割当可能範囲などがでます
- `[BINARY]`: アドレスについての2進数表記がでます
- `[FLAGS]`: 当てはまる場合、以下のアドレスの属性がでます、[仕様はここを参照](https://docs.python.org/ja/3.11/library/ipaddress.html#ipaddress.IPv4Address.is_multicast)
    - private address
    - Global address
    - Link local address
    - Loopback address
    - Multicast address
    - Unspecified address
    - Reserved address
- `[Supplement]`: 補足情報がでます
    - `Integer`: 整数表記の場合
    - `PTR record`: 逆引きレコード名

```
> ipcal 192.0.2.1/27

[ADDRESS]
IP address : 192.0.2.1
Netmask    : 255.255.255.224
Hostmask   : 0.0.0.31
NW prefix  : 192.0.2.0/27

Network   : 192.0.2.0
Min host  : 192.0.2.1
Max host  : 192.0.2.30
Broadcast : 192.0.2.31

[BINARY]
IP address : 11000000.00000000.00000010.00000001
Netmask    : 11111111.11111111.11111111.11100000
Hostmask   : 00000000.00000000.00000000.00011111
NW prefix  : 11000000.00000000.00000010.00000000

[FLAGS]
Private address

[Supplement]
Integer : 3221225985
PTR record: 1.2.0.192.in-addr.arpa
```

## installation
### install
`pip`を使うことで，以下のコマンドで導入できます．(要`git`のインストール)

```
pip install git+https://github.com/takamasa272/ip_calculator
```
