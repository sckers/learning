/* BIFS 618
Homework 4, Question 2, part 3
hwk4_2_3.java
Sarah Kerscher
*/

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;

class hwk4_2_3{
  // Scanner object for user input
  private static Scanner input = new Scanner(System.in);

  public static void main(String[] args){

	  // create needed objects
    ReadTextFile readFile = new ReadTextFile();
	  DNA DNAobject = new DNA();
	  ArrayList<String[]> fileEntries = new ArrayList<String[]>();
	  ArrayList<String[]> zincEntries = new ArrayList<String[]>();
    String formattedSeq;

	  // open the file requested by the user
	  Scanner openFile = readFile.openFile();

	  // parse file
	  fileEntries = DNAobject.parseFASTA(openFile);

	  // search entries for zinc Finger
	  zincEntries = DNAobject.findFeature(
		"C[GALMFWKQESPVICYHRNDT]{2}C[GALMFWKQESPVICYHRNDT]{17}C[GALMFWKQESPVICYHRNDT]{2}C",
		fileEntries);

	  // print each entry that has a zinc Finger
	  for(String[] zincEntry : zincEntries){
  		// print header
  		System.out.printf("\n%s\n", zincEntry[0]);
  		// print zinc finger sequence
  		System.out.printf("Zinc Finger Site:  %s\n", zincEntry[2]);
  		// print start and end positions of zinc finger
  		System.out.printf("Zinc Finger Position:  %s - %s\n", zincEntry[3], zincEntry[4]);
  		// print sequence
  		DNAobject.setSeq(zincEntry[1]);
  		System.out.printf("%s\n\n", DNAobject.annotateFeature(50, zincEntry[3], zincEntry[4]));
	  }

	  // close the file
	  readFile.closeFile();
  }
}
