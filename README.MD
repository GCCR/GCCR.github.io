[![GitHub Pages build status](https://github.com/GCCR/GCCR.github.io/workflows/Build%20and%20deploy%20Jekyll%20site%20to%20GitHub%20Pages/badge.svg)](https://github.com/GCCR/GCCR.github.io/actions)

# ~ Official website of the [GCCR](https://GCCR.github.io) ~

## Contributing to the website

:point_right: To add new survey links, edit [_data/survey-links.yml](./_data/survey-links.yml) and **be careful with the indentation !**

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
cd GCCR.github.io
```
The `master` branch is used to build the website.
Modifications on this branch will directly affect the website so push commits on this branch only after testing them locally.

When making big changes, you should push your commits to a new branch, then open a pull-request so that it can be reviewed by others. Once approved, your branch will be merged with the master branch which will automatically trigger an update of the website.

A few reminders about `git`:
* To identify which branch you're working on, use `git branch`.
* To switch between branches, use the `git checkout` command.
* If you realize too late that you've started working on the `master` branch instead of a new branch, you can move your changes to a new branch with the `git switch -c my-new-branch` command. 
* To push your changes from a branch `new-branch` to GitHub, use `git push -u origin new-branch`. 

3. **Running the website locally**

You'll need to install a few plugins first
```shell
bundle install
```

You're done ! To run the server locally, type `bundle exec jekyll serve` and the default address should be [http://localhost:4000/](http://localhost:4000/)

I heavily suggest that you quickly go through [Jekyll's tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) to understand how Jekyll works.

4. **Organization of the repo**

* `surveys` folder: all the translations for the surveys pages are located here
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

