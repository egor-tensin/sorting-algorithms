# Sorting algorithms

Getting the hang out of sorting algorithms.
Hosted on [GitHub Pages](https://pages.github.com) at https://egor-tensin.github.io/sorting_algorithms/.

## Installation

[Jekyll](http://jekyllrb.com/) is used to build a set of static HTML pages from a collection of templates and resources.
Jekyll doesn't support Windows, however at the moment of writing one can get it to work using the excellent tutorial at http://jekyll-windows.juthilo.com/.

I'm using [Bundler](http://bundler.io/) to set up a development environment.
After the `bundler` gem is installed, project dependencies can be installed by running

    bundle install

in the project's root directory.

## Development

To run a local web server, run

    bundle exec jekyll serve --watch --drafts --config _config.yml,_config_dev.yml

from the project's root directory.
You can then review your changes at http://localhost:4000/.

Please note that the support for `--watch`ing for modification on Windows is kind of iffy at the moment of writing.
One possible workaround is to add `--force_polling` to `jekyll`s options:

    bundle exec jekyll serve --watch --force_polling --drafts --config _config.yml,_config_dev.yml

It might still not work though, so you might end up having to re-run `jekyll` manually.
For details, refer to http://jekyll-windows.juthilo.com/4-wdm-gem/.

Note that `_config_dev.yml` is included to rewrite some of the `site` fields from `_config.yml` during development.
In particular, it

* sets `minified_externals` to `false` so that the properly formatted versions of external CSS stylesheets and JavaScript files are included instead of the `min`ified versions,
* sets `include_comments` to `false` to exclude the Disqus comments section from the posts,
* opts for the `rouge` gem for syntax highlighting instead of the default [Pygments](http://pygments.org/),
* sets `baseurl` to an empty string, pretending the website access from the root directory of a domain instead of from `sorting_algorithms/`.

## Licensing

This project, including all of the files and their contents, is licensed under the terms of the MIT License.
See LICENSE.txt for details.

This website is build upon the Twitter Bootstrap framework, which is also MIT Licensed and copyright 2015 Twitter.

A MIT Licensed CSS style sheet from https://github.com/mojombo/tpw/blob/master/css/syntax.css created by Tom Preston-Werner is used for syntax highlighting.
