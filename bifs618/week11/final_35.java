/*BIFS 618
Final, Question 35
File name: final_35.java
Sarah Kerscher
*/

import org.biojava.bio.BioException;
import org.biojavax.bio.seq.RichSequence;
import org.biojavax.bio.seq.RichSequenceIterator;
import org.biojavax.bio.seq.RichSequence.IOTools;

import java.io.*;
import java.util.Scanner;
import javax.swing.JOptionPane;
import java.util.ArrayList;

public class final_35{

  // read in sequence file
  public static BufferedReader openFile(){
      BufferedReader br = null;

        try {
          br = new BufferedReader(new FileReader("seq.fasta"));
        }
        catch (FileNotFoundException e) {
          System.out.println("trouble reading "+file.getName());
          e.printStackTrace();
          }

      return br;
  }

  // process sequence file
  public static void main(String[] args) throws BioException{
      BufferedReader br = openFile();
      RichSequenceIterator it = IOTools.readGenbankDNA(br, null);
      ArrayList<String> seqList = new ArrayList<String>;
      Integer count = 0;

      // parse input file
      while (it.hasNext()){
        count++;
        RichSequence s = it.nextRichSequence();
        seqList += s.seqString();
      }

      // ask user for search seq
      Objects[] selection = new Object[count];
      for(int i = 0; i < selection.length(); i++){
        selection[i] = "Seq " + toString(i + 1);
      }
      String accNum = JOptionPane.showInputDialog(frame, "Select sequence to search.",
                        "Select", JOptionPane.PLAIN_MESSAGE, null, selection);

      // if no selection, system exit
      if(accNum == null){
        System.out.println("End of program");
        System.exit(0);
      }
  }
}
