#!/usr/bin/env perl
#
# Takes a list of files on the command line and checks for valid
# UTF-8 data. Used for checking .po files.
#
# Copyright © 2009 Tobias Quathamer <toddy@debian.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

use strict;
use warnings;

my $exit_status = 0;

foreach my $filename (@ARGV) {
  my $content_type_checked = 0;
  open FILE, "< $filename";
  while (<FILE>) {
    # Check for valid UTF-8 encoding
    unless (m/\A(
      [\x09\x0A\x0D\x20-\x7E]            # ASCII
    | [\xC2-\xDF][\x80-\xBF]             # non-overlong 2-byte
    |  \xE0[\xA0-\xBF][\x80-\xBF]        # excluding overlongs
    | [\xE1-\xEC\xEE\xEF][\x80-\xBF]{2}  # straight 3-byte
    |  \xED[\x80-\x9F][\x80-\xBF]        # excluding surrogates
    |  \xF0[\x90-\xBF][\x80-\xBF]{2}     # planes 1-3
    | [\xF1-\xF3][\x80-\xBF]{3}          # planes 4-15
    |  \xF4[\x80-\x8F][\x80-\xBF]{2}     # plane 16
    )*\z/x) {
      # Found invalid characters for UTF-8
      printf("Error in file %s at line number %d:\n", $filename, $.);
      # Show the line with the error
      print;
      $exit_status = 1;
      # Skip the rest of the current file
      last;
    }
    # Check that the Content-Type header field is set correctly.
    if (!$content_type_checked && /Content-Type: text\/plain; charset=UTF-8/) {
      $content_type_checked = 1;
    }
  }
  unless ($content_type_checked) {
    printf("Error in file %s:\n", $filename);
    print("Could not detect correct Content-Type header field.\n");
    $exit_status = 1;
  }
  close FILE;
}

exit($exit_status);
