/*
Class Name: BIFS618
Week 4, exercise 2
File name: MainRandSeq.java
Author: Sarah Kerscher
*/

public class MainRandSeq {
  /*
  * @param args
  */
  public static void main(String[] args) {
    // create class file object
    RandomSeq RSObject = new RandomSeq();

    // generate random sequence
    String seq = RSObject.getRandomSeq(102);
    RSObject.setSeq(seq);

    // print formatted sequence with specific length per line
    RSObject.formatSeq(21);
  }
}
