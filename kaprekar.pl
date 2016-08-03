# kaprekar.pl 2016/08/03(Wed) walkingmask
# Seek kaprekar number in a parallel distributed processing

use strict;
use warnings;
use threads;

my $thnum = 3; # The number of threads
my $maxnum = 1000000;

# Distribution of tasks
my $tasks = [[], [], [], []];
for (0 .. $maxnum) {
  push(@{$tasks->[$_%$thnum]}, $_);
}

# Seek kaprekar number
sub kap {
  foreach my $num (@_) {
    my @str = split(//, ''.$num);
    my $num1 = join('', reverse(sort(@str)));
    my $num2 = join('', sort(@str));
    if ($num1 - $num2 == $num) {
      print $num."\n";
    }
  }
}

# The start of the thread
my @threads;
for (0 .. $thnum) {
    my $thread = threads->new(\&kap, @{$tasks->[$_]});
    push(@threads, $thread);
}
# Waiting
foreach(@threads){
  my ($return) = $_->join;
}
