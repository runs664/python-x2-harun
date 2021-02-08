program FloorAndCeiling;
var 
	N : real;
	C, F : real;
begin
	readln(N);
	if (((N - trunc(N)) <> 0) and (N > 0)) then begin
		F := trunc(N);
		C := trunc(N+1);
	end else if (((N - trunc(N)) <> 0) and (N < 0)) then begin
		F := trunc(N-1);
		C := trunc(N);
	end else begin
		F := N;
		C := N+1;
	end;
	writeln(F:0:0,' ',C:0:0);
end.