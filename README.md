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

    bundle exec jekyll serve --baseurl '' --watch --drafts

from the project's root directory.
You can then review your changes at http://localhost:4000/.

To exclude the comments section, include the `_config-exclude-comments.yml` configuration file using

    bundle exec jekyll serve --baseurl '' --watch --drafts --config _config.yml,_config-exclude-comments.yml

Please note that the support for `--watch`ing for modification on Windows is kind of iffy at the moment of writing.
One possible workaround is to add `--force_polling` to `jekyll`s options:

    bundle exec jekyll serve --baseurl '' --watch --force_polling --drafts --config _config.yml,_config-exclude-comments.yml

It might still not work though, so you might end up having to re-run `jekyll` manually.
For details, refer to http://jekyll-windows.juthilo.com/4-wdm-gem/.

I'm also using the `rouge` gem for syntax highlighting during development instead of [Pygments](http://pygments.org/).
The reason for this was that Pygments required Python 2 to be installed, while I'm trying to switch to Python 3 completely.
The downside is that at the moment of writing GitHub Pages only supported Pygments, so I had to include a separate configuration file `_config-rouge.yml` during development.

To sum up, on Linux use

    bundle exec jekyll serve \
        --baseurl '' \
        --watch \
        --drafts \
        --config _config.yml,_config-exclude-comments.yml,_config-rouge.yml

and on Windows (hoping for the best) use

    bundle exec jekyll serve ^
        --baseurl '' ^
        --watch --force_polling ^
        --drafts ^
        --config _config.yml,_config-exclude-comments.yml,_config-rouge.yml

to run a local web server.

## Licensing

This project, including all of the files and their contents, is licensed under the terms of the MIT License.
See LICENSE.txt for details.

This website is build upon the Twitter Bootstrap framework, which is also MIT Licensed and copyright 2015 Twitter.

A MIT Licensed CSS style sheet from https://github.com/mojombo/tpw/blob/master/css/syntax.css created by Tom Preston-Werner is used for syntax highlighting.
