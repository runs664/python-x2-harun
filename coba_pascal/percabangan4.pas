program percabangan4;
var N : longint;
begin
	readln(N);
	case (N) of
		1..9: begin writeln('satuan'); end;
		10..99: begin writeln('puluhan'); end;
		100..999: begin writeln('ratusan'); end;
		1000..9999: begin writeln('ribuan'); end;
		10000..99999: begin writeln('puluhribuan'); end;
	end;
end.