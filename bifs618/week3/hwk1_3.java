/*
Class Name: BIFS618
Homwork 1, Question 3
File name: hwk1_3.java
Author: Sarah Kerscher
*/

public class hwk1_3 {
  /*
  * @param args
  */
  public static void main(String[] args) {
    // declare and initialize variables containing the given sequences
    String plusStrand = "ATGCTTGACC";
    String minusStrand = "TACGAACTGG";

    // Show the DNA horizontally
    System.out.printf("\nThe double-stranded DNA:\n%s\n%s\n\n", plusStrand,
      minusStrand);

    // Show DNA in vertical order
    System.out.println("In a vertical order:");

    // use for loop and charAt() to print strands vertically
    for (int i = 0; i < plusStrand.length(); i++){
      System.out.printf("%s%s\n", plusStrand.charAt(i),
        minusStrand.charAt(i));
    }
    System.out.println("\nAuthor: Sarah Kerscher\n");
  }
}
