---
title: "Clog - Download"
---

# How To Build Clog

This is for developers.
Specifically those who know how to use tools, satisfy dependencies, and want to set up a development environment.
It is not user-friendly.

You\'ll need these tools:

- [Git](https://git-scm.com/)
- [CMake](https://cmake.org)
- Make
- C++ compiler, currently gcc 4.7+ or clang 3.3+, for full C++11 support

## Downloading the Repo

The next step is to obtain the code.
This means getting the released tarball.
You can download the tarball with `curl`, as an example of just one of many ways to download the tarball.

```
$ curl -L -O https://github.com/GothenburgBitFactory/clog/releases/download/v{{< latest_version clog >}}/clog-{{< latest_version clog >}}.tar.gz
```

## Building the Tarball

Expand the tarball, build Clog, and install it.
This copies files into the right place, and installs the man page.

```
$ tar xzf clog-{{< latest_version clog >}}.tar.gz
$ cd clog-{{< latest_version clog >}}
$ cmake -DCMAKE_BUILD_TYPE=release .
...
$ make
...
$ sudo make install
```

## Submitting a Patch

[See here for details](/clog/docs/clone/#submitting-a-patch).
