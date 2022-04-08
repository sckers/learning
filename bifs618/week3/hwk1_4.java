/*
Class Name: BIFS618
Homwork 1, Question 4
File name: hwk1_4.java
Author: Sarah Kerscher
*/

// import scanner for user input
import java.util.Scanner;

public class hwk1_4 {
  /*
  * @param args
  */
  public static void main(String[] args) {
    // initialize Scanner
    Scanner input = new Scanner(System.in);

    // declare variables
    int counter = 0;
    int number;
    int largest = 0;

    // run loop to get user input
    while (counter < 10) {
      System.out.println("Enter a positive integer:");
      number = input.nextInt();

      // check if the new input is larger or smaller than the largest value so far
      if (number > largest) {
        largest = number;
      }
      counter++;
    }

    // print the largest number
    System.out.printf("The largest value you entered is %d.\n\nAuthor: Sarah Kerscher\n",
      largest);
  }
}
