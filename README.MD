# ~ Official website of the [GCCR](https://GCCR.github.io) ~

## Contributing to the website

:point_right: To add new survey links, edit [_data/survey-links.yml](./_data/survey-links.yml) and **be careful with the indentation !**

### *For authors*

Coming soon!

### *For developers*

1. **Setting up the environment**

Start by installing Jekyll and its dependencies by following the instructions [here](https://jekyllrb.com/docs/installation/)

We recommend you to update Ruby Gems and the bundler after that:
```shell
gem update --system
bundle update --bundler
```

2. **Cloning the repository**
```shell
git clone https://github.com/GCCR/GCCR.github.io.git
git checkout dev
```
There are two branches on this repo: the `master` branch which is used to build the website.
Modifications on this branch will directly affect the website so push commits on this branch only after testing them locally.

The `dev` branch. When making big changes, you should push your commits to this branch first, and then merge it with the master branch.

* To switch between branches, use the `git checkout` command. 
* To identify which branch you're working on, use `git branch`. 
* To push your changes from `dev` to remote (GitHub) `dev` branch, use `git push -u origin dev`. 

Then the admin's will merge `dev` to `master` through the GitHub interface.

3. **Running the website locally**

You'll need to install a few plugins first
```shell
cd GCCR.github.io
bundle install
```

You're done ! To run the server locally, type `bundle exec jekyll serve` and the default address should be [http://localhost:4000/](http://localhost:4000/)

I heavily suggest that you quickly go through [Jekyll's tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) to understand how Jekyll works.

4. **Organization of the repo**

* `_data` folder
  These files should **NOT** be modified manually, **except**:
  * To modify the links of the navigation bar, edit [_data/navigation.yml](./_data/navigation.yml)
  * To add new survey links, edit [_data/survey-links.yml](./_data/survey-links.yml)
* `_includes` folder: all the repetitive HTML code (navigation bar, footer, contact form...*etc*.) is gathered here
* `_layouts` folder: contains templates for the website pages (a default layout shared by every page, and a template for blog posts which inherits from the default one)
* `_posts` folder: where blog/news posts will be located. :warning: All files in this folder should be named `YYYY-MM-DD-short-title.md`. The format used by these files is [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), but you can also use plain HTML if you're comfortable with it. The front-matter at the begining of each .md file is used to specify the author and the title (and maybe more things later). You can use a custom alias for the author name by creating a new entry in [_data/authors.yml](./_data/authors.yml). If you don't want to create an entry, simply type you full name, and it will use the default GCCR avatar and link the GCCR Twitter instead of your own.
* `_sass` folder: contains custom SCSS files.
* `_scripts` folder: scripts to automatically generate some files (for now, the members map and listing)
* `assets` folder: all images, javascript resources, css stylesheets...*etc*. are located here
* `news` folder: contains the front page for the blog/news section.
* `_config.yml` file: the configuration file read by Jekyll. This is where you configure the default layouts used by each page, permalinks, plugins for SEO...*etc*. You can access the value of any variable in this file through `{{ site.my_variable }}` in your HTML code.
