program percabangan3;
var N : longint;
begin
	readln(N);
	if (N > 0) then begin
		writeln('positif');
	end else if (N = 0) then begin
		writeln('nol');
	end else begin
		writeln('negatif');
	end;
end.