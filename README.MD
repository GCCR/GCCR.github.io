Website for the [GCCR](https://GCCR.github.io)

# Contributing to the website

## For authors

Coming soon

## For developers

1. **Setting up the environment**

Start by installing Jekyll and its dependencies by following the instructions [here](https://jekyllrb.com/docs/installation/)

For Ubuntu:
```shell
# install the dependencies
sudo apt-get install ruby-full build-essential zlib1g-dev
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
# install Jekyll
gem install jekyll bundler
```

You might need to update Ruby Gems and the bundler:
```shell
sudo gem update --system
bundle update --bundler
```

2. **Cloning the repository**
```shell
git clone https://github.com/GCCR/GCCR.github.io.git
git checkout dev
```
There are two branches on this repo: the `master` branch which is used to build the website.
Modifications on this branch will directly affect the website so push commits on this branch only after testing them locally.

The `dev` branch. When making changes, you should push your commits to this branch first, and then merge it with the master branch.

To switch between branches, use the `git checkout` command. To identify which branch you're working on, use `git branch`. To push your changes from `dev` to remote (GitHub) `dev` branch, use `git push -u origin dev`. Then you can merge `dev` to `master` through the GitHub interface.

3. **Running the website locally**

You'll need to install a few plugins first
```shell
cd GCCR.github.io
bundle install
```

You're done ! To run the server locally, type `bundle exec jekyll serve` and the default address should be [http://localhost:4000/](http://localhost:4000/)

I heavily suggest that you quickly go through [Jekyll's tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) to understand how the website is organized.