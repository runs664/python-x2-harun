program Manhattan;
var x1,x2,y1,y2,output : longint;
begin
	readln(x1,y1,x2,y2);
	output := Abs(x1 - x2) + Abs(y1 - y2);
	writeln(output);
end.
	