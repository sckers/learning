/*
BIFS 618
Week 7, Exercise 1
readFiles.java
Sarah Kerscher
*/

// this file contains methods for handling and reading readFiles

import java.util.Scanner;
import java.io.*;
import java.util.ArrayList;

public class readFiles{
  // establish Scanner variable for the class
  private Scanner input;

  // method to open file
  public void openFile(String name){
    try{
      input = new Scanner(new File(name));
    }
    catch(FileNotFoundException e){
      System.out.println("Error: File not found.");
    }
  }

  // method to read file
  public ArrayList<String> fileLines(){
    // establish ArrayList to store file lines
    ArrayList<String> linesArray = new ArrayList<String>();

    try{
      while (input.hasNext()){
        if (input.nextLine().startsWith(">")){
          linesArray.add(input.nextLine());
        }
      }


    }

    catch(Exception e){
      System.out.println("Error while reading file.");
    }

    return linesArray;
  }

  // method to close file
  public void closeFile(){
    if(input != null){
      input.close();
    }
  }
}
