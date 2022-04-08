/* Week5 in-class exercise
   Name: Average3.java
   Author: Sarah Kerscher
   Date: 16Feb2021

*/

public class AverageAny {

	public static void main(String[] args) {
		// initialize array to store arguments
		double argVals[] = new double[args.length];

		for (int i = 0; i < args.length; i++) {
			double temp = Double.parseDouble(args[i]);
			argVals[i] = temp;
		}

		//  TO DO:
		//
		//  a.  Compute and display the average grade
		double sum = 0;

		for (int counter = 0; counter < argVals.length; counter++) {
			sum += argVals[counter];
		}
    System.out.printf("%s%.1f\n\n", "Average grade: ", sum/argVals.length);

		//  b.  Display a PASS/FAIL message
		//        average >= 75.0  PASS
		//        average <  75.0  FAIL
                if ((sum/argVals.length) >= 75.0) {
                    System.out.println("Average >= 75.0  PASS");
                }
                else{
                    System.out.println("Average < 75.0  FAIL");
                }
                System.out.println("\n\nAuthor: Sarah Kerscher");
	}
}
