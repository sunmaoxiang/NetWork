TCP 与 UDP的不同之处是TCP传送的是一个套接字，这样保证了信息的可靠传输。

```python
serverSocket.listen(n)  # n is the most number of connect.
```

这里是允许在一个时间可以有n个TCP连接。