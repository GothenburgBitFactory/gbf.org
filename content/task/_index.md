---
title: "Taskwarrior"
lang: en
layout: single
description: "A command-line todo list manager."
homepage: "https://taskwarrior.org"
source: "https://github.com/GothenburgBitFactory/taskwarrior"
rank: 2754
menu: main
aliases:
    - /projects/taskwarrior
---
# Taskwarrior

Taskwarrior is a command-line todo list manager.

It maintains a task list, allowing you to add/remove, and otherwise manipulate your tasks.
Taskwarrior has a rich set of subcommands that allow you to do sophisticated things.
You'll find it has customizable reports, charts, GTD features, device syncing, documentation, extensions, themes, holiday files and much more.

* `git clone https://github.com/GothenburgBitFactory/taskwarrior.git`
* `brew install task`
* [Support website](https://taskwarrior.org)
* [Performance Testing](/task/performance)
* [Talks](talks) given at UBUCON
* [RFCs](https://github.com/GothenburgBitFactory/taskwarrior/blob/develop/doc/devel/rfcs/)
* [What is the latest version?](/task/latest)
* [Future plans](https://github.com/GothenburgBitFactory/taskwarrior/blob/develop/doc/devel/rfcs/plans.md)
* [Download](https://taskwarrior.org/download)

## About

Originally named `task`, the project began as a C++ demo of a todo.sh lookalike in November 2006.
This was so that features could be added that were not easily done using shell scripts, such as text formatting and color rules.
The demo needed autoconf, portability, testing and documentation, and after a lengthy effort, version 1.0.0 was released in June 2008.

Since 2006, Taskwarrior has been used in the development of ... Taskwarrior.
[Dogfood](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

Many subsequent releases have been made.
Taskwarrior has been incorporated into almost all Linux distros and Cygwin, gained man pages, online documentation, and a bug list.
Hundreds of bugs and features have been addressed, by over a hundred contributors.
There is an active IRC channel and forum.

## Testing

Taskwarrior undergoes continuous integration testing using GitHub Actions.
The test suite has almost 10,000 unit tests.
