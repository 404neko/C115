import Java.DumpedClassi4f;
import Java.GenMD5;

public class UseDump{
	public static void main(String[] args){
		if(args.length==1){
			System.out.print(DumpedClassi4f.a(args[0]));
			return;
		}
		if(args.length==3){
			System.out.print(DumpedClassi4f.a(DumpedClassi4f.a(new StringBuilder().append(DumpedClassi4f.a(args[1].trim())).append(DumpedClassi4f.a(args[0])).toString()) + args[2].toUpperCase()));
			return;
		}
		if(args.length==4){
			System.out.print(GenMD5.a(args[0] + DumpedClassi4f.a(args[1]) + args[2] + "115ud&52DaRBaew"));
			return;
		}
		else{
			System.out.print("_ERROR");
		}
	}

}