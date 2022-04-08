/* BIFS 618
Homework 4, Question 1
hwk4_1.java
Sarah Kerscher
*/

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;

class hwk4_1{
  // Scanner object for user input
  private static Scanner input = new Scanner(System.in);

  public static void main(String[] args){

	  // create needed objects
    ReadTextFile readFile = new ReadTextFile();
	  DNA DNAobject = new DNA();
	  String id;
	  String seq;
	  ArrayList<String[]> fileEntries = new ArrayList<String[]>();

	  // open the file requested by the user
	  Scanner openFile = readFile.openFile();

	  // parse file
	  fileEntries = DNAobject.parseFASTA(openFile);

	  while(true){
		  // ask the user for desired id
		  System.out.println("Please enter a sequence ID:");
		  DNAobject.setID(input.nextLine());
		  id = DNAobject.getID();

		  // if the id entered is quit
		  if(id.equals("quit")){
			  // exit the loop
			  System.out.println("\nQuitting program...\n");
			  break;
		  }

		  // if the id exists
		  else if(DNAobject.findID(fileEntries)){
			  // find the sequence that matches the ID
			  DNAobject.setSeq(DNAobject.findEntry(fileEntries));
			  // print id and seq in FASTA format
			  System.out.printf("\n%s\n%s\n", id, DNAobject.formatSeq(50));
		  }

		  //if the id does not exist
		  else if(!DNAobject.findID(fileEntries)){
			  // print error message
			  System.out.printf("\nThe sequence ID %s is not in the file.\n", id);
		  }

	  }

	  // close the file
	  readFile.closeFile();
  }
}
