Why VIM?
=======

This presentation doesn't aim to teach you how to use VIM, rather, I want to
explain and show why in the world you'd want to use a 25 year old command line
text editor over whatever it is you're using now.

I've been coding professionally in some form since 1999, starting at the very
beginning, there were lots of recommendations for using VIM, from blog posts,
from colleagues, etc.  Although I used VIM for editing configuration files on
Linux, it wasn't until 2006 that I started seriously investigating it as my
main text editor for programming.  The reasons for the delay were many, but
largely it came down to the following few items:

1. It was ugly.
2. It was not a GUI application.
3. I could not understand how navigating code (especially in a large project
   with many files) could possibly be faster using the keyboard than it could
   be with the mouse.

Number 3 is the big one.  There's something to be said about the precision you
can have with the mouse - you look on the screen, and you click where you want
to the cursor to go.  I could not fathom how you could get this precision in
VIM.  It turns out, however, that this is just not the way to approach VIM at
all.  You have to just trust that the creators and 25 years of history have
created an alternate way to do things, quickly, and in a unique way.

The fact is, constantly reaching for your mouse to do things when you don't
have to slows you down.  Think about how often you reach for your mouse as
you're coding?  What if you could do the exact same thing, in most cases,
without leaving the home row on your keyboard?  Would it make you faster?

You cannot get the most out of VIM without committing to this philosophy.  This
is the main reason that VIM has such a large learning curve.  It's a completely
different approach to something you've been doing every single day, all day,
some of you for a very long time.

In this presentation, I will be showing you how I use VIM.  For the most part,
I won't be separating what you can do with vanilla VIM vs what you can do with
VIM plugins, because I believe a good portion of VIM's strength is in the
plugins, and after 25 years, there are a lot of them.

First things first, I will demo one of my favorite things about VIM:

_DEMO_:

1. Check out your dotvim settings repository, and show how it installs plugins
   automatically.
2. Show how you can go from nothing to having a completely configured text
   editor within minutes.
3. Show that you can do everything in the terminal, but that there is also a
   GUI and explain the benefits of that.

So, How?
--------

How can VIM make you faster?  I'm going to separate this into two different
sections: **Faster Editing** and **Faster File Management**.  But first, we
need to learn some of the basics.  VIM operates in modes, and the main
important modes are:

_DEMO_: |:enew|

1. *Normal Mode*: For navigation an manipulation of text.
2. *Insert Mode*: For inserting new text.  This is the mode that most text
   editors are in at all times.
3. *Visual Mode*: For selecting text - kind of like selecting text in a regular
   editor.
4. Demo changing modes, talk about how `ESC` is the default but that you can
   change it to whatever you want, like `fd`, so that you don't have to leave
   the home row for something you do so often.

Why modes?  The benefit of separating `normal` mode from `insert` mode is that
in `normal` mode, you can use regular keys to input commands, avoiding
excessive reaching for modifier keys like `CTRL`, `ALT`, etc.  For instance, in
`normal` mode, you can use keys like `j`, `k`, `l`, `;` for moving the cursor
down, up, left, and right, meaning you don't have to leave your home row or use
more than one finger at a time to move your cursor around.

VIM starts in `normal` mode, meaning, when you open VIM, you can't just
immediately start typing code.  The reason for this is another philosophy of
VIM: you spend more time editing/manipulating/moving existing code than you do
writing new code.

Note that the presentation is only going to show a small fraction of what is
possible in VIM, that even after using it for so long, you still learn new
things all the time.

Here are some of the ways VIM can make you faster while editing a single file:

Single File
-----------

_DEMO_: |singlefile.c|

1.  Show navigation:
    * Show navigation with the home keys, `j`, `k`, `l`, and `;`.
    * Show moving around the file with `CTRL-F`, and `CTRL-B`.  Explain that,
      yes, this does use modifier keys, but that you can always bind them to
      whatever you want.
    * Show moving forward and backward by word using `w` and `b`.
    * Show moving forward and backward to a specific character.
    * Show moving to the beginning and end of the line, via `$` and `^`.
    * Show moving to the beginning and end of the file, via `gg` and `G`.
    * Show moving the cursor to the top, center, and bottom of the current
      window using `H`, `M`, and `L`.
    * Show how to center the screen using `zz`.
    * Show navigation with marks.
    * Show navigating with `%`.
    * Show navigating the file with easymotion.

2.  Show selection/copy/paste.
    * Show the three different ways to select text, with `v`, `V` and
      `CTRL-v`.
    * Show how you can reselect the last selection with `gv`.
    * Show how to copy with `y`, show how to paste with `p` and `P`.  Mention
      that you can copy without selecting with `yy`.
    * Show multiple clipboards.
    * Show how you can use block selection to change a block of code spanning
      multiple lines.
    * Show how you can use block selection to insert text on multiple lines.
    * Show text objects, `vw`, `viw`, `vis`, `vip`, `vii`, `vi}` etc (use
      |README.md| and |singlefile.py|).  Perhaps this is a good time totalk
      about operators and mention that `v` can be used as a operator for
      "select", and how operators can be combined with movement commands.

3.  Show text manipulation.
    * Show how to delete a single character with the `x` operator.  Mention
      that it goes into the default clipboard, show how it can be used to swap
      characters.
    * Show how to delete a single line with `dd`, and mention that it goes
      into the default clipboard and can be pasted later, and can be used to
      swap lines.
    * Show how commands/operators can be repeated by putting a count before
      them.
    * Talk about the difference between the `c` and `d` operators.
    * Show `D` and `C`, and `A`.
    * Show `o` and `O`.
    * Show how movement commands can be combined with operators some more, like
      `ct` and `c$` and `dG`
    * Show "change inner" and "delete inner", things like `cw`, `ciw`, `cis`,
      `cip`, `ci{`, `di{`.
    * May be a good time to show what `.` does.
    * Show the surround plugin.  Start with `ds"`, then show `cs"'`.  Show how
      you can do something like `ysiw<strong>`.
    * Show what `J` does to combine two lines into one.  Show how you can
      combine multiple lines by including a count.

Multiple Files
--------------

All that is great, but how is VIM at managing multiple files in a project?
Lucas specifically asked about tabs.  Tabs in VIM are not the same as tabs in
other editors, in fact, many believe they are named incorrectly and should have
been called "layouts", but more on that later.  Just know that tabs in VIM
are not what you think they are.

Where does this leave us?  How can we manage multiple open files at the same
time?  Why aren't tabs implemented in the way I expect?

Let's start with the basics of files in VIM.  VIM calls file that you are
editing a "buffer".  When you open VIM with more than one file, for example, by
calling VIM like so: `vim file1.txt file2.txt`, VIM opens both files in
separate buffers.  These buffers aren't required to be visible in VIM, many
buffers can be open in the background.  When you want to view a file, VIM opens
the buffer in something called a "Window".  You can have multiple windows
viewing the same buffer, at various places inside the file.

_DEMO_:

1. Show opening multiple files, show using `CtrlP` for buffers, fuzzy search
   and all of that.
2. Show opening multiple window splits, show that you can open the same file
   in many windows, at various locations in the buffer.
3. Show that you can use the keyboard to navigate windows.
4. Show that you can use easymotion to navigate windows.

Project Management
------------------

_DEMO_:

1. Explain how CtrlP works for opening files in a project.
2. Show CtrlP fuzzy match.
3. Show NERDTree, explain why you don't like it.
4. Show NetRW, opening the current directory and opening the project
   directory.

Layout Management
-----------------

Let's talk about what tabs actually do in VIM.

_DEMO_:

1.  Show how tabs are actually separate layouts.

Misc Tips/Tricks/Plugins
------------------------

_DEMO_:

1. Show autocompletion.
2. Show macros |macros.py|.  Macro is `qa0f(xf'lr:f)xESCj`
3. Show gist-vim.
4. Show `gw` |macros.py|.
5. Demo the undo tree, `Gundo` and commands like `:earlier 2m`.

Questions
---------

Ask if there are any questions.

Spacemacs
---------

Now, with all of that, you may be surprised to find out that I don't even use
VIM.  I use Emacs.  Why?  Emacs has a *much* better plugin system.  It's so
good, that some enterprising folks have implemented almost ALL of VIM as a
plugin in Emacs, and the result is that you get everything you get in VIM, but
with much better plugins.

_DEMO_:

1.  Demonstrate Magit.
    * Demo `SPC gb`.
    * Demo `SPC gs`.
    * Demo `l` in the git status window.
    * Demo rebasing (use this repository).
    * Demo viewing history.
