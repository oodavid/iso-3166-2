#!/bin/sh
# Run this to generate all the initial makefiles, etc.
srcdir=`dirname $0`
test -z "$srcdir" && srcdir=.

topdir=`pwd`
cd $srcdir
aclocal
autoconf
automake --add-missing --foreign --copy
cd $topdir
$srcdir/configure $@
