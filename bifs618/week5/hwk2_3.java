/*
BIFS 618
Homework 2, Question 3
hwk2_3.java
Sarah Kerscher
*/

import java.util.Scanner;

class hwk2_3{
	public static void main(String[] args){
		// setup scanner
		Scanner inputDNA = new Scanner(System.in);

		// request user to input their DNA string
		System.out.println("Enter your DNA string:");

		// assign the input DNA to a new variable
		String DNA = inputDNA.nextLine();

		// initialize reverse complement
		String complement = "";
		for (int i = 0; i < DNA.length(); i++) {
			switch (DNA.charAt(i)) {
				case 'A':
					complement += "T";
					break;
				case 'T':
					complement += "A";
					break;
				case 'G':
					complement += "C";
					break;
				case 'C':
					complement += "G";
					break;
			}
		}

		// print the double-stranded DNA
		System.out.printf("\nHere is the double-stranded DNA:\n%s\n%s\n\n", DNA, complement);

		System.out.println("Author: Sarah Kerscher");
	}
}
