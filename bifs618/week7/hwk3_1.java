/*
Class Name: BIFS 618
Homework 3, question 1
File name: hwk3_1.java
Author: Sarah Kerscher
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;

public class hwk3_1{
	public static void main(String[] args){
		// setup scanner
		Scanner input = new Scanner(System.in);

		// read in DNA from sequence file
		try{
			System.out.println("Please enter the file name that contains the DNA sequence");
			String myFile = input.nextLine();
			Scanner readFile = new Scanner(new File(myFile));
			String frame1 = readFile.nextLine();

			// get strings for other two frames
			String frame2 = frame1.substring(1);
			String frame3 = frame1.substring(2);

			// print all codons from the three forward reading frames
			// use codon method that takes argument of the reading frame, returns array
			// pull the array
			ArrayList<String> codons1 = codon(frame1);
			ArrayList<String> codons2 = codon(frame2);
			ArrayList<String> codons3 = codon(frame3);

			// print The DNA sequence is:
			System.out.printf("\nThe DNA sequence is:\n%s\n", frame1);

			// print Reading frame #1 codons are:
			System.out.println("\nReading frame #1 codons are:");
			for (String codon : codons1){
				System.out.printf("%s ", codon);
			}

			// print Reading frame #2 codons are:
			System.out.println("\n\nReading frame #2 codons are:");
			for (String codon : codons2){
				System.out.printf("%s ", codon);
			}

			// print Reading frame #3 codons are:
			System.out.println("\n\nReading frame #3 codons are:");
			for (String codon : codons3){
				System.out.printf("%s ", codon);
			}

			// close File
			readFile.close();
		}

		catch (FileNotFoundException e){
			System.out.println("Error: File Not Found");
		}

	}
	public static ArrayList<String> codon(String DNA){
		// initialize array
		ArrayList<String> temp = new ArrayList<String>();

		// initialize variable for tracking the index
		int index = 0;

		// loop throught the DNA string to get codons
		while (index < DNA.length() - 2){
			temp.add(DNA.substring(index, index + 3));
			index += 3;
		}

		// remove last element if it is not a true codon
		if (temp.get(temp.size() - 1).length() < 3){
			temp.remove(temp.size() - 1);
		}

		return temp;
	}
}
