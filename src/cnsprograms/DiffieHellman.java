package cnsprograms;

import java.util.*;
class DiffieHellman
{
public static void main(String args[])
{
@SuppressWarnings("resource")
Scanner sc = new Scanner(System.in);
System.out.println("Enter the value of Xa & Xb");
int Xa=sc.nextInt();
int Xb=sc.nextInt();
System.out.println("Enter a Prime no. p");
int p=sc.nextInt();
System.out.println("Enter Primitive Root a, such that a<p");
int a=sc.nextInt();
int Ya=(int)((Math.pow(a,Xa))%p);
int Yb=(int)((Math.pow(a,Xb))%p);
int Ka=(int)((Math.pow(Yb,Xa))%p);
int Kb=(int)((Math.pow(Ya,Xb))%p);
System.out.println("The Value of Ya is"+Ya);
System.out.println("The Value of Yb is" +Yb);
System.out.println("Key at A's Side Ka="+Ka);
System.out.println("Key at B's Side Kb="+Kb);
if(Ka==Kb)
{
System.out.println("Diffie-Hellman Key Exchange has successful");
}
else
{
System.out.println("Key Exchange has failed");
}
}
}