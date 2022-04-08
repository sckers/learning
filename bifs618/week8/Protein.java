/*BIFS618
Week 8 Exercise 1
Protein.java
Sarah Kerscher
*/

// design a subclass to the Sequence class called Protein
// in the subclass override the validSeq() method to validate protein sequences
// write a test class to test the validSeq() method and include your name in the output

import java.util.regex.Pattern;

public class Protein extends Sequence{

	// constructor
	public Protein(String id, String seq){
		// call to superclass constructor
		super(id, seq);
	}

	@Override // override the superclass method
	public boolean validSeq(){
		return Pattern.matches("[ARNDBCEQZGHILKMFPSTWYV]+", super.getSeq());
	}
}
