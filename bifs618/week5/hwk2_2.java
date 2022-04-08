/*
BIFS 618
Homework 2, Question 2
hwk2_2.java
Sarah Kerscher
*/

import java.util.Scanner;

class hwk2_2{
	public static void main(String[] args){
		// setup scanner
		Scanner inputDNA = new Scanner(System.in);

		// set class file
		DNA DNAclass = new DNA();

		// request user to input their DNA string
		System.out.println("Enter your DNA string:");

		// assign the input DNA to a new variable
		String temp = inputDNA.nextLine();

		// set the user's input to DNA
		DNAclass.setDNA(temp);

		// use DNA class to get length and count Gs and Cs
		double lenDNA = DNAclass.getSize();
		double countC = DNAclass.baseCount('C');
		double countG = DNAclass.baseCount('G');

		// calculate percentage of GC content
		double percentGC = ((countC + countG) / lenDNA) * 100;

		// print GC content
		System.out.printf("The GC content is %.2f%%.\n\n", percentGC);

		System.out.println("Author: Sarah Kerscher");
	}
}
