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

1.  It was ugly.
2.  It was not a GUI application.
3.  I could not understand how navigating code (especially in a large project
    with many files) could possibly be faster using the keyboard than it could
    be with the mouse.

3 contrasts a lot with how I feel about it today, and I believe the main
selling point is that it is much more efficient to use the keyboard
for *almost* anything, and VIM strives to make that possible.

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
========

How can VIM make you faster?  I'm going to separate this into two different
sections: **Faster Editing** and **Faster File Management**.  But first, we
need to learn some of the basics.  VIM operates in modes, and the main
important modes are:

_DEMO_:

1.  *Normal Mode*: For navigation an manipulation of text.
2.  *Insert Mode*: For inserting new text.  This is the mode that most text
    editors are in at all times.
3.  *Visual Mode*: For selecting text - kind of like selecting text in a
    regular editor.

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

Here are some of the ways VIM can make you faster while editing a single file:

_DEMO_:

1.  Show navigation:
    *  Show navigation with the home keys, `j`, `k`, `l`, and `;`.
    *  Show moving around the file with `CTRL-F`, and `CTRL-B`.  Explain that,
       yes, this does use modifier keys, but that you can always bind them to
       whatever you want.
    *  Show moving to the beginning and end of the line, via `$` and `^`.
    *  Show moving to the beginning and end of the file, via `gg` and `G`.
    *  Show moving the cursor to the top, center, and bottom of the current
       window using `H`, `M`, and `L`.
    *  Show how to center the screen using `zz`.
    *  Show navigation with marks.
    *  Show navigating the file with easymotion.

2.  Show selection/copy/paste.
    *  Show the three different ways to select text, with `v`, `V` and
       `CTRL-v`.
    *  Show how you can reselect the last selection with `gv`.
    *  Show how to copy with `y`, show how to paste with `p` and `P`.  Mention
       that you can copy without selecting with `yy`.
    *  Show multiple clipboards.
    *  Show how you can use block selection to change a block of code spanning
       multiple lines.
    *  Show how you can use block selection to insert text on multiple lines.