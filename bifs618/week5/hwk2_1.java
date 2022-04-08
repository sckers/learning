/*
BIFS 618
Homework 2, Question 1
hwk2_1.java
Sarah Kerscher
*/

import java.util.Scanner;

class hwk2_1{
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

		// tell the user whether the string is valid DNA
		boolean isDNA = DNAclass.isDNAvalid();
		if (isDNA) {
			System.out.println("\nThe DNA is valid.\n\n");
		}
		else {
			System.out.println("\nThe DNA is not valid.\n\n");
		}
		System.out.println("Author: Sarah Kerscher");
	}
}
