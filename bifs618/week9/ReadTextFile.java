/* BIFS 618
Homework 4, Question 1
ReadTextFile.java
Sarah Kerscher
*/

import java.io.*;
import java.util.Scanner;

class ReadTextFile{
  // Scanner object for user input
  private Scanner input = new Scanner(System.in);
  private Scanner openFile;

  // open file from user input
  public Scanner openFile(){
    System.out.println("Enter the sequence file name:");
    try{
      File userFile = new File(input.nextLine());
      openFile = new Scanner(userFile);
    }
    catch(FileNotFoundException e){
      System.out.println("Error: File Not Found.");
      System.exit(1);
    }
    
    return openFile;
  }

  public void closeFile(){
    if(openFile != null){
      openFile.close();
    }
  }
}
