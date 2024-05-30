# Practice Garage Setup

## Brew

The first thing you’re going to want to get to setup the project is Brew.
Brew is a package manager — a program to install other programs — and it
will make it very convenient for you to install the dependencies that
both this project and the main product will require.

The Brew installation instructions can be found [on their website][1] and
they’re extremely straight-forward.

Using Brew to install other programs is very easy:

```sh
# Install the programs ‘foo’ and ‘bar’
brew install foo bar
```

Before using brew it can be a good idea to *update* your sources to make
sure you have the latest versions of packages available for download, and
to *upgrade* to update all your installed packages to the latest
versions:

```sh
brew update
brew upgrade
```

[1]: https://brew.sh/

## Git

You should know what Git is.  If you don’t know what Git is you can
Google it.  You can install Git using Brew, and then use it to clone this
repository:

```sh
brew install git
git clone 'REPOSITORY URL'
```

## Node Version Manager (NVM) and Node Package Manager (NPM)

We use NodeJS for the frontend in both our main product as well as this
garage project, and specifically we use NodeJS Hydrogen (aka v18).  If
you simply installed NodeJS on your system then you would end up with the
latest version which is not what we want.  Instead we will use Node
Version Manager (NVM) to install the very specific version of NodeJS we
want.

Additionally we need Node Package Manager (NPM) to… manage packages.  You
should know what NPM is.

To install NVM simply follow the instructions on [their project page][2].
Like with Brew the instructions are very straight-forward and you should
be able to figure it out.

To install NPM simply use Brew:

```sh
brew install npm
```

Once both NVM and NPM are installed, we can now use NVM to install and
select our NodeJS version.  If you ever find that you are on the wrong
version of NodeJS for whatever reason, simply re-run the `nvm use`
command.

```sh
nvm install lts/hydrogen
nvm use lts/hydrogen
```

When working on a project, you can also use `npm` to install the projects
dependencies by issuing the following command:

```sh
npm install

# Or this; the same command but shorter
npm i
```

[2]: https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script

## Python

We use Python, you know Python, but you need the right version.  We use
Python3.9, and luckily Brew lets you get the specific version you need.

```
brew install python@3.9
```

## Virtual Env Wrapper

Python installs all dependencies globally, and this is really really
*really* bad.  If you aren’t careful you can royally fuck up your
environment.  Luckily we have virtual environments as a solution to this
problem.  Python ships with support for virtual environments out of the
box but they’re a bit clunkly.  For slightly better ergonomics we make
use of Virtual Env Wrapper to make our virtual environments.

You can install Virtual Env Wrapper with Brew:

```sh
brew install virtualenv virtualenvwrapper
```

Once that is installed, you need to source the `virtualenvwrapper.sh`
script.  This sets some environment variables in your shell, giving you
access to various functionality.  By default you need to do this each
time you start up your shell — which sucks — so instead you’re going to
source it in your shell startup script which is automatically executed
when you launch a new shell.

First you need to figure out what shell you’re using.  You will probably
be using either Bash or Zsh.  If you have a different shell you probably
know what you’re doing.  If you don’t know what you’re doing, you can run
the following:

```sh
[ -n "${BASH_VERSION}" ] && echo Bash
[ -n "${ZSH_VERSION}"  ] && echo Zsh
```

If you’re using Bash then your startup script will be located at
`~/.bash_profile`, and if you’re on Zsh then it will be located at
`~/.zshrc`.

Open your shells startup script with your preferred text editor, and
include the following lines:

```sh
. "$(brew --prefix)/bin/virtualenvwrapper.sh"
```

Now the next time you open a shell, you will have everything you need to
setup and use virtual environments.

If you want to make a virtual environment, you can issue the following
command:

```sh
mkvirtualenv -a . -p "$(which python3.9)" 'VIRTUAL ENVIRONMENT NAME'
```

Once a virtual environment has been created, the following commands are
good to know:

```sh
# Enter the specified virtual environment
workon 'VIRTUAL ENVIRONMENT NAME'

# Exit the current virtual environment
deactivate
```

## Pip

Once you have a virtual environment working, you will want to actually
install your dependencies, which in Python is done via Pip.  By
convention the projects you work on will have a `requirements.txt` file
listing their dependencies, and you can simply provide this file to Pip
to install the listed dependencies:

```sh
pip install -r requirements.txt
```

**Important Note!**

Once you get passed the garage project and begin to work on our product,
you will actually want to ignore the root `requirements.txt` and instead
use `app/requirements.txt`.

## Google Cloud SDK

The Google Cloud SDK is important for allowing us to do various tasks
such as deploying our code to test- and staging-environments, as well as
being able to run a datestore emulator.  To download the Google Cloud SDK
simply go to their [install page][3] and select the version that
corresponds to your machine.

Once you’ve downloaded and extracted the Google Cloud SDK, we want to
install it by using the provided script:

```sh
# I am assuming you’ve downloaded this to your home directory.  If you
# downloaded the GC SDK to elsewhere (like your Downloads/ folder) then
# you need to manually correct this path.
~/google-cloud-sdk/install.sh
```

Now that it’s all installed, we want to add the provided binaries to our
system PATH so we can use them from anywhere.  Add the following to your
shells startup script:

```sh
readonly GCLOUD_SDK=/path/to/google-cloud-sdk
# If you use Zsh, replace ‘bash’ in the file paths with ‘zsh’.
[ -f "$GCLOUD_SDK/path.bash.inc" ]       && . "$GCLOUD_SDK/path.bash.inc"
[ -f "$GCLOUD_SDK/completion.bash.inc" ] && . "$GCLOUD_SDK/completion.bash.inc"
```

At this point you can close your shell and open a new one so that your
environment is properly setup.  Once you’ve done that we need to install
the proper components for Google Cloud to function:

```sh
gcloud components install app-engine-python beta cloud-datastore-emulator
```

[3]: https://cloud.google.com/sdk/docs/install

---

## Project Initialization

Before you do anything you want to start the datastore.  This is where
all your data will be stored by the backend.  We can do this with gcloud:

```sh
gcloud beta emulators datastore start \
    --project practice-garage --host-port localhost:8000
```

After that, you need to run the script `dev_appserver.py`, which runs the
backend with the appropriate environment variables set:

```sh
./dev_appserver.py
```

Sadly Google did not include a datastore viewer in gcloud, but luckily
for us there is a package called [Datastore Emulator UI][4] (or DSUI for
short) to get this functionality back.  To install run the following:

```sh
npm i -g @streamrail/dsui
```

Then to run DSUI, run the following:

```sh
dsui -r practice-garage -e localhost:8000
```

[4]: https://github.com/streamrail/dsui
