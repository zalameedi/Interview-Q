using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

/*Enter your solution*/    

public class Comparator
{
    public Comparator()
    {

    }
    public bool compare(int a, int b)
    {
        if (a==b)
        {
            return true;
        }
        return false;
    }

    public bool compare(string a, string b)
    {
        if (a==b)
        {
            return true;
        }
        return false;
    }

    public bool compare(int[] a, int[] b)
    {
        if (a.Length == b.Length)
        {
            for(int i=0; i < a.Length; i++)
            {
                if (a[i] != b[i])
                {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
}


class Solution {
    static void Main(String[] args) {
		Comparator comp = new Comparator();
        int testCases = Convert.ToInt32(Console.ReadLine());
        while(testCases-- > 0){
            int condition = Convert.ToInt32(Console.ReadLine());
            if(condition == 1){
                string s1=Console.ReadLine();
                string s2=Console.ReadLine();
                if(comp.compare(s1,s2)){
                    Console.WriteLine("Same");
                }
                else{
                    Console.WriteLine("Different");
                }
            }
            else if(condition == 2){
                int num1=Convert.ToInt32(Console.ReadLine());
                int num2=Convert.ToInt32(Console.ReadLine());
                if(comp.compare(num1,num2)){
                    Console.WriteLine("Same");
                }
                else{
                    Console.WriteLine("Different");
                }
            }
            else if(condition == 3){
                Console.ReadLine();
                int[] arr1 = Console.ReadLine().Split(' ').Select( x=> Convert.ToInt32(x)).ToArray();
                int[] arr2 = Console.ReadLine().Split(' ').Select( x=> Convert.ToInt32(x)).ToArray();
                if(comp.compare(arr1,arr2)){
                    Console.WriteLine("Same");
                }
                else{
                    Console.WriteLine("Different");
                }
            }
        }
	}
}
