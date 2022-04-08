/*
Class Name: BIFS 618
Homework 3, question 2
File name: hwk3_2.java
Author: Sarah Kerscher
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;

public class hwk3_2{
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
			System.out.println();
			for (String amino : codon2aa(codons1)){
				System.out.printf("%s   ", amino);
			}

			// print Reading frame #2 codons are:
			System.out.println("\n\nReading frame #2 codons are:");
			for (String codon : codons2){
				System.out.printf("%s ", codon);
			}
			System.out.println();
			for (String amino : codon2aa(codons2)){
				System.out.printf("%s   ", amino);
			}

			// print Reading frame #3 codons are:
			System.out.println("\n\nReading frame #3 codons are:");
			for (String codon : codons3){
				System.out.printf("%s ", codon);
			}
			System.out.println();
			for (String amino : codon2aa(codons3)){
				System.out.printf("%s   ", amino);
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

	public static ArrayList<String> codon2aa(ArrayList<String> codons){
		// initialize amino acid ArrayList
		ArrayList<String> aminos = new ArrayList<String>();
		String amino;

		// for each codon in the given array, convert to aa and add to new array
		for (String codon : codons){
			switch(codon){
				case "GCU":
				case "GCC":
				case "GCA":
				case "GCG":
				case "GCT":
					amino = "A";
					break;
				case "CGU":
				case "CGT":
				case "CGC":
				case "CGA":
				case "CGG":
				case "AGA":
				case "AGG":
					amino = "R";
					break;
				case "AAU":
				case "AAT":
				case "AAC":
					amino = "N";
					break;
				case "GAU":
				case "GAT":
				case "GAC":
					amino = "D";
					break;
				case "UGU":
				case "TGT":
				case "UGC":
				case "TGC":
					amino = "C";
					break;
				case "CAA":
				case "CAG":
					amino = "Q";
					break;
				case "GAA":
				case "GAG":
					amino = "E";
					break;
				case "GGU":
				case "GGT":
				case "GGC":
				case "GGA":
				case "GGG":
					amino = "G";
					break;
				case "CAU":
				case "CAT":
				case "CAC":
					amino = "H";
					break;
				case "AUU":
				case "ATT":
				case "AUC":
				case "ATC":
				case "AUA":
				case "ATA":
					amino = "I";
					break;
				case "UUA":
				case "TTA":
				case "UUG":
				case "TTG":
				case "CUU":
				case "CTT":
				case "CUC":
				case "CTC":
				case "CUA":
				case "CTA":
				case "CUG":
				case "CTG":
					amino = "L";
					break;
				case "AAA":
				case "AAG":
					amino = "K";
					break;
				case "AUG":
				case "ATG":
					amino = "M";
					break;
				case "UUU":
				case "TTT":
				case "UUC":
				case "TTC":
					amino = "F";
					break;
				case "CCU":
				case "CCT":
				case "CCC":
				case "CCA":
				case "CCG":
					amino = "P";
					break;
				case "AGU":
				case "AGT":
				case "AGC":
				case "UCU":
				case "TCT":
				case "UCC":
				case "TCC":
				case "UCA":
				case "TCA":
				case "UCG":
				case "TCG":
					amino = "S";
					break;
				case "ACU":
				case "ACT":
				case "ACC":
				case "ACA":
				case "ACG":
					amino = "T";
					break;
				case "UGG":
				case "TGG":
					amino = "W";
					break;
				case "UAU":
				case "TAT":
				case "UAC":
				case "TAC":
					amino = "Y";
					break;
				case "GUU":
				case "GTT":
				case "GUC":
				case "GTC":
				case "GUA":
				case "GTA":
				case "GUG":
				case "GTG":
					amino = "V";
					break;
				case "UAA":
				case "TAA":
				case "UAG":
				case "TAG":
				case "UGA":
				case "TGA":
					amino = "*";
					break;
				default:
					amino = "O";
			}
			aminos.add(amino);
		}

		return aminos;
	}
}
