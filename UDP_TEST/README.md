UDPClient.py is a program for send message


I use a CentOS run UDPSserver.py then I can use UDPClient.py to send message and receive the MESSAGE

Q & A

UDP 和 TCP有什么区别

1、连接方面区别

TCP面向连接（如打电话要先拨号建立连接）。

UDP是无连接的，即发送数据之前不需要建立连接。

2、安全方面的区别

TCP提供可靠的服务，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达。

UDP尽最大努力交付，即不保证可靠交付。

3、传输效率的区别

TCP传输效率相对较低。

UDP传输效率高，适用于对高速传输和实时性有较高的通信或广播通信。

4、连接对象数量的区别

TCP连接只能是点到点、一对一的。

UDP支持一对一，一对多，多对一和多对多的交互通信。