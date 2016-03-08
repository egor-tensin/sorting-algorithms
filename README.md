# Sorting algorithms

Getting the hang out of sorting algorithms.
Hosted on [GitHub Pages](https://pages.github.com) at
https://egor-tensin.github.io/sorting_algorithms/.

## Installation

[Jekyll](http://jekyllrb.com/) is used to build a set of static HTML pages from
a collection of templates and resources.
It might seem like Jekyll doesn't support Windows very well.
However, at the moment of writing one can get it to work using the excellent
tutorial at http://jekyll-windows.juthilo.com/.
I personally had no problems running Jekyll on Windows whatsoever.

I use [Bundler](http://bundler.io/) to manage project's dependencies.
Make sure you have the `bundler` gem installed; project dependencies can then
be installed by executing

    bundle install

in the project's root directory.

## Development

To run a local web server, execute

    bundle exec jekyll serve --watch --drafts --config _config.yml,_config_dev.yml

in the project's root directory.
You can then review your changes at http://localhost:4000/.

If you can't get Jekyll to properly `--watch` for file modifications on
Windows, try adding `--force_polling` to `jekyll`s options:

    bundle exec jekyll serve --watch --force_polling --drafts --config _config.yml,_config_dev.yml

It might still not work though, but you can always re-run `jekyll` manually.

Note that `_config_dev.yml` is included to rewrite some of the `site` fields
from `_config.yml` during development.
In particular, it

* sets `minified_externals` to `false` so that the properly formatted versions
  of external CSS stylesheets and JavaScript files are included instead of the
  `min`ified versions,
* sets `include_comments` to `false` to exclude the Disqus comments section
  from the posts,
* sets `baseurl` to an empty string so that the website can be accessed from
  local web server's root directory, instead of '/sorting_algorithms'.

## Accessing via file://

Jekyll doesn't provide native support for generating a static website which can
be viewed without a web server.
One easy workaround might be to `wget` the website and convert the links:

    wget -k -r http://localhost:4000/

## Licensing

This project, including all of the files and their contents, is licensed under
the terms of the MIT License.
See [LICENSE.txt](LICENSE.txt) for details.

This website is build upon the Twitter Bootstrap framework, which is also MIT
Licensed and copyright 2015 Twitter.

A MIT Licensed CSS style sheet from
https://github.com/mojombo/tpw/blob/master/css/syntax.css created by Tom
Preston-Werner is used for syntax highlighting.
