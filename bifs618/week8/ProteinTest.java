/*BIFS618
Week 8 Exercise 1
ProteinTest.java
Sarah Kerscher
*/

// this test file will help evaluate that Protein.java works properly

import java.util.Scanner;

public class ProteinTest{
  public static void main(String[] args){
    // initialize variables
    String id;
    String seq;
    Scanner input = new Scanner(System.in);

    // request id and seq from user
    System.out.println("Enter the sequence ID:");
    id = input.nextLine();
    System.out.println("Enter the sequence:");
    seq = input.nextLine();

    // create Protein object
    Protein p = new Protein(id, seq);

    // test for protein sequence
    if (p.validSeq()) {
      System.out.println("The entry is a protein sequence.");
    }

    else {
      System.out.println("The entry is not a protein sequence.");
    }

    System.out.println("\nAuthor: Sarah Kerscher\n");

  }
}
