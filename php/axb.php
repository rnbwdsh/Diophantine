<!-- <html> -->
<!-- <body bgcolor="FFFFCCC"> -->
<?php
include ("check_input.php");
include ("library.php");
include ("lllhermite_.php");
global $transposed;

// $matrix = "0 1 0 0 0 -1 0 -1 -1 1 1 0 0 1 0 2 -2 0 -3 -4 1 -4 -2 3 2 0 0  4 1 -3 0 0 0 4 0 3 3 -3 -3 0 0  -3 0 -1 1 1 0 2 0 2 2 -2 -2 0 0  -1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0";
$matrix = "0 0 1 -1 -1 0 0 0 2 0 0 2 -4 -4 0 0 0 6 0 1 -3 4 3 0 0 0 -7 1 0 -1 2 2 0 0 0 -3 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 0 0";
$a = split ( '[ ]+', $matrix );
$rows = 7;
$cols = count ( $a ) / 7;
$ii = "0";
for($i = "1"; le ( $i, $rows ); $i = bcadd ( $i, "1" )) {
	for($j = "1"; le ( $j, $cols ); $j = bcadd ( $j, "1" )) {
		$k = bcadd ( $ii, $j );
		$k = bcsub ( $k, "1" );
		$mat[$i][$j] = $a[$k];
	}
	$ii = bcadd ( $cols, $ii );
}

$m = bcsub ( $cols, "1" );
$t = test_zeromat ( $mat, $rows, $m );
// echo "Augmented matrix [A|B]=";
// printmat1 ( $mat, $rows, $cols );
// echo "<br>\n";
$transposed = transpose ( $mat, $rows, $cols );
$m1 = "1";
$n1 = "1";
$n = $rows;

$a = split ( '[ ]+', "-2 -1 9 1 2");
$b = split ( '[ ]+', "4 2 -5 7 -6");
$c = split ( '[ ]+', "8 -1 11 -1 5");
$d = split ( '[ ]+', "-5 1 3 -2 1");

// // Scalar functions
// for($i = "0"; lt ( $i, "5" ); $i = bcadd ( $i, "1" )) {
// //  	print $a[$i];
// //  	print $b[$i];
// //  	print $c[$i];
// //  	print $d[$i];
//   print "-------------- i = $i --------------\n";
//  	print "introot($a[$i], $b[$i], $c[$i], $d[$i]): " . introot(abs($a[$i]), abs($b[$i]), $c[$i], $d[$i]) . "\n";
//  	$out = egcd($a[$i], $b[$i]); 	
// 	print "egcd($a[$i], $b[$i]): " . $out . ", " . $multiplier1 . ", " . $multiplier2 . "\n";
// 	print "lnearint($a[$i], $b[$i]): " . lnearint($a[$i], $b[$i]) . "\n";
// 	ratior($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "ratior($a[$i], $b[$i], $c[$i], $d[$i]): " . $rationum . ", " . $ratioden . "\n";
// 	multr($a[$i], $b[$i], $c[$i], $d[$i]);	
// 	print "multr($a[$i], $b[$i], $c[$i], $d[$i]): " . $multnum . ", " . $multden . "\n";
// 	subr($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "subr($a[$i], $b[$i], $c[$i], $d[$i]): " . $subnum . ", " . $subden . "\n";
// 	addr($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "addr($a[$i], $b[$i], $c[$i], $d[$i]): " . $addnum . ", " . $addden . "\n";
// 	print "comparer($a[$i], $b[$i], $c[$i], $d[$i]): " . comparer($a[$i], abs($b[$i]), $c[$i], abs($d[$i])) . "\n";
// }


// 

// // Scalar functions
// for($i = "0"; lt ( $i, "5" ); $i = bcadd ( $i, "1" )) {
// 	//  	print $a[$i];
// 	//  	print $b[$i];
// 	//  	print $c[$i];
// 	//  	print $d[$i];
// 	print "-------------- i = $i --------------\n";
// 	print "introot($a[$i], $b[$i], $c[$i], $d[$i]): " . introot(abs($a[$i]), abs($b[$i]), $c[$i], $d[$i]) . "\n";
// 	$out = egcd($a[$i], $b[$i]);
// 	print "egcd($a[$i], $b[$i]): " . $out . ", " . $multiplier1 . ", " . $multiplier2 . "\n";
// 	print "lnearint($a[$i], $b[$i]): " . lnearint($a[$i], $b[$i]) . "\n";
// 	ratior($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "ratior($a[$i], $b[$i], $c[$i], $d[$i]): " . $rationum . ", " . $ratioden . "\n";
// 	multr($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "multr($a[$i], $b[$i], $c[$i], $d[$i]): " . $multnum . ", " . $multden . "\n";
// 	subr($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "subr($a[$i], $b[$i], $c[$i], $d[$i]): " . $subnum . ", " . $subden . "\n";
// 	addr($a[$i], $b[$i], $c[$i], $d[$i]);
// 	print "addr($a[$i], $b[$i], $c[$i], $d[$i]): " . $addnum . ", " . $addden . "\n";
// 	print "comparer($a[$i], $b[$i], $c[$i], $d[$i]): " . comparer($a[$i], abs($b[$i]), $c[$i], abs($d[$i])) . "\n";
// }


function print_all($m, $n, $m1, $n1) {
	global $B;
	global $L;
	global $A;
	global $D;
	print "A: \n";
	printmatrix($A, $m, $n);
	print "B: \n";
	printmatrix($B, $m, $m);
	print "L: \n";
	for($r="2";le($r,$m);$r=bcadd($r,"1")){
		for($s="1";lt($s,$r);$s=bcadd($s,"1")){
			print $L[$r][$s] . " ";
		}
		print "\n";
	}
	print "D: \n";
	printarray($D, $m);
	print "\n";
}


global $col1;
global $col2;
global $nplus1;
global $B;
global $L;
global $A;
global $D;
global $hnf;
global $unimodular_matrix;
global $rank;
global $lcv;
global $choleskynum;
global $choleskyden;
global $G;

$arrays[0] = "-3 -2 -4 -3 -1 0 -3 0 1 3 3 -4 3 -1 3 -2 -4 -2 -1 0 2 1 0 -2 -4 3 3 -4 0 0 4 4 3 -4 2 4 1 0 -3 -2 1 2 2 1 -2 0 2 0 -3 -1 4 0 -2 -1 0 4 4 2 0 0 -4 1 -4 4 -4 0 -2 3 4 4";
$arrays[1] = "-1 0 0 -3 -3 -3 4 0 1 4 0 -2 -2 4 2 -4 0 -3 -4 2 -2 3 1 -4 2 -1 1 -4 0 1 4 -3 -2 2 -1 1 -4 -2 4 1 -3 -2 -1 -3 0 -4 1 -3 3 1 -4 -1 0 -3 0 0 3 3 -4 0 1 1 -1 -3 2 2 -3 3 2 2";
$arrays[2] = "-1 -2 3 -1 4 0 -4 -3 4 -2 -3 2 -2 4 -4 3 3 2 0 -4 -1 2 4 0 4 0 2 0 0 0 -1 -1 -2 0 -1 -1 3 -3 4 2 3 -1 2 2 -4 -3 -1 -1 2 3 -4 0 -1 -1 4 0 1 -4 -2 0 4 2 3 0 -2 -2 2 -2 -4 1";
$arrays[3] = "-3 3 4 -1 0 -4 -1 -4 2 -2 1 2 3 -1 -3 3 -3 -2 1 -2 -4 2 2 -2 -3 -1 -2 -4 0 2 0 -4 -3 - 3 1 2 0 -3 1 -1 -1 -1 3 1 1 4 -3 -3 0 2 0 1 -4 1 -3 0 -1 0 1 0 0 0 -2 -2 4 0 4 1 2 0";
$arrays[4] = "4 -3 0 3 0 3 4 -4 0 -3 -4 4 -3 -4 -3 -3 2 0 -1 -1 0 3 4 -1 2 -2 2 2 0 3 -3 1 0 0 2 0 0 -3 1 1 0 -4 -3 -3 0 1 -3 -1 1 0 4 3 2 2 1 -1 0 -2 2 -2 2 4 0 3 0 4 -2 -4 4 4";

for($i = "0"; lt ( $i, "5" ); $i = bcadd ( $i, "1" )) {
	$a = split ( '[ ]+', $arrays[$i] );
	$rows = 7;
	$cols = count ( $a ) / 7;
	$ii = "0";
	for($i = "1"; le ( $i, $rows ); $i = bcadd ( $i, "1" )) {
		for($j = "1"; le ( $j, $cols ); $j = bcadd ( $j, "1" )) {
			$k = bcadd ( $ii, $j );
			$k = bcsub ( $k, "1" );
			$mat[$i][$j] = $a[$k];
		}
		$ii = bcadd ( $cols, $ii );
	}
	
	$m = bcsub ( $cols, "1" );
	$t = test_zeromat ( $mat, $rows, $m );
	$n = $rows;
	// echo "Augmented matrix [A|B]=";
	// printmat1 ( $mat, $rows, $cols );
	// echo "<br>\n";
// 	printmatrix($mat, $rows, $cols);
// 	for($i = "1"; le ( $i, $rows ); $i = bcadd ( $i, "1" )) {
// 		for($j = "1"; le ( $j, $cols ); $j = bcadd ( $j, "1" )) {
// 			$transposed[$j][$i] = $mat[$i][$j];
// 			print $transposed[$j][$i];			
// 		}
// 	}
 	$transposed = transpose ( $mat, $rows, $cols );
	axb_header ( $transposed, $m, $n, $m1, $n1 );
	lllhermite($G, $m, $n, $m1, $n1);	
// 	print "llhermite: " . $hnf . ", " . $unimodular_matrix . ", " . $rank . "\n";
	print_all($m, $n, $m1, $n1);
	print "flagcol(transposed, m, n): " . flagcol($A, $m, $n) . "\n";	
	swap2(4, $m, $n);
	print "swap2($k, $m, $n): " . "\n";
	print_all($m, $n, $m1, $n1);
	
	
// 	reduce2($k, $i, $m, $n, $D);
// 	print "reduce2($k, $i, $m, $n, $D): " . $col1 . ", " . $col2;
// 	minus($j, $m, $L);
// 	print "minus($j, $m, $L): " . $L;

// 	zero_row_test($matrix, $n, $i);
// 	print "zero_row_test($matrix, $n, $i): ";
// 	shortest_distance($A, $m, $n);
// 	print "shortest_distance($A, $m, $n): ";
// 	cholesky($A, $m);
// 	print "cholesky($A, $m): ";
// 	gram($A, $m, $n);
// 	print "gram($A, $m, $n): ";
// 	lcasvector($A, $X, $m, $n);
// 	print "lcasvector($A, $X, $m, $n): ";
}


// exit ();

// echo "<br>\n";
// print "<p>\n";
// flush ();
// print "<a href=\"./axb.html\">Return to main page</a><br>\n";
flush ();
// ?>
<!-- </body> -->
<!-- </html> -->
