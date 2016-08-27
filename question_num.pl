#!/usr/bin/env perl
use strict;
use warnings;

my $ans = 100;
#my $ans = int(rand(9999));
my @anstr = split(//, $ans);
my $i = 1;

local $| = 1;

my @start = split(//, "Let's start number guessing game!\n");
for my $ch (@start) {
  print "$ch";
  select undef, undef, undef, 0.1;
}

my $n = sprintf("%04d",$i);
print "[in  $n]> ";
while (my $in = <STDIN>) {
  chomp($in);

  print "[out $i]> ";

  if ($in == $ans) {
    last;
  }
  else {
    if (($ans - 1) < $in && $in < ($ans + 1)) {
      print "AhsdogaWDoisGdADFhEQgoha NEnenNenaneEAeneaaEANneaaNEARNEARNEARNEARRRRRRRRR!!!! \n";
    }
    elsif (($ans - 5) < $in && $in < ($ans + 5)) {
      print "Realy nearrrraedfasga!!!!!!!!!!!\n";
    }
    elsif (($ans - 10) < $in && $in < ($ans + 10)) {
      print "Near! Near! Near!\n";
    }
    elsif (($ans - 50) < $in && $in < ($ans + 50)) {
      print "Near!\n";
    }
    elsif (($ans - 500) < $in && $in < ($ans + 500)) {
      print "N...?\n";
    }
    else {
      print "You are awful...\n";
    }
  }

  if ($i == 5) {
    print "----- Hint 1: The number of digit is ... ", length($ans), "!\n";
  }
  if ($i == 10) {
    print "----- Hint 2: The numbers of the first digit is ... ", $anstr[0], "!\n";
  }
  if ($i == 20 && $ans > 9) {
    print "----- Hint 3: The numbers of the second digit is ... ", $anstr[1], "!\n";
  }
  if ($i == 30 && $ans > 99) {
    print "----- Hint 3: The numbers of the third digit is ... ", $anstr[2], "!\n";
  }

  $i++;
  $n = sprintf("%04d",$i);
  print "[in  $n]> "
}

my @success = split(//, "YYYYoooouuuu aaaaarrrrreeeee awesome!! awesome!! awesome!!!!!!!!! FOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!\n");
for my $ch (@success) {
  print "$ch";
  select undef, undef, undef, 0.1;
}

my $score = "Your score is ".(length($ans) / $i * 100)."!";
my @end = split(//, $score);
for my $ch (@end) {
  print "$ch";
  select undef, undef, undef, 0.1;
}
for my $i (1..10) {
  print "\r                              ";
  select undef, undef, undef, 1.0;
  print "\r$score";
  select undef, undef, undef, 1.0;
}
print "\n";

exit 0;
