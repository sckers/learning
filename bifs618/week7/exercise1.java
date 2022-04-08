/*
BIFS 618
Week 7, Exercise 1
exercise1.java
Sarah Kerscher
*/

// Write a program that takes in a FASTA file and prints the number
// of sequences in the file

import java.util.Scanner;
import java.io.*;
import java.util.ArrayList;

public class exercise1{
  public static void main(String[] args){
    // set up Scanner
    Scanner input = new Scanner(System.in);

    // set up object for readfile class
    readFiles r = new readFiles();

    // initialize ArrayList for storing file line from readFiles
    ArrayList<String> headers = new ArrayList<String>();

    // request file name from user
    System.out.println("Enter the file name that contains the FASTA data:");
    String fileName = input.nextLine();

    // process file
    r.openFile(fileName);
    headers = r.fileLines();
    r.closeFile();

    // print number of sequences to console
    System.out.printf("File %s contains %d sequences.", fileName, headers.size());
    System.out.println("\n\n Author: Sarah Kerscher");
  }
}
