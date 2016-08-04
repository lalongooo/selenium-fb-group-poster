Selenium Facebook Group Poster
===================
**A Selenium Script to post an image with text on the Facebook Groups you are member.**

Setup
----------

 - Verify you have Python 2.7.x installed
``` shell
$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
 - Install [pip](https://pip.pypa.io/en/stable/installing/)
 - Install python [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not required but strongly    recommended).
``` shell
$ pip install virtualenv
```
 - Create your virtual environment
``` shell
$ virtualenv venv
```
 - Activate your virtual environment
``` shell
$ source venv/bin/activate
```
 - Install [Python bindings for Selenium](https://pypi.python.org/pypi/selenium)
``` shell
$ (venv) pip install selenium
```
 - Clone this repo
``` shell
git clone https://github.com/lalongooo/selenium-fb-group-poster
```
 - Move to the `selenium-fb-group-poster`

``` shell
$ (venv) cd selenium-fb-group-poster
```
Configure the script and enjoy!
----------

There is a `main` method in the script, you need to edit and provide your Facebook user and password, the message you want to post, whether you want to attache an image, along within its path and the links of the Facebook Groups you are member of:
``` shell 
 def main():

	# Your Facebook account user and password
	usr = ""
	pwd = ""
	message = "Checkout an amazing selenium script for posting in Facebook Groups!\nhttps://github.com/lalongooo/selenium-fb-group-poster"
	attach_image = True
	image_path = "/path/to/the/photo/you/want/to/upload"
	group_links = [
		# Your Facebook Groups links.
		# IMPORTANT: You must be a member of the group, being ADMIN nor required.
		"https://www.facebook.com/groups/ayearofrunning/", # A group of Mark Zuckerberg
	]
 ```

 Run the script
``` shell
$ (venv) python fbposter.py
```

 
To do:
----------
 - Provide parameters via the command line instead of editing the script.
 - Improve/add exception handling
 - ???

License
----------

This project is licensed under the [MIT license](LICENSE).

Questions?
----------

If you have any questions, please feel free to email me at hdez.jeduardo@gmail.com, or better yet, [fill out an issue](https://github.com/lalongooo/selenium-fb-group-poster/issues/new) so everyone can benefit from what's your question about.
