# Minitalk

![42 School](https://img.shields.io/badge/42-School-blue)

A small data exchange program using UNIX signals - 42 Project

## 📋 Project Overview

This project is part of the 42 School curriculum. The goal is to code a small data exchange program using UNIX signals. It consists of a client and server that communicate with each other using only SIGUSR1 and SIGUSR2 signals.

## ✨ Features

- Server starts and displays its PID
- Client takes two parameters: server PID and a string to send
- Client sends the string to the server using only SIGUSR1 and SIGUSR2 signals
- Server receives the string and displays it
- Support for Unicode characters (bonus part)
- Signal acknowledgment from server to client (bonus part)

## 📦 Installation

```bash
git clone https://github.com/kaisen1337/minitalk.git
cd minitalk
make
```

## 🚀 Usage

### Starting the server
```bash
./server
```
The server will display its PID.

### Sending a message from client
```bash
./client [SERVER_PID] [MESSAGE]
```

### Example
```bash
$ ./server 
Server PID: 12345

# In another terminal
$ ./client 12345 "Hello from 42!"
```

## 📐 Implementation

- Uses SIGUSR1 and SIGUSR2 to transmit binary data
  - SIGUSR1 represents binary 0
  - SIGUSR2 represents binary 1
- Each character is converted to binary (8 bits)
- For bonus: supports Unicode characters (up to 32 bits)
- For bonus: server acknowledges receipt of messages

## 🧪 Testing

To test the program, try sending:
- Short strings
- Long strings
- Empty strings
- Strings with special characters
- Strings with Unicode characters

## 🛡️ Error Handling

The program handles various error cases:
- Invalid PID
- Failed signal sending
- Memory allocation errors

## 📚 Resources

- [UNIX Signals Documentation](https://man7.org/linux/man-pages/man7/signal.7.html)
- [42 Documentation](https://cdn.intra.42.fr/pdf/pdf/91836/en.subject.pdf)

## ⚖️ License

This project is part of the curriculum of 42 School. Please check their policy for details.

---
Made by kaisen1337
Last updated: 2025-02-27
