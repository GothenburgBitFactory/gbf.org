---
title: "Taskwarrior Performance Testing"
aliases:
- /projects/performance

---
# Taskwarrior Performance Testing

The performance charts are generated using [Google Charts](https://developers.google.com/chart), and represent the results from running `make performance` for a release build.
All times shown are microseconds (μs).
[The average human eye blink takes 350,000 μs](https://en.wikipedia.org/wiki/Millisecond).

The data used is the text of all the Shakespeare tragedies, with data manipulation that turns every spoken line into a task.
The result is a sample data set that includes 2,129 pending tasks and 5,957 completed tasks.
This yields an 8,086 task database.
This data is then queried twice to warm any caches.

The tests are all run on the same hardware, OS, and under similar load.
Because of this, any OS upgrade or new hardware requires all tests to be re-run, and sometimes this is not possible because of toolchain differences.
It is expected that there will be minor variations between tests.

Note: The 'other' category was introduced with 2.5.0 and represents the total runtime (launch to exit, measured internally), with all the other categories subtracted.
It therefore represents unmeasured time.
In the case of `export` and `import`, the 'other' category is significant.
With 2.5.0.beta3 the time spent converting tasks to JSON is counted as 'render' time.

## `All Tests Combined`

Aggregated time (in seconds) for all 20 tests, by version.
This total is measured externally, and therefore includes unmeasured time, and launch time.
{{< google_chart combined >}}

## `task next`
This test yields only the pending tasks.
This test is sensitive to changes in the `next` report definition.
{{< google_chart next >}}

## `task list`
This test yields only the pending tasks.
This test is sensitive to changes in the `list` report definition.
{{< google_chart list >}}

## `task all`
This test yields all pending and completed tasks.
This test is sensitive to changes in the `all` report definition.
{{< google_chart all >}}

## `task add`
This test adds a task with project, priority, tags and an average-sized description.
{{< google_chart add >}}

## `task export`
This test exports all 8,086 tasks to a JSON file.
Starting with task-2.5.0.beta3, time spent composing JSON is measured as 'render' time.
{{< google_chart export >}}

## `task import`
This test imports all 8,086 tasks from a JSON file.
The 'other' category represents mostly JSON parsing.
{{< google_chart import >}}
