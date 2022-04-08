/* Week5 in-class exercise
   Name: Average3.java
   Author: Sarah Kerscher
   Date: 16Feb2021

*/

public class Average3 {

	public static void main(String[] args) {

		double grade1, grade2, grade3;
		grade1 = Double.parseDouble(args[0]);
		grade2 = Double.parseDouble(args[1]);
		grade3 = Double.parseDouble(args[2]);

		//  TO DO:
		//
		//  a.  Compute and display the average grade
		double average = (grade1 + grade2 + grade3) / 3;
                System.out.printf("%s%.1f\n\n", "Average grade: ", average);

		//  b.  Display a PASS/FAIL message
		//        average >= 75.0  PASS
		//        average <  75.0  FAIL
                if (average >= 75.0) {
                    System.out.println("Average >= 75.0  PASS");
                }
                else{
                    System.out.println("Average < 75.0  FAIL");
                }
                System.out.println("\n\nAuthor: Sarah Kerscher");
	}
}
