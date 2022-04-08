/*
Class Name: BIFS618
Homwork 1, Question 2
File name: hwk1_2.java
Author: Sarah Kerscher
*/

// need Scanner class to get user input
import java.util.Scanner;

public class hwk1_2 {
  /*
  * @param args
  */
  public static void main(String[] args) {
    // Create scanner for user input
    Scanner input = new Scanner(System.in);

    // Prompt user for clone Name
    System.out.println("\nEnter the name of your clone: ");
    String clone = input.nextLine();

    // Prompt user for DNA sequence
    System.out.println("\nEnter your DNA sequence: ");
    String seq = input.nextLine();

    // Output FASTA formatted sequence
    System.out.printf("\n>%s\n%s\n\nAuthor: Sarah Kerscher\n", clone, seq);
  }
}
