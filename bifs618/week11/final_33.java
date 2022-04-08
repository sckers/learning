/*BIFS618
Final, Question 33
final_33.java
Sarah Kerscher
*/

import java.util.*;
import java.time.*;
import java.io.*;
import java.lang.*;
import java.time.format.*;

public class final_33{

  private static Formatter fastaFile;
  private static String fileName;

  public static void createFile(){
    // declare variables
    DateTimeFormatter timeStamp = DateTimeFormatter.ofPattern("yyyyMMddHHmmss");
    fileName = "seqs_" + timeStamp.format(LocalDateTime.now()) + ".fasta";

    // create file
    try{
      fastaFile = new Formatter(fileName);
    }

    catch(Exception e){
      System.out.println("File error");
    }
  }

  public static void main(String[] args) throws FileNotFoundException {

    // declare variables
    Scanner input = new Scanner(System.in);

    // call to create file
    createFile();

    // request clone id and sequence from user
    // while the user hasn't entered exit
    while(true){
      // request id from user
      System.out.println("\nEnter the sequence ID or 'exit':");
      String id = input.nextLine();

      // if user enters exit
      if(id.equals("exit")){
        // stop asking for id and seq
        break;
      }

      // request seq from user
      System.out.println("Enter the sequence:");
      String seq = input.nextLine();

      // append to our file
      fastaFile.format(">%s\n%s\n", id, seq);
    }

    // call to close file
    closeFile();

    // print ids and seqs in fasta format
    File myFile = new File(fileName);
    Scanner scanFile = new Scanner(myFile);

    System.out.println("\n\n");
    while(scanFile.hasNextLine()){
      System.out.println(scanFile.nextLine());
    }
  }

  // close file
  public static void closeFile(){
    fastaFile.close();
  }
}
